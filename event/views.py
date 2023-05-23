from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from .Serializer import EventSerializer,EventRUDSerializer
from .models import Event
from rest_framework.pagination import LimitOffsetPagination,PageNumberPagination
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rich import print
# Create your views here.

class CustomPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'page'

class V3App(ListAPIView):
    serializer_class=EventSerializer
    pagination_class = CustomPagination
    ordering_fields = ['created_at']
    queryset=Event.objects.all() 
    created_atsearch_fields = ['event_type']

    def get_queryset(self):
        queryset = super().get_queryset()
        event_type = self.request.query_params.get('type', None)
        event_id = self.request.query_params.get('id', None)
        if  event_id:
            queryset = queryset.filter(id=event_id)

        if event_type:
            queryset = queryset.filter(event_type=event_type)
        return queryset
    
class V3AppCrud(RetrieveUpdateDestroyAPIView):
    serializer_class=EventRUDSerializer
    queryset=Event.objects.all()