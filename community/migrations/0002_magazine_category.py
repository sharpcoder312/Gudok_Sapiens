from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='magazine', to='services.category'),
        ),
    ]
