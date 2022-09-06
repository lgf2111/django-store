from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, SellerProductListView
from . import views

urlpatterns = [
    path('', ProductListView.as_view(), name='store-home'),
    path('seller/<str:username>', SellerProductListView.as_view(), name='seller-products'),
    path('product/new', ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('about/', views.about, name='store-about'),
]