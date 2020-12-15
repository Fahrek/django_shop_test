from django.urls import path
from .views import process_order, OrderList, OrderDetail
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('process_order/', process_order, name='process_order'),
    path('myorders/', login_required(OrderList.as_view(), login_url='/autenticacion/acceder'), name='order_list'),
    path('<int:pk>', login_required(OrderDetail.as_view(), login_url='/autenticacion/acceder'), name='order_detail'),
]
