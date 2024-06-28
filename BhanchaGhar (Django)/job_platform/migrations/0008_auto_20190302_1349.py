# Generated by Django 2.1.5 on 2019-03-02 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_platform', '0007_auto_20190302_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='displaypic',
            field=models.ImageField(blank=True, default='profilepics/default_profilepic.png', null=True, upload_to='profilepics/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
