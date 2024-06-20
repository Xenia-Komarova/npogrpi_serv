from django.shortcuts import render

from core.send import send_email_to_admin
from website.models import Product

from .forms import ProductSearchForm, ProductSelectionForm


def product_search(request):
    if request.method == 'POST':
        form = ProductSearchForm(request.POST)
        if form.is_valid():
            type = form.cleaned_data['type']
            diameter_column = form.cleaned_data['diameter_column']
            diameter_shank = form.cleaned_data['diameter_shank']
            diameter_open_borehole = form.cleaned_data['diameter_open_borehole']

            # Фильтрация продукции
            products = Product.objects.filter(
                incalc__in=[True],
                type=type,
                diameter_column=diameter_column,
                diameter_shank=diameter_shank,
                diameter_open_borehole=diameter_open_borehole
            )

            if products.exists():
                # Если найдены продукты, отображаем результат
                send_email_to_admin(form.cleaned_data)
                return render(request, 'calculator/result.html', {'products': products})
            else:
                # Если ничего не найдено, отображаем сообщение
                return render(request, 'calculator/no_result.html')
    else:
        form = ProductSearchForm()

    return render(request, 'calculator/calculator.html', {'form': form})

def mgrp(request):
    if request.method == 'POST':
        form = ProductSelectionForm(request.POST)
        if form.is_valid():
            diameter_column = form.cleaned_data['diameter_column']
            diameter_shank = form.cleaned_data['diameter_shank']
            diameter_open_borehole = form.cleaned_data['diameter_open_borehole']
            stages_quantity = form.cleaned_data['stages_quantity']

            # Расчет количества оборудования
            packers_quantity = stages_quantity
            ball_sleeves_quantity = max(0, stages_quantity - 1)
            hydraulic_sleeves_quantity = 1
            activation_sleeves_quantity = 1
            quanitys = {
                'packers_quantity': packers_quantity,
                'ball_sleeves_quantity': ball_sleeves_quantity,
                'hydraulic_sleeves_quantity': hydraulic_sleeves_quantity,
                'activation_sleeves_quantity': activation_sleeves_quantity
            }

            # Получение продукции
            products = Product.objects.filter(
                type__inmgrp__in=[True],
                diameter_column=diameter_column,
                diameter_shank=diameter_shank,
                diameter_open_borehole=diameter_open_borehole
            )

            if products.exists():
                send_email_to_admin(form.cleaned_data)
                total_price = 0.0
                for prod in products:
                    if prod.type.slug == 'paker':
                        total_price += prod.price * stages_quantity
                    elif prod.type.slug == 'mufta_grp_sharovaiya':
                        total_price += prod.price * (stages_quantity - 1)
                    else:
                        total_price += prod.price
                
                context = {
                    'products': products,
                    'stages_quantity':stages_quantity,
                    'quanitys':quanitys,
                    'total_price':total_price,
                }
                return render(request, 'calculator/mgrp_result.html', context)
            else:
                return render(request, 'calculator/no_result.html')
    else:
        form_mgrp = ProductSelectionForm()
    return render(request, 'calculator/mgrp.html', {'form_mgrp': form_mgrp})
