# Generated by Django 5.0 on 2024-01-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(default='')),
            ],
        ),
        migrations.AddField(
            model_name='ranking',
            name='game_overall_score',
            field=models.IntegerField(null=True),
        ),
    ]
