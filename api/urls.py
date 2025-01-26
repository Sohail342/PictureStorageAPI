from django.urls import path
from .views import Pictures, PictureDetail, Categories, CategoryPictures

urlpatterns = [

    path("api/pictures/", Pictures.as_view()),
    path("api/pictures/<int:pk>/", PictureDetail.as_view()),
    path("api/categories/", Categories.as_view()),
    path("api/categories/<int:pk>/", Categories.as_view()),
    path("api/categories/<int:pk>/pictures/", CategoryPictures.as_view(), name="category_pictures"),


]
