# Generated by Django 5.0 on 2024-01-13 15:37

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_blogimage_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='package/images/')),
                ('name', models.CharField(default='package_image', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('days', models.PositiveSmallIntegerField(default=5)),
                ('night', models.PositiveSmallIntegerField(default=5)),
                ('people_max_limit', models.PositiveSmallIntegerField(default=10)),
                ('pickup_location', models.CharField(max_length=50)),
                ('drop_of_location', models.CharField(max_length=50)),
                ('map_embed_link', models.TextField()),
                ('price_quad_sharing', models.IntegerField(default=0)),
                ('price_triple_sharing', models.IntegerField(default=0)),
                ('price_double_sharing', models.IntegerField(default=0)),
                ('rating', models.PositiveSmallIntegerField(default=5)),
                ('image_list', models.ManyToManyField(to='app.blogimage')),
            ],
        ),
        migrations.CreateModel(
            name='Iternary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('details', ckeditor.fields.RichTextField(blank=True, default='--empty--', null=True)),
                ('package', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='iternaries', to='app.package')),
            ],
        ),
        migrations.CreateModel(
            name='Inclusive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('package', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inclusives', to='app.package')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exclusive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('package', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.package')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
