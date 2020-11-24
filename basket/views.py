from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


@login_required
def view_basket(request):
    """ A view to return the basket """

    return render(request, 'basket/basket.html')


@login_required
def add_to_basket(request, pk):
    """ A view to add item to the basket """

    """ Get the data from the FORM """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ Check if basket variable included in session """
    """ or return empty dictionary to create one """
    basket = request.session.get('basket', {})

    """ Add item to basket or update quantity """
    if pk in list(basket.keys()):
        basket[pk] += quantity
    else:
        basket[pk] = quantity

    """ Update variable in the session with updated version """
    request.session['basket'] = basket

    """ Redirect user back to redirect url """
    return redirect(redirect_url)


@login_required
def edit_basket(request, item_id):
    """ A view to edit items in the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        basket.pop(item_id)

    request.session['basket'] = basket

    return redirect(reverse('view_basket'))
