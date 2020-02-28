# Generated by Django 2.2.7 on 2020-02-28 13:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import users.managers
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('login', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Last Name')),
                ('midname', models.CharField(blank=True, max_length=255, verbose_name='Mid Name')),
                ('phone', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number   must be entered in the format: '+999999999'. Up to 14 digits allowed.", regex='^\\+?1?\\d{9,14}$')])),
                ('last_seen', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('city', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('avatar', models.ImageField(blank=True, help_text='Maximum file size allowed is 2Mb', null=True, upload_to='avatars/', validators=[users.models.validate_image])),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=True, verbose_name='status_user')),
                ('conference', models.BooleanField(default=True, verbose_name='conference_user')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_company', to='company.Company')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_department', to='company.Department')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to=settings.AUTH_USER_MODEL)),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_of_role', to='company.Role')),
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
            name='CreateUserMany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('many_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
