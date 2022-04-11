from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index3"),
    path('deal_order', views.deal_order, name="deal_order"),
    path('print_order/<int:id>/<str:filename>', views.print_order, name="print_order"),
]
