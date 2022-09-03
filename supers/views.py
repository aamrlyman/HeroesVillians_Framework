from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from super_types.serializers import Super_Type_Serializer 
from .models import Super
from supers import serializers
from .serializers import SuperSerializer
from super_types.models import SuperType

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        
        super_by_type = request.query_params.get('super_type')
        super_by_name = request.query_params.get('sort')
        supers = Super.objects.all()

        if super_by_name:
            supers = supers.order_by(super_by_name)
            serializer = SuperSerializer(supers, many = True)
            return Response(serializer.data)

        elif super_by_type:
            supers = supers.filter(super_type__type = super_by_type) 
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data)
    
        else:
            heros = supers.filter(super_type__type = 'Hero')
            villians = supers.filter(super_type__type = "Villian") 
            hero_serializer = SuperSerializer(heros, many= True)
            villians_serializer = SuperSerializer(villians, many= True)
            all_supers_by_type = {
                'heros': hero_serializer.data,
                'villians': villians_serializer.data,
            }
            return Response(all_supers_by_type)
            

    elif request.method == "POST":
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)



@api_view (["GET", "PUT", "DELETE"])
def supers_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == "GET":
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SuperSerializer(super, data=request.data);
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def supers_by_type_dict(request):
    super_types = SuperType.objects.all()
    super_type_dict = {}
    for super_type in super_types:
        supers = Super.objects.filter(super_type_id = super_type.id)
        super_serializer = SuperSerializer(supers, many=True)
        super_type_dict[super_type.type] = {
            "type": super_type.type,
            "supers": super_serializer.data
        }
    return Response(super_type_dict)

