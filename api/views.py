from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import *
import json

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(bmi)
    return bmi

@api_view(['GET'])
def getData(request):
    # person = {'name': 'Dennis', 'age': 28}
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getConditions(request):
    conditions = Condition.objects.all()
    serializer = ConditionSerializer(conditions, many=True)
    print(conditions)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def addCondition(request):
    serializer = ConditionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def getNutritionalAdvice(request):
    data = json.loads(request.body)
    print(data['weight'])
    bmi = calculate_bmi(data['weight'], data['height'])
    conditions = Condition.objects.all()
    serializer = ConditionSerializer(conditions, many=True)
    foundConditions = serializer.data
    for condition in foundConditions:
        if bmi is condition['bmi']:
            return Response(condition['advice'])

    
