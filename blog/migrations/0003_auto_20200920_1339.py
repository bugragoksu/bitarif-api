# Generated by Django 3.0.8 on 2020-09-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image_link',
            field=models.URLField(),
        ),
    ]
