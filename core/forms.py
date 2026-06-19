from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .models import Student, Company, Job, Application, Interview, PlacementResult, Notification

# ============================================================================
# AUTHENTICATION FORMS
# ============================================================================

class StudentRegistrationForm(UserCreationForm):
    """
    Form for student registration.
    Creates a new User and Student profile.
    """
    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address'
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password'
        })

    def clean_email(self):
        """Ensure email is unique"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        """Set username to email"""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class StudentLoginForm(AuthenticationForm):
    """
    Form for student login.
    """
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
            'autofocus': True
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        })
    )


class StudentPasswordChangeForm(PasswordChangeForm):
    """
    Form for students to change their password.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Old Password'
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'New Password'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm New Password'
        })
    )


# ============================================================================
# STUDENT FORMS
# ============================================================================

class StudentProfileForm(forms.ModelForm):
    """
    Form for creating and updating student profile.
    """
    class Meta:
        model = Student
        fields = ('roll_number', 'branch', 'cgpa', 'phone', 'skills', 'graduation_year', 'resume')
        widgets = {
            'roll_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Roll Number'
            }),
            'branch': forms.Select(attrs={
                'class': 'form-control'
            }),
            'cgpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'CGPA (0.00 - 10.00)',
                'step': '0.01',
                'min': '0',
                'max': '10'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '10-digit Phone Number',
                'pattern': '[0-9]{10}'
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter skills separated by comma (e.g., Python, Java, C++)',
                'rows': 4
            }),
            'graduation_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Year of Graduation'
            }),
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx'
            })
        }


# ============================================================================
# COMPANY FORMS (ADMIN)
# ============================================================================

class CompanyForm(forms.ModelForm):
    """
    Form for admin to create and update companies.
    """
    class Meta:
        model = Company
        fields = ('company_name', 'hr_name', 'email', 'phone', 'package', 'website', 'description')
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company Name'
            }),
            'hr_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'HR Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'package': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Package (LPA)',
                'step': '0.01'
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Website URL'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Company Description',
                'rows': 4
            })
        }


# ============================================================================
# JOB FORMS (ADMIN)
# ============================================================================

class JobForm(forms.ModelForm):
    """
    Form for admin to create and update job postings.
    """
    class Meta:
        model = Job
        fields = ('company', 'job_title', 'description', 'min_cgpa', 'deadline', 'job_type', 'location')
        widgets = {
            'company': forms.Select(attrs={
                'class': 'form-control'
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Job Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Job Description',
                'rows': 6
            }),
            'min_cgpa': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minimum CGPA (0.00 - 10.00)',
                'step': '0.01',
                'min': '0',
                'max': '10'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'job_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Location'
            })
        }


# ============================================================================
# APPLICATION FORMS
# ============================================================================

class ApplicationStatusForm(forms.ModelForm):
    """
    Form for admin to update application status.
    """
    class Meta:
        model = Application
        fields = ('status',)
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-control'
            })
        }


# ============================================================================
# INTERVIEW FORMS (ADMIN)
# ============================================================================

class InterviewForm(forms.ModelForm):
    """
    Form for admin to schedule interviews for applications.
    """
    class Meta:
        model = Interview
        fields = ('interview_type', 'date', 'time', 'venue', 'notes')
        widgets = {
            'interview_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time'
            }),
            'venue': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Interview Venue/Meeting Link'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional Notes (optional)',
                'rows': 3
            })
        }


# ============================================================================
# PLACEMENT RESULT FORMS (ADMIN)
# ============================================================================

