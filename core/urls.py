from django.urls import path, include

from core.views import TestAPIView, CheckListAPIView, CheckListsAPIView

urlpatterns = [
    # path('/', test_api),
    # path("", TestAPIView.as_view()),
    path("api/checklist/", CheckListAPIView.as_view()),
    path("api/checklist/<int:pk>", CheckListsAPIView.as_view()),
]
