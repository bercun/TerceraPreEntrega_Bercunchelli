# Generated by Django 4.2.5 on 2023-11-01 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppRecetas', '0003_cheff_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
