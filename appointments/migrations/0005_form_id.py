# Generated by Django 4.0.3 on 2022-06-05 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_remove_form_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='Id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appointments.report'),
            preserve_default=False,
        ),
    ]