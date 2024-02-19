from django.db import models
class ScrapedItem(models.Model):
    url = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_link = models.URLField()
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Item - {self.item_link}"