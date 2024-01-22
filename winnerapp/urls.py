from django.urls import path
from  winnerapp import views
from  django.contrib import admin
from django.contrib.auth import views as auth_views



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
]