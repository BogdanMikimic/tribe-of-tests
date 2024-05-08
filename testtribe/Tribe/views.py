from django.shortcuts import render, redirect
from Tribe.models import *
from decimal import Decimal
from datetime import datetime
from django.views.decorators.http import require_POST


def calculate_and_update_value_in_database(my_resource_name: str):
    """
    Takes the current time and the latest time the value was saved at and calculates,
    then updates the values in the
    :param my_resource_name:
    :return:
    """
    resource = Resources.objects.filter(resource_name=my_resource_name).get()
    time_difference = datetime.now() - resource.stored_resource_quantity_at_time
    difference_in_seconds = time_difference.total_seconds()
    # production can be negative or positive
    value_to_modify_existing_storage_with = Decimal(difference_in_seconds) * resource.net_production_per_second
    # updates the date in database to current time
    resource.stored_resource_quantity_at_time = datetime.now()
    resource.save()
    if value_to_modify_existing_storage_with > 0:
        individual_stock_increase_decrease(my_resource_name, value_to_modify_existing_storage_with)


def individual_stock_increase_decrease(my_resource_name: str, neg_or_pos_value_modif: int | float) -> None:
    """
    Increases or decreases the value of a stored resource.
    It increases up to maximum allowed qty, but no more. If more is provided, stops at max quantity.
    It decreases the quantity to zero, but does not go under.
    DO NOT use it for purchases, because if there is not enough stored to match the price, it decreases the quantity
    all the way to zero and saves it as zero
    :param my_resource_name: Resource name as string
    :param neg_or_pos_value_modif: value to decrease or increase the stock with (takes positive or negative values)
    :return: None
    """
    calculate_and_update_value_in_database(my_resource_name)
    resource = Resources.objects.filter(resource_name=my_resource_name).get()
    if (resource.stored_resource_quantity + Decimal(neg_or_pos_value_modif)) >= resource.max_storage_capacity:
        resource.stored_resource_quantity = resource.max_storage_capacity
    elif (resource.stored_resource_quantity + Decimal(neg_or_pos_value_modif)) < 0:
        resource.stored_resource_quantity = 0
    else:
        resource.stored_resource_quantity += Decimal(neg_or_pos_value_modif)
    resource.save()


def purchase_with_multiple_resources_costs(resource_costs: list[tuple]) -> str | None:
    """
    Expects a list of tuples with the name of the resource and quantity.
    Checks if there are enough of all resources to make the purchase.
    If so, makes the purchase, if not it does not.
    :param resource_costs:
    :return:
    """
    # check that there are enough resources in the database
    for resource_and_quantities in resource_costs:
        resource = Resources.objects.filter(resource_name=resource_and_quantities[0]).get()
        if (resource.stored_resource_quantity - Decimal(resource_and_quantities[1])) < 0:
            return f'Not enough {resource_and_quantities[0]}'

    # if there are, make the payments
    for resource_and_qty in resource_costs:
        individual_stock_increase_decrease(resource_and_qty[0], -resource_and_qty[1])


def individual_purchase_charge(my_resource_name: str, required_quantity):
    """
    Charges one of the resources (decreases the existing quantity)
    :param my_resource_name: Resource name as string
    :param required_quantity: Value to decrease existing quantity with
    :return: True if the transaction went through
    """
    calculate_and_update_value_in_database(my_resource_name)
    resource = Resources.objects.filter(resource_name=my_resource_name).get()
    if (resource.stored_resource_quantity - Decimal(required_quantity)) < 0:
        return f'Not enough {my_resource_name}'
    else:
        individual_stock_increase_decrease(my_resource_name, -required_quantity)
        return True


def tribe_village(request):
    stats = Resources.objects.all()
    apes = Apes.objects.all()
    apes_count = Decimal('0')
    for ape in apes:
        apes_count += ape.how_many_apes_of_that_type
    return render(request, 'Tribe/tribe_village.html', {'stats': stats, 'apes_count': apes_count})


def story(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/story.html', {'stats': stats})


def workshops(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/workshops.html', {'stats': stats})


def jungle(request):
    stats = Resources.objects.all()
    return render(request, 'Tribe/jungle.html', {'stats': stats})


def my_notes(request):
    stats = Resources.objects.all()
    if request.method == 'POST':
        my_text = request.POST.get('item_text')
        entry = Notes()
        entry.text = my_text
        entry.save()
        return redirect(request.path)

    existing_notes = Notes.objects.all()
    return render(request, 'Tribe/my_notes.html', {'existing_notes': existing_notes, 'stats': stats})


def buy_worker_ape(request):
    apes = Apes.objects.filter(ape_type_name='worker').get()
    # make purchase

    apes.how_many_apes_of_that_type += Decimal('1')
    apes.save()
    return redirect('tribe_village')