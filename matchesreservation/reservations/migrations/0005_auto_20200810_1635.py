# Generated by Django 3.0.3 on 2020-08-10 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20200810_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='stadium',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='reservations.Stadium'),
        ),
    ]
