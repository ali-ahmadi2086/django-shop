from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from shop.models import Product
from .forms import CartAddForm


class CartSummaryView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'cart/cart_summary.html', {'cart': cart})


class CartAddView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
        return redirect('shop:detail', product.id)


class CartRemoveView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        cart.remove(product)
        return redirect('cart:cart_summary')


class CartUpdateView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, pk=product_id)
        quantity_change = request.POST.get('quantity_change')
        new_quantity = request.POST.get('quantity')

        if quantity_change is not None:
            try:
                quantity_change = int(quantity_change)
            except ValueError:
                quantity_change = 0

            current_quantity = cart.cart.get(str(product.id), {}).get('quantity', 1)
            new_quantity = max(1, current_quantity + quantity_change)

        elif new_quantity is not None:
            try:
                new_quantity = int(new_quantity)
            except ValueError:
                new_quantity = 1

            new_quantity = max(1, new_quantity)

        else:
            new_quantity = 1

        cart.update(product, new_quantity)
        return redirect('cart:cart_summary')