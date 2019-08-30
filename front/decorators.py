from django.shortcuts import render,redirect

def auth_session(func):

    def check_session(request, *args, **kwargs):

        #1、获取session,判断session是否有标识符

        dicts = request.session.get('loginFlag')
        if not dicts:
            return redirect(to='/front')

        #重置session的存活时间

        request.session.set_expiry(0)
        request.session.clear_expired()

        #如果已经登录、则传对应的处理方法

        return func(request, *args, **kwargs)
    return check_session