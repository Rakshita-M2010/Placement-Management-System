# Placement Management System - Complete Implementation

A production-ready Django placement management system with custom admin portal, student portal, and comprehensive role-based access control.

## 🎯 Project Overview

This is a full-stack Django application designed to automate placement process management for educational institutions. It includes:
- **Student Module**: Registration, profile management, job browsing, applications, and interview tracking
- **Admin Module**: Company management, job postings, application tracking, interview scheduling, and placement reports
- **Role-Based Access Control**: Separate authentication for students and admin staff
- **Real-Time Dashboard**: Live statistics and analytics

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 5.0.14 |
| **Database** | MySQL / SQLite |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Authentication** | Django Authentication + Custom Decorators |
| **Python Version** | 3.11+ |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- pip (Python package manager)
- MySQL Server (optional - SQLite works for development)

### Step 1: Clone the Project
```bash
cd PlacementMgmt
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv311
# Windows
venv311\Scripts\activate
# Mac/Linux
source venv311/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

Dependencies include:
- Django 5.0.14
- djangorestframework 3.17.1
- mysqlclient 2.2.8
- python-decouple (for environment variables)

### Step 4: Run Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
# Enter username (use email format)
# Enter email
# Enter password (min 8 characters)
# Confirm password
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Server starts at: `http://localhost:8000/`

---

## 🔐 Authentication & Access Control

### Student Access
- **URL**: `http://localhost:8000/auth/login/`
- **Registration**: `http://localhost:8000/auth/register/`
- Students must create profile before accessing jobs/applications
- Only students can view job listings and apply

### Admin Access
- **URL**: `http://localhost:8000/admin/dashboard/`
- Requires `is_staff=True` and `is_superuser=True` flags
- Admin users are redirected to admin dashboard on login
- Unauthorized users are blocked with error message

### Role-Based Decorators
```python
@admin_required  # Protects admin views
@login_required  # Protects authenticated views
```

---

## 📋 Database Models

### 1. **Student**
```
- user (One-to-One with User)
- roll_number
- branch (CSE, ECE, ME, CE, EE, AE)
- cgpa (0.00 - 10.00)
- phone
- skills (comma-separated)
- graduation_year
- resume (file upload)
- created_at, updated_at
```

### 2. **Company**
```
- company_name
- hr_name
- email
- phone
- package (LPA)
- website
- description
- created_at, updated_at
```

### 3. **Job**
```
- company (Foreign Key)
- job_title
- description
- min_cgpa
- deadline
- job_type (Full-Time, Internship)
- location
- created_at, updated_at
```

### 4. **Application**
```
- student (Foreign Key)
- job (Foreign Key)
- status (Applied, Shortlisted, Interview Scheduled, Selected, Rejected)
- applied_date, updated_at
- Unique constraint: (student, job)
```

### 5. **Interview**
```
- application (One-to-One)
- interview_type (Technical, HR, Group Discussion, Final Round)
- date, time
- venue
- notes
- created_at, updated_at
```

---

## 🎓 Student Module Features

### Dashboard (`/student/dashboard/`)
- View applications count by status
- Quick statistics (shortlisted, interviews, selected)
- Recently applied jobs

### Profile Management (`/student/profile/`)
- Create/Edit profile with:
  - Roll number, branch, CGPA
  - Phone number, skills
  - Resume upload
  - Graduation year
- Changes update immediately

### Job Browsing (`/jobs/`)
- List all active jobs with pagination
- Filter by eligibility (CGPA matching)
- Search functionality
- View detailed job information

### Applications (`/applications/`)
- View all submitted applications
- Track application status in real-time
- See interview schedule when scheduled
- Status updates from admin reflect immediately

### Interview Tracking
- View scheduled interviews with:
  - Date, time, venue
  - Interview type
  - Associated company

---

## 👨‍💼 Admin Module Features

### Dashboard (`/admin/dashboard/`)
- Overview cards:
  - Total students, companies, jobs, applications
  - Placed students count
  - Recent application activity

### Student Management (`/admin/students/`)
- **List Students**: Search by name, email, roll number
- **View Details**: Full student profile with all applications
- **Edit Profile**: Update any student information
- **Delete Student**: Remove student and associated account
- Pagination support

### Company Management (`/admin/companies/`)
- **Add Company**: Create new recruiting company
- **Edit Company**: Update company information
- **Delete Company**: Remove company (cascades to jobs)
- Search by company name or HR name
- Display company details and packages

### Job Management (`/admin/jobs/`)
- **Create Job**: Post new job with all details
- **Edit Job**: Update job information and requirements
- **Delete Job**: Remove job posting
- Auto-display on student jobs page
- Filter by company and deadline

### Application Management (`/admin/applications/`)
- **View All Applications**: Paginated list with search
- **Update Status**: Change application status (Applied → Shortlisted → Interview Scheduled → Selected/Rejected)
- Status changes reflect on student dashboard immediately
- Filter by status and company

### Interview Scheduling (`/admin/interviews/`)
- **Schedule Interview**: Create interview for shortlisted students
- **Edit Interview**: Modify interview details
- **View Schedule**: Complete interview calendar
- Set interview type (Technical, HR, Group, Final)
- Auto-update application status to "Interview Scheduled"

### Placement Reports (`/admin/reports/`)
- **Overall Statistics**:
  - Total students, companies, jobs, applications
  - Placement rate percentage
  - Placed students count
- **Package Information**:
  - Highest package offered
  - Average package across placements
- **Status Distribution**: Pie chart of applications by status
- **Top Companies**: By applications and placements
- **Key Metrics**:
  - Applications per student
  - Jobs per company
  - Unplaced students count

---

## 🛣 URL Routes (Core App)

### Authentication
```
GET/POST    /auth/register/              student_register
GET/POST    /auth/login/                 student_login
POST        /auth/logout/                student_logout
GET/POST    /auth/change-password/       student_change_password
```

### Student Module
```
GET/POST    /student/profile/create/     student_profile_create
GET/POST    /student/profile/            student_profile
GET         /student/dashboard/          student_dashboard
```

### Jobs & Applications
```
GET         /jobs/                       job_list
GET         /jobs/<id>/                  job_detail
POST        /jobs/<id>/apply/            apply_for_job
GET         /applications/               student_applications
```

### Admin Dashboard
```
GET         /admin/dashboard/            admin_dashboard
GET         /admin/reports/              admin_reports
```

### Admin - Students
```
GET         /admin/students/             admin_students
GET         /admin/students/<id>/        admin_student_detail
GET/POST    /admin/students/<id>/edit/   admin_student_edit
POST        /admin/students/<id>/delete/ admin_student_delete
```

### Admin - Companies
```
GET         /admin/companies/            admin_company_list
GET/POST    /admin/companies/create/     admin_company_create
GET/POST    /admin/companies/<id>/edit/  admin_company_edit
POST        /admin/companies/<id>/delete/admin_company_delete
```

### Admin - Jobs
```
GET         /admin/jobs/                 admin_job_list
GET/POST    /admin/jobs/create/          admin_job_create
GET/POST    /admin/jobs/<id>/edit/       admin_job_edit
POST        /admin/jobs/<id>/delete/     admin_job_delete
```

### Admin - Applications
```
GET         /admin/applications/         admin_applications
GET/POST    /admin/applications/<id>/... admin_application_update
```

### Admin - Interviews
```
GET         /admin/interviews/           admin_interviews
GET/POST    /admin/interviews/<id>/...   admin_interview_schedule
GET/POST    /admin/interviews/<id>/edit/ admin_interview_edit
```

---

## 📁 Project Structure

```
PlacementMgmt/
├── core/
│   ├── models.py              # Database models
│   ├── views.py               # All view functions
│   ├── forms.py               # All forms
│   ├── urls.py                # URL routing
│   ├── admin.py               # Django admin config
│   ├── migrations/            # Database migrations
│   ├── static/
│   │   ├── css/style.css
│   │   ├── js/script.js
│   │   └── images/
│   ├── media/resume/          # Uploaded resumes
│   └── templates/
│       ├── base.html          # Student base template
│       ├── admin_base.html    # Admin base template
│       ├── home.html
│       ├── student/
│       │   ├── dashboard.html
│       │   ├── profile.html
│       │   ├── jobs.html
│       │   ├── applications.html
│       │   ├── login.html
│       │   ├── register.html
│       │   └── ...
│       ├── admin_panel/
│       │   ├── dashboard.html
│       │   ├── students.html
│       │   ├── student_detail.html
│       │   ├── company_list.html
│       │   ├── job_list.html
│       │   ├── applications.html
│       │   ├── interviews.html
│       │   ├── reports.html
│       │   └── ...
│       └── ...
├── PlacementMgmt/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py
├── db.sqlite3
└── requirements.txt
```

---

## 🎨 UI/UX Features

### Bootstrap 5 Integration
- Responsive design for mobile, tablet, desktop
- Professional color scheme with gradients
- Icons from Font Awesome 6.4.0

### Admin Dashboard
- Modern dark theme with accent colors
- Cards for statistics
- Tables with hover effects
- Search and filtering
- Pagination support
- Success/error messages

### Student Portal
- Clean, intuitive interface
- Job eligibility indicators
- Application tracking dashboard
- Resume upload with validation
- Real-time status updates

---

## 🔄 Data Flow Examples

### Example 1: Job Application
1. Student logs in
2. Browses available jobs (filtered by CGPA eligibility)
3. Clicks "Apply" button
4. Application created with "Applied" status
5. Appears immediately in student applications list
6. Admin views application in dashboard

### Example 2: Interview Scheduling
1. Admin updates application status to "Shortlisted"
2. Admin schedules interview from applications page
3. Sets interview type, date, time, venue
4. Application status auto-updates to "Interview Scheduled"
5. Student sees interview on their dashboard automatically
6. Interview appears in admin interview list

### Example 3: Student Placement
1. Admin updates application status to "Selected"
2. Student sees "Selected" status on their dashboard
3. Admin views reports - placed students count updates
4. Average/highest package calculated automatically

---

## 🧪 Testing the Application

### Create Test Data
```bash
# Login as admin
python manage.py shell
>>> from core.models import Student, Company, Job
>>> from django.contrib.auth.models import User

# Create a company
>>> Company.objects.create(
...     company_name="Tech Corp",
...     hr_name="John Doe",
...     email="hr@techcorp.com",
...     phone="9876543210",
...     package=12.5
... )

# Create a job
>>> Job.objects.create(
...     company_id=1,
...     job_title="Software Engineer",
...     description="3+ years experience required",
...     min_cgpa=7.0,
...     deadline="2025-12-31",
...     location="Bangalore"
... )
```

### Student Test Flow
1. Go to `/auth/register/` and create account
2. Complete profile at `/student/profile/create/`
3. Browse jobs at `/jobs/`
4. Apply for eligible jobs
5. View applications at `/applications/`

### Admin Test Flow
1. Login with superuser credentials
2. Visit `/admin/dashboard/`
3. Manage students at `/admin/students/`
4. Manage companies at `/admin/companies/`
5. Post jobs at `/admin/jobs/create/`
6. Update applications at `/admin/applications/`
7. Schedule interviews at `/admin/interviews/`
8. View reports at `/admin/reports/`

---

## 🚀 Deployment Checklist

- [ ] Set `DEBUG = False` in settings.py
- [ ] Configure `ALLOWED_HOSTS` in settings.py
- [ ] Use MySQL database instead of SQLite
- [ ] Set secure `SECRET_KEY`
- [ ] Configure `STATIC_ROOT` and `MEDIA_ROOT`
- [ ] Run `python manage.py collectstatic`
- [ ] Set up environment variables
- [ ] Configure email backend for notifications
- [ ] Enable HTTPS
- [ ] Set up backup strategy

---

## 📝 Notes

### Key Design Decisions
1. **One-to-One Student-User**: Allows extending Django's User model
2. **Admin Decorator Pattern**: Reusable authentication checks
3. **Status-Based Flow**: Clear application lifecycle
4. **Real-Time Updates**: Changes immediately visible to students
5. **Cascading Deletes**: Removing company removes related jobs

### Performance Optimizations
- Pagination for large datasets
- Database indexes on frequently queried fields
- Efficient SQL queries with select_related/prefetch_related
- Search using icontains for flexibility

### Security Features
- CSRF protection on all forms
- SQL injection prevention via ORM
- Password hashing with Django auth
- Login required decorators on protected views
- File upload validation

---

## 🤝 Contributing

For improvements:
1. Test thoroughly before deploying
2. Follow Django best practices
3. Document any new features
4. Maintain existing code style

---

## 📞 Support & Documentation

- Django Documentation: https://docs.djangoproject.com/
- Bootstrap Documentation: https://getbootstrap.com/docs/5.0/
- Font Awesome Icons: https://fontawesome.com/icons

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Last Updated**: June 2026  
**Version**: 1.0.0  
**Status**: Production Ready ✅
