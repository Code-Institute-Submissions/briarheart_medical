# Generated by Django 3.1 on 2020-08-27 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medications', '0005_auto_20200827_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meds',
            options={'verbose_name_plural': 'Medications'},
        ),
        migrations.AlterField(
            model_name='meds',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
