from django.db import models
from django.utils import timezone  # Import timezone for handling date and time
from django.contrib.auth.models import User  # Import the User model

CLEANING_TYPES = (
    ('UL', 'Ultrasonic'),
    ('ST', 'Steam'),
    ('MA', 'Manual'),
)

class Jewels(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jewels')  # Establishing the relationship
    name = models.CharField(max_length=255)
    material = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def has_met_cleaning_standard_today(self, clean_standard=1):
        """
        Determine if the jewel has been cleaned at least `clean_standard` times today.

        Args:
            clean_standard (int): The number of cleanings expected for the current day.

        Returns:
            bool: True if the cleaning standard for today has been met, False otherwise.
        """
        today = timezone.now().date()  # Get the current date
        cleanings_today = self.cleanings.filter(date=today).count()  # Count cleanings for today
        return cleanings_today >= clean_standard
    
class Cleaning(models.Model):
    jewel = models.ForeignKey(Jewels, on_delete=models.CASCADE, related_name='cleanings')
    cleaning_type = models.CharField(max_length=2, choices=CLEANING_TYPES)
    date = models.DateField('Cleaning Date')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.get_cleaning_type_display()} cleaning on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Collector(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    jewels = models.ManyToManyField(Jewels, related_name='collectors')

    def __str__(self):
        return self.name
