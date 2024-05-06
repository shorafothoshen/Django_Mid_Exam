
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home, name="Home"),
    path("category/<slug:category_slug>",views.Home, name="FilterCategory"),
    path("accounts/",include("author.urls")),
    path("Details/<slug:slug>/",views.DetailsCar.as_view(), name="carDetails"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)