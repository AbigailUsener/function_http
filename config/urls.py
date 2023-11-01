from django.contrib import admin
from django.urls import path
from app.views import greeting
from app.views import how_old
from app.views import order
urlpatterns = [
    path('hey/<str:name>', greeting),
    path('age-in/<int:end>/<int:birthyear>',how_old),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>',order),
    path('admin/', admin.site.urls),
]