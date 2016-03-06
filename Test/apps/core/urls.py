from django.conf.urls import url, include

urlpatterns = [

    url(r'', include('apps.test1.urls', namespace="test1_app")),
    url(r't2', include('apps.test2.urls', namespace="test2_app")),

]
