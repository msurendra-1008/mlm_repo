from django import forms
from django.contrib.auth.models import Group
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import DateField

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
    # input_type_format = '%d/%m/%Y'


class BasicDetailsForm(forms.ModelForm):
    class Meta:
        model = BasicDetails
        fields = '__all__'
        exclude = ('user','submission_date')

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = "__all__"
        exclude = ('user',)
        widgets = {
            'dob':DateInput(),
            # 'update_age_dob':DateInput(),
        }

class UPAAddressForm(forms.ModelForm):
    class Meta:
        model = UPAAddress
        fields = '__all__'
        exclude = ('user',)

class AdditionalDetailForm(forms.ModelForm):
    class Meta:
        model = AdditionalDetails
        fields = '__all__'
        exclude = ('user',)
        

class UPAIdentityProofForm(forms.ModelForm):
    class Meta:
        model = UPAIdentityProof
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'id_issued_at':DateInput(),
            'add_issued_at':DateInput(),
            'issue_date':DateInput(),
            'valid_upto':DateInput(),
            'add_issue_date':DateInput(),
            'add_valid_upto':DateInput(),
        }

class BeneficiaryDetailsForm(forms.ModelForm):
    class Meta:
        model = BeneficiaryDetails
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'birth_date':DateInput(),
            'update_age_dob':DateInput(),
            'id_issued_at':DateInput(),
            'add_issued_at':DateInput(),
        }
        

class SponsorIntroductionDetailForm(forms.ModelForm):
    class Meta:
        model = SponsorIntroductionDetail
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'date':DateInput(),
        }

class ServiceRequiredForm(forms.ModelForm):
    class Meta:
        model = ServiceRequired
        fields = '__all__'
        exclude = ('user',)

class OperationModeForm(forms.ModelForm):
    class Meta:
        model = OperationMode
        fields = "__all__"
        exclude = ('user',)
        widgets = {
        # 'date': DateWidget(usel10n=True, bootstrap_version=3,),
        # 'total_amount': forms.TextInput(attrs={'disabled': True}),
        # 'amount_in_figure': forms.TextInput(attrs={'disabled': True}),
    }


class VerificationForm(forms.ModelForm):
    class Meta:
        model = Verification
        fields = ['applicant_name','applicant_image','id_proof','verifier_id','verifier_image']
        exclude = ('user',)

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['sponsor_uid_no','sponsor_name','mobile_no','full_name','father_name','validity_time']
        

class ChangeAddressRecordForm(forms.ModelForm):
    class Meta:
        model = ChangeAddressRecord
        fields = '__all__'
        exclude = ('user_admin','upa','modification_date')


class ChangeAdditionalRecordForm(forms.ModelForm):
    class Meta:
        model = ChangeAdditionalRecord
        fields = '__all__'
        exclude = ('user_admin','upa','modification_date')

class ChangeBeneficiaryRecordForm(forms.ModelForm):
    class Meta:
        model = ChangeBeneficiaryRecord
        field = '__all__'
        exclude = ('user_admin','upa','modification_date')

class ChangeServiceRequiredRecordForm(forms.ModelForm):
    class Meta:
        model = ChangeServiceRequiredRecord
        fields = '__all__'
        exclude = ('user_admin','upa','modification_date')

class ChangeOperationModeRecordForm(forms.ModelForm):
    class Meta:
        model = ChangeOperationModeRecord
        fields = '__all__'
        exclude = ('user_admin','upa','modification_date')
        