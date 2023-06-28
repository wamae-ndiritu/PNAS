from rest_framework import serializers
from base.models import *

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = '__all__'

class BodyBuilderGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyBuilderGoal
        fields = '__all__'

class BodyDiabeticGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabeticGoal
        fields = '__all__'

class BodyExpectantMotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyExpectantMotherGoal
        fields = '__all__'
