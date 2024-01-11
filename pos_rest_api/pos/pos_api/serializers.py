from rest_framework import serializers
from pos.models import Stocks

class StocksSerializer(serializers.ModelSerializer):
  
    #creator = serializers.SerializerMethodField('get_stock_creator')
    class Meta:

        model = Stocks 
        fields = '__all__' #+creator 
    
    '''
    def get_stock_creator(self,stocks):

        username = stocks.creator.username 

        return username
    '''