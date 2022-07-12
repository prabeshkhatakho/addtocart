from .views import *
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('items',ProductListView.as_view(), name = 'items' )
]