from django.db import models


class ProductUserReview(models.Model):
    RATING_CHOICES_DEFAULT = 5
    RATING_CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    product = models.ForeignKey('Product')
    user = models.ForeignKey('auth.User')
    rating = models.PositiveSmallIntegerField('rating', choices=RATING_CHOICES,
                                              default=RATING_CHOICES_DEFAULT)
    text = models.TextField('text review')


class Category(models.Model):
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=140)
    description = models.TextField('description')
    price = models.PositiveIntegerField('price')
    category = models.ForeignKey('Category')
    reviews = models.ManyToManyField('auth.User', through='ProductUserReview')

    def __str__(self):
        return self.name

