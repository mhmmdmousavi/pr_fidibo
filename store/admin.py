from django.contrib import admin
from store.models import Cart, Cart_Item, Order, Order_Item, Payment
# Register your models here.

admin.site.register(Cart)
admin.site.register(Cart_Item)
admin.site.register(Order)
admin.site.register(Order_Item)
admin.site.register(Payment)