from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import *
from .serializers import *
import json

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
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
    print(serializer.data)
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
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    else:
        print("Not Valid!")
    return Response(serializer.data)

@api_view(['POST'])
def getNutritionalAdvice(request):
    # data = json.loads(request.body)
    bmi = calculate_bmi(request.data['weight'], request.data['height'])
    conditions = Condition.objects.all()
    serializer = ConditionSerializer(conditions, many=True)
    foundConditions = serializer.data
    print(bmi)
    if bmi <= 18.5:
        for condition in foundConditions:
            print(condition.title)
            if condition['title'] == "under weight":
                return Response(condition['advice'])
    elif bmi >= 18.5 and bmi < 25:
        for condition in foundConditions:
            if condition['title'] == "normal weight":
                return Response(condition['advice'])
    elif bmi >= 25 and bmi < 30:
        for condition in foundConditions:
            if condition['title'] == "over weight":
                return Response(condition['advice'])
    else:
        for condition in foundConditions:
            if condition['title'] == "obese":
                return Response(condition['advice'])
    return Response("error")


    
