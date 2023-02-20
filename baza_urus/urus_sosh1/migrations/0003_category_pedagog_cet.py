# Generated by Django 4.1.3 on 2022-12-02 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('urus_sosh1', '0002_alter_pedagog_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Категория')),
            ],
        ),
        migrations.AddField(
            model_name='pedagog',
            name='cet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='urus_sosh1.category'),
        ),
    ]