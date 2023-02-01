# Generated by Django 3.2.8 on 2021-10-30 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_displayimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displayimage',
            name='slider1',
            field=models.ImageField(blank=True, help_text='Dimension: 920 * 690', null=True, upload_to='Display_images'),
        ),
        migrations.AlterField(
            model_name='displayimage',
            name='slider1a',
            field=models.ImageField(blank=True, help_text='Dimension: 210 * 130', null=True, upload_to='Display_images'),
        ),
    ]