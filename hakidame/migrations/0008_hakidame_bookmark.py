# Generated by Django 4.1.7 on 2023-03-25 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakidame', '0007_hakidame_update_at_hakidametag_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hakidame',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
    ]
