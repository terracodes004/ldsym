# Generated by Django 5.1.3 on 2024-11-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0007_alter_faq_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='file',
            field=models.FileField(max_length=500, upload_to=''),
        ),
    ]