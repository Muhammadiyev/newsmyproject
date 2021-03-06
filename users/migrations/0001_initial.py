# Generated by Django 2.2.7 on 2020-09-09 10:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import users.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last Name')),
                ('midname', models.CharField(blank=True, max_length=255, verbose_name='Mid Name')),
                ('phone', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number   must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('last_seen', models.CharField(blank=True, max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('city', models.IntegerField(blank=True, choices=[(1, 'Qoraqalpog‘iston Respublikasi'), (2, 'Andijon viloyati'), (3, 'Buxoro viloyati'), (4, 'Jizzax viloyati'), (5, 'Qashqadaryo viloyati'), (6, 'Navoiy viloyati'), (7, 'Namangan viloyati'), (8, 'Samarqand viloyati'), (9, 'Sirdaryo viloyati'), (10, 'Surxondaryo viloyati'), (11, 'Toshkent viloyati'), (12, 'Farg‘ona viloyati'), (13, 'Xorazm viloyati'), (14, 'Toshkent shahri')], default=14, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, verbose_name='status_user')),
                ('conference', models.BooleanField(default=True, verbose_name='conference_user')),
                ('online_user', models.BooleanField(default=False, verbose_name='online_user')),
                ('order', models.IntegerField(blank=True, default=1)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_company', to='company.Company')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_department', to='company.Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CheckPasswordUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_password', models.CharField(blank=True, max_length=150, verbose_name='check_password')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('creator_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
