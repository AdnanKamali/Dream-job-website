# Generated by Django 4.2 on 2023-04-12 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('position_salary', models.CharField(max_length=255)),
                ('position_location', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('company_location', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='job.category')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]