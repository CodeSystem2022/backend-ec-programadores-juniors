# Generated by Django 4.2.6 on 2023-11-08 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_category_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]