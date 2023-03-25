from upa.admin import ChangeOperationModeRecordAdmin
from django.http.response import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
# from django.core.urlresolvers import resolve
# Create your views here.
from django.contrib.auth.models import User
from .models import *
from .forms import *
import inflect

class UPABasicDetailView(LoginRequiredMixin, View):

    # @has_permissions_check(perms=['users.employee_management'])
    def dispatch(self, request, *args, **kwargs):
        return super(UPABasicDetailView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        ref_no = None
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = BasicDetails.objects.get(user_id=profile.id)
            print(instance)
            form = BasicDetailsForm(instance=instance)
        except:
            print("except part is running")
            try:
                print("try in except part is running")
                ref_no = request.GET.get('ref_no')
                uid_no = Enrollment.objects.get(reference_no = ref_no)
                print("this is uid no",uid_no.sponsor_uid_no)
                prof = Profile.objects.get(uid_no = uid_no.sponsor_uid_no)
                print(prof.uid_no)
                form = BasicDetailsForm(initial={'sponsor_uid':prof.uid_no})
            except:
                print("except in except part is running")
                form = BasicDetailsForm()
                pass

        context = {'form':form,'profile':profile,'ref_no':ref_no}
        return render(request, 'upa/basic_details.html', context)

    def post(self, request, *args, **kwargs):
        current_url = request.resolver_match.url_name
        print(current_url)
        id = request.POST.get('id')
        print(id)
        profile = Profile.objects.get(id=kwargs['id'])
        # form = BasicDetailsForm(request.POST)
        
        try:
            instance = BasicDetails.objects.get(user_id = profile.id)
            form = BasicDetailsForm(request.POST,instance=instance)
        except:
            form = BasicDetailsForm(request.POST)
            pass
        print(request.POST['sponsor_uid'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('personal-form',profile.id)
        else:
            print(form.errors)
            messages.error(request,'You cannot use this UID No.')
            context = {'form': form,'profile':profile,}
            return render(request, 'upa/basic_details.html', context)

class PersonalInformationView(LoginRequiredMixin, View):

    # @has_permissions_check(perms=['users.employee_management'])
    def dispatch(self, request, *args, **kwargs):
        return super(PersonalInformationView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        # id = request.GET.get('id')
        # print(id)
        # user = User.objects.get(id=kwargs['id'])
        # print(user.id)
        profile = Profile.objects.get(id=kwargs['id'])
        print(profile.id)
        
        try:
            instance = PersonalInformation.objects.get(user_id=profile.id)
            form = PersonalInformationForm(instance=instance)
        except:
            form = PersonalInformationForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request, 'upa/personal_information.html', context)

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(id=kwargs['id'])
        profile = Profile.objects.get(id=kwargs['id'])
        
        try:
            instance = PersonalInformation.objects.get(user_id = profile.id)
            form = PersonalInformationForm(request.POST,instance=instance)
        except:
            form = PersonalInformationForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('address-form',profile.id)
        else:
            context = {'form': form,'profile':profile,}
            return render(request, 'upa/personal_information.html', context)

class AddressView(LoginRequiredMixin, View):

    # @has_permissions_check(perms=['users.employee_management'])
    def dispatch(self, request, *args, **kwargs):
        return super(AddressView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(id=kwargs['id'])
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = UPAAddress.objects.get(user_id=profile.id)
            form = UPAAddressForm(instance=instance)
        except:
            form = UPAAddressForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request, 'upa/address_detail.html', context)

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(id=kwargs['id'])
        profile = Profile.objects.get(id=kwargs['id'])
        
        try:
            instance = UPAAddress.objects.get(user_id = profile.id)
            form = UPAAddressForm(request.POST,instance=instance)
        except:
            form = UPAAddressForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('additional-form',profile.id)
        else:
            context = {'form': form,'profile':profile,}
            return render(request, 'upa/personal_information.html', context)

class AdditionalView(LoginRequiredMixin, View):

    # @has_permissions_check(perms=['users.employee_management'])
    def dispatch(self, request, *args, **kwargs):
        return super(AdditionalView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # user = User.objects.get(id=kwargs['id'])
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = AdditionalDetails.objects.get(user_id=profile.id)
            form = AdditionalDetailForm(instance=instance)
        except:
            form = AdditionalDetailForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request, 'upa/additional_details.html', context)

    def post(self, request, *args, **kwargs):
        # user = User.objects.get(id=kwargs['id'])
        profile = Profile.objects.get(id=kwargs['id'])
        
        try:
            instance = AdditionalDetails.objects.get(user_id = profile.id)
            form = AdditionalDetailForm(request.POST,instance=instance)
        except:
            form = AdditionalDetailForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('upa-identity-form',profile.id)
        else:
            context = {'form': form,'profile':profile,}
            return render(request, 'upa/personal_information.html', context)

class UPAIdentityView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(UPAIdentityView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = UPAIdentityProof.objects.get(user_id = profile.id)
            form = UPAIdentityProofForm(instance=instance)
        except:
            form = UPAIdentityProofForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request,'upa/upa_identity_proof.html',context)

    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = UPAIdentityProof.objects.get(user_id = profile.id)
            form = UPAIdentityProofForm(request.POST,instance=instance)
        except:
            form = UPAIdentityProofForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save() 
            return redirect('beneficiary-details-form',profile.id)
        else:
            print(form.errors)
        context = {'form':form,'profile':profile}
        return render(request,'upa/upa_idenity_proof.html',context)

class BeneficiaryDetailsView(LoginRequiredMixin,View):
    def dispatch(self, request, *args,**kwargs):
        return super(BeneficiaryDetailsView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = BeneficiaryDetails.objects.get(user_id = profile.id)
            form = BeneficiaryDetailsForm(instance=instance)
        except:
            form = BeneficiaryDetailsForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request,'upa/beneficiary_details.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = BeneficiaryDetails.objects.get(user_id = profile.id)
            form = BeneficiaryDetailsForm(request.POST,instance=instance)
        except:
            form = BeneficiaryDetailsForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('sponsor-details-form',profile.id)
        else:
            print(form.errors)
        context = {'form':form,'profile':profile}
        return render(request,'upa/beneficiary_details.html',context)

class SponsorIntruductionView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(SponsorIntruductionView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = SponsorIntroductionDetail.objects.get(user_id = profile.id)
            form = SponsorIntroductionDetailForm(instance=instance)
        except:
            form = SponsorIntroductionDetailForm()
            pass
        context = {'form':form,'profile':profile}
        return render(request,'upa/sponsor_introduction_detail.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = SponsorIntroductionDetail.objects.get(user_id = profile.id)
            form = SponsorIntroductionDetailForm(request.POST,instance=instance)
        except:
            form = SponsorIntroductionDetailForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('service-required-form',profile.id)
        else:
            print(form.errors)
        context = {'form':form,'profile':profile}
        return render(request,'upa/sponsor_introduction_detail.html',context)

class ServiceRequiredView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ServiceRequiredView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        upa_type = UPAIdentityProof.objects.filter(user_id = profile.id)
        for upa_type in upa_type:
            print("checking upa type->",upa_type.upa_type)
        charges = BussinessCardFees.objects.filter()
        for charge in charges:
            green = charge.green_bussiness_card
            yellow = charge.yellow_bussiness_card
            red = charge.red_chip_bussiness_card
            account_passbook = charge.account_passbook
            e_account_statement = charge.e_account_statement
            vc_general = charge.vc_general
            vc_pvc = charge.vc_pvc
            green_atm = charge.green_atm_charge
            yellow_atm = charge.yellow_atm_charge
            red_atm = charge.red_atm_charge
            blue_atm = charge.blue_atm_charge
            pass
        try:
            instance = ServiceRequired.objects.get(user_id = profile.id)
            form = ServiceRequiredForm(instance = instance,initial={
                                                                    'green_card_charge':green,
                                                                    'yellow_card_charge':yellow,
                                                                    'red_card_charge':red,
                                                                    'account_passbook_charge':account_passbook,
                                                                    'e_account_statement_charge':e_account_statement,
                                                                    'general_color_charge':vc_general,
                                                                    'pvc_color_charge':vc_pvc,
                                                                    'green_atm_card_charge':green_atm,
                                                                    'yellow_atm_card_charge':yellow_atm,
                                                                    'red_atm_card_charge':red_atm,
                                                                    'blue_atm_card_charge':blue_atm,
                                                                    })
        except:
            form = ServiceRequiredForm(initial={
                                                'green_card_charge':green,
                                                'yellow_card_charge':yellow,
                                                'red_card_charge':red,
                                                'account_passbook_charge':account_passbook,
                                                'e_account_statement_charge':e_account_statement,
                                                'general_color_charge':vc_general,
                                                'pvc_color_charge':vc_pvc,
                                                'green_atm_card_charge':green_atm,
                                                'yellow_atm_card_charge':yellow_atm,
                                                'red_atm_card_charge':red_atm,
                                                'blue_atm_card_charge':blue_atm,
                                                })
            pass
        context = {'form':form,'profile':profile,'upa_type':upa_type}
        return render(request,'upa/service_required.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = ServiceRequired.objects.get(user_id = profile.id)
            form = ServiceRequiredForm(request.POST,instance=instance)
        except:
            form = ServiceRequiredForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('operation-mode-form',profile.id)
        else:
            print(form.errors)
        context = {'form':form,'profile':profile}
        return render(request,'upa/service_required.html',context)

class OperationModeView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(OperationModeView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            services = ServiceRequired.objects.filter(user_id=profile.id)
            
            total = 0
            charges = []
            for service in services:
                ####  bussiness card s
                if service.royal_green_card == "Yes" or "":
                    print("green_card_s->",service.green_card_charge)
                    charges.append(int(service.green_card_charge))
                if service.royal_yellow_card == "Yes" or "":
                    print("yellow card charge->",service.yellow_card_charge)
                    charges.append(int(service.yellow_card_charge))
                if service.royal_red_card == "Yes" or "":
                    print("red card charge->",service.red_card_charge)
                    charges.append(int(service.red_card_charge))
                # visiting card charge
                if service.general_color_card == "Yes" or "":
                    print("visiting card->",service.general_color_charge)
                    charges.append(int(service.general_color_charge))
                if service.pvc_color_card == "Yes" or "":
                    print("pvc color card->",service.pvc_color_charge)
                    charges.append(int(service.pvc_color_charge))
                # account section charge
                if service.accouont_passbook == "Yes" or "":
                    print("passbook charge->",service.account_passbook_charge)
                    charges.append(int(service.account_passbook_charge))
                if service.e_account_statement == "Yes" or "":
                    print("e statement charge->",service.e_account_statement_charge)
                    charges.append(int(service.e_account_statement_charge))
                if service.royal_green_atm == "Yes" or "":
                    print("green atm charge->",service.green_atm_card_charge)
                    charges.append(int(service.green_atm_card_charge))
                if service.royal_yellow_atm == "Yes" or "":
                    print("yellow atm charge->",service.yellow_atm_card_charge)
                    charges.append(int(service.yellow_atm_card_charge))
                if service.royal_red_atm == "Yes" or "":
                    print("red atm charge->",service.red_atm_card_charge)
                    charges.append(int(service.red_atm_card_charge))
                if service.royal_blue_atm == "Yes" or "":
                    print("blue atm charge->",service.blue_atm_card_charge)
                    charges.append(int(service.blue_atm_card_charge))
                else:
                    print("no it is not yes")
            print("Main charge->",charges)
            for charge in range(0,len(charges)):
                total = total+charges[charge]
            print(total)
            charge_in_words = inflect.engine()
            in_word = charge_in_words.number_to_words(total)
            print("charges in word->",in_word)
            instance = OperationMode.objects.get(user_id = profile.id)
            form = OperationModeForm(instance = instance,initial={'total_amount':total,'amount_in_figure':in_word.upper()})
            
        except:
            form = OperationModeForm(initial={'total_amount':total,'amount_in_figure':in_word.upper()})
            
            pass
        context = {'form':form,'profile':profile}
        return render(request,'upa/operation_mode.html',context)

    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = OperationMode.objects.get(user_id = profile.id)
            form = OperationModeForm(request.POST,instance=instance)
        except:
            form = OperationModeForm(request.POST)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('verification-form', profile.id)
        else:
            print(form.errors)
        context = {'form':form,'profile':profile}
        return render(request,'upa/operation_mode.html',context)

class VerificationView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(VerificationView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = Verification.objects.get(user_id = profile.id)
            form = VerificationForm(instance=instance)
        except:
            form = VerificationForm(initial={'applicant_name':profile.user.username})
            pass
        context = {'form':form,'profile':profile}
        return render(request,'upa/verifcation_form.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            instance = Verification.objects.get(user_id = profile.id)
            form = VerificationForm(request.POST,request.FILES,instance=instance)
        except:
            form = VerificationForm(request.POST,request.FILES)
            pass
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('thank-you')
        context = {'form':form,'profile':profile}
        return render(request,'upa/verficaton_form.html',context)





def thank_you(request):
    user_id = request.user.id
    return render(request,'thank_you.html')

def error_500(request):
    data = {
        'error':"You cannot use this UID",
    }
    return render(request, '500.html', status=500)

def error_404(request,exception):
    data = {}
    return render(request, '404.html', data)

class EnrollmentView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(EnrollmentView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = EnrollmentForm()
        context = {'form':form,'profile':profile}
        return render(request,'upa/enrollment_form.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = profile
            instance.save()
            return redirect('/')
        context = {'form':form,'profile':profile}
        return render(request,'upa/enrollment_form.html',context)

class ChangeAddressView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ChangeAddressView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try: 
            add = UPAAddress.objects.get(user_id = profile.id)
        except UPAAddress.DoesNotExist:
            add= None
        form = ChangeAddressRecordForm(instance=add)
        context = {'form':form}
        return render(request,'upa/change_address_form.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = ChangeAddressRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_admin = request.user
            instance.upa =profile
            instance.save()
            return redirect('/')
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_address_form.html',context)

class ChangeAdditionalRecordView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ChangeAdditionalRecordView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*arsgs,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            additional = AdditionalDetails.objects.get(user_id = profile.id)
        except AdditionalDetails.DoesNotExist:
            additional = None
        form = ChangeAdditionalRecordForm(instance=additional)
        context = {'form':form}
        return render(request,'upa/change_additional_form.html',context)

    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = ChangeAdditionalRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_admin = request.user
            instance.upa = profile
            instance.save()
            return redirect('changes-request-status')
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_additional_form.html',context)

class ChangeBeneficiaryRecordView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ChangeBeneficiaryRecordView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            bene = BeneficiaryDetails.objects.get(user_id = profile.id)
        except BeneficiaryDetails.DoesNotExist:
            bene = None
        form = BeneficiaryDetailsForm(instance=bene)
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_beneficiary_form.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = ChangeBeneficiaryRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_admin = request.user
            instance.upa = profile
            instance.save()
            return redirect('changes-request-status')
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_beneficiary_form.html',context)

class ChangeServiceRequiredRecordView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ChangeServiceRequiredRecordView,self).dispatch(request, *args, **kwargs)

    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            ser = ServiceRequired.objects.get(user_id = profile.id)
        except ServiceRequired.DoesNotExist:
            ser = None
        form = ChangeServiceRequiredRecordForm(instance=ser)
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_service_required_form.html',context)
    
    def post(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        form = ChangeServiceRequiredRecordForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user_admin = request.user
            instance.upa = profile
            instance.save()
            return redirect('changes-request-status')
        context = {'form':form,'profile':profile}
        return render(request,'upa/change_service_required_form.html',context)

class ChangeOperationModeRecordView(LoginRequiredMixin,View):
    def dispatch(self, request, *args, **kwargs):
        return super(ChangeOperationModeRecordView,self).dispatch(request, *args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(id=kwargs['id'])
        try:
            oper = OperationMode.objects.get(user_id = profile.id)
        except OperationMode.DoesNotExist:
            oper = None
        form = ChangeOperationModeRecordForm(instance=oper)
        context = {'form':form}
        return render(request,'upa/change_operation_mode_form.html',context)