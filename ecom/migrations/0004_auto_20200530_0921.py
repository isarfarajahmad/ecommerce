# Generated by Django 3.0.4 on 2020-05-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_auto_20200530_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tags',
            field=models.ManyToManyField(to='ecom.Tag'),
        ),
    ]
