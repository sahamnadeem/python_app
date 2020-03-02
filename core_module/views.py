from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
import json
from .forms import RegFormAlpha, RegFormBeta, RegFormGama, RegFormOmga, LoginForm
from django.contrib.auth.models import User
from .models import UserDetails
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def index(request):
    login_url = '/login'
    return render(request, 'dashboard/dashboard.html')


# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             print(form.cleaned_data['email'])
#             print(form.cleaned_data['password'])
#             user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
#             # user = User.objects.get(email=form.cleaned_data['email'])
#             print(user)
#             if user is not None:
#                 # A backend authenticated the credentials
#                 return render(request, 'dashboard/dashboard.html', {'user': user})
#             else:
#                 # No backend authenticated the credentials
#                 return render(request, 'auth/login.html', {'error': 'Wrong credentials'})
#
#         else:
#             # in case of form failed
#             return render(request, 'auth/login.html', {'form': form})
#     else:
#         return render(request, 'auth/login.html')
#
#     return Http404


def register(request, slug=None):
    """
    Register the user
    :param request: HTTP object
    :param slug: is the optional params which return stage
    :return: view
    """

    if slug == 'beta':
        if request.method == 'POST':
            formB = RegFormBeta(request.POST)
            # check whether it's valid:
            if formB.is_valid():
                request.session['form_b_data'] = formB.cleaned_data
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return redirect('/register/gama')
            else:

                # in case of form failed
                return render(request, 'auth/signup-stage-beta.html', {'form': formB})

        # Restore form from cache
        if request.session.get('form_b_data'):
            formB = RegFormBeta(initial=request.session.get('form_b_data'))
            return render(request, 'auth/signup-stage-beta.html', {'form': formB})
        else:
            return render(request, 'auth/signup-stage-beta.html')

    if slug == 'gama':
        if request.method == 'POST':
            formG = RegFormGama(request.POST, request.FILES)
            # check whether it's valid:
            if formG.is_valid():
                # request.session['form_g_data'] = formG.cleaned_data
                # handle file upload
                in_file = request.FILES['avatar'].name
                request.session['form_g_data'] = in_file

                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return redirect('/register/omga')
            else:

                # in case of form failed
                return render(request, 'auth/signup-stage-gama.html', {'form': formG})

        # Restore form from cache
        if request.session.get('form_g_data'):
            #formG = RegFormGama(initial=request.session.get('form_g_data'))
            return render(request, 'auth/signup-stage-gama.html')
        else:
            return render(request, 'auth/signup-stage-gama.html')

    if slug == 'omga':
        print("omga")
        if request.method == 'POST':
            print("omga post")
            formO = RegFormOmga(request.POST, request.FILES)
            # check whether it's valid:
            if formO.is_valid():
                in_file = request.FILES['cover_photo'].name
                request.session['form_o_data'] = in_file
                # request.session['form_g_data'] = formG.cleaned_data
                # handle file upload
                # {'name': 'Asif Raza', 'gender': 'male', 'country': 'pakistan', 'email': 'doctor@doctor.com', 'password': '12345678'} {'web_url': 'asdf', 'about': 'asdf', 'skills': 'turntablist'}
                # request.session['form_a_data']['name']
                if User.objects.filter(email=request.session['form_a_data']['email']).exists():
                    request.session.flush()
                    return HttpResponse("User already exists")

                else:
                    user = User.objects.create_user(first_name=request.session['form_a_data']['name'],
                                                    email=request.session['form_a_data']['email'],
                                                    password=request.session['form_a_data']['password'],
                                                    username=request.session['form_a_data']['email'])
                    user_details = UserDetails.objects.create(user_id=user.id,
                                                              gender=request.session['form_a_data']['gender'],
                                                              country=request.session['form_a_data']['country'],
                                                              about=request.session['form_b_data']['about'],
                                                              web_url=request.session['form_b_data']['web_url'],
                                                              skills=request.session['form_b_data']['skills'],
                                                              avatar=request.session['form_g_data'],
                                                              cover_photo=request.session['form_o_data'])
                    user.save()
                    user_details.save()
                    request.session.flush()

                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return render(request, 'registration/login.html', {'message': "You have successfully registered!"})
            else:

                # in case of form failed
                return render(request, 'auth/signup-stage-omga.html', {'form': formO})

        # Restore form from cache
        if request.session.get('form_g_data'):
            # formO = RegFormOmga(initial=request.session.get('form_g_data'))
            return render(request, 'auth/signup-stage-omga.html')
        else:
            return render(request, 'auth/signup-stage-omga.html')

    else:

        # Alpha processing
        if request.method == 'POST':
            formA = RegFormAlpha(request.POST)
            # check whether it's valid:
            if formA.is_valid():
                request.session['form_a_data'] = formA.cleaned_data
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return redirect('/register/beta')
            else:

                # in case of form failed
                return render(request, 'auth/signup-stage-alpha.html', {'form': formA})

        # Restore form from cache
        if request.session.get('form_a_data'):
            formA = RegFormAlpha(initial=request.session.get('form_a_data'))
            return render(request, 'auth/signup-stage-alpha.html', {'form': formA})
        else:
            return render(request, 'auth/signup-stage-alpha.html')

    raise Http404

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


