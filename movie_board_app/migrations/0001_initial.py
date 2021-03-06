# Generated by Django 3.0.5 on 2020-04-19 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=50)),
                ('youtube_trailer_link', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=50)),
                ('recommendee', models.CharField(max_length=50)),
                ('recommender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_board_app.Recommender')),
            ],
        ),
    ]
