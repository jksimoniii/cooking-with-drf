from rest_framework import serializers
from polls import models


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Choice


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Question
