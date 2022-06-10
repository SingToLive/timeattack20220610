from django.db import models

class OrderStatus(models.model):
    class Meta:
        db_table = 'order status'
    order_status = (
        ('OC', 'Order Completed'),
        ('PC', 'Payment Completed'),
        ('OC', 'Order Cancled'),
        ('SD', 'Shipping Departure'),
        ('DC', 'Delivery Complete'),
    )
    order_complete = models.CharField(max_length=2, choices=order_status)


class Category(models.model):
    class Meta:
        db_table = "category"
    name = models.CharField(max_length=50)

class Product(models.model):
    class Meta:
        db_table = "custom_user"
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True)
    description = models.TextField(max_length=1000)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)