# Generated by Django 5.1.3 on 2024-11-30 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0010_comment_hate_likes_alter_faq_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
