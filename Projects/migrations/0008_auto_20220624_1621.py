# Generated by Django 3.1.2 on 2022-06-24 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0007_auto_20220624_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogslist',
            name='blPublishedDay',
            field=models.CharField(default=True, max_length=100, verbose_name='Blogs Published Day'),
        ),
        migrations.AddField(
            model_name='blogslist',
            name='blPublishedMonth',
            field=models.CharField(default=True, max_length=100, verbose_name='Blogs Published Month'),
        ),
        migrations.AddField(
            model_name='blogslist',
            name='blPublishedYear',
            field=models.CharField(default=True, max_length=100, verbose_name='Blogs Published Year'),
        ),
        migrations.AlterField(
            model_name='blogslist',
            name='blPublishedDate',
            field=models.DateField(auto_now=True, verbose_name='Blogs Published Date'),
        ),
    ]
