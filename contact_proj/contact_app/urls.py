from django.urls import path
from .views import contact_us#,successView

urlpatterns = [
    path('contact_us/', contact_us, name='contact_us'),
]
