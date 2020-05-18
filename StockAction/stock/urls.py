from django.urls import path
from . import views

urlpatterns = [path('',views.home,name='home'),
path('viewmore/<int:id>', views.viewmore, name='view')
]