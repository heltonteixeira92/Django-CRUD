from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def list_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form})


def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product)  # o instance já pega o form preenchido

    if form.is_valid():
        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':  # ele vai entrar como GET e passar direto para o ultimo return
        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})
    # quando ele chega no html e confimar o form vai voltar como POST e entrar o if para deletar

