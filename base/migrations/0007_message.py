# Generated by Django 3.0.14 on 2021-06-19 23:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20210619_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
