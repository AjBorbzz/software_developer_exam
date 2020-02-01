from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm
from django.http import QueryDict
from .filter import CarFilter


def index(request):
    latest_car = Car.objects.all()
    filter_cars = CarFilter(request.GET, queryset=latest_car)

    if request.method == 'POST':
        entries = QueryDict(request.POST['content'])
        for index, entry_id in enumerate(entries.getlist('entry[]')):
            # save index of entry_id as it's new order value
            entry = Car.objects.get(id=entry_id)
            entry.order = index
            entry.save()

    context = {
        'latest_car': latest_car,
        'filter': filter_cars,
    }

    return render(request, 'pages/index.html', context)


def instructions(request):
    latest_car = Car.objects.all()
    filter_cars = CarFilter(request.GET, queryset=latest_car)
    context = {
        'latest_car': latest_car,
        'filter': filter_cars,
    }
    return render(request, 'pages/instructions.html', context)


def enroll(request):
    form = CarForm()
    if request.method == 'POST':
        print('Printing POST: ', request.POST)
        form = CarForm(request.POST)
        if form.is_valid():
            print("Form printing {}".format(form))
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'pages/enroll.html', context)
