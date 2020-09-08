# Generated by Django 2.2.7 on 2020-09-08 09:47

from django.db import migrations, models
import django.db.models.deletion
import uploaded_choices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=1)),
                ('file', models.FileField(blank=True, upload_to=uploaded_choices.models.user_directory_path)),
                ('type', models.CharField(max_length=1)),
                ('company', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
        ),
    ]
