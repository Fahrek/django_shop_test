class Cart:

    def __init__(self, request):
        # Inicializamos request y sesion, y creamos la variable cart que va a estar disponible
        # en toda nuestra clase utilizando self.cart
        self.request = request
        self.session = request.session

        cart = self.session.get("cart")

        if not cart:
            cart = self.session['cart'] = {}  # Generamos cart como diccionario
        self.cart = cart

    def add(self, product):  # Añadir un producto
        if str(product.id) not in self.cart.keys():  # Si el carrito no tiene ningún producto lo añadimos nuevo
            self.cart[product.id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url

            }
        else:
            # En el caso de que SÍ exista algún producto recorremos todos los items de nuestro carrito y comprobamos
            # si la key actual de la iteración es igual a la key del producto que estamos intentando añadir.
            # Si es igual significa que ya existia en el carrito y lo que hacemos es incrementar la cantidad en una ud.
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    break
        self.save()

    def save(self):  # Guardamos la sesión de carrito en sesión correctamente
        self.session['cart'] = self.cart
        self.session.modified = True  # Forma de decir que la sesion está actualizada y que queremos persistir su info

    def remove(self, product):  # Borramos un producto del carrito
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):  # Decrementamos el número de productos en el carrito
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity'] - 1
                if value['quantity'] < 1:  # Si el producto es 0 como ya no existe lo eliminamos del carrito
                    self.remove(product)
                else:
                    self.save()
                break
            else:  # Si no existe este producto que estamos intentando decrementar
                print("El producto no existe en el carrito")

    def clear(self):  # Limpiamos el carrito de productos
        self.session['cart'] = {}
        self.session.modified = True



