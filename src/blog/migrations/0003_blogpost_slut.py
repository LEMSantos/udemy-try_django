# Generated by Django 2.2 on 2021-05-16 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='slut',
            field=models.SlugField(default='hello-world'),
            preserve_default=False,
        ),
    ]
