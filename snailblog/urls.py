from django.urls import path
from . import views
from .views import video

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact_us,name='contact'),
    path('blog/', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
    path('post/<int:pk>/', views.post_detail,name='post_detail'),
    path('post/new/', views.post_new,name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish',views.post_publish, name='post_publish'),
    path('post/<pk>/remove',views.post_remove,name='post_remove'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]