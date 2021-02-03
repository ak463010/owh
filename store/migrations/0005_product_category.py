# Generated by Django 3.1.6 on 2021-02-02 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
