# Generated by Django 4.0.4 on 2022-09-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='posts_images/%m'),
        ),
    ]
