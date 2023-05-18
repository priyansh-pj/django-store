from django.urls import path
from . import views
urlpatterns = [
    path("", views.store_landing,name="landing"),
    path("items/<str:id>/", views.items,name="items"),
    path("checkout/<str:id>/", views.checkout,name="checkout"),
    path("api/category",views.api_category,name="api_category"),
    path("api/items",views.api_items,name="api_items")

]