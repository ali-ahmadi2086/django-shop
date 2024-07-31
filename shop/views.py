from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from cart.forms import CartAddForm
from .models import Product, Category


class IndexView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'shop/index.html', {'products': products})


class AboutView(View):
    def get(self, request):
        return render(request, 'shop/about.html')


class DetailProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = CartAddForm()
        return render(request, 'shop/detail_product.html', {"product": product, 'form': form})


class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'shop/category.html', {"category": category})


class CatProductView(View):
    def get(self, request, cat):
        cat = cat.replace('-', ' ')
        try:
            category = Category.objects.get(name=cat)
            products = Product.objects.filter(category=category)
            return render(request, 'shop/product.html', {'products': products, 'category': category})
        except:
            messages.error(request, 'دسته بندی وجود ندارد')
            return redirect('shop:home')