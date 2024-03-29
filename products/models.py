from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254,
                            null=True,
                            blank=True)
    friendly_name = models.CharField(max_length=254,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254,
                           null=True,
                           blank=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     default=1)
    description = models.TextField()
    colours = models.BooleanField(default=False,
                                  null=True,
                                  blank=True)
    image1_url = models.URLField(max_length=1024,
                                 null=True,
                                 blank=True)
    image1 = models.ImageField(null=True,
                               blank=True)
    image2_url = models.URLField(max_length=1024,
                                 null=True,
                                 blank=True)
    image2 = models.ImageField(null=True,
                               blank=True)
    image3_url = models.URLField(max_length=1024,
                                 null=True,
                                 blank=True)
    image3 = models.ImageField(null=True,
                               blank=True)
    certification = models.CharField(max_length=254,
                                     null=True,
                                     blank=True)
    standard = models.CharField(max_length=254,
                                null=True,
                                blank=True)
    dimensions = models.CharField(max_length=254,
                                  null=True,
                                  blank=True)
    material = models.CharField(max_length=254,
                                null=True,
                                blank=True)
    qty_1 = models.IntegerField(default=50)
    price_1 = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=1)
    qty_2 = models.IntegerField(default=100)
    price_2 = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=0.9)
    qty_3 = models.IntegerField(default=250)
    price_3 = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=0.8)
    qty_4 = models.IntegerField(default=500)
    price_4 = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=0.7)
    qty_5 = models.IntegerField(default=1000)
    price_5 = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=0.6)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                default=0)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
