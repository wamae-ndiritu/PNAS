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

class DiabeticGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiabeticGoal
        fields = '__all__'

class ExpectantMotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpectantMotherGoal
        fields = '__all__'


class NormalWeightItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalWeightItems
        fields = '__all__'


class UnderWeightItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderWeightItems
        fields = '__all__'

class OverWeightItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OverWeightItems
        fields = '__all__'

class ObeseItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObeseItems
        fields = '__all__'
