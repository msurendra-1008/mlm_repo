from mimetypes import init
import pdb
from django.http.response import HttpResponse
from django.template import context
from django.shortcuts import redirect, get_object_or_404
from dashboard.forms import *
from upa.models import AdditionalDetails, BasicDetails, BeneficiaryDetails, BussinessCardFees, Enrollment, OperationMode, PersonalInformation, ServiceRequired, SponsorIntroductionDetail, UPAAddress, UPAIdentityProof
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from datetime import date
from .decorators import admin_only
from .models import *
from django.template.loader import render_to_string
from .helpers import *

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    today = date.today()
    user = Profile.objects.filter(user = request.user,initial_form_status = False)
    enroll = None
    bd = None
    try:
        for u in user:
            enroll = Enrollment.objects.get(user_id = u.id,valid_upto__gt = today)
            print(enroll.valid_upto)
    except:
        pass
    try:
        for u in user:
            bd= BasicDetails.objects.filter(user_id = u.id)
            print(bd)
    except:
        pass
    context ={'user':user,'enroll':enroll,'bd':bd}
    return render(request,'accounts/home.html',context)

@admin_only
def upa_list(request):
    upas = Profile.objects.filter(uid_no__isnull=False)
    context = {'upas':upas}
    return render(request,'dashboard/upa_list.html',context)

@admin_only
def upa_view(request,pk):
    upa_details = Profile.objects.get(pk=pk)
    left_uid_no = None
    middle_uid_no = None
    right_uid_no = None
    basic=None
    personal=None
    upa_add=None
    additional=None
    upa_identity=None
    beneficiary=None
    sponsor_details=None
    service=None
    operations=None
    try:
        left_uid_no = Profile.objects.get(user_id = upa_details.left_upa.id)
        middle_uid_no = Profile.objects.get(user_id = upa_details.middle_upa.id)
        right_uid_no = Profile.objects.get(user_id = upa_details.right_upa.id)

        # upa details
        basic = BasicDetails.objects.get(user_id = upa_details.id)
        personal = PersonalInformation.objects.get(user_id = upa_details.id)
        upa_add = UPAAddress.objects.get(user_id = upa_details.id)
        additional = AdditionalDetails.objects.get(user_id = upa_details.id)
        upa_identity = UPAIdentityProof.objects.get(user_id = upa_details.id)
        beneficiary = BeneficiaryDetails.objects.get(user_id = upa_details.id)
        sponsor_details = SponsorIntroductionDetail.objects.get(user_id = upa_details.id)
        service = ServiceRequired.objects.get(user_id = upa_details.id)
        operations = OperationMode.objects.get(user_id = upa_details.id)
       
    except:
        pass
    
    context = {'upa_details':upa_details,
                'left_uid_no':left_uid_no,
                'middle_uid_no':middle_uid_no,
                'right_uid_no':right_uid_no,
                'basic':basic,
                'personal':personal,
                'upa_add':upa_add,
                'additional':additional,
                'upa_identity':upa_identity,
                'beneficiary':beneficiary,
                'sponsor_details':sponsor_details,
                'service':service,
                'operations':operations,
    }
    return render(request,'dashboard/upa_detail.html',context)



def update_request_upa(request):
    
    uid_no = None
    group = None
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == "Admin":
        pass
    else:
        uid_no = Profile.objects.get(user_id = request.user.id)
        print(uid_no.id)
    try:
        form = UPAChangeRequestForm(initial={'upa_id':uid_no.uid_no})
    except:
        form = UPAChangeRequestForm()
        pass
    if request.method == "POST":
        form = UPAChangeRequestForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_id = uid_no.id
            instance.save()
            return redirect('home')
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'dashboard/request_application.html',context)

def change_request_status(request):
    req_status = None
    group = None
    profile = ""
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == "Admin":
        # user = request.user
        # profile = Profile.objects.get(user_id = user)
        req_status = UPAChangeRequest.objects.all().order_by('request_no')
    else:
        user = request.user
        profile = Profile.objects.get(user_id = user)
        req_status = UPAChangeRequest.objects.filter(user_id =profile.id)
        print(req_status)
    context = {'req_status':req_status,'group':group,'profile':profile}
    return render(request,'dashboard/request_status.html',context)

def reply_to_request(request,pk):
    if request.user.groups.exists():
        group = request.user.groups.all()[0].name
    if group == "Admin":
        req = UPAChangeRequest.objects.get(pk=pk)
        print(req)
        form = UPAChangeRequestReplyForm(instance = req)
    if request.method == "POST":
        form = UPAChangeRequestReplyForm(request.POST, instance = req)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.status = "Read"
            instance.save()
            return redirect('home')
        else:
            print(form.errors)
    context = {'form':form}
    return render(request,'dashboard/reply_message.html',context)


def upa_tree(request):
    upas = Profile.objects.filter(uid_no__isnull = False)
    print("printng upas:",upas)
    tree_list = []
    print("printing tree: ", tree_list)
    for i in upas:
        # print("Parent",i)
        # print("Left UPA",i.left_upa)
        # print("Middle UPA",i.middle_upa)
        # print("Right UPA",i.right_upa)

        # for j in Profile.objects.filter(user_id = i.left_upa.id):
        #     print(j.left_upa)
        #     print("under left upa",j)
        # for j in Profile.objects.filter(user_id = i.middle_upa.id):
        #     print(j.middle_upa)
        #     print("under middle upa",j)
        # for j in Profile.objects.filter(user_id = i.right_upa.id):
        #     print(j.right_upa)
        #     print("under right upa",j)
        tree = build_tree(i.user)
        tree_list.append(tree)
    print("printing tree: ", tree_list)    
    # context = {'upas':upas,'j':j}
    context = {'tree_list': tree_list}
    return render(request,'dashboard/upa_tree.html',context)

@login_required(login_url="/login")
def income_setting(request):
    incomes = IncomeSetting.objects.all()
    incomes_for_women_old = IncomeSettingForWomenOld.objects.all()
    context = {'incomes':incomes,'income_for_others':incomes_for_women_old}
    return render(request,'dashboard/income_setting.html',context)

def update_income_setting(request,pk):
    incomes = IncomeSetting.objects.get(pk=pk)
    old_incomes = incomes.income
    form = IncomeSettingForm(instance=incomes)
    if request.method == "POST":
        form = IncomeSettingForm(request.POST,instance=incomes)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.updated_by = request.user
            qs.previous_income = old_incomes
            qs.save()
            return redirect('income-setting')
    context = {'incomes':incomes,'form':form}
    return render(request,'dashboard/income_setting_form.html',context)

def update_income_setting_for_women_old(request,pk):
    incomes = IncomeSettingForWomenOld.objects.get(pk=pk)
    old_income = incomes.income
    form = IncomeSettingForWomenOldForm(instance=incomes)
    if request.method == "POST":
        form = IncomeSettingForm(request.POST,instance=incomes)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.updated_by = request.user
            qs.previous_income_for_women_old = old_income
            qs.save()
            return redirect('income-setting')
    context = {'incomes':incomes,'form':form}
    return render(request,'dashboard/income_setting_women_old_form.html',context)

def create_income_setting(request):
    form = IncomeSettingForm()
    if request.method == "POST":
        form = IncomeSettingForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.save()
            return redirect('income-setting')
    context = {'form':form}
    return render(request,'dashboard/income_setting_form.html',context)


'''
Here we are creating the income setting for women old and below 18 year child
'''

def create_income_for_women_old(request):
    form = IncomeSettingForWomenOldForm()
    if request.method == "POST":
        form = IncomeSettingForWomenOldForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.save()
            return redirect('income-setting')
    context = {'form':form}
    return render(request,'dashboard/income_setting_women_old_form.html',context)

def delete_income_setting(request, pk):
    # qs = get_object_or_404(IncomeSetting, pk=pk)
    # qs.delete()
    # return redirect('income-setting')
    res = delete_income_object(request, IncomeSetting, pk, 'income-setting')
    return res

def delete_income_setting_for_women_old(request, pk):
    # qs = get_object_or_404(IncomeSettingForWomenOld, pk=pk)
    # qs.delete()
    # return redirect('income-setting')
    res = delete_income_object(request, IncomeSettingForWomenOld, pk, 'income-setting')
    return res

'''
here we can view the all upa details of the according to the form section
'''

def upa_view_form_wise(request):
    basic_details_count = BasicDetails.objects.all().count()
    print(basic_details_count)
    context = {'basic_details_count':basic_details_count}
    return render(request,'dashboard/upa_view_form_wise.html',context)


def firm_list(request):
    firms = FirmRegistration.objects.filter(active_firm = True)
    context = {'firms':firms}
    return render(request,'dashboard/firm_list.html',context)

def firm_detail(request,pk):
    firm_details = FirmRegistration.objects.get(pk=pk)
    context = {'firm_details':firm_details}
    return render(request,'dashboard/firm_detail.html',context)

def registering_firm(request):
    if request.method ==  "GET":
        pk = request.GET['pk']
        print(pk)
        instance = FirmRegistration.objects.get(pk = pk)
        instance.status = "Registered"
        instance.save()
        return redirect('firm-list')


def firm_registration(request):
    page = "Firm Registration Form"
    form = FirmRegistrationForm()
    if request.method == 'POST':
        form = FirmRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            qs = form.save(commit = False)
            qs.created_by = request.user
            qs.active_firm = True
            qs.save()
            return redirect('firm-list')
    context = {'form':form,'page':page}
    return render(request,'dashboard/firm_registration_form.html',context)

def update_firm(request,pk):
    page = "Update Firm Registration Form"
    instances = FirmRegistration.objects.get(pk=pk)
    form = FirmRegistrationForm(instance=instances)
    if request.method == "POST":
        form = FirmRegistrationForm(request.POST,request.FILES,instance=instances)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.updated_by = request.user
            qs.active_firm = True
            qs.save()
            return redirect('firm-list')
    context = {'form':form,'page':page}
    return render(request,'dashboard/firm_registration_form.html',context)


def tender_display(request):
    tenders = TenderProduct.objects.all().order_by('-id')
    print(tenders)
    context = {'tenders':tenders}
    return render(request,'dashboard/tender_display.html',context)

def newest_raised_tender_list(request):
    tenders = TenderProduct.objects.filter(active=True).order_by('-id')
    context = {'tenders':tenders}
    return render(request,'dashboard/newest_raised_tender_list.html',context)

def compare_list_particular_tender(request,pk):
    # pk = request.GET.get('id')
    qs = TenderRaise.objects.filter(tender_product_id = pk)
    print(qs)
    context = {'tenders':qs,'pk':pk}
    return render(request,'dashboard/compare_particular_tender_invitation.html',context)

def tender_form(request):
    pk = request.GET.get('id')
    qs = TenderProduct.objects.get(pk=pk)
    print(qs)
    form = TenderForm(initial={'tender_product':qs})
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = TenderForm(request.POST)
        product_quantity = request.POST['amount_range']
        if form.is_valid():
            qs = form.save(commit=False)
            qs.total_product_quantity = product_quantity
            qs.save()
            return redirect('thank_for_vendors')
    context = {'form':form}
    return render(request,'dashboard/tender_form.html',context)


def tender_fillup_list(request):
    tender_fill_ups = TenderRaise.objects.all()
    print(tender_fill_ups)
    context = {'tenders':tender_fill_ups}
    return render(request,'dashboard/tender_fillup_list.html',context)

def thank_for_vendors(request):
    return render(request,'dashboard/vendors_thank_you_page.html')

def compare_negotiate(request):
    qs = TenderRaise.objects.all().order_by('-id')
    context = {'tenders':qs}
    return render(request,'dashboard/tender_compare_negotiate.html',context)

def new_negotiation_of_tender(request,pk):
    id = request.GET.get('id')
    # qss = TenderRaise.objects.get(pk = id)
    # print("last page",qss.id)
    qss = TenderRaise.objects.get(pk=pk)
    form = TenderForm(instance=qss)
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = TenderForm(request.POST,instance=qss)
        ngt_qty = request.POST['negotiate_quantity']
        print(type(ngt_qty))
        print(type(qss.total_product_quantity))
        if form.is_valid():
            qs = form.save(commit=False)
            # qs.tender_status = "Negotiated"
            qs.save()
            qss.total_product_quantity = qss.total_product_quantity+int(ngt_qty)
            qss.save()
            return redirect('compare-list-particular-tender',id)
    context = {'form':form}
    return render(request,'dashboard/new_negotiation_tender_form.html',context)

def tender_accept(request):
    if request.method == "GET":
        id = request.GET.get('name')
        print("now accessing the name in accept",id)
        pk = request.GET['pk']
        qs = TenderRaise.objects.get(pk=pk)
        qs.tender_status = "Accepted"
        qs.save()
        return redirect('tender_fill_list')

def tender_reject(request):
    if request.method == "GET":
        # import pdb
        # pdb.set_trace()
        pk = request.GET['pk']
        qs = TenderRaise.objects.get(pk=pk)
        qs.tender_status = "Rejected"
        qs.save()
        return redirect('tender_fill_list')

def new_accept(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = TenderRaise.objects.get(pk=pk)
    qs.tender_status = "Accepted"
    qs.save()
    # return redirect('tender_fill_list')
    return redirect('compare-list-particular-tender',id)

def new_reject(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = TenderRaise.objects.get(pk=pk)
    qs.tender_status = "Rejected"
    qs.save()
    # return redirect('tender_fill_list')
    return redirect('compare-list-particular-tender',id)

def negotiate(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = TenderRaise.objects.get(pk=pk)
    qs.tender_status = "Negotiated"
    qs.save()
    return redirect('compare-list-particular-tender',id)

def pre_purchase_requisition_for_related_tender(request,pk):
    qs = TenderProduct.objects.get(pk=pk)
    total_product_quantity_by_vendor = TenderRaise.objects.filter(tender_product_id = pk,tender_status="Accepted")
    # print(total_product_quantity_by_vendor.amount_range)
    for amount in total_product_quantity_by_vendor:
        print(amount.amount_range)
    context = {"tender":qs,'pk':pk}
    return render(request,'dashboard/pre_purchase_for_one_tender_main.html',context)

def purchase_requisition_for_one_tender(request,pk):
    # id = request.GET.get('id')
    qs = TenderRaise.objects.filter(tender_product_id = pk,tender_status="Accepted")
    print(qs)
    context = {'accepted':qs,'pk':pk}
    return render(request,'dashboard/purchase_requisition_for_one_tender.html',context)

def accepted_tender_firm(request):
    tenders = FinalProductFromTender.objects.all().order_by('-id')
    print("final tender",tenders)
    context = {'accepted':tenders}
    return render(request,'dashboard/accepted_tender_list.html',context)

def final_tender_product(request):
    pk = request.GET.get('tender_id')
    qs = TenderRaise.objects.get(pk=pk)
    print(qs.tender_product)
    form = FinalTenderProductForm(initial={'final_tender_product':qs})
    if request.method == "POST":
        form = FinalTenderProductForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.save()
            return redirect('tender_compare_negotiate_list')
    context = {'form':form}
    return render(request,'dashboard/negotiation_form.html',context)

def bulk_order(request):
    pk = request.GET.get('firm_id')
    qs = FinalProductFromTender.objects.get(pk=pk)
    print("firm name",qs)
    form = BulkOrderForm(initial={'tender_firm':qs,'product_name':qs})
    if request.method == "POST":
        form = BulkOrderForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.save()
            return redirect('accepted-tender-firm')
    context = {'form':form}
    return render(request,'dashboard/bulk_order_form.html',context)

def bulk_order_list(request):
    qs = PrePurchaseBreakupOrder.objects.all()
    context = {'bulks':qs}
    return render(request,'dashboard/bulk_order_list.html',context)

def create_tender(request):
    page_name = "Create New Invitation E-Tender"
    form = CreateTenderForm()
    if request.method == "POST":
        form = CreateTenderForm(request.POST,request.FILES)
        print(request.POST)
        # import pdb
        # pdb.set_trace()
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.active = False
            qs.save()
            # return redirect('tender_display')
            return redirect('created-tender-edit-from-admin')
    context = {'form':form,'page_name':page_name}
    return render(request,'dashboard/create_tender.html',context)
    

def update_created_tender(request,pk):
    page_name = "Update Newest Created E-Tender"
    instances = TenderProduct.objects.get(pk=pk)
    print(instances)
    form = CreateTenderForm(instance=instances)
    if request.method == "POST":
        form = CreateTenderForm(request.POST,request.FILES,instance=instances)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.updated_by = request.user
            qs.active = False
            qs.save()
            return redirect('tender_display')
    context = {'page_name':page_name,'form':form}
    return render(request,'dashboard/create_tender.html',context)


def new_tender_edit_from_Admin(request):
    qs = TenderProduct.objects.filter(active=False).order_by('-id')
    context = {'tenders':qs}
    return render(request,'dashboard/new_raised_tender_edit_from_admin.html',context)

def approvedToOpenForTender(request):
    if request.method == "GET":
        import pdb
        pdb.set_trace()
        pk = request.GET['id']
        qs = TenderProduct.objects.get(pk=pk)
        print(qs)
        qs.active = True
        qs.save()
        return redirect('created-tender-edit-from-admin')

def create_pre_purchase_order_breakup(request,pk):
    page_name = "Purchase Breakup Monthwise"
    id = request.GET.get('id')
    tpdt_qs = TenderProduct.objects.get(pk=id)
    print(tpdt_qs)
    # pk = request.GET.get('firm_id')
    # print("Tender id",id)
    # print(pk)
    qss = TenderRaise.objects.get(pk=pk)
    print(qss)
    form = PrePurchaseBreakupOrderForm(initial= {'tender_product':qss,'company_name':qss.company_name,'total_product_count':qss.total_product_quantity})
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = PrePurchaseBreakupOrderForm(request.POST)
        pdt_count = request.POST['product_count']
        # new_pdt = int(pdt_count)
        # print(type(new_pdt))
        print(type(qss.amount_range))
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qss.total_product_quantity = int(qss.total_product_quantity) - int(pdt_count)
            tpdt_qs.total_product_quantity_by_vendor = int(tpdt_qs.total_product_quantity_by_vendor)-int(pdt_count)
            qs.save()
            qss.save()
            tpdt_qs.save()
            return redirect('purchase-requisition-etender',id)

    context = {'page_name':page_name,'form':form}
    return render(request,'dashboard/create_pre_purchase_breakup.html',context)

def order_breakup(request,pk):
    try:
        id = request.GET.get('id')
        print('sjdjsa',pk)
        order_breakups = PrePurchaseBreakupOrder.objects.filter(tender_product__id=pk)
        # qss = BulkOrderToTenderFirm.objects.get(pk=pk)
        print(order_breakups)
    except:
        pass
    context = {'order_breakups':order_breakups}
    return render(request,'dashboard/related_breakup.html',context)

def total_supply_order(request):
    total_supplies = PrePurchaseBreakupOrder.objects.all()
    context = {'total_supplies':total_supplies}
    return render(request,'dashboard/total_supply_order.html',context)


def OrderForVendor(request):
    if request.method == "GET":
        pk = request.GET['pk']
        qs = PrePurchaseBreakupOrder.objects.get(pk=pk)
        qs.order_status = "Sent To Vendor"
        qs.save()
        return redirect('total-supply-order')

def purchase_order(request):
    total_supplies = PrePurchaseBreakupOrder.objects.filter(order_status="Sent To Vendor")
    context = {'total_supplies':total_supplies}
    return render(request,'dashboard/purchase_order_vendor.html',context)

def recieved_products(request):
    qs = TenderRaise.objects.filter(tender_status = "Accepted")
    print(qs)
    context = {'tender_firms':qs}
    return render(request,'dashboard/recieved_products.html',context)

def firm_detail_for_etender(request,pk):
    # qs = TenderRaise.objects.get(pk=pk)
    # print(qs.id)
    try:
        qss = RecievedProducts.objects.filter(tender_product__id = pk)
        print(qss)
    except:
        pass
    context = {'pk':pk,'tender_firms':qss}
    return render(request,'dashboard/firm_detail_for_etender.html',context)

def create_recieved_product(request):
    id = request.GET.get('id')
    qs = TenderRaise.objects.get(pk=id)
    print(qs,qs.company_name)
    form = RecievedProductForm(initial={'tender_product':qs,'company_name':qs.company_name})
    if request.method == "POST":
        form = RecievedProductForm(request.POST)
        if form.is_valid():
            ss = form.save(commit=False)
            ss.save()
            return redirect('firm-detail-for-etender',id)
    context = {'form':form}
    return render(request,'dashboard/product_recieved_form.html',context)

def detail_of_recieved_product(request,pk):
    qs = RecievedProducts.objects.get(pk=pk)
    print(qs)
    context = {}
    return render(request,'dashboard/details_recieved_product.html',context)

def recieved_product_accept(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = RecievedProducts.objects.get(pk=pk)
    qs.tender_status = "Accepted"
    qs.save()
    # return redirect('tender_fill_list')
    return redirect('firm-detail-for-etender',id)

def recieved_product_reject(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = RecievedProducts.objects.get(pk=pk)
    qs.tender_status = "Rejected"
    qs.save()
    # return redirect('tender_fill_list')
    return redirect('firm-detail-for-etender',id)


from django.db.models import Q
def rejected_products(request):
    qs = RecievedProducts.objects.filter(
        Q(tender_status='Rejected') |
        Q(tender_status='On Exchange') |
        Q(tender_status='Exchanged') 
    )
    print(qs)
    context = {'tender_firms':qs}
    return render(request,'dashboard/recieved_rejcted_product.html',context)

def exchange_rejected_product(request):
    pk = request.GET.get('id')
    qs = RecievedProducts.objects.get(pk=pk)
    form = ExchangeRejectedProductForm(instance=qs)
    if request.method == "POST":
        form = ExchangeRejectedProductForm(request.POST,instance=qs)
        if form.is_valid():
            qss = form.save(commit=False)
            qss.tender_status = "Exchanged"
            qss.save()
            return render('product-recieved-rejected')
    context = {'form':form}
    return render(request,'dashboard/exchange_rejected_product_form.html',context)

def recieved_product_exchange(request,pk):
    id = request.GET.get('id')
    print(id)
    qs = RecievedProducts.objects.get(pk=pk)
    qs.tender_status = "On Exchange"
    qs.save()
    # return redirect('tender_fill_list')
    return redirect('product-recieved-rejected')



'''
Begining of Store Keeping Unit
1. Management of store capacity and infrastucture and rack design.
2. Store location will vary location wise.
'''

def store_list(request):
    qs = StoreKeepingUnit.objects.all()
    context = {'stores':qs}
    return render(request,'dashboard/store_list.html',context)


def store_creation(request):
    page_name = "Store Creation Form"
    form = StoreKeepingUnitForm()
    if request.method == "POST":
        form = StoreKeepingUnitForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.created_by = request.user
            qs.save()
            return redirect('store-list')
    context = {'form':form,'page_name':page_name}
    return render(request,'dashboard/store_creation_form.html',context)

def update_store_creation(request,pk):
    page_name = "Update Store Creation Form"
    qss = StoreKeepingUnit.objects.get(pk=pk)
    form = StoreKeepingUnitForm(instance=qss)
    if request.method == "POST":
        form = StoreKeepingUnitForm(request.POST,instance=qss)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.updated_by = request.user
            qs.save()
            return redirect('store-list')
    context = {'form':form,'page_name':page_name}
    return render(request,'dashboard/store_creation_form.html',context)

def product_addition_in_store(request,pk):
    page_name = "Product Addition Form"
    qs = StoreKeepingUnit.objects.get(pk=pk)
    print(qs)
    form = ProductInStoreForm(initial={'store':qs})
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        form = ProductInStoreForm(request.POST)
        if form.is_valid():
            qs = form.save(commit=False)
            qs.added_by = request.user
            qs.save()
            return redirect('store-list')
    context = {'form':form,'page_name':page_name}
    return render(request,'dashboard/product_addition_form.html',context)

def product_updated_list(request):
    qs = ProductInStore.objects.filter(product_status = "Active")
    context = {'products':qs}
    return render(request,'dashboard/updated_product_list.html',context)

def product_all_list(request):
    qs = ProductInStore.objects.all()
    context = {'products':qs}
    return render(request,'dashboard/all_product_list.html',context)