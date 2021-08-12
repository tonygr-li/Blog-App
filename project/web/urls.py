from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from. import views

urlpatterns = [
	# name is used to identify the url so it should be unique
    # views means to go see the views.py file
    path('', views.home, name='web-home'),
    path('home/', views.home, name='web-home'),
    path('about/', views.about, name='web-about'),
    path('portfolio/', views.portfolio, name='web-portfolio'),
    path('contact/', views.contact, name='web-contact'),
    path('about/', views.about, name='web-about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)