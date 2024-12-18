# Generated by Django 5.1.2 on 2024-10-22 17:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_remove_skill_category_delete_skillscategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='portfolio.skillscategory'),
            preserve_default=False,
        ),
    ]
