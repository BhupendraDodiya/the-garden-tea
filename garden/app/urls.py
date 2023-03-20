from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('infor/',views.infor,name='inquirey'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
