from django.shortcuts import render


def store_index(request):
    return render(request, template_name='index.html')


def product_list(request):
    return render(request, template_name='store/product_list.html')
