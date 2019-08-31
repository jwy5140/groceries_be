import graphene
from graphene_django import DjangoObjectType

from .models import List

class ListType(DjangoObjectType):
    class Meta:
        model = List


class Query(graphene.ObjectType):
    lists = graphene.List(ListType)

    def resolve_lists(self, info, **kwargs):
        return List.objects.all()

class CreateList(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    items = graphene.String()

    #2
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        items = graphene.String()

    #3
    def mutate(self, info, url, description):
        list = List(name=name, description=description, items=items)
        link.save()

        return CreateList(
            id=list.id,
            name=list.name,
            description=list.description,
            items=list.items,
        )


#4
class Mutation(graphene.ObjectType):
    create_list = CreateList.Field()