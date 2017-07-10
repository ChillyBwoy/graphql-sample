# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 15:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductUserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')], default=5, verbose_name='rating')),
                ('text', models.TextField(verbose_name='text review')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(through='goods.ProductUserReview', to=settings.AUTH_USER_MODEL),
        ),
    ]
