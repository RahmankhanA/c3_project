# Generated by Django 3.2.4 on 2021-06-20 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_pizza_pizzasize'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='_id',
            new_name='id',
        ),
    ]
