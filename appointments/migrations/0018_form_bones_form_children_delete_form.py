# Generated by Django 4.0.3 on 2022-06-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0017_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_bones',
            fields=[
                ('Name', models.TextField()),
                ('Address', models.TextField()),
                ('Phone', models.TextField()),
                ('Clinic', models.TextField()),
                ('Notes', models.TextField()),
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Form_children',
            fields=[
                ('Name', models.TextField()),
                ('Address', models.TextField()),
                ('Phone', models.TextField()),
                ('Clinic', models.TextField()),
                ('Notes', models.TextField()),
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Form',
        ),
    ]