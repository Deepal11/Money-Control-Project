from django.urls import path
from . import views

urlpatterns = [path('',views.home,name='home'),
path('viewmore1', views.viewmore1, name='view'),
path('viewmore2', views.viewmore2, name='view'),
path('viewmore3', views.viewmore3, name='view'),
path('viewmore4', views.viewmore4, name='view'),
path('viewmore5', views.viewmore5, name='view'),
path('viewmore6', views.viewmore6, name='view'),
path('viewmore7', views.viewmore7, name='view'),
path('viewmore8', views.viewmore8, name='view'),
path('viewmore9', views.viewmore9, name='view'),
path('viewmore10', views.viewmore10, name='view'),
path('viewmore11', views.viewmore11, name='view'),
path('viewmore12', views.viewmore12, name='view'),
path('viewmore13', views.viewmore13, name='view'),
path('viewmore14', views.viewmore14, name='view'),
path('viewmore15', views.viewmore15, name='view'),
path('viewmore16', views.viewmore16, name='view')
]