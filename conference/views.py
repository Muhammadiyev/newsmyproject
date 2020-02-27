from django.shortcuts import render
from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import TypeConf, ConferenceUser, Conference
from . import serializers
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import authentication
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from rest_framework.views import APIView
from django.conf import settings
from otp.models import PhoneOTP
import random
from django.template.loader import render_to_string

import requests

User = get_user_model()


def send_email(email):

    context = {
        'conference': Conference.objects.filter().order_by('-created_at').first()
    }
    email_html_message = render_to_string('email/send_email.html', context)
    email_plaintext_message = render_to_string('email/send_email.txt', context)
    email = EmailMultiAlternatives(
        'your colleagues created a video confession',
        email_html_message,
        settings.DEFAULT_FROM_EMAIL,
        email,
        # reply_to=(email,),
    )
    email.attach_alternative(email_html_message, "text/html")
    email.send()


class ConferenceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Conference.objects.all()
    serializer_class = serializers.ConferenceSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['typeconf', 'user']

    def create(self, request, *args, **kwargs):
        response = super(ConferenceViewSet, self).create(
            request, *args, **kwargs)
        userIds = request.data['usersofroleofdepartments']
        phone = User.objects.filter(
            id__in=userIds).values_list('phone', flat=True)
        phone_number = list(phone)

        if len(phone_number) != 0:
            for ph in phone_number:
                phone = str(ph)
                user = User.objects.filter(phone__iexact=phone)
                key = send_otp(phone)
                if key:
                    PhoneOTP.objects.create(phone=phone, otp=key)

        email = User.objects.filter(
            id__in=userIds).values_list('email', flat=True)
        send_email(email)
        return response

def send_otp(phone):
    if phone:
        key = random.randint(9999, 99999)
        return key
    else:
        return False


class ConferenceGetViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Conference.objects.all()
    serializer_class = serializers.ConferenceGetSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['typeconf', 'user']


class ConferenceUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ConferenceUser.objects.all()
    serializer_class = serializers.ConferenceUserSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    filter_backends = (filters.DjangoFilterBackend,
                       SearchFilter, OrderingFilter)
    filter_fields = ['see_user', 'conference']


class TypeConfViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TypeConf.objects.all()
    serializer_class = serializers.TypeConfSerializer
    authentication_classes = [authentication.TokenAuthentication, ]
