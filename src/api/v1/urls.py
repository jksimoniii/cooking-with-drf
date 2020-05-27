from django.urls import include, path

urlpatterns = [
    path('polls/', include('api.v1.polls.urls'))
]
