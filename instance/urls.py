from django.urls import path

from instance.views import GetInstanceState, CreateInstanceAPIView

urlpatterns = [
    path('create_instance/', CreateInstanceAPIView.as_view()),
    path('get_state/<str:instance_id>/', GetInstanceState.as_view()),
]
