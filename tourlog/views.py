from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import *
from .models import Datas
from .models import Detail
# import uuid
# import time
# from .utils import generate_unique_reference_id

#LOGIN FORM
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        emp_id = request.POST.get('EMP_ID')  

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if emp_id exists in the database
            if Datas.objects.filter(EmpCode=emp_id).exists():
                login(request, user)
                # Redirect to one file if emp_id exists
                return render(request,"app/viewreg.html",{'EmpCode':emp_id})
            else:
                # Redirect to another file if emp_id doesn't exist
                return render(request,"app/reg.html")
        else:
            messages.error(request, 'Username or Password is incorrect')

    return render(request, "app/loginn.html")

#logout
def logoutUser(request):
    logout(request)
    return redirect('home')

#Signup
def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created')
            return redirect('home')

    context = {'form': form}
    return render(request, "app/signup.html", context)


#Update
def updateData(request,EmpCode):
    myd=Datas.objects.get(EmpCode=EmpCode)
    return render(request,'app/update.html',{'data':myd})

#Finalview
def final(request,EmpCode):
    myd=Datas.objects.get(EmpCode=EmpCode)
    return render(request,'app/finalreg.html',{'data':myd})

from .models import Datas  
#Reg
def reg(request):
    latest_entry = None  # Initialize latest_entry as None
    
    if request.method == 'POST':
        code = request.POST.get('code')
        name = request.POST.get('name')
        salutation = request.POST.get('salutation')
        des = request.POST.get('des')
        pay = request.POST.get('pay')
        age = request.POST.get('age')
        ename = request.POST.get('ename')
        ph = request.POST.get('ph')
        mob = request.POST.get('mob')
        addr = request.POST.get('addr')
        pt = request.POST.get('pt')
        exp = 'exp' in request.POST  # Will be True if 'exp' is present
        pexp = 'pexp' in request.POST
        pn = request.POST.get('pn')
        no = 'no' in request.POST  # Will be True if 'no' is present
        yes = 'yes' in request.POST
        rs = request.POST.get('rs')
        travel_date1_str = request.POST.get('travel_date1')
        from_place1 = request.POST.get('from_place1')
        to_place1 = request.POST.get('to_place1')
        mode_of_travel1 = request.POST.get('mode_of_travel1')
        flight_number1 = request.POST.get('flight_number1')
        departure_date1_str = request.POST.get('departure_date1')
        departure_time1_str = request.POST.get('departure_time1')
        arrival_date1_str = request.POST.get('arrival_date1')
        arrival_time1_str = request.POST.get('arrival_time1')
        travel_date2_str = request.POST.get('travel_date2')
        from_place2 = request.POST.get('from_place2')
        to_place2 = request.POST.get('to_place2')
        mode_of_travel2 = request.POST.get('mode_of_travel2')
        flight_number2 = request.POST.get('flight_number2')
        departure_date2_str = request.POST.get('departure_date2')
        departure_time2_str = request.POST.get('departure_time2')
        arrival_date2_str = request.POST.get('arrival_date2')
        arrival_time2_str = request.POST.get('arrival_time2')
        travel_date3_str = request.POST.get('travel_date3')
        from_place3 = request.POST.get('from_place3')
        to_place3 = request.POST.get('to_place3')
        mode_of_travel3 = request.POST.get('mode_of_travel3')
        flight_number3 = request.POST.get('flight_number3')
        departure_date3_str = request.POST.get('departure_date3')
        departure_time3_str = request.POST.get('departure_time3')
        arrival_date3_str = request.POST.get('arrival_date3')
        arrival_time3_str = request.POST.get('arrival_time3')
        travel_date4_str = request.POST.get('travel_date4')
        from_place4 = request.POST.get('from_place4')
        to_place4 = request.POST.get('to_place4')
        mode_of_travel4 = request.POST.get('mode_of_travel4')
        flight_number4 = request.POST.get('flight_number4')
        departure_date4_str = request.POST.get('departure_date4')
        departure_time4_str = request.POST.get('departure_time4')
        arrival_date4_str = request.POST.get('arrival_date4')
        arrival_time4_str = request.POST.get('arrival_time4')
        travel_date5_str = request.POST.get('travel_date5')
        from_place5 = request.POST.get('from_place5')
        to_place5 = request.POST.get('to_place5')
        mode_of_travel5 = request.POST.get('mode_of_travel5')
        flight_number5 = request.POST.get('flight_number5')
        departure_date5_str = request.POST.get('departure_date5')
        departure_time5_str = request.POST.get('departure_time5')
        arrival_date5_str = request.POST.get('arrival_date5')
        arrival_time5_str = request.POST.get('arrival_time5')

        # Check if 'rs' is provided and not empty
        if rs:
            rs_value = rs  
        else:
            rs_value = None  

        # Create a new Datas object
        obj = Datas(
            EmpCode=code,
            Name=name,
            salutation=salutation,
            Desg=des,
            Grade_Pay=pay,
            Age=age,
            Email_ID=ename,
            Phone=ph,
            Mobile=mob,
            Office_Address=addr,
            Purpose_of_Tour=pt,
            NICSI_Expenditure=exp,
            Project_Expenditure=pexp,
            Project_No=pn,
            no=no,
            yes=yes,
            Rs=rs_value,  # Use the determined rs_value
            travel_date1=travel_date1_str,
            from_place1=from_place1,
            to_place1=to_place1,
            mode_of_travel1=mode_of_travel1,
            flight_number1=flight_number1,
            departure_date1=departure_date1_str,
            departure_time1=departure_time1_str,
            arrival_date1=arrival_date1_str,
            arrival_time1=arrival_time1_str,
            travel_date2=travel_date2_str,
            from_place2=from_place2,
            to_place2=to_place2,
            mode_of_travel2=mode_of_travel2,
            flight_number2=flight_number2,
            departure_date2=departure_date2_str,
            departure_time2=departure_time2_str,
            arrival_date2=arrival_date2_str,
            arrival_time2=arrival_time2_str,
            travel_date3=travel_date3_str,
            from_place3=from_place3,
            to_place3=to_place3,
            mode_of_travel3=mode_of_travel3,
            flight_number3=flight_number3,
            departure_date3=departure_date3_str,
            departure_time3=departure_time3_str,
            arrival_date3=arrival_date3_str,
            arrival_time3=arrival_time3_str,
            travel_date4=travel_date4_str,
            from_place4=from_place4,
            to_place4=to_place4,
            mode_of_travel4=mode_of_travel4,
            flight_number4=flight_number4,
            departure_date4=departure_date4_str,
            departure_time4=departure_time4_str,
            arrival_date4=arrival_date4_str,
            arrival_time4=arrival_time4_str,
            travel_date5=travel_date5_str,
            from_place5=from_place5,
            to_place5=to_place5,
            mode_of_travel5=mode_of_travel5,
            flight_number5=flight_number5,
            departure_date5=departure_date5_str,
            departure_time5=departure_time5_str,
            arrival_date5=arrival_date5_str,
            arrival_time5=arrival_time5_str,
        )

        # Save the object to the database
        obj.save()

        # Set latest_entry to the newly created object
        latest_entry = obj

    return render(request, "app/reg.html", {'latest_entry':latest_entry})



def finalreg(request):
    return render(request,"app/finalreg.html")


def first(request):
    return render(request,"app/first.html")

# def refid():
#     # Generate a unique reference ID using UUID
#     return str(uuid.uuid4().hex[:12])


def det(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        Name = request.POST.get('Name')
        Emp = request.POST.get('Emp')
        obj = Detail(
            Name=Name,
            Emp=Emp,
        )

        obj.save()
    return render(request,"app/detail.html")