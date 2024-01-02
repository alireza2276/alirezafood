from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Product, OrderItem
from .forms import AddToCartProductForm, OrderForm
from django.contrib import messages


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['product_update_quantity_form'] = AddToCartProductForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart_detail.html', {'cart': cart})


def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartProductForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']
        cart.add(product, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart_detail')


def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect('cart_detail')

def cart_clear(request):

    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, 'Your cart successfully removed from your cart')

    else:
        messages.warning(request, 'Your cart is empty')

    return redirect('product_list')


def order_create(request):
    order_form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, 'You can not proceed, because your cart is empty!')
        return redirect('product_list')
    if request.method == 'POST':

        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()


        for item in cart:
            product = item['product_obj']
            OrderItem.objects.create(
                order = order_obj,
                    product = product,
                    quantity = item['quantity'],
                    price = product.price,
                )
            
        cart.clear()


    return render(request, 'order_create.html', context={
        'form': order_form
    })





