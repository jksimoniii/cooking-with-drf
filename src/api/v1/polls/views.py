from rest_framework import viewsets

from api.mixins import TenantAwareModelViewSet
from api.v1.polls import serializers
from polls import models


class ChoiceViewSet(TenantAwareModelViewSet, viewsets.ModelViewSet):
    serializer_class = serializers.ChoiceSerializer
    queryset = models.Choice.objects.all()


class QuestionViewSet(TenantAwareModelViewSet, viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = models.Question.objects.all()

