# Generated by Django 3.1.4 on 2021-07-22 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0010_auto_20210722_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='max_people_count',
            field=models.IntegerField(default=1),
        ),
    ]
