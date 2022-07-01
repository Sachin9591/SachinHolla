from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import *
import datetime
import random
import math
import os


# Create your views here.
def datetime_return():
    dateTimeFormats = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return dateTimeFormats


def date_return():
    dateFormats = datetime.date.today().strftime("%Y%m%d%H%M%S")
    return dateFormats


# function to generate OTP
def generate_otp(otp_length):
    # Declare a digits variable
    # which stores all digits
    digits = "0123456789"
    OTP = ""
    # length of password can be changed
    # by changing value in range
    for i in range(otp_length):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def index(request):
    resumeCV = ResumeUploadsList.objects.filter(resumeActive=True)
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    techSkillsDetails = TechnicalSkillsList.objects.filter(tSkillActive=True)
    blogsDetails = BlogsList.objects.filter(blActive=True)
    return render(request, 'index.html', {'Resume_CV': resumeCV, 'Serv_Details': servDetails,
                                          'Testimonial_Det': testMonDetails, 'TechSkills_Det': techSkillsDetails,
                                          'Blogs_Det': blogsDetails})


def index_five(request):
    resumeCV = ResumeUploadsList.objects.filter(resumeActive=True)
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    techSkillsDetails = TechnicalSkillsList.objects.filter(tSkillActive=True)
    blogsDetails = BlogsList.objects.filter(blActive=True)
    return render(request, 'index-5.html', {'Resume_CV': resumeCV, 'Serv_Details': servDetails,
                                            'Testimonial_Det': testMonDetails, 'TechSkills_Det': techSkillsDetails,
                                            'Blogs_Det': blogsDetails})


def index_six(request):
    resumeCV = ResumeUploadsList.objects.filter(resumeActive=True)
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    techSkillsDetails = TechnicalSkillsList.objects.filter(tSkillActive=True)
    blogsDetails = BlogsList.objects.filter(blActive=True)
    return render(request, 'index-6.html', {'Resume_CV': resumeCV, 'Serv_Details': servDetails,
                                            'Testimonial_Det': testMonDetails, 'TechSkills_Det': techSkillsDetails,
                                            'Blogs_Det': blogsDetails})


def index_eight(request):
    resumeCV = ResumeUploadsList.objects.filter(resumeActive=True)
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    techSkillsDetails = TechnicalSkillsList.objects.filter(tSkillActive=True)
    blogsDetails = BlogsList.objects.filter(blActive=True)
    return render(request, 'index-8.html', {'Resume_CV': resumeCV, 'Serv_Details': servDetails,
                                            'Testimonial_Det': testMonDetails, 'TechSkills_Det': techSkillsDetails,
                                            'Blogs_Det': blogsDetails})


def index_one(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-1.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def index_two(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-2.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def index_three(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-3.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def index_four(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-4.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def index_nine(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-9.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def index_ten(request):
    servDetails = ServicesIndexList.objects.filter(servActive=True)
    testMonDetails = TestimonialsList.objects.all()
    return render(request, 'index-10.html', {'Serv_Details': servDetails, 'Testimonial_Det': testMonDetails})


def blog(request):
    return render(request, 'blog.html')


def blog_black(request):
    return render(request, 'blog-black.html')


def blog_details(request):
    return render(request, 'blog-details.html')


def blog_details_black(request):
    return render(request, 'blog-details-black.html')


def not_found_error(request, exception):
    return render(request, 'not-found-404.html')


def download_resume(request, path):
    filePath = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(filePath):
        with open(filePath, 'rb') as f:
            resp = HttpResponse(f.read(), content_type="application/resumeFile")
            resp['Content-Disposition'] = 'inline;filename='+os.path.basename(filePath)
            return resp
    raise Http404


def ct_msg_send(request):
    if request.method == 'POST':
        user_subject = request.POST['subject']
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_message = request.POST['message']
        subjects = user_name + " - " + user_subject
        send_mail(subject=subjects, message=user_message, from_email=user_email,
                  recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False)
        return HttpResponseRedirect(reverse('home'))
    else:
        return redirect('home')
