# Generated by Django 4.1.7 on 2023-04-13 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_booksdetails_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksdetails',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('[+-/%$]', inverse_match=True)]),
        ),
    ]