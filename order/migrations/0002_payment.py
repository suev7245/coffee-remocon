# Generated by Django 2.2 on 2019-07-18 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=100)),
                ('payment_method_type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('item_code', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('approved_at', models.DateTimeField()),
                ('tid', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
