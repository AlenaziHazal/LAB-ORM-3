# Generated by Django 4.2.7 on 2023-11-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='name_publisher',
            field=models.CharField(max_length=2048, null=True),
        ),
    ]
