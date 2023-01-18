from django.db import models

# Create your models here.


class Markets(models.Model):
    market_name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    area = models.CharField(max_length=200)

    class Meta:
        db_table = 'markets'

    def __str__(self):
        return self.market_name


class Categories(models.Model):
    category_name = models.CharField(max_length=200)
    market = models.ForeignKey(Markets, on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.category_name


class Items(models.Model):
    item_name = models.CharField(max_length=200)
    price = models.FloatField()
    updated_at = models.DateTimeField()
    updated_by = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'items'

    def __str__(self):
        return self.item_name
