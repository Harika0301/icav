# Generated by Django 4.1.7 on 2023-04-14 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_booksdetails_isbn13'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booksdetails',
            options={'ordering': ['-id']},
        ),
    ]