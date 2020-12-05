from django.conf import settings
from django.contrib import admin
from django.urls import include, path
# from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework import routers

from apiv0 import views as apiv0_views
from apiv1 import views as apiv1_views
from apiv2 import views as apiv2_views

router = routers.DefaultRouter()
router.register('books', apiv2_views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v0/books/', apiv0_views.BookListCreateAPIView.as_view()),
    path('api/v0/books/<pk>/', apiv0_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books/', apiv1_views.BookListCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', apiv1_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v2/', include(router.urls)),
]

if settings.DEBUG:
    # urlpatterns += [path('docs/', include_docs_urls(title='APIドキュメント'))]
    urlpatterns += [
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'),
             name='swagger-ui'),
        path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
