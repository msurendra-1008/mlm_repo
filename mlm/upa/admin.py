from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(BasicDetails)
admin.site.register(PersonalInformation) 
admin.site.register(UPAAddress) 
admin.site.register(AdditionalDetails) 
admin.site.register(UPAIdentityProof) 
admin.site.register(BeneficiaryDetails) 
admin.site.register(BussinessCardFees) 
admin.site.register(SponsorIntroductionDetail) 
admin.site.register(ServiceRequired) 
admin.site.register(OperationMode) 
admin.site.register(Verification) 
admin.site.register(Enrollment) 

class ChangeAddressDetailAdmin(admin.ModelAdmin):
    model = ChangeAddressRecord
    list_display = ['user_admin','upa','modification_date']

    # def get_upa(self,obj):
    #     return obj.upa.user
    # get_upa.admin_order_field = 'upa'
    # get_upa.short_discription = "UPA Name"

admin.site.register(ChangeAddressRecord,ChangeAddressDetailAdmin)

class ChangeAdditionalRecordAdmin(admin.ModelAdmin):
    model = ChangeAdditionalRecord
    list_display = ['user_admin','upa','modification_date']
admin.site.register(ChangeAdditionalRecord,ChangeAdditionalRecordAdmin)

class ChangeBeneficiaryRecordAdmin(admin.ModelAdmin):
    model = ChangeBeneficiaryRecord
    list_display = ['user_admin','upa','modification_date']
admin.site.register(ChangeBeneficiaryRecord,ChangeBeneficiaryRecordAdmin)

class ChangeServiceRequiredRecordAdmin(admin.ModelAdmin):
    model = ChangeServiceRequiredRecord
    list_display = ['user_admin','upa','modification_date']
admin.site.register(ChangeServiceRequiredRecord,ChangeServiceRequiredRecordAdmin)

class ChangeOperationModeRecordAdmin(admin.ModelAdmin):
    model = ChangeOperationModeRecord
    list_display = ['user_admin','upa','modification_date']
admin.site.register(ChangeOperationModeRecord,ChangeOperationModeRecordAdmin)

# https://lims-staging.stagemyapp.com/admin/