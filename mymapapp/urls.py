from django.urls import path
from .views import home_view, signup_view, logout_view, login_view, map_view

# To make sure you can call views url like 'mymapapp:home' and not throw an exception.
app_name = 'mymapapp'

"""
The userprofile.html is only rendered using home_view if the user is logged in.
The rest of the registered url is as you expected with the view.
"""
urlpatterns = [
    path('', home_view, name = 'home'),
    path('login', login_view, name = 'login'),
    path('signup', signup_view, name = 'signup'),
    path('logout', logout_view, name = 'logout'),
    path('map', map_view, name = 'map')
]