from django.urls import path

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
    path('profiles/:username/', ProfileRetrieveAPIView.as_view()),
    path('profiles/:username/follow/', ProfileFollowAPIView.as_view()),
]
