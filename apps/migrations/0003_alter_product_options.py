# Generated by Django 5.0.3 on 2024-05-03 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]