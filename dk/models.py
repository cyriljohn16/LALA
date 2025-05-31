from django.db import models
from django.core.validators import MinValueValidator

class Record(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    date = models.DateField()
    capital = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    srp = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    total_sold = models.PositiveIntegerField(default=0)
    total_profit = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Total Profit = (SRP × Total Sold) − Capital
        self.total_profit = (self.srp * self.total_sold) - self.capital
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
