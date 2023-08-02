from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('course/<slug:course_code>/', views.CourseTopicListView.as_view(), name='course_code'),
    path('course/<slug:course_code>/groups/', views.CourseGroupListView.as_view(), name='coursegroup_list'),
    path('course/<slug:course_code>/group/<slug:coursegroup_code>/enroll/', views.CourseGroupEnrollmentView.as_view(), name='coursegroupmember_create'),
    path('course/group/member/<int:pk>/<slug:status>/', views.CourseGroupMemberUpdate.as_view(), name='coursegroupmember_update'),
]
