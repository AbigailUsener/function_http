from django.contrib import admin
from django.urls import path
from app.views import greeting
from app.views import how_old
from app.views import order
urlpatterns = [
    path('hello/<str:name>', greeting),
    path('how_old/<int:end>/<int:birthyear>',how_old),
    path('order/<int:burgers>/<int:fries>/<int:drinks>',order),
    path('admin/', admin.site.urls),
]