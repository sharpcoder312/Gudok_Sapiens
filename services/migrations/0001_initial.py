# Generated by Django 3.2.6 on 2021-08-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='services.category')),
            ],
            options={
                'verbose_name': 'sub-category',
                'verbose_name_plural': 'sub-categories',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진')),
                ('img2', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진2')),
                ('img3', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진3')),
                ('img4', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진4')),
                ('name', models.CharField(max_length=30, verbose_name='서비스 명')),
                ('intro', models.CharField(max_length=30, verbose_name='한줄 소개')),
                ('content', models.TextField(verbose_name='서비스 내용')),
                ('price', models.IntegerField(verbose_name='최저 가격')),
                ('link', models.URLField(verbose_name='서비스 홈페이지')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.subcategory')),
            ],
        ),
    ]
