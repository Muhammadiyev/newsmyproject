from rest_framework import routers
from django.urls import path, include, re_path

from .views import (
    TypeConfViewSet,
    ConferenceViewSet, 
    ConferenceFViewSet,
    ConferenceUserViewSet, 
    ConferenceGetViewSet,
    ConferencePhoneViewSet,
    ConfUserIDViewSet,
    ConfUsersIDViewSet,
    ConferenceUserIDViewSet,
    ConferenceUpdatedViewSet,
    StatisticConferenceViewSet,
    StatisticConferenceUsersViewSet,
    OneToOneConfViewSet,
    OneToOneConfListViewSet,
    SettingsConfViewSet

)

app_name = 'conference'

router = routers.DefaultRouter(trailing_slash=False)

router.register('typeconference', TypeConfViewSet)

router.register('conferenceoff', ConferenceViewSet)
router.register('conferenceupdated', ConferenceUpdatedViewSet)

router.register('conferenceon', ConferenceFViewSet)
router.register('conference', ConferenceGetViewSet)
router.register('conferenceuser', ConferenceUserViewSet)
router.register('phone', ConferencePhoneViewSet)
router.register('confuserid', ConfUserIDViewSet)
router.register('confusers', ConferenceUserIDViewSet)

router.register('confusersid', ConfUsersIDViewSet)

router.register('confvebinarstatic', StatisticConferenceViewSet)
router.register('confvebinarstaticusers', StatisticConferenceUsersViewSet)


router.register('onetooneconf', OneToOneConfViewSet)
router.register('onetooneconflist', OneToOneConfListViewSet)

router.register('settingsofconf', SettingsConfViewSet)


urlpatterns = router.urls

