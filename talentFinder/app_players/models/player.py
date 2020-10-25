from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Player(models.Model):
    POSITION_CHOICES = (
        ('GK', 'goalkeeper'),
        ('RB', 'right back'),
        ('CB', 'centre back'),
        ('LB', 'left back'),
        ('CM', 'central midfileder'),
        ('LM', 'left midfileder'),
        ('RM', 'right midfileder'),
        ('RW', 'right winger'),
        ('LW', 'left winger'),
        ('FW', 'forward'),
        ('CAM', 'central attacking midfielder'),
        ('CDM', 'central defending midfielder'),

    )
    name = models.CharField(max_length=255, null=None, blank=None ,verbose_name="Name")
    last_name = models.CharField(max_length=255, null=None, blank=None ,verbose_name="Last Name")
    club = models.CharField(max_length=255, default=True, verbose_name="Club")
    position = models.CharField(max_length=3,choices=POSITION_CHOICES, verbose_name="Position")
    rating = models.FloatField(validators=[MinValueValidator(0.1), MaxValueValidator(10.0)], default=False, null=True)
    description = models.TextField(null=False, blank=True, default='')
    birth_date = models.DateField(verbose_name='Date of birth', auto_created=True)

    class Meta:
        verbose_name = 'Zawodnik'
        verbose_name_plural = 'Zawodnicy'
        app_label = 'app_players'