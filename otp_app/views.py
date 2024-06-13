from django.shortcuts import render , redirect ,HttpResponse
from django.contrib import messages
from .forms import RegisterForm ,ProfileUpdate
from django.contrib.auth import get_user_model
from .models import OtpToken

from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate , login , logout 
from .forms import ChangePasswordForm

from .models import Product , Order , Category
import datetime
from django.db.models import Q

# Password = Water1234



def search(request):
    if request.method == "POST":
        search = request.POST['searched']
        print(f"i got {search}")
        search = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search)  )

        if not search:
            messages.success(request, ('Yur Product not in List..'))
            return redirect('search')
        
        else:
             print("Yur Product  in List..")
             messages.success(request, ('Yur Product  in List..'))
             return render(request , "search.html" ,{'search':search})
    
    else:
        return render(request , "search.html",{})


def purchasedx(request):
    print(f"request.user.id==={request.user.id}")
    if request.user.is_authenticated:
        print("----------------------")
        print(f"under if statment........")
        orders = Order.objects.filter(customer = request.user)
        print(f"orders==={orders}")
    else:
        print(f"under else statment........")
        orders = None
        print(f"orders==={orders}")
        return HttpResponse("You are not authenticated....")
    

    return render(request , 'purchased.html',{'orders':orders})


def category(request,name):
    print("-----------------------")
    print(f"name ====== {name}")

    category = Category.objects.get(name=name)
    if category:
        print("---------------------")
        print(f"category matched == {category}")

    else:
        print("---------------------")
        print(f"category not matched ")

    products = Product.objects.filter(category=category)
    print(f"products ====== {products}")

    

    return render(request, 'category.html' ,{'products':products ,'name':name})

def product(request,id):
    obj = Product.objects.get(id=id)
    print(f"obj==={obj}")
    print(f"obj.id==={obj.id}")


    orders = Order.objects.filter(product=obj, customer=request.user)
    # if orders:
    #     return HttpResponse(" this product is purchased ")
    # else:
    #     print("this product is not purchased.......")


    if request.method == 'POST':
        product_id = request.POST['product_id']
        print(f"product_id==={product_id}")
        print(f" request.user==={ request.user}")
        print(f"datetime.datetime.today()==={datetime.datetime.today()}")

        product_ids = Product.objects.get(id=product_id)
        print(f"product_ids==={ product_ids }")


        orders = Order.objects.create(product=product_ids,customer=request.user,date=datetime.datetime.today(),stats=True)
        orders.save()

        print("-----order placed succesfully...........")



        return render(request , 'product.html',{'product': obj})

    return render(request , 'product.html',{'product': obj,"orders":orders})










def purchased(request):
    pass


def forget_pass(request):
    if request.method == 'POST':
        email = request.POST.get('otp_email')
        print(f"email======{email}")

        email_verify = get_user_model().objects.filter(email=email)
        print(f"email_verify======{email_verify}")

        

        if email_verify:
            print("email in the database")

            email_user = email_verify.first()
            print(f"email_user====={email_user}")

            # print(f"email_verify.username======{email_verify.username}")

            print(f"email_user.firstname======{email_user.first_name}")
            print(f"email_user.email======{email_user.email}")
            print(f"email_user.username======{email_user.username}")

            current_user = email_user
            print(f"current_user======{current_user}")

            
            forms = ChangePasswordForm(current_user)

            if request.method == 'POST':
               forms = ChangePasswordForm(current_user, request.POST)
               if forms.is_valid():
                 forms.save()
                 messages.success(request, 'Password updated succesfully.....')
                 login(request,current_user)

                 return redirect('home')
           
            
            return render(request, 'forget_pass.html', {"forms":forms})



        return render(request , 'forget_pass.html',{})

        
    return render(request , 'forget_pass.html')


def logout_user(request):
    logout(request)
    # messages.success(request , 'you sucessfully logged out')
    messages.success(request, 'You are succesfully logout.......')

    return redirect('home')


def profile_update(request):
    if request.user.is_authenticated:
        user = get_user_model().objects.get(id=request.user.id)
        print(f"user==={user}")
        forms = ProfileUpdate(request.POST or None, instance=user)

        if forms.is_valid():
           forms.save()
           print("Profile updated....")
           login(request, user)
           messages.success(request, 'profile updated succesfully.....')
           return redirect('home')

        
     
        return render(request, 'profile.html',{'forms':forms})
        
    else:
        return HttpResponse("you are not authenticated....")
    

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        print(f"current_user ====== {current_user}")
        print(f"request.first_name ======={request.user.first_name}")
        print(f"request.last_name ======{request.user.last_name}")
        print(f"request.username ======{request.user.username}")


        forms = ChangePasswordForm(current_user)

        if request.method == 'POST':
            forms = ChangePasswordForm(current_user, request.POST)
            if forms.is_valid():
             forms.save()
             messages.success(request, 'Password updated succesfully.....')
             login(request,current_user)

             return redirect('home')
            
            else:
              print("-------------------------")
              print("form is not valid")
              return render(request, 'uppassword.html', {"forms":forms})
           
            
        else:
            return render(request, 'uppassword.html', {"forms":forms})




def home(request):
    obj = Product.objects.all()
    print(f"obj==={obj}")
    return render(request , 'index.html',{'products': obj})


def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request , ("Accout created succefully,, An OTP was sent to your Email"))
            return redirect("verify-email",username=request.POST['username'])
        
    context = {"form":form}
    return render(request, "register_page.html",context)



def verify_email(request, username):
    user  = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()

    if request.method == 'POST':

        if user_otp.otp_code == request.POST['otp_code']:
            print("------------------------------")
            print(f"user_otp.otp_expires_at === {user_otp.otp_expires_at}")
            print(f"timezone.now() === {timezone.now()}")


            if user_otp.otp_expires_at > timezone.now():
                user.is_active = True
                user.save()

                messages.success(request , ("Acciut activated successfully..."))
                print("------------------------------")

                login(request,user)
                print("you succesfully logged in..........")

                return redirect("home")
            
            else:
                messages.warning(request , ("The Otp has Expired..."))
                return redirect("verify-email",username=user.username)
            
        else:
            messages.warning(request,("Invalid Otp entered,  enater valid otp"))
            return redirect("verify-email",username=user.username)
        
    context = {}
    return render(request , "verify_token.html",context)




def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST['otp_email']


        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp  = OtpToken.objects.create(user=user ,otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))

            
            subject = "Email Verification"

            message = f""" 

          Hii {user.username},, here is your OTP {otp.otp_code}  and
          it expire in 5 mintunes
          http://127.0.0.1:8000/verify-email/{user.username}
                       

                           """
            sender = "sstcdurg@gmail.com"
            receiver = [user.email,]

        
            send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False
               )

            messages.success(request, ("A new otp sent to your email"))
            return redirect("verify-email",username=user.username)
    
        else:
            messages.warning(request, ("this email not have in database..."))
            return redirect("resend-otp")
        
    context = {}

    return render(request,"resend_otp.html",context)




# i know both same but this not work at all
# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         print("--------------------------")
#         print(f"username : {username}")
#         print(f"password : {password}")

#         user = authenticate(request, username=username, pasword=password)

#         if user is not None:
#             login(request,user)
#             messages.success(request,f"hii {request.user.username} , you are loggin in succesfully....")
#             return redirect('index')
        
#         else:
#             messages.warning(request, (" Invalid Lofin Failed ,,User is None :"))
#             return redirect("signin")
        
#     return render(request,"login.html")




def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("--------------------------")
        print(f"username : {username}")
        print(f"password : {password}")
      
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            messages.success(request, f"Hi {request.user.username}, you are now logged-in")
            return redirect("home")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("signin")
        
    return render(request, "login.html")
    

        
    

    


