"""
This is the main module for the differents functions of this app.
"""
import ast

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from .models import Product, Sub_saved


def index(request):
    """Render the home page."""
    return render(request, 'catalogue/index.html')


def pagination(request, args, prods_max):
    """Allows you to create the page system """
    paginator = Paginator(args, prods_max)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def search(request):
    """The function that retrieves the user's search then render the search page or the index if no query.
    use the query "all" for all the products in the DB."""
    query = request.GET.get('query')
    if not query:
        messages.success(request, "Vous n'avez rien saisi")
        return redirect('home')
    elif query == "all":
        products = Product.objects.all()
        context = {
            "query": query,
            "page": pagination(request, products, 6)
        }
        return render(request, 'catalogue/search.html', context)
    else:
        products = Product.objects.filter(name__icontains=query)
        if not products.exists():
            context = {
                "no_product": True
            }
        else:
            context = {
                "query": query,
                "page": pagination(request, products, 6)
            }
        return render(request, 'catalogue/search.html', context)


def detail(request, product_id):
    """This function is called when a user wants to find substitutes for a product. """
    product = Product.objects.get(id=product_id)
    categories = product.categories
    categories = ast.literal_eval(categories)
    order = Product.objects.filter(categories__icontains=categories)
    sub = order.order_by('nutriscore_grade', 'id')
    substitutes = []
    for x in sub:
        try:
            if x.name == product.name:
                substitutes.remove(x)
            if x.nutriscore_grade <= product.nutriscore_grade:
                substitutes.append(x)
        except:
            pass
    context = {
        "product": product,
        "page": pagination(request, substitutes, 6),
    }
    return render(request, 'catalogue/detail.html', context)


@login_required
def save_in_db(request, sub_id):
    """When a user is connected, allows to save a product in the DB with a button."""
    if request.method == "POST":
        user = request.user
        save = Sub_saved.objects.filter(user_id=user.id,
                                        sub_id=sub_id)
        if not save:
            Sub_saved.objects.create(user_id=user.id,
                                     sub_id=sub_id)
            messages.success(request, 'Produit sauvegardé')
            return redirect('home')
        else:
            messages.success(request, 'Le produit est déjà sauvegardé')
            return redirect(request.path_info)

    else:
        return redirect('home')


@login_required
def delete_sub(request, sub_id):
    """When a user is connected, allows to delete a product in the DB """
    if request.method == "POST":
        user = request.user
        delete = Sub_saved.objects.filter(user_id=user.id,
                                          sub_id=sub_id)
        delete.delete()
        sub_save = Sub_saved.objects.filter(user_id=user.id)
        substitutes = []
        for sub in sub_save:
            prod = Product.objects.get(pk=sub.sub_id)
            substitutes.append(prod)
        context = {
            "page": pagination(request, substitutes, 6)
        }
        return render(request, 'catalogue/my_products.html', context)
    else:
        return redirect('home')


def legal_notice(request):
    return render(request, 'catalogue/legal-notice.html')


@login_required
def my_page(request):
    """Allows you to display a user's "my account" page. Must be logged in.  """
    return render(request, 'catalogue/my_page.html')


@login_required
def my_products(request):
    """Allows you to view a user's saved products. Must be logged in. """
    user = request.user
    sub_save = Sub_saved.objects.filter(user_id=user.id)
    substitutes = []
    for sub in sub_save:
        prod = Product.objects.get(pk=sub.sub_id)
        substitutes.append(prod)
    context = {
        "page": pagination(request, substitutes, 6)
    }
    return render(request, 'catalogue/my_products.html', context)
