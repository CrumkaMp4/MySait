# Generated by Django 4.1.5 on 2023-01-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websait', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebhI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Textname')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
            },
        ),
        migrations.AlterModelOptions(
            name='webdev',
            options={'verbose_name': 'Text', 'verbose_name_plural': 'Texts'},
        ),
    ]