# Generated by Django 4.1.7 on 2023-03-30 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ApartmentsRating", "0010_alter_apartmentsrating_apartment_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="apartmentsrating",
            options={
                "verbose_name": "Оценка квартиры",
                "verbose_name_plural": "Оценки квартир",
            },
        ),
    ]
