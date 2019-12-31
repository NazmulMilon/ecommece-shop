from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.shortcuts import render, get_object_or_404
from shop.models import Product


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
                id_ = item['product'].id
                quantity = item['quantity']
                product = Product.objects.filter(id=id_)
                for item in product:
                    item.quantity -= quantity
                    item.save()
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm()
        # for item in cart:
        #     print(item['product'].id)
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
