from django.shortcuts import render
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

from .models import *
import xlrd


# Create your views here.
def home(request):
    return render(request, 'index.html')


def signupdef(request):
    return render(request, 'signup.html')


def userlogindef(request):
    return render(request, 'user.html')


def userloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['mail']
        pwd = request.POST['pwd']
        d = onlineuser.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()

        if d > 0:
            d = onlineuser.objects.filter(email__exact=uid)
            name = ""
            for d1 in d:
                name = d1.name

            request.session['email'] = uid
            request.session['name'] = name
            return render(request, 'user_home.html', {'dat a': d[0]})

        else:
            return render(request, 'user.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')


def usignupactiondef(request):
    email = request.POST['email']
    ph = request.POST['ph']
    pwd = request.POST['pwd']
    name = request.POST['name']
    gen = request.POST['gen']

    d = onlineuser.objects.filter(email__exact=email).count()
    if d > 0:
        return render(request, 'signup.html', {'msg': "Email Already Registered"})

    else:
        d = onlineuser(name=name, email=email, pwd=pwd, gender=gen, phone=ph)
        d.save()
        return render(request, 'signup.html', {'msg': "Registration Success, You can Login.."})


def userhomedef(request):
    if "email" in request.session:
        uid = request.session["email"]
        d = onlineuser.objects.filter(email__exact=uid)
        return render(request, 'user_home.html', {'data': d[0]})

    else:
        return render(request, 'user.html')


def userlogoutdef(request):
    try:
        del request.session['email']
    except:
        pass
    return render(request, 'user.html')


def adminlogin(request):
    return render(request, 'admin.html')


def adminloginaction(request):
    userid = request.POST['aid']
    pwd = request.POST['pwd']
    print(userid, pwd, '< <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if userid == 'admin' and pwd == "admin":
        request.session['adminid'] = 'admin'
        return render(request, 'adminhome.html')
    else:
        err = ' Your Login Data is wrong !!'
        return render(request, 'admin.html', {' msg': err})


def adminhome(request):
    return render(request, 'adminhome.html')


def adminlogout(request):
    return render(request, 'admin.html')


def datasetpage(request):
    return render(request, 'datasetpage.html')


def classification(request):
    return render(request, 'classification.html')


def nbtrain(request):
    
    from .Training import Training
    sc = Training.train(1)

    performance.objects.filter(alg_name='Naive Bayes').delete()
    
    d = performance(alg_name='Naive Bayes', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Naive Bayes Algorithm's training completed"})


def dttrain(request):
    from .Training import Training
    sc = Training.train(4)

    performance.objects.filter(alg_name='Decision Tree').delete()
    
    d = performance(alg_name='Decision Tree', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()
    
    return render(request, 'classification.html', {'msg': "Decision Tree Algorithm's training completed"})


def svmtrain(request):
    from .Training import Training
    sc = Training.train(3)
    performance.objects.filter(alg_name='SVM').delete()
  
    d = performance(alg_name='SVM', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "SVM Algorithm's training completed"})


def nntrain(request):
    from .Training import Training
    sc = Training.train(2)
    performance.objects.filter(alg_name='Neural Networks').delete()
    d = performance(alg_name='Neural Networks', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])
    d.save()

    return render(request, 'classification.html', {'msg': "Neural Networks Algorithm's training completed"})


def rftrain(request):
    from .Training import Training
    sc = Training.train(5)
    performance.objects.filter(alg_name='Random Forest').delete()
    d = performance(alg_name='Random Forest', sc1=sc[0], sc2=sc[1], sc3=sc[2], sc4=sc[3])

    d.save()

    return render(request, 'classification.html', {'msg': "Random Forest Algorithm's training completed"})


def evaluation(request):
    d = performance.objects.all()
    val = dict({})
    for d1 in d:
        val[d1.alg_name] = d1.sc1
    from .Graphs import viewg
    viewg(val)
    return render(request, 'viewacc.html', {'data': d})




def uploaddataset(request):
    if "adminid" in request.session:

        return render(request, 'uploaddataset.html')

    else:
        return render(request, 'adminlogin.html')

def uploadaction(request):
    if "adminid" in request.session:
        file = 'AvgCalories.csv'
        file2 = 'Food and Calories - Sheet1.csv'
        import csv
        d = cal_dataset.objects.all().delete()
        with open(file, 'r') as fin:
            dr = csv.DictReader(fin)  
            to_db = [(i['avg(cal)'], i['label']) for i in dr]
            for l in to_db:
                d = cal_dataset(cal=float(l[0]), label=l[1])
                d.save()
        d = food_cal_dataset.objects.all().delete()
        with open(file2, 'r') as fin:
            dr = csv.DictReader(fin)  
            to_db = [(i['Food'], i['Serving'], i['Calories (cal)']) for i in dr]
            for l in to_db:
                d = food_cal_dataset(food=l[0], serve=l[1], cal=float(l[2]))
                d.save()
        return render(request, 'uploaddataset.html', {'msg': "Dataset Uploaded Successfully"})
    else:
        return render(request, 'adminlogin.html')




def chatstore(user, msg):
    d = chat(name=user, email=user, message=msg)
    d.save()



def chatpage(request):
   
    chat.objects.all().delete()          
    d=chat.objects.filter().all()
    uname=request.session["name"]

    chatstore('chatbot', 'chatbot', "Hello "+str(uname)+", ")
    chatstore('chatbot', 'chatbot', "Please Choose a service..  ")

    return render(request, 'chatpage.html',{'data': d, 'staz':'main'})


def dietprediction(request):
    if request.method == 'POST':
        age = float(request.POST['age'])
        w = float(request.POST['w'])
        h = float(request.POST['h'])
        gen = float(request.POST['gen'])
        bmi = float(request.POST['bmi'])
        bmr = float(request.POST['bmr'])
        h=h/100
        from .Prediction import predict
        l=[age,w,h,gen, bmi, bmr]
        print(l)

        res=predict(l)
        d=cal_dataset.objects.filter(label=int(res))
        cal=0
        for d1 in d:
            cal=d1.cal
        
        bca1=cal*0.25
        lca1=cal*0.40
        dca1=cal*0.35
        print(bca1, lca1, dca1)

        bf=[]
        lunch=[]
        dinner=[]
        t=30
        print(lca1-t, lca1+5)

        d=food_cal_dataset.objects.filter(cal__gte=bca1-t, cal__lte=bca1+t)[:5]
        for d1 in d:
            bf.append(d1.food)
        
        d=food_cal_dataset.objects.filter(cal__gte=lca1-t, cal__lte=lca1+t)[:5]
        for d1 in d:
            lunch.append(d1.food)
        
        d=food_cal_dataset.objects.filter(cal__gte=dca1-t, cal__lte=dca1+t)[:5]
        for d1 in d:
            dinner.append(d1.food)
        
        

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'stz':'list', 'staz':'main', 'bf': bf,'lunch': lunch,'dinner':dinner, 'data': d})

               
               
        
    else:
        chatstore('chatbot', 'chatbot', "Diet Plan Prediction")
        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'stz': 'diet','staz': 'main','data': d,})


def getcal(request):
    if request.method == 'POST':
        
        name=request.POST['name']
        chatstore('chatbot', 'chatbot', 'You entered "'+str(name)+'" ')

        d=food_cal_dataset.objects.filter(food__icontains=name)        
        res='Not Available'
        for d1 in d:
            res='Calories of the '+str(name)+' is "'+str(d1.cal)+' (cal)" for '+str(d1.serve)
        chatstore('chatbot', 'chatbot', res)

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'staz': 'main','data': d,})

        
    else:
        chatstore('chatbot', 'chatbot', "Get Calorie of a food")
        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'staz': 'main','stz': 'cal','data': d,})




def checkbmi(request):
    if request.method == 'POST':
        
        w = float(request.POST['w'])
        h = float(request.POST['h'])
        from .CalcBMI import bmi
        res=bmi(w,h)
        res='Your BMI is '+str(res)

        chatstore('chatbot', 'chatbot', res)

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'staz': 'main','data': d,})

        
    else:
        chatstore('chatbot', 'chatbot', "Caluculate BMI")
        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'stz': 'bmi', 'staz': 'main','data': d,})

from .CalcBMR import bmr
def checkbmr(request):
    if request.method == 'POST':
        
        gen = request.POST['gen']
        age = float(request.POST['age'])
        w = float(request.POST['w'])
        h = float(request.POST['h'])
        
        res=bmr(gen, age, w,h)
        res='Your BMR is '+str(res)

        chatstore('chatbot', 'chatbot', res)

        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'staz': 'main','data': d,})

        
    else:
        chatstore('chatbot', 'chatbot', "Caluculate BMR")
        d=chat.objects.filter().all()
        return render(request, 'chatpage.html',{'stz': 'bmr', 'staz': 'main','data': d,})


def chatstore(user,email, msg):
    d=chat(name=user,email=email,message=msg)
    d.save()
    
    