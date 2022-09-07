from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Product, Rating


class ProductListView(ListView):
    model = Product
    template_name = 'store/home.html'
    context_object_name = 'products'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context =  super(ProductListView, self).get_context_data(**kwargs)
        context.update({
        })
        return context


class SellerProductListView(ListView):
    model = Product
    template_name = 'store/seller_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        seller = get_object_or_404(User, username=self.kwargs.get('username'))
        followers = seller.profile.followers.all()
        is_following = False
        for follower in followers:
            if follower == self.request.user:
                is_following = True
                break
            else:
                is_following = False
        follower_no = len(followers)
        context = super(SellerProductListView, self).get_context_data(**kwargs)
        context.update({
            'follower_no': follower_no,
            'is_following': is_following,
        })
        return context

    def get_queryset(self):
        seller = get_object_or_404(User, username=self.kwargs.get('username'))
        return Product.objects.filter(seller=seller).order_by('-date_created')


class ProductDetailView(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        product = Product.objects.get(pk=pk)
        ratings = Rating.objects.filter(product=product)
        rating_no = len(ratings)
        followers = product.seller.profile.followers.all()
        follower_no = len(followers)
        products = Product.objects.filter(seller=product.seller)
        product_no = len(products)
        ratings_no = sum([sum([rating.rate for rating in rating_list]) for rating_list in [Rating.objects.filter(product=prod) for prod in products]])
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({
            'ratings': ratings,
            'rating_no': rating_no,
            'ratings_no': ratings_no,
            'product_no': product_no,
            'follower_no': follower_no
        })
        return context



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


class AddFollowerView(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        user.profile.followers.add(request.user)

        return redirect('seller-home', username=user.username)


class RemoveFollowerView(LoginRequiredMixin, View):
    def post(self, request, username, *args, **kwargs):
        user = User.objects.get(username=username)
        user.profile.followers.remove(request.user)

        return redirect('seller-home', username=user.username)


def product_search(request):
    if request.method == "POST":
        search = request.POST.get('search')
        products = Product.objects.filter(name__contains=search)
        context = {
            'search': search,
            'products': products,
        }
        return render(request, 'store/product_search.html', context=context)
    else:
        return render(request, 'store/product_search.html', {})