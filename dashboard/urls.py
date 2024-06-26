from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('upa_list/',upa_list,name="upa-list"),
    path('upa_detail/<int:pk>/',upa_view,name="upa-detail"),
    path('details_change_request/',update_request_upa,name="changes-request"),
    path('change_request_status/',change_request_status,name="changes-request-status"),
    path('reply_to_request/<int:pk>/',reply_to_request,name="reply_to_request"),
    path('upa_tree/',upa_tree,name="upa-tree"),
    path('income_setting/',income_setting,name="income-setting"),
    path('update_income_setting/<int:pk>/',update_income_setting,name="update-income-setting"),

    path('update_income_setting_for_women_old/<int:pk>/',update_income_setting_for_women_old,name="update-income-setting-for-women-old"),

    path('create_income_setting/',create_income_setting,name="create-income-setting"),
    path('income_setting_women_old/',create_income_for_women_old,name="income-setting-for-women-old"),
    path('delete_income_setting/<int:pk>/',delete_income_setting,name="delete-income-setting"),
    path('delete_income_setting_for_women_old/<int:pk>/',delete_income_setting_for_women_old,name="delete-income-setting-for-women-old"),
    path('upa_view_form_wise/',upa_view_form_wise,name="upa-view-form-wise"),
    path('firm_list/',firm_list,name="firm-list"),
    path('firm_detail/<int:pk>/',firm_detail,name="firm-detail"),
    path('firm_registration/',firm_registration,name="firm-registration"),
    path('firm_update/<int:pk>/',update_firm,name="firm-update"),
    path('firm_status/',registering_firm,name="firm-status"),
    path('tender_display/',tender_display,name="tender_display"),
    path('newest_raised_tender_list/',newest_raised_tender_list,name="newest_raised_tender_list"),
    path('tender_fillup/',tender_form,name="tender_fillup"),
    path('compare_list_particular_tender/<int:pk>/',compare_list_particular_tender,name="compare-list-particular-tender"),
    path('update_tender_product_quantity/<int:pk>/',new_negotiation_of_tender,name="update-tender-product-quantity"),
    path('tender_fill_list/',tender_fillup_list,name="tender_fill_list"),
    path('thank_for_vendors/',thank_for_vendors,name="thank_for_vendors"),
    path('tender_compare_negotiate_list/',compare_negotiate,name="tender_compare_negotiate_list"),
    path('tender_compare_final/',final_tender_product,name="tender_compare_final"),
    path('tender_accept/',tender_accept,name="tender_accept"),
    path('tender_reject/',tender_reject,name="tender_reject"),
    path('ntender_accept/<int:pk>/',new_accept,name="ntender_accept"),
    path('ntender_reject/<int:pk>/',new_reject,name="ntender_reject"),
    path('tender_negotiate/<int:pk>/',negotiate,name="tender_negotiate"),
    path('accepted_tender_firm/',accepted_tender_firm,name="accepted-tender-firm"),
    path('pre_purchase_requisition_for_related_tender/<int:pk>/',pre_purchase_requisition_for_related_tender,name="pre-purchase-requisition-for-related-tender"),
    path('purchase_requisition_etender/<int:pk>/',purchase_requisition_for_one_tender,name="purchase-requisition-etender"),
    path('create_bulk_order/',bulk_order,name="create-bulk-order"),
    path('bulk_order_list/',bulk_order_list,name="bulk-order-list"),
    path('create_tender/',create_tender,name="create-tender"),
    path('newest_tender_aprroval_from_admin/',new_tender_edit_from_Admin,name="created-tender-edit-from-admin"),
    path('aprroval_from_admin/',approvedToOpenForTender,name="approve-of-created-tender-by-admin"),
    path('update_created_tender/<int:pk>/',update_created_tender,name="update-created-tender"),
    path('create_pre_prequisite_breakup/<int:pk>/',create_pre_purchase_order_breakup,name="pre-prequisite-breakup"),
    path('order_breakup/<int:pk>/',order_breakup,name="order-breakup"),
    path('total_supply_order/',total_supply_order,name="total-supply-order"),
    path('send_order_to_vendor/',OrderForVendor,name="send-order-to-vendor"),
    path('purchase_order_to_vendor/',purchase_order,name="for-vendor"),
    path('recieved_products/',recieved_products,name="recieved-products"),
    path('firm_detail_for_etender/<int:pk>/',firm_detail_for_etender,name="firm-detail-for-etender"),
    path('product_recieved/',create_recieved_product,name="product-recieved"),
    path('product_recieved_details/<int:pk>/',detail_of_recieved_product,name="product-recieved-details"),
    path('product_recieved_accept/<int:pk>/',recieved_product_accept,name="product-recieved-accept"),
    path('product_recieved_reject/<int:pk>/',recieved_product_reject,name="product-recieved-reject"),
    path('product_recieved_rejected/',rejected_products,name="product-recieved-rejected"),
    path('product_recieved_rejected_exhcnage_form/',exchange_rejected_product,name="product-recieved-rejected-exchange-form"),
    path('product_recieved_exchange/<int:pk>/',recieved_product_exchange,name="product-recieved-exchange"),

    # store section
    path('store_list/',store_list,name="store-list"),
    path('store/<int:pk>',store_detail,name="store-details"),
    path('store_creation/',store_creation,name="store-creation"),
    path('update_store_creation/<int:pk>/',update_store_creation,name="update-store-creation"),
    path('product_addition_in_store/<int:pk>/',product_addition_in_store,name="product-addition-in-store"),
    path('product_updated_list/',product_updated_list,name="product-updated-list"),
    path('product_all_list/',product_all_list,name="product-all-list"),
    path('store_product_sales_details/',store_product_sales_details,name="store-product-sales-details"),
    path('store_locations/',store_locations,name="store-locations"), # it will show the all the location name of active/inactive store 
    path('store_locations_details/<int:pk>/',store_locations_details,name="store-locations-details"), 

]