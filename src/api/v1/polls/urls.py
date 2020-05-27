from rest_framework import routers

from api.v1.polls import views

poll_router = routers.SimpleRouter()
poll_router.register(r'choices', views.ChoiceViewSet, basename='choice')
poll_router.register(r'questions', views.QuestionViewSet, basename='questions')

urlpatterns = poll_router.urls
