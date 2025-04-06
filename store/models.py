from django.db import models
from accounts.models import User
from books.models import Books


class Cart (models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"cart for user{self.user.username}"
    
class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name= 'items')
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default= 1)

    def get_total_price (self):
        return self.books.price * self.quantity
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    is_paid = models.BooleanField(default= False)

    def __str__(self):
        return f"order {self.id} by {self.user.username}"
    
class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE, related_name= 'items')
    book = models.ForeignKey(Books, on_delete= models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_total_price(self):
        return self.price* self.quantity
    
class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=(
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ))

    def __str__(self):
        return f"Payment for Order #{self.order.id}"
    