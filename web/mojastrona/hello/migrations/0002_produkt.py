# Generated by Django 4.1 on 2022-09-03 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=20)),
                ('opis', models.TextField()),
                ('cena', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dostepny', models.BooleanField()),
            ],
        ),
    ]
