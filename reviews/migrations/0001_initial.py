# Generated by Django 3.2.6 on 2021-08-13 14:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='인증사진')),
                ('title', models.CharField(max_length=50, verbose_name='리뷰제목')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(15)], verbose_name='내용')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='별점')),
                ('period', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='사용기간(개월)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='services.service', verbose_name='서비스')),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
