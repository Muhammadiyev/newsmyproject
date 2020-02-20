from rest_framework import routers
from django.urls import path, include, re_path

from .views import TypeConfViewSet, ConferenceViewSet, ConferenceUserViewSet

app_name = 'conference'

router = routers.DefaultRouter(trailing_slash=False)

router.register('typeconference', TypeConfViewSet)
router.register('conferenceoff', ConferenceViewSet)
router.register('conferenceuser', ConferenceUserViewSet)

urlpatterns = router.urls
