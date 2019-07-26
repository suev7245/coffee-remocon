from order.models import Order, Payment
from rest_framework import viewsets
from order.serializers import OrderSerializer, PaymentSerializer
from django.shortcuts import reverse, redirect
from rest_framework import permissions
# import requests
# import json

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=self.request.user)
            user = request.user.username
            return redirect(reverse('kakao_pay') + '?user=' + user)


class PaymentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # def perform_create(self, serializer):
    #         print(self.request.user.__dict__)
#         serializer.save(creator=self.request.user)
