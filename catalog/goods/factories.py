import random
import factory

from django.contrib.auth.models import User
from catalog.goods.models import Category, Product, ProductUserReview


class UserFactory(factory.DjangoModelFactory):
    username = factory.Sequence(lambda n: "user_{0}".format(n))
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    class Meta:
        model = User


class CategoryFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=random.randrange(1, 2))

    class Meta:
        model = Category


class ProductFactory(factory.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=random.randrange(1, 2))
    description = factory.Faker('sentence', nb_words=random.randrange(20, 40))
    price = factory.Faker('random_int', min=3500, max=53500)
    category = factory.Iterator(Category.objects.all())

    class Meta:
        model = Product


class ProductUserReviewFactory(factory.DjangoModelFactory):
    class Meta:
        model = ProductUserReview

    user = factory.Iterator(User.objects.all())
    product = factory.Iterator(Product.objects.all())
    rating = factory.Faker('random_int', min=1, max=5)
    text = factory.Faker('sentence', nb_words=random.randrange(2, 20))
