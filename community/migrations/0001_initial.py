<<<<<<< HEAD
# Generated by Django 3.2.6 on 2021-08-19 09:23
=======
# Generated by Django 3.2.6 on 2021-08-19 16:46
>>>>>>> a7e898fecc934afda6c7e3c57a1f721c1c03d99f

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('comments', models.PositiveIntegerField(null=True, verbose_name='댓글수')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('intro', models.CharField(max_length=30, verbose_name='한줄 소개')),
                ('content', models.TextField(verbose_name='서비스 내용')),
                ('img', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='제목')),
                ('content', models.TextField(verbose_name='서비스 내용')),
                ('img', models.ImageField(blank=True, upload_to='%Y/%m/%d', verbose_name='사진')),
                ('hits', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
