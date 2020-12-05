
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #画像参照のため追加
from django.contrib.staticfiles.urls import static #画像参照のため追加
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #画像参照のため追加


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todolist.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)