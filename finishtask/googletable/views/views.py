from django.template.response import TemplateResponse
from googletable.models.data import Data
from rest_framework import generics
from googletable.serializers.DataViewSerializer import DataSerializer


class OrderView(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


def order_html(request):
    return TemplateResponse(request, 'orders.html')
