from distutils.command.upload import upload
from email.policy import default
from secrets import choice
from time import time
from unittest.util import _MAX_LENGTH
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import OneToOneField
from accounts.models import Profile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model, ModelState
from django.contrib import messages
from django.core.exceptions import ValidationError
import random
import string
from datetime import date,timedelta
from django.http import HttpResponseServerError
# Create your models here.

# class UPABranch(models.Model):
#     main_upa = OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="upa_branch")
#     left_branch = models.BooleanField(blank=True, null=True)
#     left_upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="left_branch")
#     middle_branch = models.BooleanField(blank=True, null=True)
#     middle_upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="middle_branch")
#     right_branch = models.BooleanField(blank=True, null=True)
#     right_branch = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="right_branch") 


class BasicDetails(models.Model):

    BRANCH_TYPE = (
        ('Test','Test'),
        ('Test_one','Test_one'),
    )
    UPA_TYPE = (
        ('Test','Test'),
        ('Test_one','Test_one'),
    )

    RELATION_UPA = (
        ('Test','Test'),
        ('Test_one','Test_one'),
    )

    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name='basic_details')
    sponsor_uid = models.CharField(max_length=50,blank=True, null=True,verbose_name = "Sponsor UID")
    sponsor_name = models.CharField(max_length=100,blank=True, null=True,verbose_name = "Sponsor Name")
    branch = models.CharField(max_length=50,choices=BRANCH_TYPE,blank=True, null=True,verbose_name="Branch Type")
    upa_type = models.CharField(max_length=50,choices=UPA_TYPE,blank=True, null=True,verbose_name="UPA Type")
    relation_upa = models.CharField(max_length=50,choices=RELATION_UPA,blank=True, null=True,verbose_name="Relation with UPA")
    post_applied = models.CharField(max_length=50,blank=True, null=True,verbose_name="Post Applied For")
    applicant_upa_type = models.CharField(max_length=50,blank=True, null=True,verbose_name="Applicant UPA Type")
    applicant_appl_seq_num = models.CharField(max_length=100,blank=True, null=True,verbose_name="Applicant Application Sequence Number")
    applicant_coll_ref_num = models.CharField(max_length=100,blank=True, null=True,verbose_name="Applicant Collection Refrence Number")
    applicant_reg_seq_num = models.CharField(max_length=100,blank=True, null=True,verbose_name="Applicant Registration Sequence Number")
    applicant_dis_id_number = models.CharField(max_length=100,blank=True, null=True,verbose_name="Applicant Distributor ID(D.I.D) Number")
    full_name = models.CharField(max_length=200,blank=True, null=True,verbose_name="Applicant Full Name")
    # applicant_image = models.ImageField(upload_to = )
    customer_type = models.CharField(max_length=8,choices=(("Normal","Normal"),("BPL","BPL"),("Handicap","Handicap")),blank=True,null=True)
    customer_nature = models.CharField(max_length=40,choices=(("Minor","Minor"),("Mature Female","Mature Female"),("Senior Citizen","Senior Citizen"),("None Of The Above","None Of The Above")),blank=True,null=True)
    customer_nature = models.CharField(max_length=40,choices=(("Minor","Minor"),("Mature Female","Mature Female"),("Senior Citizen","Senior Citizen"),("None Of The Above","None Of The Above")),blank=True,null=True)
    customer_education = models.CharField(max_length=40,choices=(("Educated","Educated"),("Illiterate/Un-educated","Illiterate/Un-educated")),blank=True,null=True)
    customer_work = models.CharField(max_length=15,choices=(("Employee","Employee"),("Un-employed","Un-employed")),blank=True,null=True)
    submission_date = models.DateTimeField(auto_now_add=True,blank=True, null=True,verbose_name="Form Submission Date / Time")

    def __str__(self):
        return f"{self.user}"

    def save(self,*args,**kwargs):
        id = self.sponsor_uid
        profile = Profile.objects.get(uid_no = id)
        user = User.objects.get(id = self.user.user.id)
        if profile.left_branch == False:
            # print("yes left blank")
            # print("im adding in left")
            profile.left_upa = user
            profile.left_branch = True
            profile.save()
        elif profile.middle_branch == False:
            # print("yes middle blank")
            if profile.left_upa == user:
                # print("im in left")
                pass
            else:
                # print("im adding in middle")
                profile.middle_upa = user
                profile.middle_branch = True
                profile.save()
        elif profile.right_branch == False:
            # print("yes blank")
            if profile.middle_upa == user:
                # print("user present in middle")
                pass
            else:
                # print("not present in middle")
                profile.right_upa = user
                profile.right_branch = True
                profile.save()
        elif profile.left_upa == user or profile.middle_upa == user or profile.right_upa == user:
            # print("existing part is running")
            pass
        elif profile.left_branch == True or profile.middle_branch == True or profile.right_branch == True:
            # print("not allowed part is running")
            raise ValueError("You cannot use this UID")
        super(BasicDetails,self).save(*args,**kwargs)

class PersonalInformation(models.Model):

    GENDER_TYPE = (
        ('Male','Male'),
        ('Female','Female'),
    )

    MARITAL_TYPE = (
        ('Married','Married'),
        ('Unmarried','Unmarried'),
    )

    TITLE_TYPE = (
        ('Mr','Mr'),
        ('Ms','Ms'),
        ('Mrs','Mrs'),
    )
    
    GAURDIAN_TYPE = (
        ('Father','Father'),
        ('Husband','Husband'),
        ('Gaurdian','Gaurdian'),
        ('Spouse','Spouse'),
    )
    
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="personal_details")
    personal_title = models.CharField(max_length=3,choices=TITLE_TYPE,default="Mr",blank=True,null=True)
    name = models.CharField(max_length=100,blank=True, null=True,verbose_name="Name")
    first_name = models.CharField(max_length=100,blank=True, null=True,verbose_name="First Name")
    middle_name = models.CharField(max_length=100,blank=True, null=True,verbose_name="Middle Name")
    last_name = models.CharField(max_length=100,blank=True, null=True,verbose_name="Last Name")
    other = models.CharField(max_length=100,blank=True, null=True,verbose_name="Other")
    father_name = models.CharField(max_length=100,blank=True, null=True,verbose_name="Father's Name")
    # husband/gaurdian
    title = models.CharField(max_length=3,choices=TITLE_TYPE,default="Mr",blank=True,null=True)
    gaurdian_type = models.CharField(max_length=10,choices=GAURDIAN_TYPE,blank=True,null=True)
    first_name_hg = models.CharField(max_length=100,blank=True, null=True)
    middle_name_hg = models.CharField(max_length=100,blank=True, null=True)
    gaurdian_name_hg = models.CharField(max_length=100,blank=True, null=True)
    mother_median_name = models.CharField(max_length=200,blank=True, null=True)
    mother_title = models.CharField(max_length=3,choices=TITLE_TYPE, default="Mrs",blank=True,null=True)
    first_name_m = models.CharField(max_length=100,blank=True, null=True)
    middle_name_m = models.CharField(max_length=100,blank=True, null=True)
    last_name_m = models.CharField(max_length=100,blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    update_age_dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE,blank=True, null=True)
    marital_status = models.CharField(max_length=10,choices=MARITAL_TYPE,blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    

    def __str__(self):
        return f"{self.user}"


class UPAAddress(models.Model):
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="address_details")
    # present address
    address_line_one = models.CharField(max_length=100,blank=True, null=True)
    address_line_two = models.CharField(max_length=100,blank=True, null=True)
    address_line_three = models.CharField(max_length=100,blank=True, null=True)
    address_line_four = models.CharField(max_length=100,blank=True, null=True)
    landmark = models.CharField(max_length=100,blank=True, null=True)
    town_city = models.CharField(max_length=100,blank=True, null=True)
    district = models.CharField(max_length=100,blank=True, null=True)
    sub_district = models.CharField(max_length=100,blank=True, null=True)
    postal_zip_code = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.CharField(max_length=100,blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    active_email = models.EmailField(blank=True, null=True)
    std_code = models.PositiveIntegerField(blank=True, null=True)
    isd_code = models.PositiveIntegerField(blank=True, null=True)
    same_as_above = models.BooleanField(default=False)
    # permanent address
    p_address_one = models.CharField(max_length=100,blank=True, null=True)
    p_address_two = models.CharField(max_length=100,blank=True, null=True)
    p_address_three = models.CharField(max_length=100,blank=True, null=True)
    p_address_four = models.CharField(max_length=100,blank=True, null=True)
    p_landmark = models.CharField(max_length=100,blank=True, null=True)
    p_town = models.CharField(max_length=100,blank=True, null=True)
    p_dictrict = models.CharField(max_length=100,blank=True, null=True)
    p_sub_district = models.CharField(max_length=100,blank=True, null=True)
    p_postal_code = models.PositiveIntegerField(blank=True, null=True)
    p_country = models.CharField(max_length=100,blank=True, null=True)
    p_state = models.CharField(max_length=100,blank=True, null=True)
    p_telephone = models.PositiveIntegerField(blank=True, null=True)
    p_mobile = models.PositiveIntegerField(blank=True, null=True)
    p_active_email = models.EmailField(blank=True, null=True)
    p_std_code = models.PositiveIntegerField(blank=True, null=True)
    p_isd_code = models.PositiveIntegerField(blank=True, null=True)
    customer_language = models.CharField(max_length=40,choices=(("English","English"),("Hindi","Hindi")),blank=True,null=True)
    active_mobile = models.CharField(max_length=10,blank=True,null=True)
    active_email = models.EmailField(blank=True,null=True)
    delivery_location = models.CharField(max_length=40, choices=(("Permanent","Permanent"),("Present","Present")),blank=True,null=True)

    def __str__(self):
        return f"{self.user}"

'''
Additional Details
'''

class AdditionalDetails(models.Model):

    RELIGION_TYPE = (
        ('HINDU','HINDU'),
        ('MUSLIM','MUSLIM'),
        ('Other','Other'),
    )

    CATEGORY_TYPE = (
        ('Gen','Gen'),
        ('OBC','OBC'),
        ('SC','SC'),
        ('ST','ST'),
    )

    EMPLOYEMENT_TYPE = (
        ('Yes','Yes'),
        ('No','No'),
    )

    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="additional_details")
    nickname = models.CharField(max_length=100,blank=True, null=True)
    personal_title = models.CharField(max_length=100,blank=True, null=True)
    religion = models.CharField(max_length=10,choices=RELIGION_TYPE,blank=True, null=True)
    rel_other = models.CharField(max_length=20,blank=True, null=True)
    category = models.CharField(max_length=10,choices=CATEGORY_TYPE,blank=True, null=True)
    educational_qualification = models.CharField(max_length=100,blank=True, null=True)
    occupation_type = models.CharField(max_length=100,blank=True, null=True)
    employer_name = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    self_employeed = models.CharField(max_length=10,choices=EMPLOYEMENT_TYPE,blank=True, null=True)

    # personal details
    monthly_income = models.CharField(max_length=100,blank=True, null=True)
    assets = models.CharField(max_length=20,blank=True, null=True,help_text="Approximate Value")
    source = models.CharField(max_length=100,blank=True, null=True)
    it_pan_no = models.CharField(max_length=20,blank=True, null=True)
    # it_pan_image = 
    # form 60_61
    bussiness_nature = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f"{self.user}"
        
'''
this is 5th step of the form here user will fill the relation with UPA .
'''
class UPAIdentityProof(models.Model):
    UPA_TYPE = (
        ('Normal','Normal'),
        ('BPL','BPL'),
        ('Handicap','Handicap'),
    )

    PERSONAL_INCOME_TYPE = (
        ('Monthly','Monthly'),
        ('Yearly','Yearly'),
    )

    IDENTITY_PROOF_STATUS = (
        ('Aadhar Card','Aadhar Card'),
        ('Voter ID Card','Voter ID Card'),
        ('PAN Card','PAN Card'),
        ('Passport','Passport'),
        ('Driving License','Driving License'),
    )

    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="upa_identity")
    upa_type = models.CharField(max_length=20,choices=UPA_TYPE,blank=True, null=True)
    # if BPL 
    bpl_ration_card_no  = models.CharField(max_length=100,blank=True, null=True)
    bpl_ration_card_image = models.ImageField(upload_to="additinal_details/bpl/",blank=True,null=True)
    # bpl_ration_card_image = models.CharField
    personal_income_type = models.CharField(max_length=20,choices=PERSONAL_INCOME_TYPE,blank=True, null=True)
    personal_income = models.CharField(max_length=100,blank=True, null=True)
    # if handicap
    cmo_certificate_no = models.CharField(max_length=20,blank=True, null=True)
    cmo_certificate_image = models.ImageField(upload_to="additinal_details/cmo/",blank=True,null=True)
    # cmo_certificate_image = 
    # this will for identity proof
    # aadhar_card_id = models.BooleanField(default=False)
    # voter_card_id = models.BooleanField(default=False)
    # pan_card_id = models.BooleanField(default=False)
    # passport_id = models.BooleanField(default=False)
    # driving_license_id = models.BooleanField(default=False)
    identity_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_STATUS,blank=True, null=True)

    # this will address proof
    # ration_card_add = models.BooleanField(default=False)
    # voter_card_add = models.BooleanField(default=False)
    # aadhar_card_add = models.BooleanField(default=False)
    # passport_add = models.BooleanField(default=False)
    # driving_add = models.BooleanField(default=False)
    address_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_STATUS,blank=True, null=True)

    id_proof_no = models.CharField(max_length=100,blank=True, null=True)
    id_issued_at = models.DateField(blank=True, null=True)
    id_issued_by = models.CharField(max_length=100,blank=True, null=True)
    # id_proof_image

    add_proof_no = models.CharField(max_length=100,blank=True, null=True)
    add_issued_at = models.DateField(blank=True, null=True)
    add_issued_by = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

'''
Here collecting the Beneficiary Details
ben = beneficiary
f_g = Beneficiary father/gaurdian
m_m = Beneficiary Mother Maiden 
'''

class BeneficiaryDetails(models.Model):
    RELATION_UPA_TYPE = (
        ('Father','Father'),
        ('Mother','Mother'),
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('Daughter','Daughter'),
        ('Son','Son'),
    )
    GENDER_TYPE = (
        ('Male','Male'),
        ('Female','Female'),
    )
    MARITAL_STATUS_TYPE = (
        ('Married','Married'),
        ('Unmarried','Unmarried'),
    )
    IDENTITY_PROOF_TYPE = (
        ('Aadhar Card','Aadhar Card'),
        ('Voter ID Card','Voter ID Card'),
        ('PAN Card','PAN Card'),
        ('Passport','Passport'),
        ('Driving License','Driving License'),
    )
    TITLE_TYPE = (
        ('Mr','Mr'),
        ('Ms','Ms'),
        ('Smt','Smt'),
    )
    
    GAURDIAN_TYPE = (
        ('Father','Father'),
        ('Father','Father'),
        ('Gaurdian','Gaurdian'),
        ('Spouse','Spouse'),
    )
    beneficiary_required = models.BooleanField(default=False)
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="beneficiary_details")
    beneficiary_name = models.CharField(max_length=100,blank=True, null=True)
    beneficiary_id_no = models.CharField(max_length=100,blank=True, null=True)
    relation_upa = models.CharField(max_length=20,choices=RELATION_UPA_TYPE,blank=True, null=True)
    other = models.CharField(max_length=100,blank=True, null=True)
    ben_first_name = models.CharField(max_length=100,blank=True, null=True)
    ben_middle_name = models.CharField(max_length=100,blank=True, null=True)
    ben_last_name = models.CharField(max_length=100,blank=True, null=True)
    # beneficiary father/gaurdian details
    title = models.CharField(max_length=3,choices=TITLE_TYPE,blank=True,null=True)
    gaurdian_type = models.CharField(max_length=8,choices=GAURDIAN_TYPE,blank=True,null=True)
    f_g_first_name = models.CharField(max_length=100,blank=True, null=True)
    f_g_middle_name = models.CharField(max_length=100,blank=True, null=True)
    f_g_last_name = models.CharField(max_length=100,blank=True, null=True)
    #beneficiary mother maiden detail
    m_m_first_name = models.CharField(max_length=100,blank=True, null=True)
    m_m_middle_name = models.CharField(max_length=100,blank=True, null=True)
    m_m_last_name = models.CharField(max_length=100,blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    update_age_dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100,choices=GENDER_TYPE,blank=True, null=True)
    marital_status = models.CharField(max_length=100,choices=MARITAL_STATUS_TYPE,blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    # profile_image = 
    # signature 

    # Beneficiary Address
    address_line_one = models.CharField(max_length=200,blank=True, null=True)
    address_line_two = models.CharField(max_length=200,blank=True, null=True)
    address_line_three = models.CharField(max_length=200,blank=True, null=True)
    address_line_four = models.CharField(max_length=200,blank=True, null=True)
    landmark = models.CharField(max_length=100,blank=True, null=True)
    town = models.CharField(max_length=100,blank=True, null=True)
    district = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.PositiveIntegerField(blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)

    #beneficiary identity proof

    # aadhar_card_id = BooleanField(default=False)
    # voter_card_id = BooleanField(default=False)
    # pan_card_id = BooleanField(default=False)
    # passport_id = BooleanField(default=False)
    # driving_license_id = BooleanField(default=False)
    identity_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_TYPE,blank=True, null=True)
    address_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_TYPE,blank=True, null=True)
    # ration_card_add = models.BooleanField(default=False)
    # voter_card_add = models.BooleanField(default=False)
    # aadhar_card_add = models.BooleanField(default=False)
    # passport_add = models.BooleanField(default=False)
    # driving_license_add = models.BooleanField(default=False)

    id_proof_no = models.CharField(max_length=100,blank=True, null=True)
    id_issued_at = models.DateField(blank=True, null=True)
    id_issued_by = models.CharField(max_length=100,blank=True, null=True)

    add_proof_no = models.CharField(max_length=100,blank=True, null=True)
    add_issued_at = models.DateField(blank=True, null=True)
    add_issued_by = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return f"{self.user}"



'''
Busssiness card fees
'''

class BussinessCardFees(models.Model):
    green_bussiness_card = models.PositiveIntegerField(blank=True, null=True)
    yellow_bussiness_card = models.PositiveIntegerField(blank=True, null=True)
    red_chip_bussiness_card = models.PositiveIntegerField(blank=True, null=True)
    account_passbook = models.PositiveIntegerField(blank=True, null=True,default=0)
    e_account_statement = models.PositiveIntegerField(blank=True, null=True,default=0)
    vc_general = models.PositiveIntegerField(blank=True, null=True,default=0)
    vc_pvc = models.PositiveIntegerField(blank=True, null=True,default=0)
    green_atm_charge = models.PositiveIntegerField(blank=True, null=True,default=0)
    yellow_atm_charge = models.PositiveIntegerField(blank=True, null=True,default=0)
    red_atm_charge = models.PositiveIntegerField(blank=True, null=True,default=0)
    blue_atm_charge = models.PositiveIntegerField(blank=True, null=True,default=0)

    def __str__(self):
        return f"All bussiness type card charges / Fees."

class SponsorIntroductionDetail(models.Model):
    TIME_TYPE = (
        ('3 Month','3 Month'),
        ('6 Month','6 Month'),
        ('1 Year','3 Year'),
        ('More Than 1 Year','More Than 1 Year'),
    )
    APPLICANT_TIME_TYPE = (
        ('3 Month','3 Month'),
        ('6 Month','6 Month'),
        ('1 Year','3 Year'),
        ('More Than 1 Year','More Than 1 Year'),
    )
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="sponsor_details")
    name = models.CharField(max_length=200,blank=True, null=True,help_text="Enter Sponsor Name")
    did_no = models.CharField(max_length=100,blank=True, null=True)
    account_no = models.PositiveIntegerField(blank=True, null=True)
    time_in_bussiness = models.CharField(max_length=100,choices=TIME_TYPE,blank=True, null=True)
    time_with_applicant = models.CharField(max_length=100,choices=APPLICANT_TIME_TYPE,blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    # signature = 
    
    def __str__(self):
        return f"{self.user}"
        
class ServiceRequired(models.Model):
    SERVICE_REQUIRED = (
        ('Yes','Yes'),
        ('No','No'),
    )
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="service_requireds")
    # ID CARD
    royal_green_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    green_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_yellow_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    yellow_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_red_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    red_card_charge = models.CharField(max_length=100,blank=True, null=True)
    sms_alert = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    home_delevery = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    product_display = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    book_new_update = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)

    # VISITING CARD
    general_color_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    general_color_charge = models.CharField(max_length=100,blank=True, null=True)
    pvc_color_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    pvc_color_charge = models.CharField(max_length=100,blank=True, null=True)

    # ACCOUONT SECTION
    accouont_passbook = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    account_passbook_charge = models.CharField(max_length=100,blank=True, null=True)
    e_account_statement = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    e_account_statement_charge = models.CharField(max_length=100,blank=True, null=True)

    # Bussiness ATM Card or Pay Card
    royal_green_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    green_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_yellow_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    yellow_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_red_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    red_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_blue_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    blue_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return f"{self.user}"


class OperationMode(models.Model):
    MODE_OF_OPERATION = (
        ('SELF','SELF'),
        ('JOINTLY','JOINTLY'),
    )
    JOINT_ACCOUNT = (
        ('1','1'),
        # ('2','2'),
    )
    TRANSACTION_MODE = (
        ('CARD','CARD'),
        ('CASH','CASH'),
        ('ONLINE TRANSFER','ONLINE TRANSFER'),
    )
    RELATION_WITH_UPA = (
        ('WIFE','WIFE'),
        ('SON','SON'),
        ('DAUGHTER','DAUGHTER'),
        ('OTHER','OTHER'),
    )
    user = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="operation_mode")
    # transaction_charge_amount = models.CharField(max_length=100,blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    amount_in_figure = models.CharField(max_length=250,blank=True, null=True)
    #transaction mode 
    transaction_mode = models.CharField(max_length=20,choices=TRANSACTION_MODE,blank=True, null=True)
    # upa accouont handling
    upa_account_operation_mode = models.CharField(max_length=10,choices=MODE_OF_OPERATION,blank=True, null=True)
    joint_account = models.CharField(max_length=10,choices=JOINT_ACCOUNT,blank=True, null=True)
    
    # Joint Account Details
    '''
    uid_f = means UID no. for first join account holder
    f means first
    s means second
    '''
    uid_no_f = models.CharField(max_length=20,blank=True, null=True)
    name_f = models.CharField(max_length=100,blank=True, null=True)
    relation_upa_f = CharField(max_length=100,choices=RELATION_WITH_UPA,blank=True, null=True)
    aadhar_card_f = models.CharField(max_length=16,blank=True, null=True)
    # aadhar_image = 
    account_no_f = models.CharField(max_length=20,blank=True, null=True)
    mobile_no_f = models.PositiveIntegerField(blank=True, null=True)
    email_f = models.EmailField(blank=True, null=True)
    address_one_f = models.CharField(max_length=100,blank=True, null=True)
    address_two_f = models.CharField(max_length=100,blank=True, null=True)
    dob_f = models.DateField(blank=True, null=True)
    gender_f = models.CharField(max_length=10,blank=True, null=True)
    marital_status_f = models.CharField(max_length=6,blank=True, null=True)
    extra_detail_f = models.TextField(blank=True, null=True)

    uid_no_s = models.CharField(max_length=20,blank=True, null=True)
    name_s = models.CharField(max_length=100,blank=True, null=True)
    relation_upa_s = CharField(max_length=100,choices=RELATION_WITH_UPA,blank=True, null=True)
    aadhar_card_s = models.CharField(max_length=16,blank=True, null=True)
    # aadhar_image = 
    account_no_s = models.CharField(max_length=20,blank=True, null=True)
    mobile_no_s = models.PositiveIntegerField(blank=True, null=True)
    email_s = models.EmailField(blank=True, null=True)
    address_one_s = models.CharField(max_length=100,blank=True, null=True)
    address_two_s = models.CharField(max_length=100,blank=True, null=True)
    dob_s = models.DateField(blank=True, null=True)
    gender_s = models.CharField(max_length=10,blank=True, null=True)
    marital_status_s = models.CharField(max_length=6,blank=True, null=True)
    extra_detail_s = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user}"


def random_string_generator(size=10,chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Verification(models.Model):
    user  = models.OneToOneField(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="verification")
    applicant_name = models.CharField(max_length=100,blank=True, null=True)
    applicant_image = models.ImageField(upload_to='verification/applicant/images',blank=True, null=True)
    id_proof = models.ImageField(upload_to = 'verification/applicant/id_proof',blank=True, null=True)
    verifier_id = models.IntegerField(blank=True, null=True)
    verifier_image = models.ImageField(upload_to = 'verification/verifier/images')
    verification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    def save(self,*args,**kwargs):
        if self.user:
            print(self.user)
            profile = Profile.objects.get(user_id = self.user.user.id)
            print(profile)
            if profile.uid_no is None:
                print("yes blank")
                profile.uid_no = random_string_generator().upper()
                profile.save()
            else:
                print("no not blank")
                pass     
        super(Verification,self).save(*args,**kwargs)


'''
Enrollment section....*****
here existing upa can add new customer in the team and generate new refrence id for the particular customer 
with the help of the refr. no. he can add it him/her self in that person any brach. 
'''
class Enrollment(models.Model):
    VALIDITY_TIME = (
        ('5','5'),
        ('10','10'),
        ('15','15'),
        ('20','20'),
        ('25','25'),
    )
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name="enrolment",blank=True, null=True)
    sponsor_uid_no = models.CharField(max_length=100,blank=True, null=True)
    sponsor_name = models.CharField(max_length=100,blank=True, null=True)
    mobile_no = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=100,blank=True, null=True)
    father_name = models.CharField(max_length=100,blank=True, null=True)
    validity_time = models.CharField(max_length=2,choices=VALIDITY_TIME,blank=True, null=True)
    valid_upto = models.DateField(blank=True, null=True)
    reference_no  = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    def save(self,*args,**kwargs):
        today = date.today()
        days = self.validity_time
        if not self.id:
            self.reference_no = random_string_generator().upper()
            self.valid_upto = today + timedelta(days=int(days))
        super(Enrollment,self).save(self,*args,**kwargs)



# address details.
# additional details
# beneficiary details
# service required
# operation mode


class ChangeAddressRecord(models.Model):
    user_admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="change_address_details")
    upa_id_no = models.CharField(max_length=100,blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    address_line_one = models.CharField(max_length=100,blank=True, null=True)
    address_line_two = models.CharField(max_length=100,blank=True, null=True)
    address_line_three = models.CharField(max_length=100,blank=True, null=True)
    address_line_four = models.CharField(max_length=100,blank=True, null=True)
    landmark = models.CharField(max_length=100,blank=True, null=True)
    town_city = models.CharField(max_length=100,blank=True, null=True)
    district = models.CharField(max_length=100,blank=True, null=True)
    sub_district = models.CharField(max_length=100,blank=True, null=True)
    postal_zip_code = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.CharField(max_length=100,blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    active_email = models.EmailField(blank=True, null=True)
    std_code = models.PositiveIntegerField(blank=True, null=True)
    isd_code = models.PositiveIntegerField(blank=True, null=True)
    same_as_above = models.BooleanField(default=False)
    # permanent address
    p_address_one = models.CharField(max_length=100,blank=True, null=True)
    p_address_two = models.CharField(max_length=100,blank=True, null=True)
    p_address_three = models.CharField(max_length=100,blank=True, null=True)
    p_address_four = models.CharField(max_length=100,blank=True, null=True)
    p_landmark = models.CharField(max_length=100,blank=True, null=True)
    p_town = models.CharField(max_length=100,blank=True, null=True)
    p_dictrict = models.CharField(max_length=100,blank=True, null=True)
    p_sub_district = models.CharField(max_length=100,blank=True, null=True)
    p_postal_code = models.PositiveIntegerField(blank=True, null=True)
    p_country = models.CharField(max_length=100,blank=True, null=True)
    p_state = models.CharField(max_length=100,blank=True, null=True)
    p_telephone = models.PositiveIntegerField(blank=True, null=True)
    p_mobile = models.PositiveIntegerField(blank=True, null=True)
    p_active_email = models.EmailField(blank=True, null=True)
    p_std_code = models.PositiveIntegerField(blank=True, null=True)
    p_isd_code = models.PositiveIntegerField(blank=True, null=True)
    modification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.upa}"

class ChangeAdditionalRecord(models.Model):
    EMPLOYEMENT_TYPE = (
        ('Yes','Yes'),
        ('No','No'),
    )
    user_admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="change_additional_details")
    upa_id_no = models.CharField(max_length=100,blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    educational_qualification = models.CharField(max_length=100,blank=True, null=True)
    occupation_type = models.CharField(max_length=100,blank=True, null=True)
    employer_name = models.CharField(max_length=100,blank=True, null=True)
    designation = models.CharField(max_length=100,blank=True, null=True)
    self_employeed = models.CharField(max_length=10,choices=EMPLOYEMENT_TYPE,blank=True, null=True)

    # personal details
    monthly_income = models.CharField(max_length=100,blank=True, null=True)
    assets = models.CharField(max_length=20,blank=True, null=True,help_text="Approximate Value")
    source = models.CharField(max_length=100,blank=True, null=True)
    bussiness_nature = models.CharField(max_length=100,blank=True, null=True)
    modification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.upa}"

class ChangeBeneficiaryRecord(models.Model):
    RELATION_UPA_TYPE = (
        ('Father','Father'),
        ('Mother','Mother'),
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('Daughter','Daughter'),
        ('Son','Son'),
    )
    GENDER_TYPE = (
        ('Male','Male'),
        ('Female','Female'),
    )
    MARITAL_STATUS_TYPE = (
        ('Married','Married'),
        ('Unmarried','Unmarried'),
    )
    IDENTITY_PROOF_TYPE = (
        ('Aadhar Card','Aadhar Card'),
        ('Voter ID Card','Voter ID Card'),
        ('PAN Card','PAN Card'),
        ('Passport','Passport'),
        ('Driving License','Driving License'),
    )
    user_admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="change_beneficiary_details")
    upa_id_no = models.CharField(max_length=100,blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    beneficiary_name = models.CharField(max_length=100,blank=True, null=True)
    beneficiary_id_no = models.CharField(max_length=100,blank=True, null=True)
    relation_upa = models.CharField(max_length=20,choices=RELATION_UPA_TYPE,blank=True, null=True)
    other = models.CharField(max_length=100,blank=True, null=True)
    ben_first_name = models.CharField(max_length=100,blank=True, null=True)
    ben_middle_name = models.CharField(max_length=100,blank=True, null=True)
    ben_last_name = models.CharField(max_length=100,blank=True, null=True)
    # beneficiary father/gaurdian details
    f_g_first_name = models.CharField(max_length=100,blank=True, null=True)
    f_g_middle_name = models.CharField(max_length=100,blank=True, null=True)
    f_g_last_name = models.CharField(max_length=100,blank=True, null=True)
    #beneficiary mother maiden detail
    m_m_first_name = models.CharField(max_length=100,blank=True, null=True)
    m_m_middle_name = models.CharField(max_length=100,blank=True, null=True)
    m_m_last_name = models.CharField(max_length=100,blank=True, null=True)

    birth_date = models.DateField(blank=True, null=True)
    update_age_dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100,choices=GENDER_TYPE,blank=True, null=True)
    marital_status = models.CharField(max_length=100,choices=MARITAL_STATUS_TYPE,blank=True, null=True)
    nationality = models.CharField(max_length=100,blank=True, null=True)
    # profile_image = 
    # signature 

    # Beneficiary Address
    address_line_one = models.CharField(max_length=200,blank=True, null=True)
    address_line_two = models.CharField(max_length=200,blank=True, null=True)
    address_line_three = models.CharField(max_length=200,blank=True, null=True)
    address_line_four = models.CharField(max_length=200,blank=True, null=True)
    landmark = models.CharField(max_length=100,blank=True, null=True)
    town = models.CharField(max_length=100,blank=True, null=True)
    district = models.CharField(max_length=100,blank=True, null=True)
    state = models.CharField(max_length=100,blank=True, null=True)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    telephone = models.PositiveIntegerField(blank=True, null=True)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    email_id = models.EmailField(blank=True, null=True)

    #beneficiary identity proof

    # aadhar_card_id = BooleanField(default=False)
    # voter_card_id = BooleanField(default=False)
    # pan_card_id = BooleanField(default=False)
    # passport_id = BooleanField(default=False)
    # driving_license_id = BooleanField(default=False)
    identity_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_TYPE,blank=True, null=True)
    address_proof = models.CharField(max_length=20,choices=IDENTITY_PROOF_TYPE,blank=True, null=True)
    # ration_card_add = models.BooleanField(default=False)
    # voter_card_add = models.BooleanField(default=False)
    # aadhar_card_add = models.BooleanField(default=False)
    # passport_add = models.BooleanField(default=False)
    # driving_license_add = models.BooleanField(default=False)

    id_proof_no = models.CharField(max_length=100,blank=True, null=True)
    id_issued_at = models.DateField(blank=True, null=True)
    id_issued_by = models.CharField(max_length=100,blank=True, null=True)

    add_proof_no = models.CharField(max_length=100,blank=True, null=True)
    add_issued_at = models.DateField(blank=True, null=True)
    add_issued_by = models.CharField(max_length=100,blank=True, null=True)
    modification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.upa}"

class ChangeServiceRequiredRecord(models.Model):
    SERVICE_REQUIRED = (
        ('Yes','Yes'),
        ('No','No'),
    )
    user_admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="change_service_details")
    upa_id_no = models.CharField(max_length=100,blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    # ID CARD
    royal_green_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    green_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_yellow_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    yellow_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_red_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    red_card_charge = models.CharField(max_length=100,blank=True, null=True)
    sms_alert = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    home_delevery = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    product_display = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    book_new_update = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)

    # VISITING CARD
    general_color_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    general_color_charge = models.CharField(max_length=100,blank=True, null=True)
    pvc_color_card = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    pvc_color_charge = models.CharField(max_length=100,blank=True, null=True)

    # ACCOUONT SECTION
    accouont_passbook = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    account_passbook_charge = models.CharField(max_length=100,blank=True, null=True)
    e_account_statement = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    e_account_statement_charge = models.CharField(max_length=100,blank=True, null=True)

    # Bussiness ATM Card or Pay Card
    royal_green_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    green_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_yellow_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    yellow_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_red_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    red_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    royal_blue_atm = models.CharField(max_length=10,choices=SERVICE_REQUIRED,blank=True, null=True)
    blue_atm_card_charge = models.CharField(max_length=100,blank=True, null=True)
    modification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.upa}"


class ChangeOperationModeRecord(models.Model):
    MODE_OF_OPERATION = (
        ('SELF','SELF'),
        ('JOINTLY','JOINTLY'),
    )
    JOINT_ACCOUNT = (
        ('1','1'),
        ('2','2'),
    )
    TRANSACTION_MODE = (
        ('CARD','CARD'),
        ('CASH','CASH'),
        ('ONLINE TRANSFER','ONLINE TRANSFER'),
    )
    RELATION_WITH_UPA = (
        ('WIFE','WIFE'),
        ('SON','SON'),
        ('DAUGHTER','DAUGHTER'),
        ('OTHER','OTHER'),
    )
    user_admin = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    upa = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True, null=True,related_name="change_operation_details")
    upa_id_no = models.CharField(max_length=100,blank=True, null=True)
    request_no = models.IntegerField(blank=True, null=True)
    # transaction_charge_amount = models.CharField(max_length=100,blank=True, null=True)
    total_amount = models.IntegerField(blank=True, null=True)
    amount_in_figure = models.CharField(max_length=250,blank=True, null=True)
    #transaction mode 
    transaction_mode = models.CharField(max_length=20,choices=TRANSACTION_MODE,blank=True, null=True)
    # upa accouont handling
    upa_account_operation_mode = models.CharField(max_length=10,choices=MODE_OF_OPERATION,blank=True, null=True)
    joint_account = models.CharField(max_length=10,choices=JOINT_ACCOUNT,blank=True, null=True)
    
    # Joint Account Details
    '''
    uid_f = means UID no. for first join account holder
    f means first
    s means second
    '''
    uid_no_f = models.CharField(max_length=20,blank=True, null=True)
    name_f = models.CharField(max_length=100,blank=True, null=True)
    relation_upa_f = CharField(max_length=100,choices=RELATION_WITH_UPA,blank=True, null=True)
    aadhar_card_f = models.CharField(max_length=16,blank=True, null=True)
    # aadhar_image = 
    account_no_f = models.CharField(max_length=20,blank=True, null=True)
    mobile_no_f = models.PositiveIntegerField(blank=True, null=True)
    email_f = models.EmailField(blank=True, null=True)
    address_one_f = models.CharField(max_length=100,blank=True, null=True)
    address_two_f = models.CharField(max_length=100,blank=True, null=True)
    dob_f = models.DateField(blank=True, null=True)
    gender_f = models.CharField(max_length=10,blank=True, null=True)
    marital_status_f = models.CharField(max_length=6,blank=True, null=True)
    extra_detail_f = models.TextField(blank=True, null=True)

    uid_no_s = models.CharField(max_length=20,blank=True, null=True)
    name_s = models.CharField(max_length=100,blank=True, null=True)
    relation_upa_s = CharField(max_length=100,choices=RELATION_WITH_UPA,blank=True, null=True)
    aadhar_card_s = models.CharField(max_length=16,blank=True, null=True)
    # aadhar_image = 
    account_no_s = models.CharField(max_length=20,blank=True, null=True)
    mobile_no_s = models.PositiveIntegerField(blank=True, null=True)
    email_s = models.EmailField(blank=True, null=True)
    address_one_s = models.CharField(max_length=100,blank=True, null=True)
    address_two_s = models.CharField(max_length=100,blank=True, null=True)
    dob_s = models.DateField(blank=True, null=True)
    gender_s = models.CharField(max_length=10,blank=True, null=True)
    marital_status_s = models.CharField(max_length=6,blank=True, null=True)
    extra_detail_s = models.TextField(blank=True, null=True)
    modification_date = models.DateTimeField(auto_now_add=True,blank=True, null=True)

    def __str__(self):
        return f"{self.upa}"