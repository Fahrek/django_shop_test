from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import \
    render_to_string  # Para renderizar como cadena un template y poder enviarlo por email
from django.utils.html import strip_tags  # Para sanear nuestra info
from django.views.generic.list import \
    ListView  # nos sirve para crear una función que nos devuelva info en forma de listado
from django.views.generic import DetailView  # lo mismo que ListView pero en forma de detalle
from .models import Order, OrderLine
from cart.cart import Cart


# Create your views here.
@login_required(login_url='/autenticacion/acceder')
def process_order(request):
    order = Order.objects.create(user=request.user, completed=True)  # Así damos de alta un pedido
    cart = Cart(request)  # creamos el carrito y le pasamos request
    order_lines = list()  # creamos una lista para poder recorrer la información del carrito

    for key, value in cart.cart.items():  # Key es directamente la ID del producto, se la pasamos al modelo OrderLine
        order_lines.append(
            OrderLine(
                product_id=key,
                quantity=value["quantity"],
                user=request.user,
                order=order
            )
        )  # Estamos metiendo en OrderLine un nuevo pedido para poder usar el metodo bulk_create

    OrderLine.objects.bulk_create(
        order_lines)  # Nos permite crear muchos registros de forma optimizada en BD pasando el order_lines

    send_order_email(
        order=order,
        order_lines=order_lines,
        username=request.user.username,
        user_email=request.user.email
    )

    cart.clear()

    messages.success(request, "El pedido se ha creado correctamente!")
    return redirect("listado_productos")


def send_order_email(**kwargs):
    subject = "Gracias por tu pedido"
    html_message = render_to_string("emails/nuevo_pedido.html", {
        "order": kwargs.get("order"),
        "order_lines": kwargs.get("order_lines"),
        "username": kwargs.get("username")
    })
    plain_message = strip_tags(html_message)
    from_email = "andresgqjob@gmail.com"
    to = kwargs.get("user_email")
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)
