from django.views.generic import ListView, DetailView, FormView

from .models import Post
from datetime import datetime
from django.http import HttpRequest


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AboutUs(ListView):
    model = Post
    template_name = 'about.html'


class ContactUs(ListView):
    model = Post
    template_name = 'contact.html'


class StockChart(ListView):
    model = Post
    template_name = 'chart.html'

class StockScreener(ListView):
    model = Post
    template_name = 'stock_screener.html'


