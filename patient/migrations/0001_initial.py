# Generated by Django 4.2.10 on 2024-02-20 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, null=True)),
                ('email', models.TextField(max_length=50, null=True)),
                ('password', models.TextField(max_length=50, null=True)),
            ],
        ),
    ]
