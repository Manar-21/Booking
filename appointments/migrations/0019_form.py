# Generated by Django 4.0.3 on 2022-06-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0018_form_bones_form_children_delete_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('Name', models.TextField()),
                ('Address', models.TextField()),
                ('Phone', models.TextField()),
                ('Clinic', models.TextField()),
                ('Notes', models.TextField()),
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
