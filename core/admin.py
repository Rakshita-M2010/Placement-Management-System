from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Company, Job, Application, Interview, PlacementResult, Notification

# ============================================================================
# STUDENT ADMIN
# ============================================================================

class StudentAdmin(admin.ModelAdmin):
    """
    Admin interface for Student model.
    """
    list_display = ('get_full_name', 'roll_number', 'branch', 'cgpa', 'graduation_year', 'phone')
    list_filter = ('branch', 'graduation_year', 'cgpa')
    search_fields = ('user__first_name', 'user__last_name', 'roll_number', 'user__email')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('User Information', {
            'fields': ('user',)
        }),
        ('Academic Details', {
            'fields': ('roll_number', 'branch', 'cgpa', 'graduation_year')
        }),
        ('Contact Information', {
            'fields': ('phone',)
        }),
        ('Additional Information', {
            'fields': ('skills', 'resume')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_full_name(self, obj):
        return obj.user.get_full_name() if obj.user else 'N/A'
    get_full_name.short_description = 'Full Name'


# ============================================================================
# COMPANY ADMIN
# ============================================================================

class CompanyAdmin(admin.ModelAdmin):
    """
    Admin interface for Company model.
    """
    list_display = ('company_name', 'hr_name', 'email', 'phone', 'package', 'get_job_count')
    list_filter = ('package', 'created_at')
    search_fields = ('company_name', 'hr_name', 'email')
    readonly_fields = ('created_at', 'updated_at', 'get_job_count')
    fieldsets = (
        ('Company Information', {
            'fields': ('company_name', 'website', 'description')
        }),
        ('HR Contact', {
            'fields': ('hr_name', 'email', 'phone')
        }),
        ('Package Details', {
            'fields': ('package',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_job_count(self, obj):
        count = obj.jobs.count()
        return format_html('<strong>{}</strong>', count)
    get_job_count.short_description = 'Active Jobs'


# ============================================================================
# JOB ADMIN
# ============================================================================

class JobAdmin(admin.ModelAdmin):
    """
    Admin interface for Job model.
    """
    list_display = ('job_title', 'company', 'min_cgpa', 'deadline', 'job_type', 'get_application_count', 'is_active')
    list_filter = ('job_type', 'deadline', 'min_cgpa', 'company')
    search_fields = ('job_title', 'company__company_name', 'description')
    readonly_fields = ('created_at', 'updated_at', 'get_application_count')
    fieldsets = (
        ('Job Details', {
            'fields': ('company', 'job_title', 'description', 'job_type')
        }),
        ('Eligibility & Location', {
            'fields': ('min_cgpa', 'location')
        }),
        ('Deadline', {
            'fields': ('deadline',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_application_count(self, obj):
        count = obj.applications.count()
        return format_html('<strong>{}</strong>', count)
    get_application_count.short_description = 'Applications'

    def is_active(self, obj):
        if obj.is_active:
            return format_html('<span style="color: green;">✓ Active</span>')
        else:
            return format_html('<span style="color: red;">✗ Expired</span>')
    is_active.short_description = 'Status'


# ============================================================================
# APPLICATION ADMIN
# ============================================================================

class ApplicationAdmin(admin.ModelAdmin):
    """
    Admin interface for Application model.
    """
    list_display = ('get_student_name', 'get_job_title', 'status', 'applied_date', 'has_interview')
    list_filter = ('status', 'applied_date', 'job__company')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'job__job_title')
    readonly_fields = ('applied_date', 'updated_at')
    fieldsets = (
        ('Application Details', {
            'fields': ('student', 'job')
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('applied_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_student_name(self, obj):
        return obj.student.user.get_full_name() if obj.student.user else 'N/A'
    get_student_name.short_description = 'Student'

    def get_job_title(self, obj):
        return obj.job.job_title
    get_job_title.short_description = 'Job Title'

    def has_interview(self, obj):
        if hasattr(obj, 'interview'):
            return format_html('<span style="color: green;">✓ Scheduled</span>')
        else:
            return format_html('<span style="color: orange;">⊗ Not Scheduled</span>')
    has_interview.short_description = 'Interview'


# ============================================================================
# INTERVIEW ADMIN
# ============================================================================

class InterviewAdmin(admin.ModelAdmin):
    """
    Admin interface for Interview model.
    """
    list_display = ('get_student_name', 'get_job_title', 'interview_type', 'date', 'time', 'venue')
    list_filter = ('interview_type', 'date', 'application__job__company')
    search_fields = ('application__student__user__first_name', 'application__student__user__last_name', 'application__job__job_title')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Interview Details', {
            'fields': ('application', 'interview_type')
        }),
        ('Schedule', {
            'fields': ('date', 'time', 'venue')
        }),
        ('Additional Information', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_student_name(self, obj):
        return obj.application.student.user.get_full_name() if obj.application.student.user else 'N/A'
    get_student_name.short_description = 'Student'

    def get_job_title(self, obj):
        return obj.application.job.job_title
    get_job_title.short_description = 'Job Title'


# ============================================================================
# PLACEMENT RESULT ADMIN
# ============================================================================

class PlacementResultAdmin(admin.ModelAdmin):
    """
    Admin interface for PlacementResult model.
    """
    list_display = ('get_student_name', 'get_company_name', 'status', 'package_offered', 'selection_date', 'published_date')
    list_filter = ('status', 'selection_date', 'company')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'company__company_name', 'job__job_title')
    readonly_fields = ('published_date', 'updated_at')
    fieldsets = (
        ('Placement Details', {
            'fields': ('student', 'application', 'company', 'job')
        }),
        ('Result Information', {
            'fields': ('status', 'package_offered', 'selection_date')
        }),
        ('Timestamps', {
            'fields': ('published_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_student_name(self, obj):
        return obj.student.user.get_full_name() if obj.student.user else 'N/A'
    get_student_name.short_description = 'Student'

    def get_company_name(self, obj):
        return obj.company.company_name
    get_company_name.short_description = 'Company'


# ============================================================================
# NOTIFICATION ADMIN
# ============================================================================

class NotificationAdmin(admin.ModelAdmin):
    """
    Admin interface for Notification model.
    """
    list_display = ('get_student_name', 'notification_type', 'is_read', 'created_at')
    list_filter = ('notification_type', 'is_read', 'created_at')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'title', 'message')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Notification Details', {
            'fields': ('student', 'notification_type', 'title', 'message')
        }),
        ('Related Objects', {
            'fields': ('application', 'job', 'placement_result'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_student_name(self, obj):
        return obj.student.user.get_full_name() if obj.student.user else 'N/A'
    get_student_name.short_description = 'Student'


# Register all models with their custom admin classes
admin.site.register(Student, StudentAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(PlacementResult, PlacementResultAdmin)
admin.site.register(Notification, NotificationAdmin)

# Customize admin site
admin.site.site_header = "Placement Management System - Admin Panel"
admin.site.site_title = "PMS Admin"
admin.site.index_title = "Welcome to Placement Management System Admin"
