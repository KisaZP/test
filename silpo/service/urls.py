"""silpo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views
from .views import FeedbackView


app_name = 'service'

urlpatterns = [
    path('feedback/', FeedbackView.as_view()),
    # path('ok/', TemplateView.as_view(TemplateView_name='service/ok_html', name='ok'))
    # path(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
]
