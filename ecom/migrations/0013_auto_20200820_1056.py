# Generated by Django 3.0.4 on 2020-08-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0012_auto_20200820_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
