# Generated by Django 4.2.13 on 2024-06-17 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_post_excerpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_on']},
        ),
    ]
