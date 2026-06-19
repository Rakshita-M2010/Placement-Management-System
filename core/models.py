from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# ============================================================================
# STUDENT MODEL
# ============================================================================
class Student(models.Model):
    """
    Extended student profile linked to Django's User model.
    Stores placement-related information for students.
    """
    BRANCH_CHOICES = [
        ('CSE', 'Computer Science & Engineering'),
        ('ECE', 'Electronics & Communication Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('EE', 'Electrical Engineering'),
        ('AE', 'Aerospace Engineering'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True, help_text="Student Roll Number")
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    phone = models.CharField(max_length=15)
    skills = models.TextField(blank=True, help_text="Comma-separated list of skills")
    graduation_year = models.IntegerField(
        validators=[MinValueValidator(2024), MaxValueValidator(2030)]
    )
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Students"

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.roll_number}"


# ============================================================================
# COMPANY MODEL
# ============================================================================
class Company(models.Model):
    """
    Represents a company recruiting through the placement cell.
    """
    company_name = models.CharField(max_length=100, unique=True)
    hr_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    package = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Package offered in LPA (Lakhs Per Annum)"
    )
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.company_name


# ============================================================================
# JOB MODEL
# ============================================================================
class Job(models.Model):
    """
    Job postings created by companies for recruitment.
    """
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    min_cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    deadline = models.DateField()
    job_type = models.CharField(
        max_length=20,
        choices=[('Full-Time', 'Full-Time'), ('Internship', 'Internship')],
        default='Full-Time'
    )
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-deadline']
        verbose_name_plural = "Jobs"

    def __str__(self):
        return f"{self.job_title} - {self.company.company_name}"

    @property
    def is_active(self):
        """Check if job posting is still active (deadline not passed)"""
        return self.deadline >= datetime.now().date()


# ============================================================================
# APPLICATION MODEL
# ============================================================================
class Application(models.Model):
    """
    Tracks student applications for job postings.
    """
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Interview Scheduled', 'Interview Scheduled'),
        ('Interview Completed', 'Interview Completed'),
        ('Selected', 'Selected'),
        ('Waiting List', 'Waiting List'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Applied'
    )
    applied_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-applied_date']
        unique_together = ('student', 'job')
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.job.job_title}"


# ============================================================================
# INTERVIEW MODEL
# ============================================================================
class Interview(models.Model):
    """
    Interview scheduling for shortlisted students.
    """
    INTERVIEW_TYPE_CHOICES = [
        ('Technical', 'Technical'),
        ('HR', 'HR'),
        ('Group Discussion', 'Group Discussion'),
        ('Final Round', 'Final Round'),
    ]

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='interview'
    )
    interview_type = models.CharField(
        max_length=20,
        choices=INTERVIEW_TYPE_CHOICES,
        default='Technical'
    )
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date', 'time']
        verbose_name_plural = "Interviews"

    def __str__(self):
        return f"Interview - {self.application.student.user.get_full_name()} ({self.application.job.job_title})"


# ============================================================================
# PLACEMENT RESULT MODEL
# ============================================================================
class PlacementResult(models.Model):
    """
    Stores placement results for selected/rejected candidates.
    Improved with audit trail, result finalization, and revocation capabilities.
    """
    RESULT_STATUS_CHOICES = [
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='placement_results'
    )
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        related_name='placement_result'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='placement_results'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='placement_results'
    )
    status = models.CharField(
        max_length=20,
        choices=RESULT_STATUS_CHOICES,
        default='Selected'
    )
    package_offered = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Package offered in LPA"
    )
    selection_date = models.DateField(help_text="Auto-set to today's date when result is published")
    
    # ======================== PUBLICATION AUDIT TRAIL ========================
    is_published = models.BooleanField(default=False, help_text="Result has been published and is now final")
    published_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='published_results',
        help_text="Admin who published this result"
    )
    published_date = models.DateTimeField(auto_now_add=True, help_text="Timestamp when result was published")
    
    # ======================== REVOCATION AUDIT TRAIL ========================
    is_revoked = models.BooleanField(default=False, help_text="Result has been revoked")
    revoked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='revoked_results',
        help_text="Admin who revoked this result"
    )
    revoked_date = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp when result was revoked"
    )
    revocation_reason = models.TextField(
        blank=True,
        help_text="Reason for revoking the result"
    )
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-selection_date']
        unique_together = ('student', 'application')
        verbose_name_plural = "Placement Results"
        indexes = [
            models.Index(fields=['is_published', 'is_revoked']),
            models.Index(fields=['student', 'is_published']),
        ]

    def __str__(self):
        status_info = "REVOKED" if self.is_revoked else ("PUBLISHED" if self.is_published else "DRAFT")
        return f"{self.student.user.get_full_name()} - {self.company.company_name} ({self.status}) [{status_info}]"
    
    @property
    def can_be_modified(self):
        """Check if result can be modified (not published or already revoked)"""
        return not self.is_published or self.is_revoked
    
    @property
    def can_be_published(self):
        """Check if result can be published (not published yet or was revoked)"""
        return not self.is_published or self.is_revoked


# ============================================================================
# NOTIFICATION MODEL
# ============================================================================
class Notification(models.Model):
    """
    Stores notifications for students regarding job postings, applications, and results.
    """
    NOTIFICATION_TYPE_CHOICES = [
        ('job_posted', 'New Job Posted'),
        ('application_submitted', 'Application Submitted'),
        ('shortlisted', 'Application Shortlisted'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('interview_completed', 'Interview Completed'),
        ('waiting_list', 'Waiting List'),
        ('rejected', 'Application Rejected'),
        ('selected', 'Placement Selected'),
        ('result_published', 'Result Published'),
        ('result_revoked', 'Result Revoked'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    notification_type = models.CharField(
        max_length=25,
        choices=NOTIFICATION_TYPE_CHOICES
    )
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Optional foreign keys for reference
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )
    placement_result = models.ForeignKey(
        PlacementResult,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.title}"