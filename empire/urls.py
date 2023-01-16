from django.urls import path
from . import views
# got this later 
from .views import redirect_view

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('redirect', redirect_view),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('category/<str:id>',views.categories,name='category'), 
    path('signout',views.signout,name='signout'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('profile',views.profile,name='profile'),
    path('update',views.update,name='update'),
    path('passupdate',views.passupdate,name='passupdate'),
    path('catdet/<slug:theslug>',views.catdet,name='catdet'),
    path('search',views.search,name='search'),
    path('post_like',views.post_like,name='post_like'),
]
