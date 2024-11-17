# Generated by Django 5.1.2 on 2024-10-22 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_skill_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='skill',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.skillscategory'),
        ),
    ]