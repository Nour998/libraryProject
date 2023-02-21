# Generated by Django 4.1.6 on 2023-02-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='isbnCode',
            field=models.CharField(default='00000', max_length=20, primary_key=True, serialize=False),
        ),
    ]