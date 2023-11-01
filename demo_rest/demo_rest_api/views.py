from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework import permissions
from .models import REST
from rest_framework import status
from .serializers import REST_Serializer
from rest_framework.response import Response



class rest_api_views(APIView):
    
    permission_classes = [permissions.IsAuthenticated]
    

    def get(self, request, *args, **kwargs):

        apis = REST.objects.filter(user = request.user.id)
        serializer = REST_Serializer(apis, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = {
            'roll': request.data.get('roll'), 
            'student_name': request.data.get('student_name'),
            'admission_date': request.data.get('admission_date'),
            'user': request.user.id
        }
        serializer = REST_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_object(self, id, user_id):
        try:
            return REST.objects.get(id=id, user = user_id)
        except REST.DoesNotExist:
            return None


    def get(self, request, id, *args, **kwargs):

        api_instance = self.get_object(id, request.user.id)
        if not api_instance:
            return Response({"res": "Object with id does not exists"},status=status.HTTP_400_BAD_REQUEST)

        serializer = REST_Serializer(api_instance)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id, *args, **kwargs):
        
        api_instance = self.get_object(id, request.user.id)

        if not api_instance:
            return Response({"response": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'roll': request.data.get('roll'), 
            'student_name': request.data.get('student_name'), 
            'user': request.user.id
        }

        serializer = REST_Serializer(instance = api_instance, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self, request, id, *args, **kwargs):

        api_instance = self.get_object(id, request.user.id)

        if not api_instance:
            return Response({"response": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = {
            'roll': request.data.get('roll'), 
            'student_name': request.data.get('student_name'), 
            'user': request.user.id
        }

        serializer = REST_Serializer(instance = api_instance, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, *args, **kwargs):

        api_instance = self.get_object(id, request.user.id)
        if not api_instance:
            return Response({"response": "Object with id does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        api_instance.delete()
        
        return Response({"response": "Object deleted!"},status=status.HTTP_200_OK)