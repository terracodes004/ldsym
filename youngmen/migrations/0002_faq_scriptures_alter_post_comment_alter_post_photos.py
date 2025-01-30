# Generated by Django 5.1.3 on 2024-11-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youngmen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('title', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=300)),
                ('question', models.TextField()),
                ('file', models.FileField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Scriptures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('location', models.CharField(max_length=1000)),
                ('file', models.FileField(upload_to=None)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='post',
            name='photos',
            field=models.CharField(max_length=3000),
        ),
    ]
