# Generated by Django 4.0.3 on 2022-06-05 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0008_report_num_bookings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Num_Bookings',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointments.form'),
        ),
    ]
