# Generated by Django 3.2.6 on 2021-08-19 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comment', '0001_initial'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='community.board', verbose_name='게시글'),
        ),
    ]
