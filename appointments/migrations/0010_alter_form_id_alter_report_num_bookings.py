# Generated by Django 4.0.3 on 2022-06-05 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0009_alter_report_num_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='report',
            name='Num_Bookings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.form'),
        ),
    ]
