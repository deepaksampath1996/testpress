from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .serializer import Quiz_serializer
from django.contrib import messages
from .models import Quiz
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@login_required(login_url='login')
def start(request):
    return render(request, 'start.html')


# @login_required(login_url='login')
# def home(request):
#     questions = Quiz.objects.all()
#     # if request.method == 'POST':
#     #     option1 = request.POST['option1']
#     #     option2 = request.POST['option2']
#     #     option3 = request.POST['option3']
#     #     option4 = request.POST['option4']
        
#     #     if option1 == answer:
#     #         messages.info(request,'correct answer')
#     #         return redirect('home')
#     #     elif option2 == answer:
#     #         messages.info(request,'correct answer')
#     #         return redirect('home')
#     #     elif option3 == answer:
#     #         messages.info(request,'correct answer')
#     #         return redirect('home')
#     #     elif option4 == answer:
#     #         messages.info(request,'correct answer')
#     #         return redirect('home')
   
#     return render(request, 'home.html', {'questions': questions})



@login_required(login_url='login')
def result(request):
    return render(request,'result.html')   

@login_required(login_url='login')
def test(request):
    questions = Quiz.objects.all()
    return render(request,'test.html',{'questions': questions})



@unauthenticated_user
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('start')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')    
    else:
        return render(request,'login.html')



@unauthenticated_user
def register(request):
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        #email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if username == '':
                messages.info(request,"plz enter the username")
                return redirect('register')
            elif password1 == '':
                messages.info(request,"plz enter the password")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request,'email taken')
            #     return redirect('register')    
            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1)#email=email
                user.save();
                return redirect('login')
        else:
            print('password is not matching')
            messages.info(request,'password is not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
     

def logout(request):
    auth.logout(request)
    return redirect('/')    


class QuizApiView(APIView):
    serializer_class = Quiz_serializer
    def get(self,request):
        customer_data = Quiz.objects.all().values()
        return Response({"customer_data":customer_data})
    def post(self,request):
        print("request data is:",request.data)
        serializer_obj = Quiz_serializer(data=request.data)
        
        if serializer_obj.is_valid():
            Quiz.objects.create(question = serializer_obj.data.get("question"),
                                option1 = serializer_obj.data.get("option1"),
                                option2 = serializer_obj.data.get("option2"),                   
                                option3 = serializer_obj.data.get("option3"),
                                option4 = serializer_obj.data.get("option4"),
                                answer = serializer_obj.data.get("answer"),)
        quiz = Quiz.objects.all().filter(question=serializer_obj.data["question"]).values()
        return Response({'quiz':quiz})
