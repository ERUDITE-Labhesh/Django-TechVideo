from django.urls import path
from . import views


urlpatterns = [
    path('', views.Homepage),
    path('indexpage/', views.Indexpage),
    # path('indexpage/<int:data>', views.Indexpage),
    # path('indexpage/<str:data>', views.Indexpage),
    # path('indexpage/<slug:data>', views.Indexpage),
    #path('indexpage/<data>', views.Indexpage)
]