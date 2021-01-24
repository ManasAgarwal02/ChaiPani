from django.db import models


# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=60, default='')
    phone = models.CharField(max_length=14, default='')
    organisation = models.CharField(max_length=50, default='')
    emp_id = models.CharField(max_length=14, default='')
    id_image = models.ImageField(upload_to="shop/idImages", default="")
    items_json = models.CharField(max_length=1000, default='')


