from django.urls import re_path
from rest_framework_bulk.routes import BulkRouter

from core.clients.api.views import * 

app_name = 'api_clients'
namespace = app_name

router_bulk = BulkRouter()
router_bulk.register(r'clients', ClientAPIView, basename='clients')

urlpatterns = [

] + router_bulk.urls