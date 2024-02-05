from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    swiper_contents = SwiperContent.objects.all()
    products = Product.objects.all()
    course = courses.objects.all()
    news = News.objects.all()
    team = Team.objects.all()
    swiper_content = Portfolio_content.objects.all()
    return render(request,'index.html',{'swiper_contents': swiper_contents,'products': products,'swiper_content': swiper_content,'news':news,'team':team,'course':course})

@login_required(login_url='signin')
def admin_page(request):
    return render(request,'admin.html')


def swiper_view(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        
        

        # Save the data to the database
        swiper_content = SwiperContent.objects.create(
            image=image,
            
            
        )

        # Redirect or do other actions after saving
        return redirect('swiper_view')  # Replace 'success_page' with your actual success page URL

    swiper_contents = SwiperContent.objects.all()
    return render(request, 'add_slider_content.html', {'swiper_contents': swiper_contents})


def edit_swiper_contents(request, content_id):
    content = get_object_or_404(SwiperContent, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        
       

        # Update the SwiperContent instance with the new data
        content.image = image
       
        
        content.save()

        return redirect('swiper_view')  # Redirect to the Swiper view after editing

    return render(request, 'edit_swiper_content.html', {'content': content})


def delete_swiper_content(request, content_id):
    content = get_object_or_404(SwiperContent, id=content_id)
    content.delete()
    return redirect('swiper_view')




def add_toper(request):
    if request.method == 'POST':
        image = request.FILES['image']
        heading = request.POST['heading']
        description = request.POST['description']

        product = Product.objects.create(
            image=image,
            heading=heading,
            description=description
        )
        product.save()
        
        return redirect('add_toper')
    products = Product.objects.all()

    return render(request, 'add_toper.html',{'products':products})


def edit_toper(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        image = request.FILES.get('image', product.image)
        heading = request.POST.get('heading', product.heading)
        description = request.POST.get('description', product.description)

        product.image = image
        product.heading = heading
        product.description = description
        product.save()

        return redirect('add_toper')

    return render(request, 'edit_toper.html', {'product': product})




def delete_toper_content(request, toper_id):
    content = get_object_or_404(Product, id=toper_id)
    content.delete()
    return redirect('add_toper')






def add_swiper_content(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']

        Portfolio_content.objects.create(video_url=video_url, heading=heading, paragraph=paragraph)
        return redirect('add_swiper_content')
    swiper_contents = Portfolio_content.objects.all()

    return render(request, 'add_swiper_content.html',{'swiper_contents': swiper_contents})
    


def edit_swiper_content(request, swiper_content_id):
    swiper_content = get_object_or_404(Portfolio_content, id=swiper_content_id)

    if request.method == 'POST':
        video_url = request.POST.get('video_url', swiper_content.video_url)
        heading = request.POST.get('heading', swiper_content.heading)
        paragraph = request.POST.get('paragraph', swiper_content.paragraph)

        swiper_content.video_url = video_url
        swiper_content.heading = heading
        swiper_content.paragraph = paragraph
        swiper_content.save()

        return redirect('add_swiper_content')

    return render(request, 'edit_portfolio_content.html', {'swiper_content': swiper_content})



def delete_portfolio_content(request, portfolio_id):
    content = get_object_or_404(Portfolio_content, id=portfolio_id)
    content.delete()
    return redirect('add_swiper_content')



def save_news_section(request):
    if request.method == 'POST':
       
            # Extract values from the form
            title = request.POST.get('title')
            content = request.POST.get('content')
            image = request.FILES.get('image')  # Assuming the image is a file field

            # Validate required fields
           

            # Create a new blog instance
            new_blog = News(
                title=title,
                
                content=content,
                image=image
            )

            # Save the blog to the database
            new_blog.save()

            
            return redirect('save_news_section')
    news = News.objects.all()
    return render(request,'add_news.html',{'news':news})




def edit_news(request, blog_id):
    news = get_object_or_404(News, pk=blog_id)

    if request.method == 'POST':
        # Extract values from the form
        title = request.POST.get('title')
        
        content = request.POST.get('content')
        image = request.FILES.get('image')



        # Update the blog instance
        news.title = title
        
        news.content = content
        if image:
            news.image = image

        
        news.save()

        return redirect('save_news_section')  
    else:
        
        return render(request, 'edit_blog.html', {'news': news})
    


def delete_news(request, news_id):
    content = get_object_or_404(News, id=news_id)
    content.delete()
    return redirect('save_news_section')


def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news_details.html', {'news': news})



def contact_submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact_US.objects.create(
            name=name,
            email=email,
            phone_no=phone,
            message=message

        )
        contact.save()
        messages.info(request,'We will get you soon')
        return redirect('index')
    

def contact_admin(request):
    contact = Contact_US.objects.all()
    return render(request,'admin_contacts.html',{'contact':contact})


def delete_contact(request, contact_id):
    content = get_object_or_404(Contact_US, id=contact_id)
    content.delete()
    return redirect('contact_admin')


def about_us(request):
    team = Team.objects.all()
    return render(request,'about_us.html',{'team':team})


def add_team(request):
    if request.method == 'POST':
        image = request.FILES['image']
        heading = request.POST['heading']
        description = request.POST['description']
        qualification = request.POST['qualification']

        product = Team.objects.create(
            image=image,
            heading=heading,
            description=description,
            qualification=qualification
        )
        product.save()
        return redirect('add_team')
    team = Team.objects.all()

    return render(request, 'add_team.html',{'team':team})



def edit_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == 'POST':
        image = request.FILES.get('image', team.image)
        heading = request.POST.get('heading', team.heading)
        description = request.POST.get('description', team.description)
        qualification = request.POST.get('qualification',team.qualification)

        team.image = image
        team.heading = heading
        team.description = description
        team.qualification = qualification
        team.save()

        return redirect('add_team')

    return render(request, 'edit_team.html', {'team': team})




def delete_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.delete()
    return redirect('add_team')





def online_admission(request):
    return render(request,'online_admision.html')


def register_online_admission(request):
    
    if request.method == 'POST':
        fname = request.POST['fname']
        sname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        phno = request.POST['phno']
        dob = request.POST['dob']
        qualification = request.POST['qualification']
        course = request.POST['course']

        admision = Online_admission.objects.create(
            
            fname=fname,
            lname=sname,
            email=email,
            phonno =phno,
            gender=gender,
            dob=dob,
            qualification=qualification,
            course=course
        )
        admision.save()
        return redirect('online_admission')



def online_admin_admision(request):
    online = Online_admission.objects.all()
    return render(request,'online_admin_admission.html',{'online':online})




def delete_admision(request,admision_id):
    content = get_object_or_404(Online_admission, id=admision_id)
    content.delete()
    return redirect('online_admin_admision') 


def contact_page(request):
    return render(request,'contact_us.html')




def contact_page_submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact_US.objects.create(
            name=name,
            email=email,
            phone_no=phone,
            message=message

        )
        contact.save()
        messages.info(request,'We will get you soon')
        return redirect('contact_page')



def students_corner(request):
    student = Add_student_corner.objects.all()
    syllabus = Syllabus.objects.all()
    return render(request,'students_corner.html',{'student':student,'syllabus':syllabus})


def add_students_corner(request):
    if request.method == 'POST':
        image = request.FILES['image']
        students = Add_student_corner.objects.create(
           image=image 
        )
        students.save()
        return redirect('add_students_corner')
    students = Add_student_corner.objects.all()  
    return render(request,'add_students_corner.html',{'students':students})


def student_add_corner(request, student_id):
    student = get_object_or_404(Add_student_corner, id=student_id)  # Use 'id' as the lookup parameter
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            student.image = image
            student.save()
            return redirect('add_students_corner')
    else:
        return render(request, 'edit_students_corner.html', {'student': student})
    

def delete_student(request,student_id):
    content = get_object_or_404(Add_student_corner, id=student_id)
    content.delete()
    return redirect('add_students_corner')


def logout(request):
	auth.logout(request)
	return redirect('index')



def topers(request):
    toper = Product.objects.all()
    return render(request,'toppers.html',{'toper':toper})


def career(request):
    return render(request,'careers.html')


def careers_section(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        qualification = request.POST['Qualification']
        DOB = request.POST['Date']
        resume = request.FILES.get('resume')
        career = careers.objects.create(

            name=name,
            phone=phone,
            email=email,
            resume=resume,
            qualafication=qualification,
            dob=DOB
            )
        career.save()
        messages.info(request,'We will get back you soon')
        return redirect('career')


def admin_careers(request):
    carer = careers.objects.all()
    return render(request,'admin_careers.html',{'carer':carer})


def carerr_delete(request,career_id):
    content = get_object_or_404(careers, id=career_id)
    content.delete()
    return redirect('admin_careers')


def add_syllabus(request):
    syllabus = Syllabus.objects.all()
    return render(request,'ad_sylabus_section.html',{'syllabus':syllabus})


def add_syllabus_section(request):
    if request.method == 'POST':
        name = request.POST['heading']
        pdf_file = request.FILES.get('pdf_files')
        sylabus = Syllabus.objects.create(
               name=name,
               sylabbus_pdf=pdf_file
               )
        sylabus.save()
        return redirect('add_syllabus')


def syllabus_delete(request,syllabus_id):
    content = get_object_or_404(Syllabus, id=syllabus_id)
    content.delete()
    return redirect('add_syllabus')


def login_page(request):
    return render(request,'login.html')


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_page')
        else:
            messages.error(request, 'Invalid credentials or you do not have admin access.')
            return redirect('login_page')

    return redirect('login_page')


def add_courese(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST['name']
        url = request.POST['url']
        course = courses.objects.create(
            image=image,
            name=name,
            url=url
            )
        course.save()
        return redirect('add_courese')
    cours = courses.objects.all()
    return render(request,'add_courses.html',{'cours':cours})


def edit_course(request,course_id):
    course = get_object_or_404(courses, pk=course_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        
        url = request.POST.get('url')
        image = request.FILES.get('image')



        # Update the blog instance
        course.name = name
        
        course.url = url
        if image:
            course.image = image

        
        course.save()

        return redirect('add_courese')  
    else:
        
        return render(request, 'edit_course.html', {'course': course})
    

def delete_course(request,course_id):
    course = get_object_or_404(courses, id=course_id)
    course.delete()
    return redirect('add_courese')


