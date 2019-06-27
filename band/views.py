from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from band.models import Person
from band.serializers import PersonSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class BandList(APIView):
    def get(self, request, format=None):
        person = Person.objects.all()
        serializer = PersonSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        person = PersonSerializer(data=request.data)
        if person.is_valid():
            person.save()
            return Response(person.data, status=status.HTTP_201_CREATED)
        return Response(person.errors, status=status.HTTP_400_BAD_REQUEST)
