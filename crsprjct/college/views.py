from django.shortcuts import render,HttpResponseRedirect,reverse
from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from .urls import *
from .models import *
from random import *
from .utils import sendmail

# Create your views here.

def index(request):
        if "c_email" in request.session:
            uid=User.objects.get(email=request.session['c_email'])
            cid=College.objects.get(user_id=uid)
            com_count=Company.objects.all().count()
            stu_count=Student.objects.all().count()
            vaca_count=Vacancy.objects.all().count()
            l_com=Company.objects.filter().order_by("-id")[:5]
            context={
                "uid":uid,
                "cid":cid,
                "com_count":com_count,
                "stu_count":stu_count,
                "vaca_count":vaca_count,
                "l_com":l_com,
            }
            print("===================================")
            return render(request,"index.html",{"context":context})
        
        elif "com_email" in request.session:
            uid=User.objects.get(email=request.session['com_email'])
            com_id=Company.objects.get(user_id=uid)
            l_stu=Student.objects.filter().order_by("-id")[:5]
            com_count=Company.objects.all().count()
            stu_count=Student.objects.all().count()
            vaca_count=Vacancy.objects.all().count()
            l_com=Company.objects.filter().order_by("-id")[:5]
            context={
                "uid":uid,
                "com_id":com_id,
                "com_count":com_count,
                "stu_count":stu_count,
                "vaca_count":vaca_count,
                "l_com":l_com,
                "l_stu":l_stu,
            }
            print("===================================>")
            return render(request,"index.html",{"context":context})
        
        elif "s_email" in request.session:
            uid=User.objects.get(email=request.session['s_email'])
            sid=Student.objects.get(user_id=uid)
            com_count=Company.objects.all().count()
            stu_count=Student.objects.all().count()
            vaca_count=Vacancy.objects.all().count()
            l_com=Company.objects.filter().order_by("-id")[:5]
            context={
                "uid":uid,
                "sid":sid,
                "com_count":com_count,
                "stu_count":stu_count,
                "vaca_count":vaca_count,
                "l_com":l_com,
            }
            print("===================================>>")
            return render(request,"index.html",{"context":context})

        else:
            return render(request,"login.html")
    
def login(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        com_count=Company.objects.all().count()
        stu_count=Student.objects.all().count()
        vaca_count=Vacancy.objects.all().count()
        l_com=Company.objects.filter().order_by("-id")[:5]
        context={
            "uid":uid,
            "cid":cid,
            "com_count":com_count,
            "stu_count":stu_count,
            "vaca_count":vaca_count,
            "l_com":l_com,
        }
        print("===================================")
        return render(request,"index.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        l_stu=Student.objects.filter().order_by("-id")[:5]
        com_count=Company.objects.all().count()
        stu_count=Student.objects.all().count()
        vaca_count=Vacancy.objects.all().count()
        l_com=Company.objects.filter().order_by("-id")[:5]
        context={
            "uid":uid,
            "com_id":com_id,
            "com_count":com_count,
            "stu_count":stu_count,
            "vaca_count":vaca_count,
            "l_com":l_com,
            "l_stu":l_stu,
        }
        print("===================================>")
        return render(request,"index.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        com_count=Company.objects.all().count()
        stu_count=Student.objects.all().count()
        vaca_count=Vacancy.objects.all().count()
        l_com=Company.objects.filter().order_by("-id")[:5]
        context={
            "uid":uid,
            "sid":sid,
            "com_count":com_count,
            "stu_count":stu_count,
            "vaca_count":vaca_count,
            "l_com":l_com,
        }
        print("===================================>>")
        return render(request,"index.html",{"context":context})

    else:
        return render(request,"login.html")

def login_check(request):
    email=request.POST['email']     
    password=request.POST['password']

    uid=User.objects.get(email=email)
    if uid.role=="College":
        uid=User.objects.get(email=email)
        cid=College.objects.get(user_id=uid)
        
        if uid.password==password:
            request.session['c_email']=uid.email
            request.session['fname']=cid.f_name
            context={
                "uid":uid,
            }
            if uid.status=="Pending":
                return render(request,"fc-password.html",{'context':context}) 
            elif uid.status=="Active":
                return HttpResponseRedirect(reverse("index"))
            else:
                e_msg="Invalid Email Or Password"
                return render(request,"login.html",{"e_msg":e_msg})
            
        else:
            e_msg="Invalid Email or Password"
            return render(request,"login.html",{"e_msg":e_msg})
        
    elif uid.role=="Company":
        uid=User.objects.get(email=email)
        com_id=Company.objects.get(user_id=uid)
        
        if uid.password==password:
            request.session['com_email']=uid.email
            request.session['fname']=com_id.hr_f_name
            context={
                "uid":uid,
            }
            if uid.status=="Pending":
                return render(request,"fc-password.html",{'context':context}) 
            elif uid.status=="Active":
                return HttpResponseRedirect(reverse("index"))
            else:
                e_msg="Invalid Email Or Password"
                return render(request,"login.html",{"e_msg":e_msg})
            
        else:
            e_msg="Invalid Email or Password"
            return render(request,"login.html",{"e_msg":e_msg})
        
    elif uid.role=="Student":
        uid=User.objects.get(email=email)
        sid=Student.objects.get(user_id=uid)
        
        if uid.password==password:
            request.session['s_email']=uid.email
            request.session['fname']=sid.f_name
            context={
                "uid":uid,
            }
            if uid.status=="Pending":
                return render(request,"fc-password.html",{'context':context}) 
            elif uid.status=="Active":
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request,"login.html",{"e_msg":e_msg})
            
        else:
            e_msg="Invalid Email Or Password"
            return render(request,"login.html",{"e_msg":e_msg})
        
def signout(request):
    if "c_email" in request.session:
        del request.session['c_email']
        return render(request,"login.html")
    
    elif "s_email" in request.session:
        del request.session['s_email']
        return render(request,"login.html")
    
    elif "com_email" in request.session:
        del request.session['com_email']
        return render(request,"login.html")
    
    else:
        return render(request,"login.html")

def college_signup(request):
    if request.POST:
        role="College"
        name=request.POST['name']
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        email=request.POST['email']
        contact=request.POST['contact']
        address=request.POST['address']
        
        password=str(randint(11,99))+f_name[:2]+l_name[-2:]+str(randint(11,99))
        user_obj=User.objects.create(role=role,email=email,password=password)
        coll_id=College.objects.create(user_id=user_obj,f_name=f_name,l_name=l_name,contact=contact,address=address,name=name)
        context={
            "user_obj":user_obj,
            "coll_id":coll_id,
        }
        
        sendmail("Login Details","reg_mail",email,{"user_obj":user_obj,"coll_id":coll_id})
        return render(request,"login.html",{"context":context})
    else:
        return render(request,"signup.html")

def company_signup(request):
    if request.POST:
        role="Company"
        email=request.POST['email']
        name=request.POST['name']
        owner=request.POST['owner']
        hr_f_name=request.POST['hr_f_name']
        hr_l_name=request.POST['hr_l_name']
        address=request.POST['address']
        contact=request.POST['contact']
        url=request.POST['url']

        password=str(randint(11,99))+hr_f_name[:2]+hr_l_name[-2:]+str(randint(11,99))
        user_object_id=User.objects.create(role=role,email=email,password=password)
        com_id=Company.objects.create(user_id=user_object_id,name=name,hr_f_name=hr_f_name,hr_l_name=hr_l_name,address=address,contact=contact,url=url,owner=owner)

        context={
            "user_object_id":user_object_id,
            "com_id":com_id,
        }
        sendmail("Login Details","reg_com_mail",email,{"user_object_id":user_object_id,"com_id":com_id})
        return render(request,"login.html",{"context":context})
    else:
        return render(request,"com_signup.html")

def all_company(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        c_id=Company.objects.all()
        context={
            "uid":uid,
            "cid":cid,
            "c_id":c_id,
        }
        return render(request,"all-company.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        c_id=Company.objects.all()
        context={
            "uid":uid,
            "com_id":com_id,
            "c_id":c_id,
        }
        return render(request,"all-company.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        c_id=Company.objects.all()
        context={
            "uid":uid,
            "sid":sid,
            "c_id":c_id,
        }
        return render(request,"all-company.html",{"context":context})
    else:
        return HttpResponseRedirect(reverse(signout))

def student_signup(request):
    if request.POST:
        role="Student"
        email=request.POST['email']
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        contact=request.POST['contact']
        enroll=request.POST['enroll']
        s_picture=request.FILES['s_picture']
        resume=request.FILES['resume']

        password=str(randint(11,99))+f_name[:2]+l_name[-2:]+str(randint(11,99))
        user_object_id=User.objects.create(role=role,email=email,password=password)
        stu_id=Student.objects.create(user_id=user_object_id,f_name=f_name,l_name=l_name,contact=contact,enroll=enroll,s_picture=s_picture,resume=resume)

        context={
            "user_object_id":user_object_id,
            "stu_id":stu_id,
        }
        sendmail("Login Details","reg_stu_mail",email,{"user_object_id":user_object_id,"stu_id":stu_id})
        return render(request,"login.html",{"context":context})
    
    else:
        return render(request,"stu_signup.html")

def add_vacancy_page(request):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        context={
            "uid":uid,
            "com_id":com_id,
        }
        return render(request,"add-vacancy.html",{"context":context})

    else:
        return render(request,"login.html")        

def add_vacancy(request):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        print("----------------------------------------->",uid.email)
        language = request.POST['language']
        vac_count = request.POST['vac_count']
        date = request.POST['date']

        Vacancy.objects.create(com_id=com_id,language=language,vac_count=vac_count,date=date)

        context={
            "uid":uid,
            "com_id":com_id,
        }
        return render(request,"all-vacancy.html",{"context":context})

    else:
        return render(request,"login.html")        

def all_vacancy(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        vid=Vacancy.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "cid":cid,
            "vid":vid,
        }
        return render(request,"all-vacancy.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        vid=Vacancy.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "vid":vid,
        }
        return render(request,"all-vacancy.html",{"context":context})
    
    if "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        vid=Vacancy.objects.all()
        aid=Apply.objects.get(s_id=sid)
        print("===================================>>",aid.status)
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "sid":sid,
            "vid":vid,
            "aid":aid,
        }
        return render(request,"all-vacancy.html",{"context":context})

    else:
        return render(request,"login.html")
    
def my_vac(request):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        mid=Vacancy.objects.filter(com_id=com_id)
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "mid":mid,
        }
        return render(request,"my-vacancy.html",{"context":context})

def forgot_password_page(request):
    return render(request,"forgot-password.html")

def send_OTP(request):
    email=request.POST['email']
    otp=randint(1111,9999)
    uid=User.objects.get(email=email)
    if uid:
        uid.otp=otp
        uid.save()  
        if uid.role=='College':
            cid=College.objects.get(user_id=uid)
            sendmail("Forgot Password","main",email,{'otp':otp})
            return render(request,"reset_password.html",{"email":email})
        elif uid.role=='Company':
            com_id=Company.objects.get(user_id=uid)
            sendmail("Forgot Password","main",email,{'otp':otp})
            return render(request,"reset_password.html",{"email":email})
        elif uid.role=="Student":
            sid=Student.objects.get(user_id=uid)
            sendmail("Forgot Password","main",email,{'otp':otp})
            return render(request,"reset_password.html",{"email":email})
    else:
        e_msg="Invalid Email"
        return render(request,"forgot_password.html",{"e_msg":e_msg})

def reset_password(request):
    email=request.POST['email']
    otp=request.POST['otp']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    uid=User.objects.get(email=email)
    if uid:
        if str(uid.otp)==otp:
            if new_password==confirm_password:
                uid.password=new_password
                uid.save()
                e_msg1="Successfully Reset Password"
                return render(request,"login.html",{"e_msg1":e_msg1})
            else:
                e_msg="Both Password Must be same"
                return render(request,"forgot-password.html",{"e_msg":e_msg})
        else:
            e_msg="Invalid OTP"
            return render(request,"forgot-password.html",{"e_msg":e_msg})
    else:
        e_msg="Invalid email"
        return render(request,"forgot-password.html",{"e_msg":e_msg})

def fc_password(request):
    email=request.POST['email']
    old_password=request.POST['old_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']

    uid=User.objects.get(email=email)

    if uid.role=="College":
        cid=College.objects.get(user_id=uid)
        if uid.status=="Pending" and uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            uid.status="Active"
            cid.save()
            uid.save()
            request.session['cid']=cid.id
            request.session['c_email']=uid.email
            return HttpResponseRedirect(reverse('index'))
        
    elif uid.role=="Company":
        com_id=Company.objects.get(user_id=uid)
        if uid.status=="Pending" and uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            uid.status="Active"
            com_id.save()
            uid.save()
            request.session['com_id']=com_id.id
            request.session['com_email']=uid.email
            return HttpResponseRedirect(reverse('index'))
        
    elif uid.role=="Student":
        sid=Student.objects.get(user_id=uid)
        if uid.status=="Pending" and uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            uid.status="Active"
            sid.save()
            uid.save()
            request.session['sid']=sid.id
            request.session['s_email']=uid.email
            return HttpResponseRedirect(reverse('index'))

    else:
        e_msg="Invalid Password"
        return render(request,"login.html",{'e_msg':e_msg})
    
def profile(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        context={
            "uid":uid,
            "cid":cid,
        }
        return render(request,"profile.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        context={
            "uid":uid,
            "com_id":com_id,
        }
        return render(request,"view-profile.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        context={
            "uid":uid,
            "sid":sid,
        }
        return render(request,"s-profile.html",{"context":context})

    else:
        return render(request,"login.html")   

def profile_update(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        name=request.POST['c_name']
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        contact=request.POST['contact']
        password=request.POST['password']
        address=request.POST['address']
        if "c_picture" in request.FILES:
            c_picture=request.FILES['c_picture']
            cid.c_picture=c_picture
            cid.save()
        
        uid.password=password
        cid.name=name
        cid.f_name=f_name
        cid.l_name=l_name
        cid.contact=contact
        cid.address=address
        uid.save()
        cid.save()

        context={
            "uid":uid,
            "cid":cid,
        }
        return HttpResponseRedirect(reverse("index"))
        
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        password=request.POST['password']
        name=request.POST['name']
        hr_f_name=request.POST['hr_f_name']
        hr_l_name=request.POST['hr_l_name']
        contact=request.POST['contact']
        address=request.FILES['address']
        url=request.FILES['url']
        if "picture" in request.FILES:
            picture=request.FILES['picture']
            com_id.picture=picture
            com_id.save()
        
        uid.password=password
        com_id.name=name
        com_id.hr_f_name=hr_f_name
        com_id.hr_l_name=hr_l_name
        com_id.contact=contact
        com_id.address=address
        com_id.url=url
        uid.save()
        com_id.save()

        context={
            "uid":uid,
            "com_id":com_id,
        }
        return HttpResponseRedirect(reverse("index"))

    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        password=request.POST['password']
        f_name=request.POST['f_name']
        l_name=request.POST['l_name']
        contact=request.POST['contact']
        enroll=request.POST['enroll']
        resume=request.FILES['resume']
        if "s_picture" in request.FILES:
            s_picture=request.FILES['s_picture']
            sid.s_picture=s_picture
            sid.save()
        
        uid.password=password
        sid.f_name=f_name
        sid.l_name=l_name
        sid.contact=contact
        sid.enroll=enroll
        sid.resume=resume
        uid.save()
        sid.save()

        context={
            "uid":uid,
            "sid":sid,
        }

        return HttpResponseRedirect(reverse("index"))
    
    else:
        return HttpResponseRedirect(reverse("login"))

def view_profile(request,pk):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        c_id=Company.objects.get(id=pk)

        context={
            "uid":uid,
            'cid':cid,
            'c_id':c_id,
        }
        return render(request,"view-profile.html",{"context":context})

    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        c_id=Company.objects.get(id=pk)

        context={
            "uid":uid,
            'c_id':c_id,
            'com_id':com_id,
        }
        return render(request,"view-profile.html",{"context":context})

    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=College.objects.get(user_id=uid)
        c_id=Student.objects.get(id=pk)

        context={
            "uid":uid,
            'cid':cid,
            'c_id':c_id,
        }
        return render(request,"view-profile.html",{"context":context})

def all_student(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        s_id=Student.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "cid":cid,
            "s_id":s_id,
        }
        
        return render(request,"all-student.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        s_id=Student.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "s_id":s_id,
        }
        
        return render(request,"all-student.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        s_id=Student.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "s_id":s_id,
            "sid":sid,
        }
        
        return render(request,"all-student.html",{"context":context})

    else:
        return render(request,"login.html")
    
def view_sprofile(request,pk):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        sid=Student.objects.get(id=pk)

        context={
            "uid":uid,
            'cid':cid,
            'sid':sid,
        }
    return render(request,"view-sprofile.html",{"context":context})

def privacy(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        context={
            "uid":uid,
            "cid":cid,
        }
        return render(request,"pc-password.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        context={
            "uid":uid,
            "com_id":com_id,
        }
        return render(request,"pc-password.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        context={
            "uid":uid,
            "sid":sid,
        }
        return render(request,"pc-password.html",{"context":context})

    else:
        return render(request,"login.html")
    
def update_privacy(request):
    email=request.POST['email']
    old_password=request.POST['old_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])

        cid=College.objects.get(user_id=uid)
        if uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            cid.save()
            uid.save()
            request.session['cid']=cid.id
            request.session['c_email']=uid.email
            return HttpResponseRedirect(reverse('signout'))
        else:
            e_msg="Invalid Password"
            return render(request,"pc-password.html",{'e_msg':e_msg})

    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        if uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            com_id.save()
            uid.save()
            request.session['com_id']=com_id.id
            request.session['com_email']=uid.email
            return HttpResponseRedirect(reverse('signout'))
        else:
            e_msg="Invalid Password"
            return render(request,"pc-password.html",{'e_msg':e_msg})
            
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        if uid.password==old_password and new_password==confirm_password:
            uid.password=new_password
            sid.save()
            uid.save()
            request.session['sid']=sid.id
            request.session['s_email']=uid.email
            return HttpResponseRedirect(reverse('signout'))
        else:
            e_msg="Invalid Password"
            return render(request,"pc-password.html",{'e_msg':e_msg})

    else:
        e_msg="Invalid Password"
        return render(request,"login.html",{'e_msg':e_msg})

def add_suggesion_page(request):
    if "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        context={
            "uid":uid,
            "sid":sid,
        }
        return render(request,"add-suggesion.html",{"context":context})

def add_suggesion(request):
    if "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        subject = request.POST['subject']
        messege = request.POST['messege']

        Suggetion.objects.create(s_id=sid,subject=subject,messege=messege)

        context={
            "uid":uid,
            "sid":sid,
        }
        return render(request,"all-suggesion.html",{"context":context})

def all_suggesion(request):
    if "c_email" in request.session:
        uid=User.objects.get(email=request.session['c_email'])
        cid=College.objects.get(user_id=uid)
        sugg_id=Suggetion.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "cid":cid,
            "sugg_id":sugg_id,
        }
        
        return render(request,"all-suggesion.html",{"context":context})
    
    elif "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        sugg_id=Suggetion.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "sugg_id":sugg_id,
        }
        
        return render(request,"all-suggesion.html",{"context":context})
    
    elif "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        sid=Student.objects.get(user_id=uid)
        sugg_id=Suggetion.objects.all()
        print("______________________________________++++",uid.email)
        context={
            "uid":uid,
            "sid":sid,
            "sugg_id":sugg_id,
        }
        
        return render(request,"all-suggesion.html",{"context":context})

    else:
        return render(request,"login.html")

def job_apply(request,pk):
    if "s_email" in request.session:
        uid=User.objects.get(email=request.session['s_email'])
        com_id=Company.objects.get(id=pk)
        sid=Student.objects.get(user_id=uid)
        status = "Applied"
        Apply.objects.create(com_id = com_id , s_id = sid , status = status)
        context={
            "uid":uid,
            "com_id":com_id,
            "sid":sid,
        }
        return HttpResponseRedirect(reverse("index"))

def applied_cand(request):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        aid=Apply.objects.filter(com_id=com_id)
        iid=Interview.objects.all()
        context={
            "uid":uid,
            "com_id":com_id,
            "aid":aid,
            "iid":iid,
        }
    return render(request,"candidate.html",{"context":context})

def view_resume(request,pk):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        aid=Apply.objects.filter(com_id=com_id)
        sid=Student.objects.get(id=pk)
        print("================================>",sid.f_name)
        context={
            "uid":uid,
            "com_id":com_id,
            "aid":aid,
            "sid":sid,
        }
    return render(request,"resume.html",{"context":context})

def int_approval(request,pk):
    if "com_email" in request.session:
        email = request.POST['email']
        date = request.POST['date']
        time = request.POST['time']
        status = "Approve"
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        aid=Apply.objects.get(id=pk)
        iid=Interview.objects.all()
        Interview.objects.create(a_id = aid , date = date , time = time , status = status)
        # sid=Student.objects.get(id=pk)
        print("================================>",aid.s_id.user_id.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "aid":aid,
            "iid":iid,
        }
    return HttpResponseRedirect(reverse("index"))

def approve(request):
    id = request.POST['id']
    email = request.POST['email']
    messege = request.POST['messege']
    date = request.POST['date']
    time = request.POST['time']
    status = "Approve"
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        # sid=Student.objects.get(user_id=id)
        aid=Apply.objects.get(s_id=id)
        
        
        print("===================>123",id)

        Interview.objects.create(a_id = aid.s_id.user_id.email , messege = messege , date = date , time = time , status = status)

        # sid=Student.objects.get(id=pk)
        # print("================================>",aid.s_id.user_id.email)
        context={
            "uid":uid,
            "com_id":com_id,
            "aid":aid,
            # "sid":sid,
        }
    return HttpResponseRedirect(reverse("index"))

def Schedules(request):
    if "com_email" in request.session:
        uid=User.objects.get(email=request.session['com_email'])
        com_id=Company.objects.get(user_id=uid)
        aid=Apply.objects.filter(com_id=com_id)
        iid=Interview.objects.filter(status="Approve")
        context={
            "uid":uid,
            "com_id":com_id,
            "aid":aid,
            "iid":iid,
        }
    return render(request,"schedules.html",{"context":context})

def emailajax(request):
    email=request.GET.get('email',None)
    data={
        'is_taken':User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)
