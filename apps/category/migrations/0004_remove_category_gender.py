# Generated by Django 4.2.6 on 2023-11-08 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='gender',
        ),
    ]
