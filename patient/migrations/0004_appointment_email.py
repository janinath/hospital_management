# Generated by Django 4.2.10 on 2024-03-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
