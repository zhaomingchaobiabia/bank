from django.db import models


# Create your models here.

# 项目表
class Project_List(models.Model):
    project_name = models.CharField(max_length=20)
    tel = models.CharField(max_length=11)
    loan_type = models.CharField(max_length=20, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    loan = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True)
    loanuse = models.CharField(max_length=50, null=True, blank=True)
    min_money = models.IntegerField(null=True, blank=True)
    max_money = models.IntegerField(null=True, blank=True)
    valid_time = models.IntegerField(null=True, blank=True)
    repay_type = models.CharField(max_length=11, null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    project_password = models.CharField(max_length=32, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    get_money = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "Project_List"


# 项目投资表
class project_invest(models.Model):
    project_id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey('User_info', on_delete=models.CASCADE)
    money = models.IntegerField(null=True, blank=True)
    invest_time = models.DateTimeField(null=True, blank=True)
    pay_time = models.IntegerField(null=True, blank=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    get_money = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "project_invest"


# 资金记录表
class Money_record(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    from_src = models.CharField(max_length=100, null=True, blank=True)
    change_time = models.DateTimeField(null=True, blank=True)
    banlence = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "Money_record"


# 还款记录表
class payment_history(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    repay_time = models.DateTimeField(null=True, blank=True)
    balance = models.IntegerField(null=True, blank=True, default=0)
    status = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = "payment_history"


# 后台用户信息表
class t_back_user_info(models.Model):
    tel = models.CharField(max_length=11, null=True, blank=True)
    password = models.CharField(max_length=11, null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    jobtime = models.DateTimeField(null=True, blank=True)
    photo = models.FileField(null=True, blank=True)

    class Meta:
        db_table = "t_back_user_info"


# 用户信息表
class User_info(models.Model):
    tel = models.CharField(max_length=11)
    password = models.CharField(max_length=32)
    realname = models.CharField(max_length=50)
    postcard = models.CharField(max_length=18)
    banlence = models.FloatField(default=0)
    pay = models.CharField(max_length=32, default='111')
    img = models.FileField()
    createtime = models.DateTimeField()
    flag = models.IntegerField(blank=True, default=1)

    class Meta:
        db_table = "t_user_info"


# 借款表
class Borrow(models.Model):
    realname = models.CharField(max_length=50)
    tel = models.CharField(max_length=11)
    region = models.CharField(max_length=50, blank=True)
    money = models.IntegerField(blank=True)
    loan = models.IntegerField(blank=True)
    loantype = models.CharField(max_length=50, blank=True)
    loanuse = models.CharField(max_length=50, blank=True)
    status = models.IntegerField(blank=True, default=1)

    class Meta:
        db_table = "t_borrow_info"


# 登录记录表
class Login_info(models.Model):
    userid = models.IntegerField()
    ip = models.CharField(max_length=100)
    logintime = models.DateTimeField()

    class Meta:
        db_table = "t_login_info"


# 角色表
class Role(models.Model):
    rolename = models.CharField(max_length=11)
    roledesc = models.CharField(max_length=32)
    status = models.IntegerField(blank=True)

    class Meta:
        db_table = "t_role"


# 角色权限表
class Role_perm(models.Model):
    roleid = models.IntegerField()
    modname = models.CharField(max_length=100)

    class Meta:
        db_table = "t_role_perm"


# 用户角色表
class User_role(models.Model):
    roleid = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        db_table = "t_user_role"
