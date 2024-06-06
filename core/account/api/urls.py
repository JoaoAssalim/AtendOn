from django.urls import re_path
from rest_framework_bulk.routes import BulkRouter

from core.account.api.views import * 

app_name = 'api_account'
namespace = app_name

router_bulk = BulkRouter()
router_bulk.register(r'account', AccountAPIView, basename='account')
router_bulk.register(r'auth', LoginAPIView, basename='auth')

urlpatterns = [

] + router_bulk.urls