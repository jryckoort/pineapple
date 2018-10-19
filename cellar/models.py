from django.db import models
import datetime

def year_choices():
    return [(r,r) for r in range(1990, datetime.date.today().year+1)]

def year_choices_plus_15():
    return [(r,r) for r in range(1990, datetime.date.today().year+16)]

def current_year():
    return datetime.date.today().year

class Wine(models.Model):
    EFFERVESCENT = 'Effervescent'
    QUIET = 'Tranquille'
    TYPES = (
        (EFFERVESCENT, 'Effervescent'),
        (QUIET, 'Tranquille'),
    )

    SOFT = 'Doux'
    DRY = 'Sec'
    SUGAR = (
        (SOFT, 'Doux'),
        (DRY, 'Sec'),
    )

    RED = 'Rouge'
    WHITE = 'Blanc'
    ROSE = 'Rosé'
    COLOR = (
        (RED, 'Rouge'),
        (WHITE, 'Blanc'),
        (ROSE, 'Rosé'),
    )

    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)
    wine_region = models.ForeignKey('WineRegion', on_delete=models.PROTECT)
    house = models.CharField(max_length=200)
    calling = models.CharField(max_length=200)
    vines = models.ManyToManyField('Vine')
    type = models.CharField(max_length=200, choices=TYPES)
    sugar = models.CharField(max_length=200, choices=SUGAR)
    color = models.CharField(max_length=200, choices=COLOR)
    quantity_left = models.IntegerField()
    origin = models.CharField(max_length=200)
    year = models.IntegerField(choices=year_choices(), default=current_year)
    start_drink_year = models.IntegerField(choices=year_choices(), default=current_year)
    end_drink_year = models.IntegerField(choices=year_choices_plus_15(), default=current_year)

    def __str__(self):
        return self.name

class Vine(models.Model):
    BLACK = 'Noir'
    WHITE = 'Blanc'

    COLORS = (
        (BLACK, 'Noir'),
        (WHITE, 'Blanc'),
    )

    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLORS)

    def __str__(self):
        return self.name

class WineRegion(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey('WineCountry', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class WineCountry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
