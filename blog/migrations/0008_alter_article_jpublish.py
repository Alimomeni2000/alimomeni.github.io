# Generated by Django 5.1.2 on 2024-10-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='jpublish',
            field=models.DateTimeField(),
        ),
    ]