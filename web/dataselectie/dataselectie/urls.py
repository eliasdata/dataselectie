# Packages
from django.conf.urls import include, url

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^dataselectie/bag/', include('datasets.bag.urls')),
    url(r'^status/', include('health.urls'))
]
