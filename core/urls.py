from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('create/team/', views.CreateTeam.as_view(), name="create_team"),
    path('list/team/', views.ListTeam.as_view(), name="list_team"),
    path('update/team/<int:pk>/', views.UpdateTeam.as_view(), name="update_team"),
    path('delete/team/<int:pk>/', views.DeleteTeam.as_view(), name="delete_team"),

    path('create/stadium/', views.CreateStadium.as_view(), name="create_stadium"),
    path('list/stadium/', views.ListStadium.as_view(), name="list_stadium"),
    path('update/stadium/<int:pk>/', views.UpdateStadium.as_view(), name="update_stadium"),
    path('delete/stadium/<int:pk>/', views.DeleteStadium.as_view(), name="delete_stadium"),

    path('create/city/', views.CreateCity.as_view(), name="create_city"),
    path('list/city/', views.ListCity.as_view(), name="list_city"),
    path('update/city/<int:pk>/', views.UpdateCity.as_view(), name="update_city"),
    path('delete/city/<int:pk>/', views.DeleteCity.as_view(), name="delete_city"),

    path('create/player/', views.CreatePlayer.as_view(), name="create_player"),
    path('list/player/', views.ListPlayer.as_view(), name="list_player"),
    path('update/player/<int:pk>/', views.UpdatePlayer.as_view(), name="update_player"),
    path('delete/player/<int:pk>/', views.DeletePlayer.as_view(), name="delete_player"),

]
