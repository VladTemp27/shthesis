# Generated by Django 4.0.2 on 2022-05-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
