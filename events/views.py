from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .models import Event,Volunteers,City,Submission
from .forms import EventForm, ApplaudersForm, SeatWarmersForm, SignupForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from .token import account_activation_token
from django.http import HttpResponse



# Create your views here.
def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "username or password doesn't exist")
    if request.user.is_authenticated:
        return redirect('home')
    context = {'page': page}
    return render(request, 'events/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now youu can login your account.')
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')
    


def registerPage(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activation link has been sent to your email id"
            message = render_to_string('events/acc_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete these registration')
    context = {'form': form}
    return render(request, 'events/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    events = Event.objects.filter(
            Q(name__icontains=q)|
            Q(city__name__icontains=q)|
            Q(description__icontains=q))
    city = City.objects.all()
    paginator = Paginator(events, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'events': events, 'city': city, 'page_obj':page_obj}
    return render(request, 'events/home.html', context)


def room(request, pk):
    events = Event.objects.get(id=pk)
    if request.method == 'POST':
        submission = Submission.objects.create(
            event = events
        )
        submission.save()
        participant = User.objects.get(username=request.user.username)
        submission.participants.add(participant)
        return redirect('home')
    context = {'events': events}
    return render(request, 'events/room.html', context)


def create_event(request):
    form = EventForm()
    context = {'form': form}
    return render(request, 'events/eventform.html', context)


def applauders(request):
    form = ApplaudersForm()
    if request.method == 'POST':
        form = ApplaudersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been successfully submitted')
            return redirect('home')
        else:
            messages.error(request, 'There was an error while submitting your request')
    context = {'form': form}
    return render(request, 'events/applaudersform.html', context)


def seatwarmers(request):
    form = SeatWarmersForm
    if request.method == 'POST':
        form = SeatWarmersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been successfully submitted')
            return redirect('home')
        else:
            messages.error(request, 'There was an error while submitting your request')
    context = {'form': form}
    return render(request, 'events/applaudersform.html', context)



def volunteers(request):    
    if request.method == 'POST' or request.method == 'FILE':
        volunteer = Volunteers.objects.create(
            firstname = 'firstname',
            lastname = 'lastname',
            age = 'age',
            height = 'height',
            picture = 'picture'
        )
        volunteer.save()
        return redirect('home')
    context = {}
    return render(request, 'events/volunteersform.html', context)
