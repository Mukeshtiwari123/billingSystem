from django.db import models

class Customer(models.Model):
    # Assuming you might also want to track customers or clients
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bills')
    date_issued = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Auto-calculated later

    def __str__(self):
        return f"Bill {self.pk} - {self.customer.name}"

    def save(self, *args, **kwargs):
        self.total_amount = sum(item.amount for item in self.bill_items.all())
        super().save(*args, **kwargs)
    
    class Bill(models.Model):
    # fields as previously defined

        def update_total_amount(self):
            self.total_amount = self.bill_items.aggregate(total=models.Sum('amount'))['total'] or 0
            self.save(update_fields=['total_amount'])


class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_items')
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2)
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Automatically calculated

    def save(self, *args, **kwargs):
    # Calculate the amount by multiplying quantity by the unit price
        self.amount = self.quantity * self.unit_price
        super().save(*args, **kwargs)  # Save the BillItem instance to the database


    def __str__(self):
        return f"{self.description} on Bill {self.bill.pk}"
