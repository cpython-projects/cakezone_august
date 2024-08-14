# Generated by Django 5.0.8 on 2024-08-13 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_dish_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='menu.category'),
        ),
    ]
