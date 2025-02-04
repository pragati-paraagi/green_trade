# Generated by Django 5.0.6 on 2024-09-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_message_room_name_remove_message_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='read_by_recipient',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='read_by_sender',
            field=models.BooleanField(default=False),
        ),
    ]
