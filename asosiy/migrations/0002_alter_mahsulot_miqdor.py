# Generated by Django 4.2 on 2023-06-01 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mahsulot',
            name='miqdor',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
