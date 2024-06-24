from django.urls import path
from core.views import TestAPIView, CheckListAPIView, CheckListsAPIView
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    # path('/', test_api),
    # path("", TestAPIView.as_view()),
    path("api/checklist/", CheckListAPIView.as_view()),
    path("api/checklist/<int:pk>", CheckListsAPIView.as_view()),
    path(
        "openapi",
        get_schema_view(
            title="Your Project", description="API for all things …", version="1.0.0"
        ),
        name="openapi-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="index.html",
            extra_context={"schema_url": "openapi-schema"},
        ),
        name="api_doc",
    ),
]
