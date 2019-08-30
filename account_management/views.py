from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from front import models
import datetime
#向表格中传入时间数据
from datetime import datetime
from django.core.paginator import Paginator
from front.models import project_invest, Borrow, payment_history, Money_record, User_info,Project_List
from front.decorators import auth_session
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# 异步请求 返回数据
from django.http.response import JsonResponse



# Create your views here.


@auth_session
def account_recharge(request):  # 账户充值
    cz = float(request.POST.get("czje"))
    id = request.session.get("loginFlag").get("id")

    # 获取账户余额
    t = models.User_info.objects.filter(id=id).values("banlence").first()["banlence"]
    if not t:
        t = 0

    # 余额数与充值数相加，并更新用户余额
    money = cz + t
    models.User_info.objects.filter(id=id).update(banlence=money)

    # 添加用户资金记录数据
    u_money = money
    from_src = "用户充值"
    chang_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res = models.Money_record(
        user_id=id,
        money=cz,
        from_src="用户充值",
        change_time=datetime.now(),
        banlence=u_money
    )
    res.save()
    if not models.Money_record.objects.filter(user_id=id):
        u_money = t
    return JsonResponse({"u_money": u_money, "cz": cz, "from_src": from_src, "change_time": chang_time})


# 资金记录
@auth_session
def money_record(request):
    # 获取资金记录数据
    id = request.session.get("loginFlag").get("id")
    tel = request.session.get("loginFlag").get("tel")
    user = models.User_info.objects.get(id=id)
    data = models.Money_record.objects.filter(user_id=id).order_by("-change_time")
    # 进行分页
    p = Paginator(data, 5)
    # 获取要查询第几页的数据
    page = int(request.GET.get("page")) if request.GET.get("page") else 1
    # 返回页面所需要的数据
    data = p.get_page(page)
    return render(request, "front/myAccount.html", {"data": data, "user": user, "tel": tel})


@auth_session
def investment_management(request):  # 投资管理
    id = request.session.get("loginFlag").get("id")
    # 获取用户信息
    user = models.User_info.objects.get(id=id)

    # 累计投资金额
    m = models.project_invest.objects.filter(user_id=id).values_list("money")
    money = 0
    # 判断投资金额是否为空
    if not m.first():
        money = 0
    else:
        # 计算累计投资金额
        for i in m:
            money += i[0]

    money = '%.2f' % money

    # 投标中的项目数
    # 获取该用户总共投资的项目id
    p = models.project_invest.objects.filter(user_id=id).order_by("pay_time")

    # 对所有项目进行筛选 获取投标中的项目
    count = 0
    if not p.values_list("project_id").first():
        count = 0
    else:
        # 计算筹资中的项目数量
        for i in p.values_list("project_id"):
            t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()
            if t[0] == "筹资中":
                count += 1

    # 还款中的项目数量
    back = 0
    if not p.values_list("project_id").first():
        back = 0
    else:
        # 计算已完成的项目数量
        for i in p.values_list("project_id"):
            t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()
            if t[0] == "已完成":
                back += 1

    # 投资中的项目
    # 获取投资中项目名称
    c_zi = []

    if not p.first():
        count = 0
    else:
        # 计算筹资中的项目数量
        for i in p.values_list("project_id"):
            # print(i)
            # print(i[0])
            v = {"p_name": "", "j_name": "", "y_money": "", "l_money": "", "zt": "", "pay_time": ""}

            # 获取id为i[0]的项目
            t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()

            # 项目的投资金额
            mon = p.filter(project_id=i[0]).values_list("money").first()[0]

            # 项目的收益时间
            pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
            if not pay_time:
                pay_time = "暂无"
            else:
                pay_time = pay_time.strftime("%Y-%m-%d %H:%M:%S")

            if t[0] == "筹资中":
                # 项目名
                p_name = models.Project_List.objects.get(id=i[0]).project_name
                v["p_name"] = p_name
                # print(p_name)
                # 借款者
                j_name = models.Project_List.objects.get(id=i[0]).tel
                v["j_name"] = j_name
                # 应收金额
                y_money = (models.Project_List.objects.get(id=i[0]).rate * mon) / 100 + mon
                v["y_money"] = y_money
                # print(y_money)
                # 应收利息
                l_money = (models.Project_List.objects.get(id=i[0]).rate * mon) / 100
                v["l_money"] = l_money
                # 状态
                zt = "筹资中"
                v["zt"] = zt
                # 时间
                v["pay_time"] = pay_time
                c_zi.append(v)

    return render(request, "front/tzgl.html",
                  {"money": money, "count": count, "back": back, "user": user, "c_zi": c_zi})


def tou_zi(request):
    id = request.session.get("loginFlag").get("id")
    p = models.project_invest.objects.filter(user_id=id)
    c_zi = []

    # 计算筹资中的项目数量
    for i in p.values_list("project_id"):
        # print(i)
        # print(i[0])
        v = {"p_name": "", "j_name": "", "y_money": "", "l_money": "", "zt": "", "pay_time": ""}
        # 获取id为i[0]的项目
        t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()

        # 项目的投资金额
        money = p.filter(project_id=i[0]).values_list("money").first()[0]
        # print(money)

        # 项目的收益时间
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        if not pay_time:
            pay_time = "暂无"
        else:
            pay_time = pay_time.strftime("%Y-%m-%d %H:%M:%S")
        # print(investtime)
        if t[0] == "筹资中":
            # 项目名
            p_name = models.Project_List.objects.get(id=i[0]).project_name
            v["p_name"] = p_name
            # print(p_name)
            # 借款者
            j_name = models.Project_List.objects.get(id=i[0]).tel
            v["j_name"] = j_name
            # 应收金额
            y_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100 + money
            v["y_money"] = y_money
            # print(y_money)
            # 应收利息
            l_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100
            v["l_money"] = l_money
            # 状态
            zt = "筹资中"
            v["zt"] = zt
            # 时间
            v["pay_time"] = pay_time
            c_zi.append(v)

    return JsonResponse({"c_zi": c_zi})


def huan_kuan(request):
    id = request.session.get("loginFlag").get("id")
    p = models.project_invest.objects.filter(user_id=id)
    w_cheng = []

    # 计算已完成的项目数量
    for i in p.values_list("project_id"):
        # print(i)
        # print(i[0])
        v = {"p_name": "", "j_name": "", "y_money": "", "l_money": "", "zt": "", "pay_time": ""}
        # 获取id为i[0]的项目
        t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()

        # 项目的投资金额
        money = p.filter(project_id=i[0]).values_list("money").first()[0]
        # print(money)

        # 项目的收益时间
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        if not pay_time:
            pay_time = "暂无"
        else:
            pay_time = pay_time.strftime("%Y-%m-%d %H:%M:%S")
        # print(investtime)
        if t[0] == "已完成":
            # 项目名
            p_name = models.Project_List.objects.get(id=i[0]).project_name
            v["p_name"] = p_name
            # print(p_name)
            # 借款者
            j_name = models.Project_List.objects.get(id=i[0]).tel
            v["j_name"] = j_name
            # 应收金额
            y_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100 + money
            v["y_money"] = y_money
            # print(y_money)
            # 应收利息
            l_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100
            v["l_money"] = l_money
            # 状态
            zt = "还款中"
            v["zt"] = zt
            # 时间
            v["pay_time"] = pay_time
            w_cheng.append(v)

    return JsonResponse({"w_cheng": w_cheng})


def wan_cheng(request):
    id = request.session.get("loginFlag").get("id")
    p = models.project_invest.objects.filter(user_id=id)
    x_hui = []

    # 计算已销毁的项目数量
    for i in p.values_list("project_id"):
        # print(i)
        # print(i[0])
        v = {"p_name": "", "j_name": "", "y_money": "", "l_money": "", "zt": "", "pay_time": ""}
        # 获取id为i[0]的项目
        t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()

        # 项目的投资金额
        money = p.filter(project_id=i[0]).values_list("money").first()[0]
        # print(money)

        # 项目的收益时间
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        if not pay_time:
            pay_time = "暂无"
        else:
            pay_time = pay_time.strftime("%Y-%m-%d %H:%M:%S")
        # print(investtime)
        if t[0] == "已销毁":
            # 项目名
            p_name = models.Project_List.objects.get(id=i[0]).project_name
            v["p_name"] = p_name
            # print(p_name)
            # 借款者
            j_name = models.Project_List.objects.get(id=i[0]).tel
            v["j_name"] = j_name
            # 应收金额
            y_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100 + money
            v["y_money"] = y_money
            # print(y_money)
            # 应收利息
            l_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100
            v["l_money"] = l_money
            # 状态
            zt = "已完成"
            v["zt"] = zt
            # 时间
            v["pay_time"] = pay_time
            x_hui.append(v)

    return JsonResponse({"x_hui": x_hui})


def zhuan_rang(request):
    id = request.session.get("loginFlag").get("id")
    p = models.project_invest.objects.filter(user_id=id)
    l_biao = []

    # 计算已流标的项目数量
    for i in p.values_list("project_id"):
        # print(i)
        # print(i[0])
        v = {"p_name": "", "j_name": "", "y_money": "", "l_money": "", "zt": "", "pay_time": ""}
        # 获取id为i[0]的项目
        t = models.Project_List.objects.filter(id=i[0]).values_list("status").first()

        # 项目的投资金额
        money = p.filter(project_id=i[0]).values_list("money").first()[0]
        # print(money)

        # 项目的收益时间
        pay_time = p.filter(project_id=i[0]).values_list("pay_time").first()[0]
        if not pay_time:
            pay_time = "暂无"
        else:
            pay_time = pay_time.strftime("%Y-%m-%d %H:%M:%S")
        # print(investtime)
        if t[0] == "已流标":
            # 项目名
            p_name = models.Project_List.objects.get(id=i[0]).project_name
            v["p_name"] = p_name
            # print(p_name)
            # 借款者
            j_name = models.Project_List.objects.get(id=i[0]).tel
            v["j_name"] = j_name
            # 应收金额
            y_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100 + money
            v["y_money"] = y_money
            # print(y_money)
            # 应收利息
            l_money = (models.Project_List.objects.get(id=i[0]).rate * money) / 100
            v["l_money"] = l_money
            # 状态
            zt = "转让中"
            v["zt"] = zt
            # 时间
            v["pay_time"] = pay_time
            l_biao.append(v)

    return JsonResponse({"l_biao": l_biao})


def password_management(request):  # 密码管理
    data = 123
    return render(request, "front/index.html", {"data": data})
    # return redirect(to="/")


@auth_session
def repayment_account(request):  # 账户还款
    # 1 查询当前登录用户的id
    # 2 获取当前登录的账号的id  /tel
    id = request.session.get("loginFlag").get("id")

    tel=request.session.get("loginFlag").get("tel")
    user=project_invest.objects.filter(user_id=id)
    print(id,tel)
    # 3 累计投资
    invest_money=0
    #投标中数目
    number=0
    #还款中数目
    back_money_number=0
    for a in user:
        invest_money=invest_money+int(a.money)

        # 4投标中(bi)
        project_list=Project_List.objects.get(id=a.project_id)
        if project_list.status=="筹资中":
            number=number+1

        # 5 还款中(笔)
        print(datetime.now(),a.pay_time)
        if a.pay_time>=datetime.now():
            back_money_number=back_money_number+1

    print(invest_money,number,back_money_number)

    #借款并且已经发布贷款金额的项目 总金额
                # 1、	申请中
            # 2、	已通过
            # 3、	已作废
            # 4、	已发布

    user_borr=Borrow.objects.filter(tel=tel,status=4)
    borrow_money = 0
    for a in user_borr:
        borrow_money = borrow_money + int(a.money)

    # 借款并且已通过 未发布贷款金额的 总金额
    user_borr = Borrow.objects.filter(tel=tel, status=2)
    borrow_money_nogive = 0
    for a in user_borr:
        borrow_money_nogive = borrow_money_nogive + int(a.money)
    print(borrow_money,borrow_money_nogive)
    #6 你本月要还款
    data=""
    if borrow_money:
        data='请输入还款金额'
    else:
        if borrow_money_nogive:
            data="用户暂无还款信息"


    return render(request,"front/wyhk.html",{ "tel":tel,"name":"abc", "id":id,"data":data,"invest_money":invest_money,"borrow_money":borrow_money,"number":number,"back_money_number":back_money_number})
    # return redirect(to="/")

def personal_reimbursement(request):  #个人还款

    money=int(request.GET.get("money"))  #用户输入的还款金额
    user_id=int(request.GET.get("id"))   #当前用户id
    bal=int(request.GET.get("blance"))  #用户应该还金额
    print(money,user_id,bal)


    #计算用户余额
    user_info = User_info.objects.filter(id=user_id).first()
    tel=user_info.tel
    balance = user_info.banlence-bal
    if float(bal)>0:
        if balance<0:
            kk = Money_record(
                user_id=user_id,
                money=0,
                from_src="余额不足，还款失败",
                change_time=datetime.now(),
            )
            # 通过模型将数据保存到数据库
            kk.save()
            #余额不足还款失败
            return JsonResponse({"msg": "余额不足，还款失败","money":bal})
        else:

            if float(money) >= float(bal):
                #查询用户余额
                ff=User_info.objects.filter(id=user_id).first().banlence
                gg=float(ff)-float(bal)
                # 3扣除用户余额

                dd=User_info.objects.filter(id=user_id)
                print(user_id, gg,dd)
                dd.update(banlence=gg)
                #4 更新借款表状态
                user_borr = Borrow.objects.filter(tel=tel, status=4)

                user_borr.update(status=5)



                # 2通过模型将数据保存到数据库
                kk = Money_record(
                    user_id=user_id,
                    money=bal,
                    from_src='还款',
                    change_time=datetime.now(),
                )

                kk.save()
                return JsonResponse({"msg": "已还款,多余的金额已返还","money":0})
            else:
                # 查询用户余额
                ff = User_info.objects.filter(id=user_id).first().banlence
                gg = float(ff) - float(bal)

                # 3扣除用户余额

                dd = User_info.objects.filter(id=user_id)
                print(user_id, gg, dd)
                dd.update(banlence=gg)
                # 3扣除用户余额

                # 4 更新借款表状态
                user_borr = Borrow.objects.filter(tel=tel, status=4)
                if  user_borr:
                    hh=float(user_borr.first().money)-float(money)
                    user_borr.update(money=hh)
                    user_borr.update(status=4)

                    # 2通过模型将数据保存到数据库
                    kk = Money_record(
                        user_id=user_id,
                        money=money,
                        from_src="部分还款",
                        change_time=datetime.now(),
                    )

                    kk.save()

                    return JsonResponse({"msg": "部分还款","money":hh})

    else:
        return JsonResponse({"msg": "本月无需还款","money":0})

