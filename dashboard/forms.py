from django.forms import fields
from dashboard.models import *
from django import forms
from django.core import validators
from django.forms.fields import DateField
from django.forms import widgets

class DateInput(forms.DateInput):
    input_type = 'date'

class UPAChangeRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UPAChangeRequestForm,self).__init__(*args,**kwargs)
        self.fields['upa_id'].required = True
        self.fields['subject'].required = True
        self.fields['message'].required = True

    class Meta:
        model = UPAChangeRequest
        fields = ['upa_id','subject','message','form_name']

    # def clean(self):
    #     super(UPAChangeRequestForm,self).clean()
    #     upa_no = self.cleaned_data.get('upa_no')

    #     if upa_no == None:
    #         raise forms.ValidationError("Please Provied UPA ID")
    #     return self.cleaned_data

class UPAChangeRequestReplyForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UPAChangeRequestReplyForm,self).__init__(*args,**kwargs)
        self.fields['reply_message'].required = True
    class Meta:
        model = UPAChangeRequest
        fields = ['upa_id','subject','message','reply_message']



class IncomeSettingForm(forms.ModelForm):
    class Meta:
        model = IncomeSetting
        fields = ['child_one','child_two','child_three','income']


class IncomeSettingForWomenOldForm(forms.ModelForm):
    class Meta:
        model = IncomeSettingForWomenOld
        fields = ['category_type','income']
        

class FirmRegistrationForm(forms.ModelForm):
    class Meta:
        model = FirmRegistration
        fields = '__all__'
        exclude = ('created_by','created_at',)


class TenderForm(forms.ModelForm):
    class Meta:
        model = TenderRaise
        fields = '__all__'



class BulkOrderForm(forms.ModelForm):
    class Meta:
        model = BulkOrderToTenderFirm
        fields = ['tender_firm','product_name','product_count']


class CreateTenderForm(forms.ModelForm):
    class Meta:
        model = TenderProduct
        fields = ['tender_product_no','product_image','product_name','tender_product_quantity','tender_date']
        widgets = {
            'tender_date':DateInput(),
        }

class FinalTenderProductForm(forms.ModelForm):
    class Meta:
        model = FinalProductFromTender
        fields = ['final_tender_product','negotiated_quantity','negotiated_price']


class PrePurchaseBreakupOrderForm(forms.ModelForm):
    class Meta:
        model = PrePurchaseBreakupOrder
        fields = ['tender_product','company_name','product_count','total_product_count','order_month']
        widgets = {
            'order_month':DateInput(),
        }

class RecievedProductForm(forms.ModelForm):
    class Meta:
        model = RecievedProducts
        fields = ['tender_product','company_name','quantity_by_firm','product_price']

class ExchangeRejectedProductForm(forms.ModelForm):
    class Meta:
        model = RecievedProducts
        fields = ['tender_product','company_name','quantity_by_firm','product_price','exchange_quantity']

'''
Store Keeping Unit
'''

class StoreKeepingUnitForm(forms.ModelForm):
    class Meta:
        model = StoreKeepingUnit
        fields = ['location','store_name','store_address_one','store_address_two','store_address_three','store_size','no_of_racks','avg_section_rack']

from django.db.models import Q       
class ProductInStoreForm(forms.ModelForm):
    product_names = forms.ModelChoiceField(queryset=RecievedProducts.objects.filter(
        Q(tender_status='Accepted') |
        Q(tender_status='Exchanged') 
    ))
    class Meta:
        model = ProductInStore
        fields = ['store','box_name','product_names','product_quantity_in_box','rack_row','section_number_on_rack']