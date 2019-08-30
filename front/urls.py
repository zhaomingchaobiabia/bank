from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='front'),  # 主页
    path('reg', views.reg),  # 注册页面
    path('reg_login', views.reg_login),  # 注册页面 2
    path('myaccount', views.myaccount),  # 注册成功返回页面
    path('myAccount', views.myAccount),  # 用户页面
    path('login', views.login),  # 登录界面
    path('login_name', views.login_name),  # 验证登录用户名
    path('log_in', views.log_in),  # 登录界面__验证用户和 密码是否正确
    path('loan', views.loan),
    path('finish', views.finish),  # 查看已完成项目
    path('exit', views.exit),  # 退出登录
    path('check', views.check),  # 注册 异步 查询用户是否存在
    path('index_show', views.index_show),  # 首页异步显示
]