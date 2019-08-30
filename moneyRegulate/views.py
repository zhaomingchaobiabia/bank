from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .forms import *
from .models import *
import re, datetime, time
from front.decorators import auth_session

# Create your views here.
flags = True
bal = 0


def borrow_screen(request):
    # 获取网页数据
    data = request.GET
    name = data.get('name')
    tel = data.get('tel')

    # 获取用户个人信息
    user = User_info.objects.filter(tel=tel).first()
    # 判断用户是否为黑名单
    if user:
        if user.flag == 2:  # 2代表被拉黑
            return JsonResponse({'msg': '您没有借款资格'})

        # 根据用户id获取还款记录表中用户信息
        paym = payment_history.objects.filter(user_id=user.id).first()
        # 判断用户是否欠款
        if paym:
            if paym.status == '1' or paym.status == '2':
                return JsonResponse({'msg': '请先还完款后在进行申请借款'})

    # 获取已提交借款请求用户
    bor = Borrow.objects.filter(tel=tel).first()
    # 判断用户是否已提交过借款请求
    if bor:
        if bor.status == 1 or bor.status == 2 or bor.status == 4:  # 1代表已发起借款未审核
            return JsonResponse({'msg': '您已经发布过借款请求，请耐心等待管理员审核'})

    # 获取已发布项目的用户信息
    pro = Project_List.objects.filter(tel=tel).first()
    # 判断用户是否已发布项目
    if pro:
        # 获取项目投资时间
        time = pro.valid_time
        return JsonResponse({'msg': f'您的借款申请正在筹资中，请耐心等待{time}天'})

    # 必选项不为空
    if tel == '' or name == '' or data.get('region') == '' or data.get('money') == '' or data.get('loan') == '':
        return JsonResponse({'msg': '必选项不能为空'})

    # 判断手机号格式：
    regex = '^[1](3|5|6|7|8)\d{9}$'
    res = re.match(regex, tel)
    print(res)
    if not res:
        return JsonResponse({'msg': '手机号格式不正确'})

    # 判断金额
    regex = '^\d+$'
    res = re.match(regex, data.get('money'))
    if not res:
        return JsonResponse({'msg': '金额至少为是一位数的数字'})

    # 校验成功、存储数据
    bor = Borrow(
        realname=data.get('name'),
        tel=data.get('tel'),
        region=data.get('region'),
        money=data.get('money'),
        loan=data.get('loan'),
        loanuse=data.get('loantype'),
        loantype=data.get('loanuse')
    )
    bor.save()
    # return redirect(to='/property/borrow')
    return JsonResponse({'msg': '申请成功，正等待审核'})


@auth_session
def touzhi(request):
    global bal

    if request.GET.get('id') == 'false':
        id = Project_List.objects.filter(status='筹资中').first().id
        return redirect(to=f'/property/touzhi?id={id}')

    try:
        # 获取用户信息
        id = request.session.get('loginFlag').get('id')
        user = User_info.objects.filter(id=id).first()

        # 根据项目id获取项目表和项目投资表
        id = request.GET.get('id')
        # 获取项目表对象
        item = Project_List.objects.filter(id=id).first()
        balance = item.money - item.get_money
        plan = item.get_money / item.money
        plan = round(plan, 2) * 100
        ti = str(item.time)
        list = ti.split(' ')
        times = list[0]
        if balance == 0:
            Project_List.objects.filter(id=id).update(status='已完成')
            print(item.status)

        # 设置投标时间
        day = item.valid_time
        t = datetime.datetime.strptime(ti, '%Y-%m-%d %H:%M:%S')
        t1 = t + datetime.timedelta(days=day)
        t1 = str(t1)
        list = t1.split(' ')
        t1 = list[0]
        # 获取项目投资表
        pro = project_invest.objects.filter(project_id=id)
        items = {
            'name': item.project_name,  # 项目名称
            'rate': item.rate,  # 年利率
            'repay_type': item.repay_type,  # 还款方式
            'loan': item.loan,  # 投资期限
            'valid_time': item.valid_time,  # 可投时间
            'money': item.money,  # 项目总额
            'time': times,  # 发布时间
            'balance': balance,
            'plan': plan,
            't1': t1,
            'info': item.loanuse
        }
        bal = balance
        return render(request, 'front/touzhi.html',
                      {'p_id': id, 'name': user.realname, 'balance': user.banlence, 'tel': user.tel, 'item': items,
                       'pro': pro, })

    except:
        return render(request, 'front/index.html')


def tbmoney(request):
    global flags
    # 获取用户输入数据信息
    tbm = request.GET.get('tbm')
    # 项目余额
    balance = bal

    # 获取用户余额
    id = request.session.get('loginFlag').get('id')
    user = User_info.objects.filter(id=id).first()
    bl = user.banlence
    # 判断
    if tbm == None:
        flags = False
        return JsonResponse({'msg': '内容不能为空'})
    # 判断用户输入类型
    regex = '^\d+$'
    res = re.match(regex, tbm)
    if not res:
        flags = False
        return JsonResponse({'msg': '投标金额为数字'})
    if int(tbm) < 50 and balance >= 50:
        flags = False
        return JsonResponse({'msg': '投标金额50起投'})
    if int(tbm) > bl:
        flags = False
        return JsonResponse({'msg': '您的账户余额不足，请充值'})
    if balance == 0:
        flags = False
        return JsonResponse({'msg': '项目已结束'})
    if int(tbm) > balance:
        flags = False
        return JsonResponse({'msg': f'项目剩余投资金额为{balance}元 ,请修改投资金额'})
    flags = True
    # return JsonResponse({'msg': '金额可用'})


def bid(request, p_id):
    # 如果金额验证成功
    if flags is True:
        # 获取用户输入数据信息
        data = request.POST
        tbm = data.get('tbm')
        tbpassword = data.get('tbpassword')
        zfpassword = data.get('zfpassword')
        # 获取项目密码
        item = Project_List.objects.filter(id=p_id).first()
        password = item.project_password
        # 判断投标密码是否正确
        if tbpassword != password:
            return redirect(to='/front')

        # 获取当前用户支付密码
        id = request.session.get('loginFlag').get('id')
        pay = User_info.objects.filter(id=id).first().pay
        # 判断支付密码是否相同
        if zfpassword != pay:
            return redirect(to='/front')

        # 获取项目理财表
        print(p_id)
        p = project_invest.objects.filter(project_id=p_id, user_id=id).first()
        if p:
            m = p.money + int(tbm)
            pro = project_invest(
                id=p.id,
                project_id=p_id,
                user_id=id,
                money=m,
                invest_time=datetime.datetime.now(),
            )
            pro.save()

        else:
            pro = project_invest(
                project_id=p_id,
                user_id=id,
                money=int(tbm),
                invest_time=datetime.datetime.now(),
            )
            pro.save()

        mr = Money_record(
            user_id=id,
            money=int(tbm),
            from_src='投资',
            change_time=datetime.datetime.now(),
            banlence=User_info.objects.filter(id=id).first().banlence-int(tbm)

        )
        mr.save()
        # 更新数据库的值
        # 更新用户余额
        balan = User_info.objects.filter(id=id).first().banlence
        bala = balan - int(tbm)
        User_info.objects.filter(id=id).update(banlence=bala)
        # 更新项目余额
        mon = Project_List.objects.filter(id=p_id).first().get_money
        m = mon + int(tbm)
        Project_List.objects.filter(id=p_id).update(get_money=m)
        print(balan, mon)

        return redirect(to=f'/property/touzhi?id={p_id}')

    return redirect(to=f'/property/touzhi?id={p_id}')


def timed(request):
    pass
