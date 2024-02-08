from django.urls import path
from .views import PostList, PostDetails, CreateResponse, DeleteResponse, PostCreate, confirm_response, PostDelete

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetails.as_view(), name='post_detail'),
    path('create', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/response/create/', CreateResponse.as_view(), name='response_create'),
    path('<int:pk>/response/delete/', DeleteResponse.as_view(), name='response_delete'),
    path('confirm/<int:response_id>/', confirm_response, name='confirm_response'),
    path('<int:pk>/delete/>', PostDelete.as_view(), name='post_delete')
]