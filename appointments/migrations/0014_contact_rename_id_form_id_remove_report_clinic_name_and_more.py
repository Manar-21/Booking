# Generated by Django 4.0.3 on 2022-06-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0013_alter_form_id_alter_report_num_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Phone', models.TextField()),
                ('Email', models.TextField()),
                ('Message', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='form',
            old_name='id',
            new_name='Id',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Clinic_Name',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Num_Bookings',
        ),
    ]
