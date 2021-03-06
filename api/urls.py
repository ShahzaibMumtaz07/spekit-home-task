from django.urls import path
from .views import DocumentView,FolderView, TopicView, GetDocuments

app_name = "api"

urlpatterns = [
    path('documents/', DocumentView.as_view(), name = 'documents' ),
    path('folders/', FolderView.as_view(), name = 'folders' ),
    path('topics/', TopicView.as_view(), name = 'topics' ),
    path('documents/<int:pk>/', DocumentView.as_view(), name = 'documents' ),
    path('folders/<int:pk>/', FolderView.as_view(), name = 'folders' ),
    path('topics/<int:pk>/', TopicView.as_view(), name = 'topics' ),
    path('get_documents/', GetDocuments.as_view(), name = 'get-documents' ),
]

