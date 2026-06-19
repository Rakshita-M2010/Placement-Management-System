# 🚀 QUICK START GUIDE - Placement Management System

## Getting Started in 5 Minutes

### Step 1: Start the Server ✅
```bash
cd PlacementMgmt
python manage.py runserver
```

Server runs at: **http://127.0.0.1:8000/**

### Step 2: Create Admin User
```bash
python manage.py createsuperuser
```

Enter:
- **Username**: admin (or your email)
- **Email**: admin@example.com
- **Password**: (secure password)

### Step 3: Access the System

#### 👤 Student Portal
- **Register**: http://127.0.0.1:8000/auth/register/
- **Login**: http://127.0.0.1:8000/auth/login/
- **Home**: http://127.0.0.1:8000/

#### 👨‍💼 Admin Portal
- **Login** (use superuser credentials): http://127.0.0.1:8000/auth/login/
- **Dashboard**: http://127.0.0.1:8000/admin/dashboard/ (auto-redirect)

---

## 📋 TEST WORKFLOWS

### 🎓 Student Workflow (5 minutes)
```
1. Go to /auth/register/
   └─ Fill: First Name, Last Name, Email, Password
   
2. Create Profile at /student/profile/create/
   └─ Fill: Roll Number, Branch, CGPA, Phone, Skills, Resume
   
3. Browse Jobs at /jobs/
   └─ See eligible jobs (CGPA matched automatically)
   
4. Apply for Job
   └─ Click "Apply" on any eligible job
   └─ See application in /applications/
   
5. Track Status at /applications/
   └─ Watch status change from admin panel
   
6. View Dashboard at /student/dashboard/
   └─ See stats: Applications, Shortlisted, Interviews, Selected
```

### 🔧 Admin Workflow (10 minutes)
```
1. Login with superuser credentials
   └─ Auto-redirects to /admin/dashboard/
   
2. Manage Students at /admin/students/
   └─ Search students by name/email/roll number
   └─ View student details with applications
   └─ Edit student profile or delete
   
3. Create Company at /admin/companies/create/
   └─ Fill: Company Name, HR Name, Email, Phone, Package
   
4. Post Job at /admin/jobs/create/
   └─ Select company, enter job title, min CGPA, deadline
   └─ Job appears on student jobs list immediately
   
5. Manage Applications at /admin/applications/
   └─ Filter by status
   └─ Click "Update Status" to change (Applied → Shortlisted...)
   └─ Status updates on student dashboard in real-time
   
6. Schedule Interview at /admin/interviews/
   └─ Select shortlisted application
   └─ Enter date, time, venue, type
   └─ Interview appears on student dashboard
   └─ Application auto-updates to "Interview Scheduled"
   
7. View Reports at /admin/reports/
   └─ See placement statistics
   └─ View highest package, average package
   └─ See company rankings by placements
```

---

## 📍 KEY PAGES & FEATURES

### Student Pages
| URL | Feature |
|-----|---------|
| `/` | Home page with overview |
| `/auth/register/` | Student registration |
| `/auth/login/` | Student login |
| `/student/profile/create/` | Create initial profile |
| `/student/profile/` | View/edit profile |
| `/student/dashboard/` | Application statistics |
| `/jobs/` | Browse available jobs |
| `/jobs/<id>/` | Job details with apply button |
| `/applications/` | Track applications & status |
| `/auth/change-password/` | Change password |

### Admin Pages
| URL | Feature |
|-----|---------|
| `/admin/dashboard/` | Admin overview |
| `/admin/students/` | Manage students (search/edit/delete) |
| `/admin/students/<id>/` | Student details & applications |
| `/admin/companies/` | Manage companies |
| `/admin/companies/create/` | Add new company |
| `/admin/jobs/` | Manage jobs |
| `/admin/jobs/create/` | Post new job |
| `/admin/applications/` | View applications (filter by status) |
| `/admin/interviews/` | Schedule/manage interviews |
| `/admin/reports/` | Placement analytics & reports |

---

## 🎨 What You Can Test

### Real-Time Features
1. **Post a job as admin** → Appears instantly on student jobs page
2. **Apply for job as student** → Appears in student applications
3. **Update status to "Shortlisted"** → Status updates on student dashboard
4. **Schedule interview** → Student sees interview with time & venue
5. **Mark as "Selected"** → Placement count increases in reports

### Search & Filter
1. **Search students** by name/email/roll number
2. **Filter applications** by status (Applied, Shortlisted, etc.)
3. **Search companies** by name or HR
4. **Filter jobs** by deadline

### Statistics
1. **Total students, companies, jobs, applications** on dashboard
2. **Placement percentage** in reports
3. **Highest/average package** in reports
4. **Company rankings** by applications and placements

### User Management
1. **Create student account** with profile
2. **Edit student details** (CGPA, skills, resume)
3. **Delete student** (account removed)
4. **Change password** for any user

---

## 🔑 Key Features to Demonstrate

### ✅ Authentication
- Email-based student login
- Admin auto-redirect (staff users)
- Permission checking
- Profile requirement

### ✅ Profile Management
- Complete student profile creation
- Resume upload
- Skills entry
- CGPA and eligibility tracking

### ✅ Job Management
- Browse jobs with eligibility indication
- CGPA-based filtering
- Application submission
- Duplicate application prevention

### ✅ Real-Time Dashboard
- Application count by status
- Interview schedule
- Placement results
- Automatic updates from admin

### ✅ Admin Controls
- Full student/company/job CRUD
- Application status workflow
- Interview scheduling
- Comprehensive reports

### ✅ Reports & Analytics
- Placement statistics
- Package information
- Company performance
- Key performance indicators

---

## 🐛 Test Cases

### Student Registration
```
✓ Create account with valid email
✓ Password confirmation required
✓ Duplicate email rejected
✓ Profile creation required
```

### Job Application
```
✓ Apply for eligible job (CGPA >= requirement)
✓ Cannot apply if ineligible
✓ Cannot apply twice to same job
✓ Application appears in my applications
```

### Admin Management
```
✓ Delete company cascades to jobs
✓ Delete student cascades to applications
✓ Update application status updates student dashboard
✓ Schedule interview auto-updates status
```

### Real-Time Updates
```
✓ New job post visible to students
✓ Application status change visible immediately
✓ Interview schedule visible to student
✓ Placement marked as "Selected" updates reports
```

---

## 🎯 Demo Script (15 minutes)

1. **Open home page** (0:00)
   - Show statistics cards
   - Show key features list
   
2. **Register student** (2:00)
   - Go to /auth/register/
   - Fill registration form
   - Create profile with skills and resume
   
3. **Create admin account** (5:00)
   - Terminal: python manage.py createsuperuser
   - Or use existing superuser
   
4. **Post job as admin** (7:00)
   - Login with admin credentials
   - Go to /admin/jobs/create/
   - Create a job from a company
   
5. **Apply for job as student** (9:00)
   - Login as student (new browser tab)
   - Go to /jobs/
   - Apply for the posted job
   
6. **Update status as admin** (11:00)
   - Go to /admin/applications/
   - Update application to "Shortlisted"
   - Show status update on student applications
   
7. **Schedule interview** (13:00)
   - Schedule interview for application
   - Set date, time, venue
   - Show interview on student dashboard
   
8. **View reports** (15:00)
   - Go to /admin/reports/
   - Show placement statistics
   - Show company rankings

---

## 📱 Mobile Testing

The system is **fully responsive** on:
- Desktop (1920x1080)
- Tablet (768x1024)
- Mobile (375x667)

Test on mobile by:
1. Open http://127.0.0.1:8000/ on phone/tablet
2. Test responsive menu (hamburger)
3. Test touch-friendly buttons
4. Test responsive tables

---

## ⚙️ Troubleshooting

### Page not found (404)
- Ensure Django server is running
- Check URL spelling
- Verify migrations applied

### "Permission denied" on admin page
- Make sure user is marked as staff
- Check superuser flag
- Logout and login again

### Resume won't upload
- Check file format (PDF, DOC, DOCX only)
- Check file size
- Check media directory permissions

### Real-time updates not showing
- Refresh page (F5)
- Check database was updated
- Check no cache issues (Ctrl+Shift+R)

### Search not working
- Check search form submission
- Verify URL parameters (?search=...)
- Check case-insensitive queries working

---

## 📞 Support

### Documentation
- `README.md` - Full project documentation
- `IMPLEMENTATION_SUMMARY.md` - Technical details
- Django Docs: https://docs.djangoproject.com/

### Quick Commands
```bash
# Run server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access database
python manage.py shell

# Clear cache
python manage.py clear_cache
```

---

## ✅ Verification Checklist

Use this checklist when testing:

- [ ] Home page loads with statistics
- [ ] Student registration works
- [ ] Student login works
- [ ] Profile creation required
- [ ] Job browsing shows eligible jobs
- [ ] Job application works
- [ ] Applications list shows status
- [ ] Admin login redirects to dashboard
- [ ] Admin can view students
- [ ] Admin can create company
- [ ] Admin can post job
- [ ] Job appears on student page
- [ ] Admin can update application status
- [ ] Status updates on student dashboard
- [ ] Admin can schedule interview
- [ ] Interview visible to student
- [ ] Reports page shows statistics
- [ ] Pagination works
- [ ] Search functionality works
- [ ] Responsive design works

---

**Ready to test!** 🎉

Start with Step 1 above and follow the workflows.  
All features are fully functional and production-ready.
