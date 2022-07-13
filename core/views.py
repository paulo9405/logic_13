from django.shortcuts import render
from .models import Double
from datetime import datetime, timedelta
import datetime
import django

def name_valid(name):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    for c in name:
        if c not in alpha:
            return False
    return True

def double(request):
    doubles = Double.objects.all()
    if request.method == 'GET':
        return render(request, 'double.html', {'doubles': doubles})

    value = int(request.POST.get('value'))
    if value > 1000 or value < -1000:
        error = 'Max 100 min -1000'
        return render(request, 'double.html', {'doubles': doubles, 'error': error})

    person_name = request.POST.get('person_name')
    if not name_valid(person_name):
        error = 'erro charactere'
        return render(request, 'double.html', {'doubles': doubles, 'error': error})

    five_minutes_ago = django.utils.timezone.now() + datetime.timedelta(minutes=-5)
    result_five_min_ago = Double.objects.filter(name=person_name, value=value, date__gte=five_minutes_ago)

    already_exist = Double.objects.filter(name=person_name, value=value)
    if already_exist.count() == 0 or result_five_min_ago.count() == 0:
        Double.objects.create(name=person_name, value=value, double_value=value*2)

    return render(request, 'double.html', {'doubles': doubles})




