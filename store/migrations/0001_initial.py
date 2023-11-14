# Generated by Django 4.2.5 on 2023-11-11 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=128)),
                ('prix', models.FloatField(default=0.0)),
                ('en_stock', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='produits')),
            ],
        ),
    ]