# Generated by Django 4.0.3 on 2022-06-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0024_form_date_alter_form_name_alter_form_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='appointments.clinic'),
        ),
    ]
