# Generated by Django 2.2 on 2019-07-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='approved_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
