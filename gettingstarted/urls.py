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
    path("db/", hello.views.db, name="db"),
<<<<<<< HEAD
    path("my_team_is_cool", hello.site.hello_world),
    path("admin/", admin.site.urls),
=======
    path("my_team_is_cool", hello.views.hello_world),
    path("sports", hello.views.sport),
>>>>>>> 6c134edde42264137666d96e9143afb8a3cc4ed0
    path("update_db/", hello.views.update_db)
]