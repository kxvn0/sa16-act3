from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    welcome_msg = "Hello, Welcome to My Portfolio."
    summary = "I am a very passionate web developer with expertise in various languages such as Ruby on Rails, HTML, CSS, and JavaScript."
    context = { 'welcome_msg': welcome_msg, 'summary': summary }
    return render(request, 'portfolio/home.html', context)

def about(request):
    bio = "I am a very dedicated web developer with a BS in Computer Science from the University of Memphis. I have had various experiences working with several programming languages such as Ruby on Rails, HTML, CSS, and JavaScript that have allowed me to create websites. I am always eager to learn new techniques and perfecting my craft as I find web development very fascinating and fun!"
    education = "I have a BS in Computer Science."
    skills = ["JavaScript", "HTML", "Ruby on Rails", "CSS", "Python"]
    context = { 'bio': bio, 'education': education,'skills': skills }
    return render(request, 'portfolio/about.html', context)

def contact(request):
    email = "tonybologna@gmail.com"
    phone_num = "901-999-9999"
    social_media = {
        'twitter': "https://x.com/tonybologna",
        'linkedin': "https://www.linkedin.com/in/tony",
        'github': "https://github.com/tonybalogna"
    }
    context = {
        'email': email,
        'phone_num': phone_num,
        'social_media': social_media,
    }
    return render(request, 'portfolio/contact.html', context)
from django.shortcuts import render

def work(request):
    projects = [
        {
            'title': "Portfolio Website",
            'description': "Developed a portfolio about my favorite sports team using Ruby on Rails.",
            'image': "rm-portfolio.png",
            'technologies': ["HTML", "CSS", "JavaScript"],
        },
        {
            'title': "E-commerce App",
            'description': "Built a platform for dog-sitting in the Memphis Area.",
            'image': "woof-sitters.png",
            'technologies': ["Ruby on Rails", "HTML", "CSS"],
        },
    ]
    return render(request, 'portfolio/work.html', {'projects': projects})

