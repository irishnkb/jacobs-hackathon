from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("items", hello.views.items, name="items"),
    path("search", hello.views.search, name="search"),
    path("db/", hello.views.db, name="db"),
    path("my_team_is_cool", hello.views.hello_world),
    path("sport", hello.views.sport),
    path("board", hello.views.board),
    path("everyday", hello.views.everyday),
    path("update_db/", hello.views.update_db)
]