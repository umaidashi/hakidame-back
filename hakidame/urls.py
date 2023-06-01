from django.urls import path

from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('new/', views.new, name="form"),
#     path('<int:hakidame_id>/', views.detail, name="detail"),
#     path('<int:hakidame_id>/edit/', views.edit, name="form"),
#     path('<int:hakidame_id>/delete/', views.delete, name="form")
# ]

urlpatterns = [
    path('', views.HakidameView.as_view(), name='hakidame'),
    path('<int:pk>/', views.HakidameDetailView.as_view(), name='hakidame-detail'),
    path('todo/', views.HakidameTodoView.as_view(), name='hakidame-todo'),
    path('bookmark/', views.HakidameBookmarkView.as_view(), name='hakidame-bookmark')
]
