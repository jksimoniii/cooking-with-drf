from rest_framework_nested import routers

from api.v1.polls.urls import poll_router
from api.v1.polls.nested import views

question_nested_router = routers.NestedSimpleRouter(poll_router, r'questions', lookup='question')
question_nested_router.register(r'choices', views.QuestionNestedChoiceView, basename='question-choice')

urlpatterns = question_nested_router.urls
