# Generated by Django 4.0.3 on 2022-06-05 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_form_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='Id',
        ),
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='Num_Bookings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.form'),
        ),
    ]
