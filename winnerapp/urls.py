from django.urls import path,re_path
from  winnerapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('',views.index,name='index'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('swiper_view',views.swiper_view,name='swiper_view'),
    path('edit/<int:content_id>/', views.edit_swiper_content, name='edit_swiper_content'),
    path('delete/<int:content_id>/', views.delete_swiper_content, name='delete_swiper_content'),
    path('add_toper',views.add_toper,name='add_toper'),
    path('toper/edit/<int:product_id>/', views.edit_toper, name='edit_toper'),
    path('delete_toper_content/<int:toper_id>/', views.delete_toper_content, name='delete_toper_content'),
    path('add_course',views.add_course,name='add_course'),
    path('edit_course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('delete_course_content/<int:course_id>/', views.delete_course_content, name='delete_course_content'),
    path('add_swiper_content',views.add_swiper_content,name='add_swiper_content'),
    path('edit_swiper_content/<int:swiper_content_id>/', views.edit_swiper_content, name='edit_swiper_content'),
    path('delete_portfolio_content/<int:portfolio_id>/', views.delete_portfolio_content, name='delete_portfolio_content'),
    path('save_news_section',views.save_news_section,name='save_news_section'),
    path('edit_news/<int:blog_id>/', views.edit_news, name='edit_news'),
    path('delete_news/<int:news_id>/', views.delete_news, name='delete_news'),
    path('news_detail/<int:news_id>/',views.news_detail,name='news_detail'),
    path('contact_submit',views.contact_submit,name='contact_submit'),
    path('contact_admin',views.contact_admin,name='contact_admin'),
    path('delete_contact/<int:contact_id>',views.delete_contact,name='delete_contact'),
    path('about_us',views.about_us,name='about_us'),
    path('add_team',views.add_team,name='add_team'),
    path('edit_team/<int:team_id>/',views.edit_team,name='edit_team'),
    path('delete_team/<int:team_id>/',views.delete_team,name='delete_team'),
    path('courses',views.courses,name='courses'),
    path('online_admission',views.online_admission,name='online_admission'),
    path('register_online_admission',views.register_online_admission,name='register_online_admission'),
    path('online_admin_admision',views.online_admin_admision,name='online_admin_admision'),
    path('delete_admision/<int:admision_id>/',views.delete_admision,name='delete_admision'),
    path('contact_page',views.contact_page,name='contact_page'),
    path('contact_page_submit',views.contact_page_submit,name='contact_page_submit'),
    path('students_corner',views.students_corner,name='students_corner'),
    path('add_students_corner',views.add_students_corner,name='add_students_corner'),
    path('student_add_corner/<int:student_id>/',views.student_add_corner,name='student_add_corner'),
    path('delete_student/<int:student_id>/',views.delete_student,name="delete_student"),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)