# Generated by Django 4.2 on 2023-08-30 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0004_funding_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funding',
            name='ends_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='funding',
            name='started_on',
            field=models.DateTimeField(null=True),
        ),
    ]
