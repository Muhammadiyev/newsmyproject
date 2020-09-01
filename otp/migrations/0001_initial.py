# Generated by Django 2.2.7 on 2020-09-01 18:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number   must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('otp', models.CharField(blank=True, max_length=9, null=True)),
                ('validated', models.BooleanField(default=False, help_text='If it is true, that means user have validate otp correctly in second API')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='When was this token generated')),
                ('count', models.IntegerField(default=1, help_text='Number of Limit')),
            ],
        ),
    ]
