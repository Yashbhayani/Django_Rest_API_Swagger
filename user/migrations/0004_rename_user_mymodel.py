# Generated by Django 5.0.2 on 2024-02-25 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Mymodel',
        ),
    ]
