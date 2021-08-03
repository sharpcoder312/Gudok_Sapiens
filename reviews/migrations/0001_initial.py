# Generated by Django 3.2.6 on 2021-08-03 09:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='리뷰제목')),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(150)], verbose_name='리뷰내용')),
                ('photo', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='리뷰사진')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='별점')),
                ('period', models.PositiveSmallIntegerField(verbose_name='사용기간')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('target_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service', verbose_name='서비스')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='유저')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='reviews.review')),
                ('users', models.ManyToManyField(related_name='requirement_review_likes', to='users.User')),
            ],
        ),
    ]