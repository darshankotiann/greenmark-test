# Generated by Django 4.1.7 on 2023-03-08 17:39

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_grid_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_details',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
