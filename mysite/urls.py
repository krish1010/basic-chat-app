from django.contrib import admin
from django.urls import path, include
from chat import views as chat_view

urlpatterns = [path("admin/", admin.site.urls), path("chat/", include("chat.urls")), path("", chat_view.default)
]
