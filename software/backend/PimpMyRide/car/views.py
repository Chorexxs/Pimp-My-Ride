from django.shortcuts import render
from django.http import JsonResponse
from .models import Car, Sensor, Light

# Create your views here.


def car_list(request):
    cars = Car.objects.all()
    data = {"cars": list(cars.values("id", "name", "model", "year"))}
    return JsonResponse(data)


def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        sensors = Sensor.objects.filter(car=car)
        lights = Light.objects.filter(car=car)
        data = {
            "id": car.id,
            "name": car.name,
            "model": car.model,
            "year": car.year,
            "sensors": list(sensors.values("id", "position", "is_active")),
            "lights": list(lights.values("id", "position", "is_on")),
        }
        return JsonResponse(data)
    except Car.DoesNotExist:
        return JsonResponse({"error": "Car not found"}, status=404)
