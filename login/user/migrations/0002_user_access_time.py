# Generated by Django 2.1.7 on 2019-03-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='access_time',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
