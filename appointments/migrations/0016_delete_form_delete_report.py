# Generated by Django 4.0.3 on 2022-06-05 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0015_report_clinic_name_report_num_bookings_alter_form_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Form',
        ),
        migrations.DeleteModel(
            name='Report',
        ),
    ]
