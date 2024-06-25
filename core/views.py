from django.shortcuts import render
from rest_framework.response import Response

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.models import CheckList
from core.serializers import CheckListSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


# @api_view()
# def test_api(request):
#     return Response({"name": "Sarfraj Ansari"})


class TestAPIView(APIView):
    def get(self, request):
        return Response({"name": "Sarfraj Kayyum Ansari"})


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer

    def get(self, request):
        data = CheckList.objects.all()

        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = None

            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CheckList.objects.get(pk=pk)
        except CheckList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
