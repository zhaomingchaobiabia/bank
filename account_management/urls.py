

from django.urls import path,re_path
#re_path （“正则匹配路径”，函数） 支持正则表达式匹配

from . import views

#给应用添加应用名,便于进行路由管理
app_name = "account_management"

urlpatterns = [
    path('account_recharge/',views.account_recharge,name="account_recharge"),   #账户充值
    path('money_record/',views.money_record,name="money_record"),      #资金记录
    path('investment_management/',views.investment_management,name="investment_management"),      #投资管理

    path('password_management/',views.password_management,name="password_management"),  #密码管理
    path('repayment_account/',views.repayment_account,name="repayment_account"),   #账户还款
    path('personal_reimbursement/',views.personal_reimbursement,name="personal_reimbursement"),   #个人还款
    path('tou_zi/',views.tou_zi,name="tou_zi"),  # 个人账户“投资中”显示的信息
    path('huan_kuan/',views.huan_kuan,name="huan_kuan"),  # 个人账户“还款中”显示的信息
    path('wan_cheng/',views.wan_cheng,name="wan_cheng"),  # 个人账户“已完成”显示的信息
    path('zhuan_rang/',views.zhuan_rang,name="zhuan_rang"),  # 个人账户“转让中”显示的信息
    # path('u_photo/',views.u_photo,name="u_photo"),  # 用户中心的头像显示
    # path('change_photo/',views.change_photo,name="change_photo"),    #用户中心头像改变



]