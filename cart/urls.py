from django.urls import path
from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.CartSummaryView.as_view(), name='cart_summary'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('update/<int:product_id>/', views.CartUpdateView.as_view(), name='cart_update'),
]