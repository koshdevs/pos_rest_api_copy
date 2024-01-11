from django.urls import path
from pos.pos_api.views import (

    api_stocks_create_view,
    api_stocks_detail_view ,
    api_stocks_update_view,
    api_stocks_delete_view,
    ApiStocksListView,
)

app_name = 'pos'  

urlpatterns = [
    path('create/', api_stocks_create_view, name="stocks-create"),
    path('list/',ApiStocksListView.as_view() , name="stocks-list"),
    path('<serial>/', api_stocks_detail_view, name="stocks-detail"),
    path('<serial>/update/', api_stocks_update_view, name="stocks-update"),
    path('<serial>/delete/', api_stocks_delete_view, name="stocks-delete")
]