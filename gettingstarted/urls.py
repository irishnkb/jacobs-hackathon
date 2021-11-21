from django.urls import path, include
from django.contrib import admin

admin.autodiscover()

import static.hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", static.hello.views.index, name="index"),
    path("items", static.hello.views.items, name="items"),
    path("db/", static.hello.views.db, name="db"),
    path("my_team_is_cool", static.hello.views.hello_world),
    path("admin/", admin.site.urls),
    path("sports", static.hello.views.sport),
    path("update_db/", static.hello.views.update_db)
]