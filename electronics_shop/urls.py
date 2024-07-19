from django.urls import path

from electronics_shop.apps import ElectronicsShopConfig
from electronics_shop.views import (ProductListAPIView, SupplierCreateAPIView,
                                    SupplierDestroyAPIView,
                                    SupplierListAPIView,
                                    SupplierRetrieveAPIView,
                                    SupplierUpdateAPIView)

appname = ElectronicsShopConfig.name

urlpatterns = [
    path("suppliers/", SupplierListAPIView.as_view(), name="suppliers-list"),
    path(
        "suppliers/<int:pk>/",
        SupplierRetrieveAPIView.as_view(),
        name="suppliers-detail",
    ),
    path("suppliers/create/", SupplierCreateAPIView.as_view(), name="suppliers-create"),
    path(
        "suppliers/<int:pk>/update/",
        SupplierUpdateAPIView.as_view(),
        name="suppliers-update",
    ),
    path(
        "suppliers/<int:pk>/delete/",
        SupplierDestroyAPIView.as_view(),
        name="suppliers-delete",
    ),
    path("products/", ProductListAPIView.as_view(), name="products-list"),
]
