from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

def home(request):
    return render(request, 'landingpages/index.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "All fields are required.")
            return redirect("signup")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("signup")

        if len(password) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("signup")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect("home")

    return render(request, "accounts/signup.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")

            next_url = request.GET.get("next")
            return redirect(next_url or "home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "accounts/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")


def varun1_view(request):
    return render(request, "accounts/varun1.html")

def varun2_view(request):
    return render(request, "accounts/varun2.html")

def varun3_view(request):
    return render(request, "accounts/varun3.html")

def varun4_view(request):
    return render(request, "accounts/varun4.html")

def varun5_view(request):
    return render(request, "accounts/varun5.html")

def varun6_view(request):
    return render(request, "accounts/varun6.html")

def varun7_view(request):
    return render(request, "accounts/varun7.html")

def varun8_view(request):
    return render(request, "accounts/varun8.html")

def varun9_view(request):
    return render(request, "accounts/varun9.html")

def varun10_view(request):
    return render(request, "accounts/varun10.html")

def varun11_view(request):
    return render(request, "accounts/varun11.html")

def varun12_view(request):
    return render(request, "accounts/varun12.html")

def varun13_view(request):
    return render(request, "accounts/varun13.html")

def varun14_view(request):
    return render(request, "accounts/varun14.html")

def varun15_view(request):
    return render(request, "accounts/varun15.html")

def varun16_view(request):
    return render(request, "accounts/varun16.html")

def varun17_view(request):
    return render(request, "accounts/varun17.html")

def varun18_view(request):
    return render(request, "accounts/varun18.html")

def varun19_view(request):
    return render(request, "accounts/varun19.html")

def varun20_view(request):
    return render(request, "accounts/varun20.html")

def varun21_view(request):
    return render(request, "accounts/varun21.html")

def varun22_view(request):
    return render(request, "accounts/varun22.html")

def varun23_view(request):
    return render(request, "accounts/varun23.html")

def varun24_view(request):
    return render(request, "accounts/varun24.html")

def varun25_view(request):
    return render(request, "accounts/varun25.html")

def varun26_view(request):
    return render(request, "accounts/varun26.html")

def varun27_view(request):
    return render(request, "accounts/varun27.html")

def varun28_view(request):
    return render(request, "accounts/varun28.html")

def varun29_view(request):
    return render(request, "accounts/varun29.html")

def varun30_view(request):
    return render(request, "accounts/varun30.html")



def dashboard(request):
    return render(request, "accounts/dashboard.html")

def add_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        bValue = request.POST.get("bValue", "")
        c=int(aValue)+int(bValue)
        print(c)
        return render(request, "accounts/add.html", {'aValue': aValue, 'bValue': bValue, 'c': c})
    return render(request, "accounts/add.html")

def sub_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        bValue = request.POST.get("bValue", "")
        c=int(aValue)-int(bValue)
        print(c)
        return render(request, "accounts/sub.html", {'aValue': aValue, 'bValue': bValue, 'c': c})
    return render(request, "accounts/sub.html")

def multiply_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        bValue = request.POST.get("bValue", "")
        c=int(aValue)*int(bValue)
        print(c)
        return render(request, "accounts/multiply.html", {'aValue': aValue, 'bValue': bValue, 'c': c})
    return render(request, "accounts/multiply.html")

def sqrt_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        c=int(aValue)**0.5
        print(c)
        return render(request, "accounts/sqrt.html", {'aValue': aValue, 'c': c})
    return render(request, "accounts/sqrt.html")

def division_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        bValue = request.POST.get("bValue", "")
        c=int(aValue)/int(bValue)
        print(c)
        return render(request, "accounts/division.html", {'aValue': aValue, 'bValue': bValue, 'c': c})
    return render(request, "accounts/division.html")

def power_view(request):
    if request.method == "POST":
        aValue = request.POST.get("aValue", "")
        bValue = request.POST.get("bValue", "")
        c=int(aValue)**int(bValue)
        print(c)
        return render(request, "accounts/power.html", {'aValue': aValue, 'bValue': bValue, 'c': c})
    return render(request, "accounts/power.html")
