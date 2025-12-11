from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.http import JsonResponse
from django.contrib import messages
import ast
from django.contrib.auth.decorators import login_required


def safe_list(value):
    if isinstance(value, list):
        return value
    try:
        return ast.literal_eval(value)
    except:
        return []
    
# Create your views here.
def index(request):

    # Check if AJAX request
    # if request.headers.get('x-requested-with') == 'XMLHttpRequest':
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.GET.get('ajax') == '1':
        profile = Profile.objects.last()
        dctProject = Projects.objects.all()
        if profile:
            data = {
                'name': profile.name,
                'professions': profile.professions,
                'email': profile.email,
                'education': profile.education,
                'experience': profile.experience,
                'location': profile.location,
                'github' : profile.github,
                'linkedin' : profile.linkedin,
                'x' : profile.x,
                'stackoverflow':profile.stackoverflow
            }
            dctProjectData = {}
            for eachData in dctProject:
                dctProjectData[eachData.name] = {
                    'description': eachData.description,
                    'tech': safe_list(eachData.tech),
                    'features': safe_list(eachData.features),
                    'link': eachData.link,
                    'code': eachData.code,
                    
                }
        else:
            data = {}
            dctProjectData = {}

        return JsonResponse({
            "profile": data,
            "projects": dctProjectData
        })

    # Normal page load — send context to template

    dctProfile = Profile.objects.last()
    dctAbout = About.objects.last()
    dctEducation = Education.objects.all()
    dctExperience = Experience.objects.all()
    dctInternship = Internship.objects.all()
    dctSkills = Skill.objects.all()
    dctProjects = Projects.objects.all()

    for p in dctProjects:
        p.tech_list = safe_list(p.tech)
        p.features_list = safe_list(p.features)
    
    context = {
        'dctProfile':dctProfile,
        'dctAbout':dctAbout,
        'dctEducation':dctEducation,
        'dctExperience':dctExperience,
        'dctInternship':dctInternship,
        'dctSkills':dctSkills,
        'dctProjects':dctProjects
    }
    return render(request,'index.html',context)

@login_required(login_url='login')
def post(request):

    if request.method == 'POST':
        strName = request.POST.get('name')
        strEmail = request.POST.get('email')
        strPhone = request.POST.get('phone')
        profilePhoto = request.FILES.get('image')
        strEduction = request.POST.get('education')
        strExperience = request.POST.get('experience')
        strLocation = request.POST.get('location')
        strGithub = request.POST.get('github')
        strLinkedIn = request.POST.get('linkedin')
        strXtwitter = request.POST.get('x-twitter')
        strStackOverFlow = request.POST.get('stackoverflow')

        strProfessions = request.POST.get('profession')
        lstProfessions = [p.strip() for p in strProfessions.split(",")]

        Profile.objects.create(
            name = strName,
            email = strEmail,
            phone = strPhone,
            profilePhoto = profilePhoto,
            education = strEduction,
            experience = strExperience,
            professions = lstProfessions,
            location = strLocation,
            github = strGithub,
            linkedin = strLinkedIn,
            x = strXtwitter,
            stackoverflow = strStackOverFlow
        )
        return redirect('home')
    
    return render(request,'post.html')

@login_required(login_url='login')
def about(request):
    if request.method == 'POST':
        profile = Profile.objects.last()
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('AboutImage')

        About.objects.create(
            profile = profile,
            title = title,
            description = description,
            image = image
        )
        messages.success(request, 'About saved successfully!')
        return redirect('post') 
    return render(request, "post.html")

@login_required(login_url='login')
def education(request):
    if request.method == 'POST':
        profile = Profile.objects.last()
        title = request.POST.get('title')
        institute = request.POST.get('institute')
        year = request.POST.get('year')
        description = request.POST.get('description')

        Education.objects.create(
            profile = profile,
            title = title,
            institute = institute,
            year = year,
            description = description
        )
        messages.success(request, 'Education saved successfully!')
        return redirect('post') 
    return render(request, "post.html")

@login_required(login_url='login')
def experience(request):
    if request.method == 'POST':
        profile = Profile.objects.last()
        company = request.POST.get('company')
        role = request.POST.get('role')
        duration = request.POST.get('duration')
        description = request.POST.get('description')
        details = request.POST.get('details')
        lstDetails = [eachDetils.strip() for eachDetils in details.split("\n") if eachDetils.strip() ]

        Experience.objects.create(
            profile = profile,
            company = company,
            role = role,
            duration = duration,
            description = description,
            details = lstDetails
        )
        messages.success(request, 'Experience saved successfully!')
        return redirect('post') 
    return render(request, "post.html")

@login_required(login_url='login')
def internship(request):
    if request.method == 'POST':
        profile = Profile.objects.last()
        title = request.POST.get('title')
        company = request.POST.get('company')
        duration = request.POST.get('duration')
        description = request.POST.get('description')
        details = request.POST.get('details')
        lstDetails = [ eachDetails.strip() for eachDetails in details.split("\n") if eachDetails.strip() ]

        Internship.objects.create(
            profile = profile,
            company = company,
            title = title,
            duration = duration,
            description = description,
            details = lstDetails
        )
        messages.success(request, 'Internship saved successfully!')
        return redirect('post') 
    return render(request, "post.html")

@login_required(login_url='login')
def skill(request):
    item = ''
    if request.method == 'POST':
        profile = Profile.objects.last()
        item = request.POST.get('item')
        proficiency = request.POST.get('proficiency')
        genre = request.POST.get('genre')

        Skill.objects.create(
            profile=profile,
            item=item,
            proficiency=proficiency,
            category=genre
        )
        messages.success(request,item + ' Added Successfully!')
        return redirect('post') 
    return render(request, "post.html")

@login_required(login_url='login')
def project(request):
    if request.method == 'POST':
        profile = Profile.objects.last()
        name = request.POST.get('name')
        image = request.FILES.get('image')
        category = request.POST.get('genre')
        description = request.POST.get('description')
        strTech = request.POST.get('tech')
        strFeatures = request.POST.get('features')
        link = request.POST.get('link')
        code = request.POST.get('code')

        lstTech = [eachTech.strip() for eachTech in strTech.split(',')]
        lstFeatures = [eachFeatures.strip() for eachFeatures in strFeatures.split("\n") if eachFeatures.strip()]

        Projects.objects.create(
            profile = profile,
            name = name,
            image = image,
            category = category,
            description = description,
            tech = lstTech,
            features = lstFeatures,
            link =link,
            code = code
        )
        messages.success(request,"Project Added successfully!!")
        return redirect('post')
    return render(request,"post.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "invalid"}, status=400)


@login_required(login_url='login')
def contactview(request):
    dctContact = Contact.objects.all().order_by('-id')
    strSearch = request.GET.get('search')
    if strSearch:
        dctContact = Contact.objects.filter(name__icontains=strSearch)

    context = {
        'dctContact':dctContact
    } 
    return render(request,'contactsview.html',context)

def notfound(request):
    return render(request,'404.html')