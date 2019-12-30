from django.urls import path

from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('', HomePageView.as_view(), name = 'home'),  
    # Note: When using Class-Based Views, always add as_view() at the end of the view name.
]