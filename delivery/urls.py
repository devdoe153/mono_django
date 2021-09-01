from django.urls import path
from delivery import views

urlpatterns = [
    path('orders/', views.order_list, name="order_list"),
    # # path('menus/', views.menu, name="menu"),
    # path('menus/<int:shop>', views.menu, name="menu"),
    # path('delivery/', views.delivery, name="delivery")
]