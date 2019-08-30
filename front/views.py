from django.shortcuts import render, redirect, reverse
from .models import User_info, Project_List
from .decorators import auth_session
import hashlib, json
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# 首页页面
def index(request):
    # 从数据库中、查询所有的资源
    data = Project_List.objects.all()

    # 把查询到的数据、放到 Paginator 插件中,每页显示5条
    p = Paginator(data, 5)

    # 获取要查询第几页的数据
    page = int(request.GET.get("page")) if request.GET.get("page") else 1
    # 返回页面所需要的数据
    data = p.get_page(page)

    # 查看当前登录用户
    if request.session.get('loginFlag'):
        tel = request.session.get('loginFlag').get('tel')
        return render(request, 'front/index.html', {"data": data, 'tel': tel})
    return render(request, 'front/index.html', {"data": data})


# 查看已完成项目
def finish(request):
    data = request.POST.get('data')
    print(data)
    if data == '投资中':
        user = list(Project_List.objects.filter(status='筹资中'))
        print(user)
        users = json.dumps(user)
        print(user)
        return JsonResponse(users)
    return redirect(to='/front')


# 注册页面
def reg(request):
    return render(request, 'front/reg.html')


# 存入数据库
def reg_login(request):
    data = request.POST

    tel = data.get("tel")
    user = User_info.objects.filter(tel=tel)
    if user:
        data = '用户名已经存在'
        return render(request, "front/reg.html", {"user": data})
    password = data.get('password')
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))  # 注意转码
    res = md5.hexdigest()
    user = User_info.objects.create(tel=data.get("tel"), password=res, banlence=0)
    request.session['loginFlag'] = {'id': user.id, 'tel': user.tel}
    return render(request, 'front/reg_ok.html', {'user': user.id, 'tel': user.tel})


# 账户姓名和身份证
def myaccount(request):
    data = request.POST
    id = data.get("data")
    user = User_info.objects.filter(id=id)
    user.update(realname=data.get('name'),
                postcard=data.get('card'))

    return redirect(to='/front/login')


# 登录异步验证用户是否存在
@csrf_exempt
def login_name(request):
    datas = request.POST
    tel = datas["data"]
    user = User_info.objects.filter(tel=tel).first()

    if user:
        if user.flag == 2:
            return JsonResponse({"data": '你没有登录资格！！'})
        return JsonResponse({"data": ''})
    return JsonResponse({"data": '该用户不存在，请重新输入。'})


# 异步查询注册用户是否存在
@csrf_exempt
def check(request):
    tel = request.POST.get('tel')
    user = User_info.objects.filter(tel=tel)
    if user:
        return JsonResponse({"tel": '该用户已存在。'})
    return JsonResponse({"tel": ''})


# 用户登录密码验证
def log_in(request):
    data = request.POST
    tel = data.get('name')
    password = data.get('password')

    md5 = hashlib.md5()  # 加密
    md5.update(password.encode('utf-8'))  # 注意转码
    res = md5.hexdigest()
    user = User_info.objects.filter(tel=tel).first()
    if user:
        if user.password == res:
            request.session['loginFlag'] = {'id': user.id, 'tel': user.tel}
            return redirect(to=reverse('front'))
        return redirect(to='/front/login')
    return redirect(to='/front/login')


# 投资页面
# @auth_session
# def touzhi(request):
#     return render(request, 'front/touzhi.html')
#

# 借款
@auth_session
def loan(request):
    tel = request.session.get('loginFlag').get('tel')
    return render(request, 'front/loan.html', {'tel': tel})


# # 还款
# @auth_session
# def wyhk(request):
#     return render(request, 'front/wyhk.html')

# 我的账户
@auth_session
def myAccount(request):
    return render(request, 'front/myAccount.html')


def login(request):
    return render(request, 'front/login.html')


# 退出登录
def exit(request):
    request.session.clear()
    request.session.clear_expired()
    return redirect(to=reverse('front'))


# 异步获取首页资源
@csrf_exempt
def index_show(request):
    data = request.POST
    data2 = data.get('data2')
    data3 = data.get('data3')
    data4 = data.get('data4')
    data5 = data.get('data5')
    dict2 = {'0': False, '1': '筹资中', '2': '已流标', '3': '已完成'}
    dict3 = {'0': False, '1': 12, '2': 18, '3': 19}
    dict4 = {'0': False, '1': 1, '2': 3, '3': 6}
    dict5 = {'0': False, '1': '先息后本', '2': '到期还本付息'}
    if dict2[data2]:
        user = Project_List.objects.filter(status=dict2[data2])
    else:
        user = Project_List.objects.all()

    data3 = dict3[data3]
    if data3 == 12:
        user = user.filter(rate__lt=12)
    elif data3 == 18:
        user = user.filter(rate__gte=12, rate__lte=18)
    elif data3 == 19:
        user = user.filter(rate__gt=18)

    data4 = dict4[data4]
    if data4 == 1:
        user = user.filter(loan__gte=1, loan__lte=3)
    elif data4 == 3:
        user = user.filter(loan__gte=3, loan__lte=6)
    elif data4 == 6:
        user = user.filter(loan__gte=6, loan__lte=12)
    data5 = dict5[data5]
    if data5:
        user = user.filter(repay_type=data5)
    ls = []
    for i in user:
        ls.append(
            {'id': i.id, 'project_name': i.project_name, 'rate': i.rate, 'loan': i.loan, 'repay_type': i.repay_type,
             'money': i.money, 'status': i.status})
    return JsonResponse({'data': ls})
