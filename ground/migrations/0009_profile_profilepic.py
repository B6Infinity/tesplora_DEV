# Generated by Django 3.1.4 on 2021-07-22 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0008_auto_20210722_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profilePic',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ground.image'),
        ),
    ]
