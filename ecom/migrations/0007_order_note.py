# Generated by Django 3.0.4 on 2020-06-02 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20200530_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
