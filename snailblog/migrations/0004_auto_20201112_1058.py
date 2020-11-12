# Generated by Django 2.2.6 on 2020-11-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snailblog', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default='Information'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='info', max_length=200),
            preserve_default=False,
        ),
    ]