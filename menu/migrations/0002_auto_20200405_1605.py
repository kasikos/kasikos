# Generated by Django 3.0.4 on 2020-04-05 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='menu', to='menu.Ingredient'),
        ),
    ]