from rest_framework.response import Response
from rest_framework.decorators import api_view
from xender.models import Details
from .serializers import DetailsSerializer

@api_view(["GET"])
def getData(request):
  #python dictionary
  #  identity = {"name" : "Sagar", "age" : 21, "city" : "London" , "bank" : "Wells Fargo"}
   items = Details.objects.all()
   serializer=DetailsSerializer(items, many=True)
   return Response(serializer.data)
  #  return Response(identity)

@api_view(["POST"])
def addDetail(request):
    serializer= DetailsSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
            #this will save data on the database
    return Response(serializer.data)