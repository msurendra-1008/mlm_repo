from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UPAChangeRequest)
admin.site.register(IncomeSetting)
admin.site.register(IncomeSettingForWomenOld)
admin.site.register(FirmRegistration)
admin.site.register(TenderProduct)
admin.site.register(TenderRaise)
admin.site.register(BulkOrderToTenderFirm)
admin.site.register(PrePurchaseBreakupOrder)
admin.site.register(FinalProductFromTender)
admin.site.register(RecievedProducts)
admin.site.register(StoreLocationDefinition)
admin.site.register(StoreKeepingUnit)
admin.site.register(ProductInStore)