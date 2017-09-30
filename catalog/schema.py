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


class DefaultProduct(DjangoObjectType):
    class Meta:
        model = ProductModel


class ProductUserReview(DjangoObjectType):
    rating_as_stars = graphene.String(
        source='get_rating_display', required=True)

    class Meta:
        model = ProductUserReviewModel
        interfaces = (
            relay.Node,
        )


class AddProductUserReview(graphene.ClientIDMutation):
    review = graphene.Field(ProductUserReview)

    class Input:
        user = graphene.ID(required=True)
        product = graphene.ID(required=True)
        text = graphene.String(required=True)
        rating = graphene.Int(required=True)

    @classmethod
    def mutate_and_get_payload(cls, input, context, info):
        _, product_id = relay.Node.from_global_id(input.get('product'))
        _, user_id = relay.Node.from_global_id(input.get('user'))
        rating = input.get('rating')
        text = input.get('text')

        inst = ProductUserReviewModel.objects.create(
            product_id=int(product_id),
            user_id=int(user_id),
            rating=int(rating),
            text=text)

        return AddProductUserReview(review=inst)


class Query(graphene.ObjectType):
    user = relay.Node.Field(User)
    all_users = DjangoConnectionField(User)

    category = relay.Node.Field(Category)
    all_categories = DjangoConnectionField(Category)

    product = relay.Node.Field(Product)
    all_products = DjangoConnectionField(Product)

    review = relay.Node.Field(ProductUserReview)
    all_reviews = DjangoConnectionField(ProductUserReview)

    product_list = graphene.List(DefaultProduct)

    custom_product_list = graphene.List(
        DefaultProduct, price__gte=graphene.Argument(graphene.Int),
        price__lte=graphene.Argument(graphene.Int))

    @graphene.resolve_only_args
    def resolve_product_list(self):
        return ProductModel.objects.all()

    def resolve_custom_product_list(self, args, context, info):
        qs = ProductModel.objects.all()
        price__gte = args.get('price__gte')
        price__lte = args.get('price__lte')

        if price__gte:
            qs = qs.filter(price__gte=price__gte)

        if price__lte:
            qs = qs.filter(price__lte=price__lte)

        return qs


class Mutations(graphene.ObjectType):
    add_product_user_review = AddProductUserReview.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
