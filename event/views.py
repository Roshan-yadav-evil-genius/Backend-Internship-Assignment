from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,ListCreateAPIView
from .Serializer import EventSerializer,EventRUDSerializer
from .models import Event
from django.db import connection,transaction
from rich import print
from django.core.files.storage import FileSystemStorage

# Create your views here.


class V3App(APIView):

    def get(self,request,id=None):
        query='SELECT * FROM event_event'
        limit = self.request.query_params.get('limit', 2)
        offset = self.request.query_params.get('page', 1)
        offset = (int(offset) - 1) * int(limit)


        event_id = self.request.query_params.get('id', None)
        event_type = self.request.query_params.get('type', None)

        if event_id or event_type:
            query += ' WHERE'
        if  event_id:
            query += f' id = {event_id}'
        if event_type:
            query+=f' event_type = "{event_type}"'

        query += f' LIMIT {limit} OFFSET {offset}'
        print({"Query":query})
        queryset = Event.objects.raw(query)
        return Response(EventSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        event_data = request.data
        # # Save the image file to a specified folder
        image_file = event_data['file']
        fs = FileSystemStorage(location='Assets/Event/Files')
        filename = fs.save(image_file.name, image_file)
        filename=f"Event/Files/{filename}"

        sql_query = f"INSERT INTO event_event (id, event_type, name, tagline, schedule, description, file, user, Category, Subcategory, rigor_rank, attendees, created_at) VALUES ({event_data['id']},'{event_data['event_type']}', '{event_data['name']}', '{event_data['tagline']}', '{event_data['schedule']}', '{event_data['description']}', '{filename}', '{event_data['user']}', '{event_data['Category']}', '{event_data['Subcategory']}', {event_data['rigor_rank']}, '{event_data['attendees']}', CURRENT_TIMESTAMP ) RETURNING id"
        print({"Query":sql_query.strip()})
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                row = cursor.fetchone()
                transaction.commit()

                queryset=Event.objects.raw(f"SELECT * FROM event_event WHERE id = {row[0]}")
            return Response({'message': 'Data inserted successfully.',"data":EventSerializer(queryset,many=True).data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)

    
    
class V3AppCrud(APIView):

    def get(self,request,id=None):
        queryset=Event.objects.raw(f"SELECT * FROM event_event WHERE id = {id}")
        if queryset:
            return Response(EventSerializer(queryset,many=True).data,status=status.HTTP_200_OK)
        else:
            return Response({"message":"No data found"},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id=None):
        event_data = request.data
        print(event_data)
        # # Save the image file to a specified folder
        image_file = event_data['file']
        fs = FileSystemStorage(location='Assets/Event/Files')
        filename = fs.save(image_file.name, image_file)
        filename=f"Event/Files/{filename}"

        sql_query = f"UPDATE event_event SET event_type = '{event_data['event_type']}', name = '{event_data['name']}', tagline = '{event_data['tagline']}', schedule = '{event_data['schedule']}', description = '{event_data['description']}', file = '{filename}', user = '{event_data['user']}', Category = '{event_data['Category']}', Subcategory = '{event_data['Subcategory']}', rigor_rank = {event_data['rigor_rank']}, attendees = '{event_data['attendees']}' WHERE id = {id}"
        print({"Query":sql_query.strip()})
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                transaction.commit()

                queryset=Event.objects.raw(f"SELECT * FROM event_event WHERE id = {id}")
            return Response({'message': 'Data updated successfully.',"data":EventSerializer(queryset,many=True).data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)})
    
    def delete(self,request,id=None):
        sql_query = f"DELETE FROM event_event WHERE id = {id}"
        print({"Query":sql_query.strip()})
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                transaction.commit()
            return Response({'message': 'Data deleted successfully.'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)},status=status.HTTP_400_BAD_REQUEST)
