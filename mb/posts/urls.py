"""mb_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path


from .views import HomePageView, PostDetailView, AboutUs, ContactUs, StockChart

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutUs.as_view(), name='about'),
    path('contact/', ContactUs.as_view(), name='contact'),
     path('chart/', StockChart.as_view(), name='chart'),
]
