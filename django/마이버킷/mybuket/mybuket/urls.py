from django.contrib import admin
from django.urls import path, include
from mybuket_app import views
from accounts import views as accounts_views
from community import views as community_views
# accountsdptj views를 가져오는데 이름이 겹치니까 저렇게 바꾼다


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # 아무것도 없을때 mybuket_app에서 가져온 views안에 있는 frist라는 함수를 실행시킨다

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    # accounts 파일 안에 views.py 안에 login 을 만들어준다 
    path('create_account/', accounts_views.create_account, name='create_account'),
    path('bucket_log/', views.bucket_log, name='bucket_log'),
    path('mypage/', views.mypage, name='mypage'),
    path('change_info/', views.change_info, name='change_info'),
   
    path('show_following1/', views.show_following1, name='show_following1'),
    path('scrap/', views.scrap, name='scrap'),
    path('mywriting/', views.mywriting, name='mywriting'),
# ----------------------------------------commmu-------------------------------------------------
    path('freehome/', community_views.freehome, name='freehome'),
    path('postcreate', community_views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', community_views.detail, name='detail'),
    path('new_comment/<int:post_id>', community_views.new_comment, name='new_comment'),


    path('chome/', community_views.chome, name='chome'),
    path('freepostcreate', community_views.freepostcreate, name='freepostcreate'),
    path('freedetail/<int:post_id>', community_views.freedetail, name='freedetail'),
    path('new_freecomment/<int:post_id>', community_views.new_freecomment, name='new_freecomment'),
]
