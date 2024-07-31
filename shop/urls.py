from django.urls import path
from . import views


app_name = 'shop'
urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('product/<int:pk>/', views.DetailProductView.as_view(), name='detail'),
    path('category/', views.CategoryView.as_view(), name='category'),
    path('category/<str:cat>/', views.CatProductView.as_view(), name='category_product'),
]