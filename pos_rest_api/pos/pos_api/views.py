from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from pos.models import Stocks 
from pos.pos_api.serializers import StocksSerializer 


@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_stocks_detail_view(request,serial):

    try: 

        stock = Stocks.objects.get(serial=serial)
        

    except Stocks.DoesNotExist: 

        return Response(status = status.HTTP_404_NOT_FOUND)
    
    user = request.user 
    if user.is_staff == False:

        return Response({'response':"you dont have permission to view"})
    
    if request.method == 'GET':

        serializer_ = StocksSerializer(stock,many=False)
        
        return Response(serializer_.data)
    

@api_view(['PUT',])
def api_stocks_update_view(request,serial):

    try: 
        stock = Stocks.objects.get(serial=serial) 

    except Stocks.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    
    if request.method == "PUT":
        serializer_ = StocksSerializer(stock,data=request.data)
        data = {}
        if serializer_.is_valid():

            serializer_.save()
            data["success"] = "stocks updated successfully"
            return Response(data=data)

        return Response(serializer_.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE',])
def api_stocks_delete_view(request,serial):

    try: 
        stock = Stocks.objects.get(serial=serial) 

    except Stocks.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "DELETE":
        del_stock = stock.delete()
        data = {}
        if del_stock:
            data["success"] = "stock delete successfully"
        else:
            data["failure"] = "deleting failed"
            
        return Response(data=data)
    
@api_view(['POST',])
def api_stocks_create_view(request):
    pass
'''
    user = User.objects.get(pk=1)

    stock = Stocks(user = user)

    if request.method == 'POST':

        serializer_ = StocksSerializer(stock,data=request.data)

        data = {}

        if serializer_.is_valid():

            serializer_.save()
            return Response(serializer_.data,status = status.HTTP_201_CREATED)
        return Response(serializer_.errors,status = status.HTTP_400_BAD_REQUEST)
'''


class ApiStocksListView(ListAPIView):

    queryset = Stocks.objects.all() 
    serializer_class = StocksSerializer 
    authentication_class = (TokenAuthentication,) 
    permission_classes = (IsAuthenticated,) 
    pagination_class = PageNumberPagination
