from django.urls import path
from order import views

urlpatterns = [
    path('shop/', views.shop, name="shop"),
    # path('menus/', views.menu, name="menu"),
    path('menus/<int:shop>', views.menu, name="menu"),
    path('order/', views.order, name="order")
]