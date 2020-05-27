from rest_framework import viewsets

from api.v1.polls import serializers
from polls import models


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()

