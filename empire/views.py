from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.utils.html import format_html
from django.contrib import messages 
from empire.models import *
from . models import *
from . forms import *
from userprofile.models import *
from userprofile.forms import *

# Create your views here.
def homepage(request):
    bloger = CompanyProfile.objects.get(pk=1)
    all = Content.objects.all()

    context = {
        'bloger':bloger,
        'all':all
    }
    return render(request,'index.html', context)

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response

def categories(request, id):
    blogcat = Content.objects.filter(category_id = id)

    context = {
        'blogcat':blogcat
    }

    return render(request, 'category.html', context)



def about(request):
    about = CompanyProfile.objects.get(pk=1)

    context = {
        'about':about
    }

    return render(request,'about.html', context)

def contact(request):
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,'Success! Your Message was Sent Successfully.')
            return redirect('homepage')
        else:
          messages.error(request, 'error')
          return redirect('Sorry there was an error sending your form.')

    context = {
        'contact': contact 
    }

    return render(request,'contact.html', context)


def signout(request):
  logout(request)
  messages.success(request,'You are now signed out')
  return redirect('homepage')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successful!!')
            return redirect('homepage')
        else:
            messages.info(request, 'Username/Password is incorrect')

    return render(request, 'register_login.html')



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        pix = request.POST['pix']
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newuser = Customer(user=user)
            newuser.username = user.username
            newuser.first_name = user.first_name
            newuser.last_name = user.last_name
            newuser.email = user.email
            newuser.phone = phone 
            newuser.address = address 
            newuser.pix = pix 
            newuser.save()
            messages.success(request, f'Congratulations {user.username} your registration is successful')
            return redirect('signin')
        else:
            messages.error(request, form.errors)

    return render(request, 'register_login.html')


def profile(request):
  userprof = Customer.objects.get(user__username = request.user.username)
 

  context = {
    'userprof':userprof
  }

  return render(request,'dashboard.html',context)

def profile(request):
  userprof = Customer.objects.get(user__username = request.user.username)
 

  context = {
    'userprof':userprof
  }

  return render(request,'dashboard.html',context)

def update(request):
  userprof = Customer.objects.get(user__username = request.user.username)
  form = ProfileForm(instance=request.user.customer)
  if request.method == 'POST':
      form = ProfileForm(request.POST, request.FILES, instance=request.user.customer)
      if form.is_valid():
          user = form.save()
          new = user.first_name.title()
          messages.success(request, f'Dear {new}, your profile has been updated successfully')
          return redirect('profile')
      else:
          new = user.first_name.title()
          messages.error(request, f'Dear {new}, your profile update generated the following errors: {form.errors}')
          return redirect('update')


  context = {
    'userprof':userprof
  }

  return render(request,'dashupdate.html',context)


def passupdate(request):
  userprof = Customer.objects.get(user__username = request.user.username)
  form = PasswordChangeForm(request.user)
  if request.method == 'POST':
      new = request.user.username.title()
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
          user = form.save()
          update_session_auth_hash(request, user)
          messages.success(request, f'Dear {new} your password change is successful!!!')
          return redirect('profile')
      else:
          messages.error(request, f'Dear {new} your password change is not successful, {form.errors}')
          return redirect('password_update')



  context = {
    'userprof':userprof,
    'form':form
  }

  return render(request,'passwordupdate.html',context)


def catdet(request, theslug):
  postdet = Content.objects.get(slug = theslug)
  comments = Comment.objects.order_by('-id').filter(post=postdet)
  form = CommentForm()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      thecom = form.save(commit=False)
      thecom.post = postdet
      thecom.commenter = request.user
      thecom.save()
      return redirect('catdet',theslug = postdet.slug)

  context = {
    'postdet':postdet,
    'comments':comments,
    'form':form,
  }
 

  return render(request,'detailpost.html',context)


@login_required(login_url='signin')
def post_like(request):
  user = request.user
  if request.method =='POST':
    post_id = request.POST.get('post_id')
    post_obj = Content.objects.get(id=post_id)

    if user in post_obj.liked.all():
      post_obj.liked.remove(user)
    else:
      post_obj.liked.add(user)
    like,created = Like.objects.get_or_create(user=user,post_id=post_id)

    if not created:
      if like.value == 'like':
        like.value = 'unlike'
      else:
        like.value = 'like'
      like.save()
  return redirect('homepage')

@login_required(login_url='signin')
def search(request):
  if request.method == 'POST':
    items = request.POST['search']
    searched = Q(Q(title__icontains=items)|Q(content__icontains=items))
    searched_item = Content.objects.filter(searched)

    context = {
      'items':items,
      'searched_item':searched_item,
    }

    return render(request,'search.html',context)
  else:
    return render(request,'search.html')
