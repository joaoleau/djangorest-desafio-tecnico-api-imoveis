from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Immobile(BaseModel):
    code = models.CharField(max_length=10)
    guest_limit = models.PositiveIntegerField()
    bathroom_count = models.PositiveSmallIntegerField()
    is_pet = models.BooleanField(default=False)
    cleaning_fee = models.DecimalField(max_digits=10, decimal_places=2)
    activation_date = models.DateField()

    def __str__(self):
        return self.code

class Advertisement(BaseModel):
    immobile = models.ForeignKey(Immobile, on_delete=models.SET_NULL, null=True)
    platform_name = models.CharField(max_length=100)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Advertisement for {self.immobile} on {self.platform_name}"

class Reservation(BaseModel):
    code = models.CharField(max_length=10, unique=True)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.SET_NULL, null=True)
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    num_guests = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Reservation {self.code} for {self.advertisement}"