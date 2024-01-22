from django.shortcuts import render
from django.contrib.auth.models import User,auth
from .models import *
from django.shortcuts import get_object_or_404,redirect
from django.contrib import messages
# Create your views here.


def index(request):
    swiper_contents = SwiperContent.objects.all()
    products = Product.objects.all()
    courses = Course.objects.all()
    news = News.objects.all()
    swiper_content = Portfolio_content.objects.all()
    return render(request,'index.html',{'swiper_contents': swiper_contents,'products': products,'courses':courses,'swiper_content': swiper_content,'news':news})


def admin_page(request):
    return render(request,'admin.html')


def swiper_view(request):
    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES['image']
        online_class_url = request.POST['online_class_url']
        offline_class_url = request.POST['offline_class_url']

        # Save the data to the database
        swiper_content = SwiperContent.objects.create(
            image=image,
            online_class_url=online_class_url,
            offline_class_url=offline_class_url
        )

        # Redirect or do other actions after saving
        return redirect('swiper_view')  # Replace 'success_page' with your actual success page URL

    swiper_contents = SwiperContent.objects.all()
    return render(request, 'add_slider_content.html', {'swiper_contents': swiper_contents})


def edit_swiper_content(request, content_id):
    content = get_object_or_404(SwiperContent, id=content_id)

    if request.method == 'POST':
        # Assuming your form sends data as a POST request
        image = request.FILES.get('image', content.image)
        online_class_url = request.POST.get('online_class_url', content.online_class_url)
        offline_class_url = request.POST.get('offline_class_url', content.offline_class_url)

        # Update the SwiperContent instance with the new data
        content.image = image
        content.online_class_url = online_class_url
        content.offline_class_url = offline_class_url
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



def add_course(request):
    if request.method == 'POST':
        image = request.FILES['image']
        url = request.POST['url']

        # Create and save the Course instance
        Course.objects.create(image=image, url=url)

        return redirect('add_course')
    courses = Course.objects.all()

    return render(request, 'add_course.html',{'courses':courses})




def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        image = request.FILES.get('image', course.image)
        url = request.POST.get('url', course.url)

        # Update the Course instance with the new data
        course.image = image
        course.url = url
        course.save()

        return redirect('add_course')

    return render(request, 'edit_course.html', {'course': course})


def delete_course_content(request, course_id):
    content = get_object_or_404(Course, id=course_id)
    content.delete()
    return redirect('add_course')


def add_swiper_content(request):
    if request.method == 'POST':
        image = request.FILES['image']
        heading = request.POST['heading']
        paragraph = request.POST['paragraph']

        Portfolio_content.objects.create(image=image, heading=heading, paragraph=paragraph)
        return redirect('add_swiper_content')
    swiper_contents = Portfolio_content.objects.all()

    return render(request, 'add_swiper_content.html',{'swiper_contents': swiper_contents})
    


def edit_swiper_content(request, swiper_content_id):
    swiper_content = get_object_or_404(Portfolio_content, id=swiper_content_id)

    if request.method == 'POST':
        image = request.FILES.get('image', swiper_content.image)
        heading = request.POST.get('heading', swiper_content.heading)
        paragraph = request.POST.get('paragraph', swiper_content.paragraph)

        swiper_content.image = image
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

