# Generated by Django 4.0.3 on 2022-06-15 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0025_alter_form_clinic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
