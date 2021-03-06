# Generated by Django 2.0 on 2018-11-16 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_developer_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Developer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='url',
            field=models.URLField(default='hello', max_length=300, unique=True),
            preserve_default=False,
        ),
    ]
