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
    resp = {}
    title = request.data['title']
    items = request.data['items'].split("-")
    new_condition = {}
    new_condition['title'] = request.data['title']
    new_condition['bmi'] = request.data['bmi']
    new_condition['comment'] = request.data['comment']
    serializer = ConditionSerializer(data=new_condition)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        resp['title'] = serializer.data['title']
        resp['bmi'] = serializer.data['bmi']
        resp['comment'] = serializer.data['comment']
    if title == "under weight":
        for item in items:
            new_item = {"item": item}
            serializer = UnderWeightItemsSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp['item'] = serializer.data['item']
    elif title == "normal weight":
        for item in items:
            new_item = {"item": item}
            serializer = NormalWeightItemsSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp['item'] = serializer.data['item']
    elif title == "over weight":
        for item in items:
            new_item = {"item": item}
            serializer = OverWeightItemsSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp['item'] = serializer.data['item']
    elif title == "obese":
        for item in items:
            new_item = {"item": item}
            serializer = ObeseItemsSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp['item'] = serializer.data['item']
    return Response(resp)

@api_view(['DELETE'])
def deleteConditions(request):
    Condition.objects.all().delete()
    return Response("All conditions deleted!")

# ADD GOAL OBJECTIVES
@api_view(['POST'])
def addGoal(request):
    resp = {}
    goal = request.data['goal']
    items = request.data['items'].split("-")
    if goal == "bodybuilder":
        for item in items:
            new_item = {"item": item}
            serializer = BodyBuilderGoalSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp = serializer.data
    elif goal == "diabetic":
        for item in items:
            new_item = {"item": item}
            serializer = DiabeticGoalSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp = serializer.data
    elif goal == "expectant":
        for item in items:
            new_item = {"item": item}
            serializer = ExpectantMotherSerializer(data=new_item)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                resp = serializer.data
    return Response(resp)

# GET OBJECTIVES BASED ON A GOAL
@api_view(['POST'])
def getGoalObjectives(request):
    items = []
    serializer = []
    goal = request.data['goal']

    if goal == "bodybuilder":
        items = BodyBuilderGoal.objects.all()
        serializer = BodyBuilderGoalSerializer(items, many=True)
    elif goal == "diabetic":
        items = DiabeticGoal.objects.all()
        serializer = DiabeticGoalSerializer(items, many=True)
    elif goal == "expectant":
        items = ExpectantMotherGoal.objects.all()
        serializer = ExpectantMotherSerializer(items, many=True)
    print(serializer.data)
    return Response(serializer.data)

# CHECK NUTRITIONAL STATUS
@api_view(['POST'])
def getNutritionalAdvice(request):
    print(request.data)
    result = {}
    height = float(request.data['height'])
    weight = float(request.data['weight'])
    bmi = calculate_bmi(weight, height)
    conditions = Condition.objects.all()
    serializer = ConditionSerializer(conditions, many=True)
    foundConditions = serializer.data
    print(bmi)
    if bmi <= 18.5:
        for condition in foundConditions:
            print(condition.title)
            if condition['title'] == "under weight":
                result['status'] = condition['title']
                # result['advice'] = 
                return Response(condition['advice'])
    elif bmi >= 18.5 and bmi < 25:
        for condition in foundConditions:
            if condition['title'] == "normal weight":
                print(condition['title'])
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


    
