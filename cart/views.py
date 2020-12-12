from django.shortcuts import redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .cart import Cart


@login_required(login_url="/autenticacion/login")
def add_product(request, product_id):
    cart = Cart(request)  # Crea el carrito
    product = Product.objects.get(id=product_id)  # Busca el producto y lo obtenemos por su ID
    cart.add(product=product)  # Lo añade al carrito, si existe lo va a incrementar
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def remove_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def decrement_product(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.decrement(product=product)
    return redirect("listado_productos")


@login_required(login_url="/autenticacion/login")
def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("listado_productos")
