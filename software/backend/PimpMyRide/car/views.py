from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class LightControlView(APIView):
    def get(self, request):
        return Response({"message": "Light is off"})

    def post(self, request):
        status = request.data.get('status', False)
        return Response({"status": status})
