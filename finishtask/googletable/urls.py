from django.urls import path
from googletable.views import views

urlpatterns = [
    path('orders', views.OrderView.as_view()),
    path('orderstemplates', views.order_html),
]
