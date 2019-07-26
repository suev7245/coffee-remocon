#payment 모델 추가
from django.contrib import admin
from order.models import Order, Payment
admin.site.register(Order)
admin.site.register(Payment)
