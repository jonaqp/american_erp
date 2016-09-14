from django.conf.urls import url, include
from .views import BrandView, BrandCreateView, BrandEditView, BrandListView

brand_patterns = ([
   url(r'^$', BrandView.as_view(), name="index"),
   url(r'^add/', BrandCreateView.as_view(), name="add"),
   url(r'^edit/', BrandEditView.as_view(), name="edit"),
   url(r'^list/', BrandListView.as_view(), name="list"),
], 'admin-client')

urlpatterns = [
    url(r'^brand/', include(brand_patterns)),

]

