# Generated by Django 5.1.2 on 2024-10-21 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='download_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]