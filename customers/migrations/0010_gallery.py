# Generated by Django 3.0 on 2021-04-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20210408_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
