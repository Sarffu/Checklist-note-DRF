from django.shortcuts import render
from rest_framework.response import Response

# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.models import CheckList, CheckListItem
from core.serializers import CheckListSerializer, CheckListItemSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from core.permissions import IsOwner


# @api_view()
# def test_api(request):
#     return Response({"name": "Sarfraj Ansari"})


class TestAPIView(APIView):
    def get(self, request):
        return Response({"name": "Sarfraj Kayyum Ansari"})


class CheckListAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        data = CheckList.objects.filter(user=request.user)

        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        # print(request.data)
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data

            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckListsAPIView(APIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            obj = CheckList.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
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


class CheckListItemCreateAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [
        IsAuthenticated,IsOwner
    ]

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChekListsItemAPIView(APIView):
    serializer_class = CheckListItemSerializer
    permission_classes = [
        IsAuthenticated,IsOwner
    ]

    def get_object(self, pk):
        try:
            obj = CheckListItem.objects.get(pk=pk)
            self.check_object_permissions(self.request,obj)
            return obj
        except CheckListItem.DoesNotExist:
            return Http404

    def get(self, request, pk):
        checkList_item = self.get_object(pk)
        serializer = self.serializer_class(checkList_item)
        serializer_data = serializer.data
        return Response(serializer_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        checklist_item = self.get_object(pk)
        serializer = self.serializer_class(
            checklist_item, data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serialized_data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        checklist_item = self.get_object(pk)
        checklist_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
