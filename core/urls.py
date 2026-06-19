from django.urls import path
from . import views

# ============================================================================
# URL PATTERNS FOR CORE APP
# ============================================================================

urlpatterns = [
    # ========================================================================
    # HOME PAGE
    # ========================================================================
    path('', views.home, name='home'),

    # ========================================================================
    # AUTHENTICATION URLS
    # ========================================================================
    path('auth/register/', views.student_register, name='register'),
    path('auth/login/', views.student_login, name='login'),
    path('auth/logout/', views.student_logout, name='logout'),
    path('auth/change-password/', views.student_change_password, name='change_password'),

    # ========================================================================
    # STUDENT PROFILE URLS
    # ========================================================================
    path('student/profile/create/', views.student_profile_create, name='student_profile_create'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),

    # ========================================================================
    # JOB URLS
    # ========================================================================
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/', views.job_detail, name='job_detail'),

    # ========================================================================
    # APPLICATION URLS
    # ========================================================================
    path('jobs/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),
    path('applications/', views.student_applications, name='student_applications'),

    # ========================================================================
    # ADMIN DASHBOARD URLS
    # ========================================================================
    path('admin-panel/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # ========================================================================
    # ADMIN COMPANY MANAGEMENT URLS
    # ========================================================================
    path('admin-panel/companies/', views.admin_company_list, name='admin_company_list'),
    path('admin-panel/companies/create/', views.admin_company_create, name='admin_company_create'),
    path('admin-panel/companies/<int:company_id>/edit/', views.admin_company_edit, name='admin_company_edit'),
    path('admin-panel/companies/<int:company_id>/delete/', views.admin_company_delete, name='admin_company_delete'),

    # ========================================================================
    # ADMIN JOB MANAGEMENT URLS
    # ========================================================================
    path('admin-panel/jobs/', views.admin_job_list, name='admin_job_list'),
    path('admin-panel/jobs/create/', views.admin_job_create, name='admin_job_create'),
    path('admin-panel/jobs/<int:job_id>/edit/', views.admin_job_edit, name='admin_job_edit'),
    path('admin-panel/jobs/<int:job_id>/delete/', views.admin_job_delete, name='admin_job_delete'),

    # ========================================================================
    # ADMIN APPLICATION MANAGEMENT URLS
    # ========================================================================
    path('admin-panel/applications/', views.admin_applications, name='admin_applications'),
    path('admin-panel/applications/<int:application_id>/update/', views.admin_application_update, name='admin_application_update'),

    # ========================================================================
    # ADMIN INTERVIEW MANAGEMENT URLS
    # ========================================================================
    path('admin-panel/interviews/', views.admin_interviews, name='admin_interviews'),
    path('admin-panel/interviews/<int:application_id>/schedule/', views.admin_interview_schedule, name='admin_interview_schedule'),
    path('admin-panel/interviews/<int:interview_id>/edit/', views.admin_interview_edit, name='admin_interview_edit'),

    # ========================================================================
    # ADMIN STUDENT MANAGEMENT URLS
    # ========================================================================
    path('admin-panel/students/', views.admin_students, name='admin_students'),
    path('admin-panel/students/<int:student_id>/', views.admin_student_detail, name='admin_student_detail'),
    path('admin-panel/students/<int:student_id>/edit/', views.admin_student_edit, name='admin_student_edit'),
    path('admin-panel/students/<int:student_id>/delete/', views.admin_student_delete, name='admin_student_delete'),

    # ========================================================================
    # ADMIN REPORTS
    # ========================================================================
    path('admin-panel/reports/', views.admin_reports, name='admin_reports'),
    path('admin-panel/reports/students/', views.student_report, name='student_report'),
    path('admin-panel/reports/companies/', views.company_report, name='company_report'),
    path('admin-panel/reports/placements/', views.placement_report, name='placement_report'),
    path('admin-panel/reports/applications/', views.application_report, name='application_report'),
    path('admin-panel/reports/interviews/', views.interview_report, name='interview_report'),

    # ========================================================================
    # PLACEMENT RESULT URLS
    # ========================================================================
    path('admin-panel/placement-results/<int:placement_result_id>/revoke/', views.admin_revoke_result, name='admin_revoke_result'),

    # ========================================================================
    # STUDENT NOTIFICATION URLS
    # ========================================================================
    path('notifications/', views.student_notifications, name='student_notifications'),
    path('notifications/<int:notification_id>/read/', views.mark_notification_read, name='mark_notification_read'),
    path('api/notifications/unread-count/', views.get_unread_notifications_count, name='get_unread_notifications_count'),

    # ========================================================================
    # STUDENT PLACEMENT RESULTS URLS
    # ========================================================================
    path('placement-results/', views.student_placement_results, name='student_placement_results'),
]

