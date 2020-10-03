from django.db import models
from customer_profiles.models import CustomerProfile

from django_countries.fields import CountryField



class BillingAddress(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=120)
    street = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.customer_profile.user.email
    
    def get_full_address(self):
        return f'{self.house_number}, {self.street}, {self.barangay}, {self.city} city, {self.province}, {self.country}'
    

class ShippingAddress(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=120)
    street = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.customer_profile.user.email
    
    def get_full_address(self):
        return f'{self.house_number}, {self.street}, {self.barangay}, {self.city} city, {self.province}, {self.country}'


class DefaultAddress(models.Model):
    customer_profile = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=120)
    street = models.CharField(max_length=200)
    barangay = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    country = CountryField(blank_label='(select country)')
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.customer_profile.user.email
    
    def get_full_address(self):
        return f'{self.house_number}, {self.street}, {self.barangay}, {self.city} city, {self.province}, {self.country}'