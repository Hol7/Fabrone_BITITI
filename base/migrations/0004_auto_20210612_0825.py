# Generated by Django 3.0.14 on 2021-06-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_project_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
