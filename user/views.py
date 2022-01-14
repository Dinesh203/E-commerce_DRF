
from django.http import HttpResponse
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import User
from .serializers import UserSerializer
# Create your views here.


class AdminView(APIView):
    """ Admin can get details, add new user, update detail, and delete
    users """

    def get(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({"status": "invalid user or id"})
            serializer = UserSerializer(User.objects.get(pk=pk))
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        if pk:
            try:
                serializer_data = UserSerializer(User.objects.get(id=pk), data=request.data, partial=True)
            except Exception as e:
                return HttpResponse(e)
            print(serializer_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({"status": "success", "data": serializer_data.data})
            else:
                return Response({"status": "error", "data": serializer_data.errors})
        else:
            return Response({"status": "invalid detail or attribute"})

    def delete(self, request, pk=None):
        if pk:
            user = User.objects.filter(pk=pk)
            if not user:
                return Response({'status': 'page not found'})
            user.delete()
            return Response({"status": "success", "data": "Item Deleted"})
        else:
            return Response({'error': 'user id not found'})


class UploadProfile(APIView):
    """ user profile upload """
    def patch(self, request, pk=None):
        if pk:
            try:
                file = request.data['profile_picture']
                serializer_data = UserSerializer(User.objects.get(id=pk), data=file, partial=True)
            except Exception as e:
                return HttpResponse(e)
            print(serializer_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return Response({"status": "success", "data": serializer_data.data})
            else:
                return Response({"status": "error", "data": serializer_data.errors})
        else:
            return Response({"status": "invalid detail or attribute"})
    # # print(request.user.profile_picture)
    # file = request.data['profile_picture']
    # image = User.objects.create(profile_picture=file)
    # print(image)
    # return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
