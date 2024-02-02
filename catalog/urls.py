from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import home_page, ProductsListView, BlogListView, BlogCreateView, BlogUpdateView, \
    BlogDetailView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

# from catalog.views import products

app_name = CatalogConfig.name

urlpatterns = [
    path('', home_page, name='home_page'),
    # path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('view/<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('create_prod/', ProductCreateView.as_view(), name='product_create'),
    path('update_prod/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete_prod/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('view_prod/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),

]
