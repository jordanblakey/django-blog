"""djangoproject URL Configuration

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

# allows including urls from subfolders.
from django.conf.urls import url, include

# import admin object from django.contrib
from django.contrib import admin

# URL patterns to match
urlpatterns = [
    # for all urls from the root, pass the urls.py from posts app.
    url(r'^$', include('posts.urls')),

    # pass urls from the built-in admin app in Django
    url(r'^admin/', admin.site.urls),

    # this seems redundant but does the same thing as the first pattern
    url(r'^posts/', include('posts.urls')),

    # Expect & pass the router a URL w/ an id,
    # Function 'details' from views.py
    # the varable name with string 'details' (not sure what this does)
]
