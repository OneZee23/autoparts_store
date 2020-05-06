from django.urls import path

from . import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("catalog/", views.AutopartsView.as_view(), name="catalog"),
    path("<slug:slug>/", views.AutopartsDetailView.as_view(), name="autopart_detail")
]