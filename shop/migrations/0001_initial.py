# Generated by Django 3.1.4 on 2020-12-05 02:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='著者名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '著者',
                'verbose_name_plural': '著者',
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='出版社名')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='タイトル')),
                ('price', models.IntegerField(null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('authors', models.ManyToManyField(blank=True, to='shop.Author', verbose_name='著者')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='shop.publisher', verbose_name='出版社')),
            ],
            options={
                'verbose_name': '本',
                'verbose_name_plural': '本',
                'db_table': 'book',
            },
        ),
    ]