"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from bookstore import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^add_category/$', views.AddCategoryView.as_view(), name='add_category'),
    url(r'^add_author/$', views.AddAuthorView.as_view(), name='add_author'),
    url(r'^books/new/$', views.AddBookView.as_view(), name='add_book'),
    url(r'^books/(?P<pk>[0-9]+)/newcomment/$', views.AddCommentView.as_view(), name='add_comment'),
    url(r'^books/$', views.books, name='books'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.DetailsBookView.as_view(), name='book_details'),
    url(r'^books/(?P<pk>[0-9]+)/edit/$', views.UpdateBookView.as_view(), name='book_edit')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
