from django.urls import path
from . import views  # Import the get_property_data function

urlpatterns = [
    path('get_property_data/<str:property_name>/<str:meter_type>/', views.get_property_data, name='get_property_data'),
    path('get_meter_types/<str:property_name>/', views.get_meter_types, name='get_meter_types'),
    path("", views.home, name="home"),
    path("d3-graph/", views.d3_graph, name="d3_graph"),
    path("register/", views.register, name="register"),
    path("about_us/", views.about_us, name="about_us"),
    path("login/", views.login, name="login"),
    path('user_actions/', views.user_actions, name='user_actions'),
]