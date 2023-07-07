from django.urls import path
from . import views

urlpatterns = [
    # Teachers
    path('teacher/', views.TeacherList.as_view()),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('teacher-login/',views.teacher_login),

    # CourseCategory
    path('category/', views.CategoryList.as_view()),
    # all courses
    path('course/', views.CourseList.as_view()),
    # chapters
    path('chapter/', views.ChapterList.as_view()),
    #Teacher Courses
    path('teacher-courses/<int:teacher_id>/', views.TeacherCourseList.as_view()),
]
