from django.urls import path
from .views import ViewOrders
from . import views

urlpatterns = [
    path('placeorder/', views.placeOrder, name='place_order'),
    path('vieworder/', ViewOrders.as_view(), name='get_view_orders'),
]