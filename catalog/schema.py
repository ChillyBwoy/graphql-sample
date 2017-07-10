import graphene

from graphene import relay
from graphene_django import DjangoObjectType, DjangoConnectionField

from catalog.goods.models import (
    Category as CategoryModel,
    Product as ProductModel,
    ProductUserReview as ProductUserReviewModel
)
from django.contrib.auth.models import User as UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel
        interfaces = (
            relay.Node,
        )


class Category(DjangoObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (
            relay.Node,
        )


class Product(DjangoObjectType):
    class Meta:
        model = ProductModel
        interfaces = (
            relay.Node,
        )


class ProductUserReview(DjangoObjectType):
    rating_as_stars = graphene.String(source='get_rating_display')

    class Meta:
        model = ProductUserReviewModel
        interfaces = (
            relay.Node,
        )


class Query(graphene.ObjectType):
    user = relay.Node.Field(User)
    all_users = DjangoConnectionField(User)

    category = relay.Node.Field(Category)
    all_categories = DjangoConnectionField(Category)

    product = relay.Node.Field(Product)
    all_products = DjangoConnectionField(Product)

    review = relay.Node.Field(ProductUserReview)
    all_reviews = DjangoConnectionField(ProductUserReview)


schema = graphene.Schema(query=Query)
