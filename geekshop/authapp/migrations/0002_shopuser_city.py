# Generated by Django 3.2.1 on 2022-05-02 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
