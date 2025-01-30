# Generated by Django 5.1.3 on 2024-11-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0013_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('data', models.CharField(max_length=100)),
                ('post_id', models.IntegerField()),
            ],
        ),
    ]
