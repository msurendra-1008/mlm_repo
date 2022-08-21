from django.urls import path,include

from .views import *

urlpatterns = [

    path('basic_details/<int:id>/',UPABasicDetailView.as_view(), name='basic-detail-form'),
    path('personal_details/<int:id>/',PersonalInformationView.as_view(), name='personal-form'),
    path('address_details/<int:id>/',AddressView.as_view(), name='address-form'),
    path('additional_details/<int:id>/',AdditionalView.as_view(), name='additional-form'),
    path('upa_identity_proof/<int:id>/',UPAIdentityView.as_view(), name='upa-identity-form'),
    path('beneficiary_details/<int:id>/',BeneficiaryDetailsView.as_view(), name='beneficiary-details-form'),
    path('sponsor_details/<int:id>/',SponsorIntruductionView.as_view(), name='sponsor-details-form'),
    path('service_required/<int:id>/',ServiceRequiredView.as_view(), name='service-required-form'),
    path('operation_mode/<int:id>/',OperationModeView.as_view(), name='operation-mode-form'),
    path('verification/<int:id>/',VerificationView.as_view(), name='verification-form'),
    path('enrollment/<int:id>/',EnrollmentView.as_view(), name='enrollment-form'),
    path('change_address_form/<int:id>/',ChangeAddressView.as_view(), name='change-address-form'),
    path('change_additional_form/<int:id>/',ChangeAdditionalRecordView.as_view(), name='change-additional-form'),
    path('change_beneficiary_form/<int:id>/',ChangeBeneficiaryRecordView.as_view(), name='change-beneficiary-form'),
    path('change_service_required_form/<int:id>/',ChangeServiceRequiredRecordView.as_view(), name='change-service-required-form'),
    path('change_operation_mode_form/<int:id>/',ChangeOperationModeRecordView.as_view(), name='change-operation-mode-form'),
    path('thank_you/',thank_you, name='thank-you'),
    path('404/',error_404, name='404'),
]
