import smtplib
from django.shortcuts import render
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from home.models import Counting, Volunteer, Pay, Email, Image, TeamPic


def home(request):
    pay = Pay.objects.all()
    count = Counting.objects.all()
    volunteer = Volunteer.objects.all().order_by('-id')
    images = Image.objects.all().order_by('-id')
    team = TeamPic.objects.all()
    return render(request, 'home.html', {'count': count, 'volunteer': volunteer, 'pay': pay, 'images': images, 'team': team})


def payhelp(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    fromEmail = Email.objects.all()

    smtpServer = 'smtp.gmail.com'
    subject = 'Thank you for contacting Maverick!'
    message = "Dear "+name+",\nWe have received your details, we will contact you soon!\nThank You!\n\n\nInstagram: https://instagram.com/maverick_foundation\nFacebook: https://www.facebook.com/maverickbag/\nWebsite: https://maverickfoundation.herokuapp.com/ "
    msg = MIMEMultipart()
    msg['From'] = fromEmail[0].email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtpServer, 587)
    server.ehlo()
    server.starttls()
    server.login(fromEmail[0].email, fromEmail[0].password)
    text = msg.as_string()
    server.sendmail(fromEmail[0].email, email, text)
    server.quit()

    admin = smtplib.SMTP(smtpServer, 587)
    admin.ehlo()
    admin.starttls()
    admin.login(fromEmail[0].email, fromEmail[0].password)
    txt = "Hello,\nYou have a new enquiry on Payment Help from\nName: "+name+"\nMobile: "+phone+"\nEmail: "+email+"\n\nPlease address at the earliest!"
    admin.sendmail(fromEmail[0].email, "araonandan7@gmail.com", txt)
    admin.quit()

    pay = Pay.objects.all()
    count = Counting.objects.all()
    volunteer = Volunteer.objects.all().order_by('-id')
    images = Image.objects.all().order_by('-id')
    team = TeamPic.objects.all()
    return render(request, 'home.html',
                  {'count': count, 'volunteer': volunteer, 'pay': pay, 'images': images, 'team': team})

def denim(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']

    fromEmail = Email.objects.all()

    smtpServer = 'smtp.gmail.com'
    subject = 'Thank you for contacting Maverick!'
    message = "Dear "+name+",\nWe have received your details, we will contact you soon!\nThank You!\n\n\nInstagram: https://instagram.com/maverick_foundation\nFacebook: https://www.facebook.com/maverickbag/\nWebsite: https://maverickfoundation.herokuapp.com/ "

    msg = MIMEMultipart()
    msg['From'] = fromEmail[0].email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(message,'plain'))

    server = smtplib.SMTP(smtpServer, 587)
    server.ehlo()
    server.starttls()
    server.login(fromEmail[0].email, fromEmail[0].password)
    text = msg.as_string()
    server.sendmail(fromEmail[0].email, email, text)
    server.quit()

    admin = smtplib.SMTP(smtpServer, 587)
    admin.ehlo()
    admin.starttls()
    admin.login(fromEmail[0].email, fromEmail[0].password)
    txt = "Hello,\nYou have a new enquiry on Denim Donation from\nName: " + name + "\nMobile: " + phone + "\nEmail: " + email + "\n\nPlease address at the earliest!"
    admin.sendmail(fromEmail[0].email, "araonandan7@gmail.com", txt)
    admin.quit()

    pay = Pay.objects.all()
    count = Counting.objects.all()
    volunteer = Volunteer.objects.all().order_by('-id')
    images = Image.objects.all().order_by('-id')
    team = TeamPic.objects.all()
    return render(request, 'home.html',
                  {'count': count, 'volunteer': volunteer, 'pay': pay, 'images': images, 'team': team})