import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('user_id', models.TextField(unique=True, validators=[django.core.validators.MinLengthValidator(
                    5), django.core.validators.MaxLengthValidator(15)], verbose_name='아이디')),
                ('email', models.EmailField(max_length=254,
                 null=True, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=256, verbose_name='비밀번호')),
                ('name', models.CharField(
                    max_length=30, null=True, verbose_name='name')),
                ('nickname', models.CharField(
                    max_length=15, null=True, verbose_name='nickname')),
                ('phonenum', models.CharField(max_length=11, null=True, validators=[
                 django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,11}$')], verbose_name='phonenum')),
                ('image', models.ImageField(blank=True, null=True,
                 upload_to='%Y/%m/%d', verbose_name='image')),
                ('gender', models.CharField(choices=[
                 ('남자', '남자'), ('여자', '여자'), ('기타', '기타')], max_length=30, null=True, verbose_name='gender')),
                ('level', models.CharField(choices=[('3', 'Lv3_미인증사용자'), ('2', 'Lv2_인증사용자'), (
                    '1', 'Lv1_관리자'), ('0', 'Lv0_개발자')], default=3, max_length=18, verbose_name='등급')),
                ('auth', models.CharField(
                    max_length=10, null=True, verbose_name='인증번호')),
                ('created_at', models.DateTimeField(
                    blank=True, default=django.utils.timezone.now, null=True, verbose_name='created_at')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                 related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.',
                 related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
