# Generated by Django 2.0.5 on 2018-06-08 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbox', '0006_auto_20180418_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='first_member',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='second_member',
        ),
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
