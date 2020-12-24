# Generated by Django 3.0.5 on 2020-12-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image_url', models.CharField(max_length=200)),
                ('small_image_url', models.CharField(max_length=200)),
                ('large_image_url', models.CharField(max_length=200)),
                ('publication_year', models.CharField(max_length=10)),
                ('publication_month', models.CharField(max_length=10)),
                ('publication_day', models.CharField(max_length=10)),
                ('publisher', models.CharField(max_length=100)),
                ('is_ebook', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=200)),
                ('average_rating', models.CharField(max_length=3)),
                ('num_pages', models.CharField(max_length=5)),
                ('edition_information', models.CharField(max_length=10)),
                ('url', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
