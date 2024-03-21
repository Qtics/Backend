from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class Product(models.Model):
    subsystem = models.CharField(max_length=255)
    assembly = models.CharField(max_length=255, null=True)
    component = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    qty = models.PositiveIntegerField(blank=True, null=True)
    min_qty = models.PositiveIntegerField(blank=True, null=True)  # Assuming quantity is always positive
    add_cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)

    def __str__(self):
        return self.component
