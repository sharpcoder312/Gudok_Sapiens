<<<<<<< HEAD
# Generated by Django 3.2.6 on 2021-08-09 07:29
=======
# Generated by Django 3.2.6 on 2021-08-08 11:58
>>>>>>> a290a77db247e240a0718b80735afd3911709973

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('likes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='users',
            field=models.ManyToManyField(related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
