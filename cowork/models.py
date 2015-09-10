from __future__ import unicode_literals
from django.db import models
from django.conf import settings



class Company(models.Model):
    user = models.ForeignKey('accounts.User',
                             related_name='companies')
    name = models.CharField(max_length=100)
    vat_id = models.CharField(verbose_name='VAT ID', max_length=32)
    website = models.URLField(verbose_name='Website', max_length=200, null=True)
    phone_number = models.IntegerField(verbose_name='Phone number', null=True)
    company_logo = models.ImageField(verbose_name='Company logo', 
                                     upload_to='logos', max_length=100, null=True)
    description = models.TextField(verbose_name='Company description', 
                                    max_length=500, null=True)

    def __unicode__(self):
        return self.name


class Location(models.Model):
    company = models.ForeignKey('Company',
        related_name='locations')
    country = models.CharField(verbose_name='Country', max_length=30)
    city = models.CharField(verbose_name='City', max_length=200)
    address_line_1 = models.CharField(verbose_name='Address line 1', max_length=200)
    address_line_2 = models.CharField(verbose_name='Address line 2', max_length=200)
    address_line_3 = models.CharField(verbose_name='Address line 3', max_length=200)
    postal_code = models.CharField(verbose_name='Postal code:', max_length=12)
    total_desks = models.IntegerField(verbose_name='Total desks')
    reserved_desks = models.IntegerField(verbose_name='Reserved desks')
    price = models.DecimalField(verbose_name='Price per desk $',
        max_digits=12, decimal_places=2)



    def __unicode__(self):
        return '%s' % (self.city)

    @property
    def free_desks(self):
        return self.total_desks - self.reserved_desks


class Desk(models.Model):
    owner = models.OneToOneField('accounts.User', related_name='desks',
        null=True)
    location = models.OneToOneField(Location, related_name='desks')
    rent_start_date = models.DateTimeField(null=True)
    rent_end_date = models.DateTimeField(null=True)

    def __unicode__(self):
        return '%s' % self.location
