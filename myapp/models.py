from django.db import models

# Create your models here.

from django.db import models

class Property(models.Model):
    property_name = models.CharField(max_length=255)
    property_address = models.TextField()
    property_location = models.CharField(max_length=255)
    property_features = models.TextField()
    type_choices = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
    ]
    unit_type = models.CharField(max_length=4, choices=type_choices)
    rent_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.property_name


class Tenant(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    document_proofs = models.CharField(max_length=255)
    agreement_end_date = models.DateField()
    monthly_rent_date = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.name