# Generated by Django 3.0.14 on 2021-06-20 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endorsement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
