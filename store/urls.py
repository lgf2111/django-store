from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='store-home'),
    path('seller/<str:username>', views.SellerProductListView.as_view(), name='seller-home'),
    path('seller/<str:username>/followers/add/', views.AddFollowerView.as_view(), name='add_follower'),
    path('seller/<str:username>/followers/remove/', views.RemoveFollowerView.as_view(), name='remove_follower'),
    path('product/new', views.ProductCreateView.as_view(), name='product-create'),
    path('product/search', views.product_search, name='product-search'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/<int:pk>/update', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', views.ProductDeleteView.as_view(), name='product-delete'),
]