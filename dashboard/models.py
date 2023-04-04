from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.db.models.base import Model, ModelState
from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.


class UPAChangeRequest(models.Model):
    REQUEST_STATUS = (
        ('Pending','Pending'),
        ('Read','Read'),
    )
    FORM_TYPE = (
        ('Address Form', 'Address Form'),
        ('Additional Detail Form', 'Additional Detail Form'),
        ('Beneficiary Detail Form', 'Beneficiary Detail Form'),
        ('Service Required Form', 'Service Required Form'),
        ('Operation Mode Form', 'Operation Mode Form'),
    )
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="changes_request")
    upa_id = models.CharField(max_length=20,blank=True, null=True)
    subject = models.CharField(max_length=100,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    request_no = models.PositiveIntegerField(blank=True, null=True)
    request_date = models.DateField(auto_now=True,blank=True, null=True)
    form_name = models.CharField(max_length=25,choices=FORM_TYPE,default="",blank=True, null=True)
    status = models.CharField(max_length=20,choices=REQUEST_STATUS,default="Pending",blank=True, null=True)
    reply_message = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.user}'

    def save(self,*args,**kwargs):
        initial = 100
        val = UPAChangeRequest.objects.all().count()
        self.request_no = initial + (int(val)+1)
        super(UPAChangeRequest,self).save(*args,**kwargs)


class IncomeSetting(models.Model):

    CHILD_TYPE = (
        ('N/A','N/A'),
        ('Normal','Normal'),
        ('BPL','BPL'),
        ('Handicap','Handicap')
    )
    
    created_by              = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='income_setting')
    updated_by              = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='income_setting_update')
    child_one               = models.CharField(max_length=15,choices=CHILD_TYPE,blank=True, null=True)
    child_two               = models.CharField(max_length=15,choices=CHILD_TYPE,blank=True, null=True)
    child_three             = models.CharField(max_length=15,choices=CHILD_TYPE,blank=True, null=True)
    income                  = models.PositiveIntegerField(default=0,blank=True, null=True)
    previous_income         = models.PositiveIntegerField(default=0,blank=True, null=True)
    created_date            = models.DateField(auto_now_add=True)
    updated_date            = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.created_by}"

class IncomeSettingForWomenOld(models.Model):
    CATEGORY_TYPE = (
        ('N/A','N/A'),
        ('BPL','BPL'),
        ('Handicap','Handicap'),
        ('Child Below 18', 'Child Below 18'),
        ('Mature Female', 'Mature Female'),
        ('Senior Citizen', 'Senior Citizen')
    )

    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='income_setting_for_old_women')
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name='income_setting_for_old_women_update')
    category_type = models.CharField(max_length=15,choices=CATEGORY_TYPE,blank=True, null=True)
    income = models.PositiveIntegerField(default=0,blank=True, null=True)
    previous_income_for_women_old = models.PositiveIntegerField(default=0,blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.created_by}"

    class Meta:
        verbose_name = "Income Setting For Women And Old"
        verbose_name_plural = "Income Setting For Women And Old"

class FirmRegistration(models.Model):
    FIRM_STATUS = (
        ('Registered','Registered'),
        ('Unregistered','Unregistered'),
    )
    FIRM_MODE = (
        ('Manufacturer','Manufacturer'),
        ('Dealer','Dealer'),
        ('Supplier','Supplier'),
        ('Agency','Agency'),
        ('Shopkeeper','Shopkeeper'),
        ('Exporter','Exporter'),
        ('Exporter','Exporter'),
        ('Contractor','Contractor'),
        ('Farmer','Farmer'),
    )
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='firm_registration')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True,related_name='update_firm_registration')
    updated_at = models.DateTimeField(auto_now=True)
    active_firm = models.BooleanField(default=True)
    gst_no = models.CharField(max_length=20,blank=True, null=True)
    status = models.CharField(max_length=12,default="Unregistered",choices=FIRM_STATUS,blank=True, null=True)
    firm_name = models.CharField(max_length=200,blank=True, null=True,help_text="Enter The Firm Name")
    firm_image = models.ImageField(upload_to = "firm/image/",blank=True, null=True)
    address_one = models.CharField(max_length=100,blank=True, null=True)
    address_two = models.CharField(max_length=100,blank=True, null=True)
    address_three = models.CharField(max_length=100,blank=True, null=True)
    address_four = models.CharField(max_length=100,blank=True, null=True)
    landmark = models.CharField(max_length=100,blank=True, null=True)
    town_city = models.CharField(max_length=100,blank=True, null=True)
    sub_district = models.CharField(max_length=100,blank=True, null=True)
    district = models.CharField(max_length=100,blank=True, null=True)
    postal_code = models.IntegerField(blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.CharField(max_length=100,blank=True, null=True)
    firm_mode = models.CharField(max_length=12,choices=FIRM_MODE,blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    contact_person = models.CharField(max_length=200,blank=True, null=True)
    contact_person_mobile = models.CharField(max_length=12,blank=True, null=True)



    def __str__(self):
        return f"{self.firm_name}"


class TenderProduct(models.Model):
    tender_product_no = models.PositiveIntegerField(unique=True,blank=True, null=True)
    product_image = models.ImageField(upload_to = "tender_product/image/",blank=True, null=True)
    product_name = models.CharField(max_length=200,blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=False,blank=True, null=True)
    tender_date = models.DateTimeField(blank=True, null=True)
    tender_product_quantity = models.PositiveIntegerField(blank=True, null=True)
    total_product_quantity_by_vendor = models.IntegerField(blank=True, null=True,default=0)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name="create_tender")
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name="update_tender")

    def __str__(self):
        return f'{self.product_name}'

    @property
    def tenderImageURL(self):
        try:
            url = self.product_image.url
        except:
            url = ""
        return url 
    
        

class TenderRaise(models.Model):

    TENDER_STATUS = (
        ('Pending','Pending'),
        ('Rejected','Rejected'),
        ('Accepted','Accepted'),
        ('Negotiated','Negotiated'),
    )

    tender_product = models.ForeignKey(TenderProduct,on_delete=models.SET_NULL,blank=True, null=True)
    company_name = models.CharField(max_length=200,blank=True, null=True)
    company_address = models.CharField(max_length=200,blank=True, null=True)
    contact_person = models.CharField(max_length=200,blank=True, null=True)
    amount_range = models.CharField(max_length=100,blank=True, null=True) # product quantity
    fixed_amount = models.PositiveIntegerField(blank=True, null=True) # product amount for sell.
    negotiate_quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    negotiate_price = models.PositiveIntegerField(default=0,blank=True, null=True)
    total_product_quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    contact_mobile = models.CharField(max_length=12,blank=True, null=True)
    tender_status = models.CharField(max_length=10,choices=TENDER_STATUS,default="Pending",blank=True, null=True)
    negotiation_update = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return f'{self.tender_product}'
    
    def save(self,*args,**kwargs):
        if not self.pk:
            if self.tender_status == "Pending":
                qs = TenderProduct.objects.filter(pk=self.tender_product_id)
                # print(qs.tender_product_no)
                for i in qs:
                    print(i.tender_product_no)
                    tpd_amnt = i.total_product_quantity_by_vendor
                    print(type(tpd_amnt))
                    i.total_product_quantity_by_vendor = int(self.amount_range) + tpd_amnt
                    i.save()
                # qs.total_product_quantity_by_vendor = self.amount_range + qs.total_product_quantity_by_vendor
            else:
                pass
                # qs = TenderProduct.objects.filter(pk=self.tender_product_id)
                # for i in qs:
                #     tpd_amnt = i.total_product_quantity_by_vendor
                #     i.total_product_quantity_by_vendor = int(self.negotiate_quantity) + tpd_amnt
                #     i.save()
        if self.pk:
            if self.tender_status == "Negotiated":
                qs = TenderProduct.objects.filter(pk=self.tender_product_id)
                for i in qs:
                    tpd_amnt = i.total_product_quantity_by_vendor
                    i.total_product_quantity_by_vendor = int(self.negotiate_quantity)+tpd_amnt
                    i.save()
        super().save(*args,**kwargs)
    
class FinalProductFromTender(models.Model):
    final_tender_product = models.ForeignKey(TenderRaise,on_delete=models.SET_NULL,blank=True, null=True)
    negotiated_quantity = models.PositiveIntegerField(blank=True, null=True)
    negotiated_price = models.PositiveIntegerField(blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    created_date = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"Product {self.final_tender_product} quantity {self.negotiated_quantity}"

# Pre-Purchase Order Creation
class BulkOrderToTenderFirm(models.Model):
    BULK_ORDER_STATUS = (
        ('Order Pending','Order Pending'),
        ('Order On The Way','Order On The Way'),
        ('Order Recieved','Order Recieved'),
    )

    tender_firm = models.ForeignKey(TenderRaise,on_delete=models.SET_NULL,blank=True,null=True)
    product_name = models.CharField(max_length=200,blank=True, null=True)
    product_count = models.PositiveBigIntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=17,choices=BULK_ORDER_STATUS,default="Order Pending",blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.tender_firm}"

class PrePurchaseBreakupOrder(models.Model):
    PRE_PURCHASE_ORDER_TYPE = (
        ('Unsend To Vendor','Unsend To Vendor'),
        ('Sent To Vendor','Sent To Vendor'),
    )
    tender_product = models.ForeignKey(TenderRaise,on_delete=models.SET_NULL,blank=True, null=True)
    company_name = models.CharField(max_length=200,blank=True, null=True)
    product_count = models.PositiveIntegerField(blank=True, null=True)
    total_product_count = models.PositiveIntegerField(blank=True, null=True)
    order_month = models.DateField(blank=True, null=True)
    order_status = models.CharField(max_length=16,choices=PRE_PURCHASE_ORDER_TYPE,default="Unsend To Vendor",blank=True, null=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)
    created_at = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.tender_product}"

    # def save(self,*args,**kwargs):
    #     if not self.pk:
    #         qs = TenderRaise.objects.filter(pk=self.tender_product_id)
    #         for i in qs:
    #             print("tender raise id",i.)
                
    #             # tpd_amnt = i.total_product_quantity_by_vendor
    #             # n.total_product_quantity_by_vendor = int(i.negotiate_quantity)+tpd_amnt
    #             # n.save()
    #     else:
    #         pass
    #     super().save(*args,**kwargs)


class RecievedProducts(models.Model):
    PRODUCT_RECIEVED_STATUS = (
        ('Pending','Pending'),
        ('Rejected','Rejected'),
        ('Accepted','Accepted'),
        ('On Exchange','On Exchange'),
        ('Exchanged','Exchanged'),
    )

    tender_product = models.ForeignKey(TenderRaise,on_delete=models.SET_NULL,blank=True, null=True)
    company_name = models.CharField(max_length=200,blank=True, null=True)
    # company_address = models.CharField(max_length=200,blank=True, null=True)
    # contact_person = models.CharField(max_length=200,blank=True, null=True)
    quantity_by_firm = models.CharField(max_length=100,blank=True, null=True) # product quantity
    product_price = models.PositiveIntegerField(blank=True, null=True) # product amount for sell.
    # negotiate_quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    # negotiate_price = models.PositiveIntegerField(default=0,blank=True, null=True)
    # total_product_quantity = models.PositiveIntegerField(default=0,blank=True, null=True)
    # contact_mobile = models.CharField(max_length=12,blank=True, null=True)
    exchange_quantity = models.PositiveIntegerField(blank=True, null=True)
    tender_status = models.CharField(max_length=13,choices=PRODUCT_RECIEVED_STATUS,default="Pending",blank=True, null=True)
    recieved_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return f"Tender: {self.tender_product} Company : {self.company_name}"



'''
Store Module
'''

class StoreLocationDefinition(models.Model):
    locatio_name = models.CharField(max_length=200,blank=True, null=True)

    def __str__(self):
        return f"{self.locatio_name}"



class StoreKeepingUnit(models.Model):

    STORE_STATUS = (
        ('Active','Active'),
        ('In Active','In Active'),
        ('Closed','Closed')
    )

    location = models.ForeignKey(StoreLocationDefinition,on_delete=models.SET_NULL,blank=True, null=True)
    store_name = models.CharField(max_length=150,blank=True, null=True)
    store_address_one = models.CharField(max_length=100,blank=True, null=True)
    store_address_two = models.CharField(max_length=200,blank=True, null=True)
    store_address_three = models.CharField(max_length=200,blank=True, null=True)
    store_size = models.CharField(max_length=100,blank=True, null=True,help_text="100 x 200")
    no_of_racks = models.IntegerField(default=0, blank=True, null=True)
    avg_section_rack = models.IntegerField(default=1,blank=True, null=True)
    store_Status = models.CharField(max_length=10,blank=True, null=True,choices=STORE_STATUS,default="Active")
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name="created_Store")
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name="updated_store")
    creation_date = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"Store Name : {self.store_name}, Store Location : {self.location}"


class ProductInStore(models.Model):

    PRODUCT_STATUS = (
        ('Active','Active'),
        ('In Active','In Active'),
    )

    store = models.ForeignKey(StoreKeepingUnit,on_delete=models.SET_NULL,blank=True, null=True)
    product_barcode = models.CharField(max_length=100,blank=True, null=True)
    box_name = models.CharField(max_length=100,blank=True, null=True)
    product_name = models.CharField(max_length=100,blank=True, null=True)
    product_names = models.ForeignKey(RecievedProducts,on_delete=models.SET_NULL,blank=True, null=True)
    product_quantity_in_box = models.IntegerField(default=1,blank=True, null=True)
    rack_row = models.IntegerField(blank=True, null=True)
    section_number_on_rack = models.IntegerField(blank=True, null=True)
    rack_and_store_design = models.ImageField(upload_to = "store/drawing/",blank=True, null=True)
    product_status = models.CharField(max_length=10,choices=PRODUCT_STATUS,default="Active",blank=True, null=True)
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name='created_product')
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,related_name='updated_product')
    added_date = models.DateField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"Box Name : {self.box_name}, Product Name : {self.product_name}"
    @property
    def storedesignUrl(self):
        try:
            url = self.rack_and_store_design.url
        except:
            url = ""
        return url