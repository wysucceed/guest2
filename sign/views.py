from sign.models import Event,Guest
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#Create your views here.
def index(request):
    #return HttpResponse("Hello Django")
    return render(request,"index.html")
#登陆动作
    return render(request,"index.html")

def login_action(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)#登录
        #if username=='admin'and password=='admin123':
            
            #return HttpResponse('login success')
            #这里如果"return render(request,"event_manage.html"),那么不用ulrs->views->html路线了，那么注释掉相关代码即可！"
            #return render(request,"event_manage.html")
            #下列
            request.session['user'] = username#将session记录到浏览器
            response= HttpResponseRedirect('/event_manage/')
            #response.set_cookie('user',username,3600)#记录cookie到浏览器
            return response

            
        else:
            return render(request,'index.html',{'error':'username or password error!'})
#发布会管理
@login_required
def event_manage(request):
    #username=request.COOKIES.get('user','')#读取浏览器cookie
    event_list = Event.objects.all()
    username=request.session.get('user','')#读取浏览器session
    return render(request,"event_manage.html",{"user":username,"events":event_list})

#发布会名称搜索
@login_required()
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,"events":event_list})
#嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器session
    guest_list = Guest.objects.all()
    paginator=Paginator(guest_list,2)
    page=request.GET.get('page')
    try:
        contacts=paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页面数据
        contacts=paginator.page(1)
    except EmptyPage:
        #如果page不在范围，取最后一个页面
        contacts=paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,"guests":contacts})
#嘉宾电话搜索
@login_required()
def search_phone(request):
    username = request.session.get('user','')
    search_phone = request.GET.get("phone","")
    guest_list = Guest.objects.filter(phone__icontains=search_phone)
    return render(request,"guest_manage.html",{"user":username,"guests":guest_list})
# 签到页面
@login_required
def sign_index(request,eid):
    username = request.session.get('user', '')  # 增加用户身份信息
    event=get_object_or_404(Event,id=eid)
    return render(request,'sign_index.html',{'user': username,'event':event})   # 增加用户身份信息

# 签到动作
@login_required
def sign_index_action(request,eid):
    username=request.session.get('user', '')  # 增加用户身份信息
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    print(result)
    if not result:
        return render(request, 'sign_index.html', {'user': username,'event': event, 'hint': 'phone error.'})  # 增加用户身份信息
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'user': username,'event': event, 'hint': 'event id or phone error.'})   # 增加用户身份信息
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'user': username,'event': event, 'hint': 'user has sign in.'})  # 增加用户身份信息
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'user': username,'event': event, 'hint': 'sign in success!.', 'guest': result})   # 增加用户身份信息

# 退出动作
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response