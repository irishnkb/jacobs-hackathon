from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import gettingstarted.static.hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", gettingstarted.static.hello.views.index, name="index"),
    path("items", gettingstarted.static.hello.views.items, name="items"),
    path("db/", gettingstarted.static.hello.views.db, name="db"),
    path("my_team_is_cool", gettingstarted.static.hello.views.hello_world),
    path("admin/", admin.site.urls),
    path("sports", gettingstarted.static.hello.views.sport),
    path("update_db/", gettingstarted.static.hello.views.update_db)
]