# serializers.py

from rest_framework import serializers
from .models import *

class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = '__all__'

class CommitteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Committee
        fields = '__all__'

class Blog1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog1
        fields = '__all__'

class Blog2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog2
        fields = '__all__'

class BoardMinutesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMinutes
        fields = '__all__'

class Blog1CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog1Category
        fields = '__all__'

class Blog2CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog2Category
        fields = '__all__'
