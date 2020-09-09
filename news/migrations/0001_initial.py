# Generated by Django 2.2.7 on 2020-09-09 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('company', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_of_company', to='company.Company')),
            ],
        ),
    ]
