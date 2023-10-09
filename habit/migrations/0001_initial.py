# Generated by Django 4.2.5 on 2023-10-08 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="место"
                    ),
                ),
                ("time", models.TimeField(blank=True, null=True, verbose_name="время")),
                ("action", models.TextField(verbose_name="действие")),
                (
                    "is_nice",
                    models.BooleanField(verbose_name="признак приятной привычки"),
                ),
                (
                    "periodicity_days",
                    models.BigIntegerField(
                        default=1, verbose_name="периодичность (дни)"
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="вознаграждение",
                    ),
                ),
                (
                    "execution_times",
                    models.BigIntegerField(
                        default=120, verbose_name="время на выполнение (секунды)"
                    ),
                ),
                (
                    "is_public",
                    models.BooleanField(
                        default=False, verbose_name="признак публичности"
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habit.habit",
                        verbose_name="связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "привычка",
                "verbose_name_plural": "привычки",
            },
        ),
    ]
