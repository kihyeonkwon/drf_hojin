# Generated by Django 4.2.5 on 2023-10-16 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_users_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
