# Generated by Django 2.1.4 on 2020-03-02 03:56

from django.db import migrations, models
import easyserializer


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField(blank=True)),
            ],
            bases=(easyserializer.SerializeableObject, models.Model),
        ),
    ]
