from django.contrib import admin
from django.urls import path , include 
from accounts import views as acc_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("admin-login/", acc_views.admin_login, name="admin-login"),
    path('', include(('core.urls', 'core'), namespace='core')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('books/', include(('books.urls', 'books'), namespace='books')),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
