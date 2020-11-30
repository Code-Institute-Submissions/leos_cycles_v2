import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings

from bike.models import Bike
from services.models import Services
from basket.models import CalendarEvent


class Order(models.Model):
    order_number = models.CharField(max_length=35, null=False, editable=False)
    full_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    date = models.DateField(auto_now_add=True)

    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number
        """

        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """

        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order
        number if it hasn't been set already
        """

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name_plural = 'Order'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    service = models.ForeignKey(Services, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    bike = models.ForeignKey(Bike, null=True, blank=True, on_delete=models.CASCADE)
    calendar_event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """

        self.lineitem_total = self.service.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order number: {self.order.order_number}'

    class Meta:
        verbose_name_plural = 'OrderLineItem'
