from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product


def home(request):
    products = Product.objects.all()
    categories = set([_.category for _ in products])
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'store/home.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    ordering = ['-date_created']


class SellerProductListView(ListView):
    model = Product
    template_name = 'store/seller_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        seller = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(seller=seller).order_by('-date_created')


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'brand', 'category', 'price', 'stock', 'description']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['name', 'brand', 'category', 'price', 'stock', 'description']

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        product = self.get_object()
        return self.request.user == product.seller


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = '/'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.seller


def about(request):
    return render(request, 'store/about.html')
