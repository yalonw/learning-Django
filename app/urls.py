from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.frontpage),
    path('settings', views.settings),
    path('add_category', views.addCategory),
    # re_path(r'^delete_category/(?P<category>\w+)', views.deleteCategory),
    path('delete_category/<str:category>', views.deleteCategory),
    path('add_record', views.addRecord),
    path('delete_record', views.deleteRecord),

    path('hello', views.hello, name='hello'),
    path('dashboard', views.dashboard, name='dashboard'),
]