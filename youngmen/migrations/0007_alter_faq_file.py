# Generated by Django 5.1.3 on 2024-11-29 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0006_alter_faq_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='file',
            field=models.FileField(max_length=500, upload_to='static/'),
        ),
    ]
