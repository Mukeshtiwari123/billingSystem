# Generated by Django 5.0.2 on 2024-03-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0002_alter_bills_bil_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bil_items',
            field=models.TextField(),
        ),
    ]