# Generated by Django 5.1.3 on 2024-12-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0018_udetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.FileField(max_length=3000, upload_to=''),
        ),
        migrations.AlterField(
            model_name='udetails',
            name='an_lds_ym',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]