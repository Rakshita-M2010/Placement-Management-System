from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Student, Company, Job, Application, Interview
from datetime import datetime, timedelta
import random
from decimal import Decimal

class Command(BaseCommand):
    help = 'Seed the database with realistic demo data for the Placement Management System'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('🔄 Starting data seed process...'))
        
        # Clear existing demo data
        self.clear_data()
        
        # Create students
        students = self.create_students()
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(students)} students'))
        
        # Create companies
        companies = self.create_companies()
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(companies)} companies'))
        
        # Create jobs
        jobs = self.create_jobs(companies)
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(jobs)} jobs'))
        
        # Create applications
        applications = self.create_applications(students, jobs)
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(applications)} applications'))
        
        # Create interviews
        interviews = self.create_interviews(applications)
        self.stdout.write(self.style.SUCCESS(f'✅ Created {len(interviews)} interviews'))
        
        self.stdout.write(self.style.SUCCESS('\n✨ Data seeding completed successfully!'))
        
        # Print statistics
        self.print_statistics()

    def clear_data(self):
        """Clear existing demo data"""
        self.stdout.write(self.style.WARNING('🗑️  Clearing existing demo data...'))
        Interview.objects.all().delete()
        Application.objects.all().delete()
        Job.objects.all().delete()
        Company.objects.all().delete()
        Student.objects.all().delete()
        User.objects.all().delete()

    def create_students(self):
        """Create 120 realistic students"""
        students = []
        branches = ['CSE', 'ECE', 'ME', 'CE', 'EE', 'AE']
        
        first_names = [
            'Rajesh', 'Priya', 'Amit', 'Neha', 'Vikram', 'Sneha', 'Arjun', 'Pooja',
            'Sanjay', 'Divya', 'Rahul', 'Anjali', 'Abhishek', 'Isha', 'Nikhil', 'Shreya',
            'Rohan', 'Aisha', 'Deepak', 'Rani', 'Karan', 'Meera', 'Suresh', 'Simran',
            'Aditya', 'Vaishali', 'Manish', 'Priyanka', 'Harshit', 'Sakshi', 'Ravi', 'Diya',
            'Akshay', 'Nisha', 'Varun', 'Komal', 'Harsh', 'Richa', 'Naveen', 'Shruti',
            'Gaurav', 'Alina', 'Siddharth', 'Megha', 'Mayank', 'Kavya', 'Shiva', 'Anaya'
        ]
        
        last_names = [
            'Sharma', 'Patel', 'Singh', 'Kumar', 'Gupta', 'Verma', 'Nair', 'Reddy',
            'Rao', 'Bhat', 'Joshi', 'Iyer', 'Chopra', 'Bansal', 'Kapoor', 'Malhotra',
            'Saxena', 'Agarwal', 'Desai', 'Pandey', 'Yadav', 'Mishra', 'Chatterjee',
            'Bhattacharya', 'Dasgupta', 'Mukherjee', 'Das', 'Roy', 'Dutta', 'Bose'
        ]
        
        graduation_years = [2024, 2025, 2026]
        used_emails = set()  # Track used emails to avoid duplicates
        
        for i in range(120):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            branch = random.choice(branches)
            roll_number = f"{branch}{i+1:03d}"
            cgpa = round(random.uniform(6.0, 10.0), 2)
            graduation_year = random.choice(graduation_years)
            
            # Create user credentials based on student name
            # Email: firstname+lastname (lowercase)@university.edu
            base_email = f"{first_name.lower()}{last_name.lower()}@university.edu"
            email = base_email
            counter = 1
            
            # If email already used, add a counter
            while email in used_emails:
                email = f"{first_name.lower()}{last_name.lower()}{counter}@university.edu"
                counter += 1
            
            used_emails.add(email)
            username = email  # Username is email for authentication
            # Password: FirstnameLast@123
            password = f"{first_name}{last_name}@123"
            
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            
            # Create student profile
            skills_list = [
                'Python', 'Java', 'C++', 'JavaScript', 'SQL', 'Django', 'React',
                'Data Structures', 'DBMS', 'OOP', 'Web Development', 'Problem Solving',
                'Communication', 'Team Work', 'Leadership', 'Machine Learning',
                'Cloud Computing', 'DevOps', 'Testing', 'Project Management'
            ]
            
            skills = ', '.join(random.sample(skills_list, random.randint(3, 7)))
            phone = f"9{random.randint(100000000, 999999999)}"
            
            student = Student.objects.create(
                user=user,
                roll_number=roll_number,
                branch=branch,
                cgpa=Decimal(str(cgpa)),
                phone=phone,
                skills=skills,
                graduation_year=graduation_year
            )
            students.append(student)
        
        return students

    def create_companies(self):
        """Create 20 realistic companies"""
        companies = []
        
        company_data = [
            ('Infosys', 'Rahul Sharma', 'hr@infosys.com', '8.50', 'https://www.infosys.com'),
            ('TCS', 'Priya Mehta', 'hr@tcs.com', '7.20', 'https://www.tcs.com'),
            ('Wipro', 'Ajay Verma', 'hr@wipro.com', '6.80', 'https://www.wipro.com'),
            ('Accenture', 'Rohit Singh', 'hr@accenture.com', '7.80', 'https://www.accenture.com'),
            ('Capgemini', 'Neha Kapoor', 'hr@capgemini.com', '6.50', 'https://www.capgemini.com'),
            ('Microsoft', 'Omega Johnson', 'omega@microsoft.com', '12.00', 'https://www.microsoft.com'),
            ('Google', 'Priyanka Gupta', 'hr@google.com', '15.00', 'https://www.google.com'),
            ('Amazon', 'Amar Patel', 'hr@amazon.com', '13.50', 'https://www.amazon.com'),
            ('Apple', 'Sarah Chen', 'hr@apple.com', '18.00', 'https://www.apple.com'),
            ('IBM', 'David Kumar', 'hr@ibm.com', '7.00', 'https://www.ibm.com'),
            ('Oracle', 'Emma Wilson', 'hr@oracle.com', '9.50', 'https://www.oracle.com'),
            ('Cisco', 'James Smith', 'hr@cisco.com', '8.75', 'https://www.cisco.com'),
            ('HCL Technologies', 'Anjali Singh', 'hr@hcl.com', '6.00', 'https://www.hcltech.com'),
            ('Tech Mahindra', 'Vivek Reddy', 'hr@techmahindra.com', '6.25', 'https://www.techmahindra.com'),
            ('Cognizant', 'Madhavi Nair', 'hr@cognizant.com', '6.75', 'https://www.cognizant.com'),
            ('PayPal', 'Ryan Garcia', 'hr@paypal.com', '14.00', 'https://www.paypal.com'),
            ('Uber', 'Lisa Anderson', 'hr@uber.com', '13.00', 'https://www.uber.com'),
            ('Flipkart', 'Ankit Joshi', 'hr@flipkart.com', '9.00', 'https://www.flipkart.com'),
            ('Swiggy', 'Deepali Verma', 'hr@swiggy.com', '7.50', 'https://www.swiggy.com'),
            ('Spotify', 'Alex Turner', 'hr@spotify.com', '16.00', 'https://www.spotify.com'),
        ]
        
        for name, hr_name, email, package, website in company_data:
            company = Company.objects.create(
                company_name=name,
                hr_name=hr_name,
                email=email,
                phone=f"91{random.randint(9000000000, 9999999999)}",
                package=Decimal(package),
                website=website,
                description=f"{name} is a leading technology company known for innovation and excellence."
            )
            companies.append(company)
        
        return companies

    def create_jobs(self, companies):
        """Create 40 jobs across companies"""
        jobs = []
        job_titles = [
            'Software Engineer', 'Senior Software Engineer', 'Junior Developer',
            'Full Stack Developer', 'Frontend Developer', 'Backend Developer',
            'Data Scientist', 'Data Analyst', 'DevOps Engineer', 'Cloud Architect',
            'Product Manager', 'QA Engineer', 'Business Analyst', 'UI/UX Designer',
            'Systems Engineer', 'Network Engineer', 'Database Administrator',
            'Machine Learning Engineer', 'Security Engineer', 'Solutions Architect'
        ]
        
        locations = [
            'Bangalore', 'Hyderabad', 'Pune', 'Mumbai', 'Delhi', 'Chennai',
            'Gurgaon', 'Noida', 'Cochin', 'Bhubaneswar'
        ]
        
        deadline_base = datetime.now().date()
        
        for i, company in enumerate(companies * 2):  # 40 jobs total
            job_title = random.choice(job_titles)
            min_cgpa = round(random.uniform(6.0, 7.5), 2)
            deadline = deadline_base + timedelta(days=random.randint(30, 120))
            location = random.choice(locations)
            
            job = Job.objects.create(
                company=company,
                job_title=job_title,
                description=f"We are looking for a talented {job_title} to join our team at {company.company_name}. "
                           f"Responsibilities include developing and maintaining software systems, "
                           f"collaborating with team members, and contributing to innovative solutions.",
                min_cgpa=Decimal(str(min_cgpa)),
                deadline=deadline,
                job_type=random.choice(['Full-Time', 'Internship']),
                location=location
            )
            jobs.append(job)
        
        return jobs

    def create_applications(self, students, jobs):
        """Create 350 realistic applications with proper status distribution"""
        applications = []
        placed_students = set()
        interview_types = ['Technical', 'HR', 'Group Discussion', 'Final Round']
        
        # Ensure at least 50 students are placed
        students_to_place = random.sample(students, 50)
        
        for i in range(350):
            student = random.choice(students)
            job = random.choice(jobs)
            
            # Check for duplicate application
            existing_app = Application.objects.filter(student=student, job=job).exists()
            if existing_app:
                continue
            
            # Determine status with realistic distribution
            if student in students_to_place and len(placed_students) < 50:
                # This student should be placed
                status = 'Selected'
                placed_students.add(student)
            else:
                # Random status for other students
                status_choices = ['Applied', 'Shortlisted', 'Interview Scheduled', 'Selected', 'Rejected']
                weights = [30, 25, 20, 15, 10]  # Realistic distribution
                status = random.choices(status_choices, weights=weights)[0]
            
            applied_date = datetime.now() - timedelta(days=random.randint(1, 120))
            
            application = Application.objects.create(
                student=student,
                job=job,
                status=status,
                applied_date=applied_date
            )
            applications.append(application)
        
        return applications

    def create_interviews(self, applications):
        """Create 80 interviews for shortlisted/interview scheduled applications"""
        interviews = []
        interview_types = ['Technical', 'HR', 'Group Discussion', 'Final Round']
        venues = [
            'Conference Room A', 'Conference Room B', 'Board Room', 'Virtual Meeting',
            'Office Building - Floor 3', 'Training Center', 'HR Department', 'Meeting Hall'
        ]
        
        # Filter applications that should have interviews
        interview_eligible = [
            app for app in applications 
            if app.status in ['Shortlisted', 'Interview Scheduled', 'Selected']
        ]
        
        # Create 80 interviews
        interview_eligible = random.sample(interview_eligible, min(80, len(interview_eligible)))
        
        for application in interview_eligible:
            interview_date = application.applied_date.date() + timedelta(days=random.randint(7, 60))
            interview_time = datetime.strptime(f"{random.choice(range(9, 17))}:{random.choice([0, 30]):02d}", "%H:%M").time()
            
            interview = Interview.objects.create(
                application=application,
                interview_type=random.choice(interview_types),
                date=interview_date,
                time=interview_time,
                venue=random.choice(venues),
                notes=random.choice([
                    'Good communication skills',
                    'Strong technical knowledge',
                    'Problem solving ability demonstrated',
                    'Team work oriented',
                    'Leadership qualities shown',
                    ''
                ])
            )
            interviews.append(interview)
        
        return interviews

    def print_statistics(self):
        """Print database statistics"""
        self.stdout.write(self.style.SUCCESS('\n📊 Database Statistics:'))
        self.stdout.write(f'  • Total Students: {Student.objects.count()}')
        self.stdout.write(f'  • Total Companies: {Company.objects.count()}')
        self.stdout.write(f'  • Total Jobs: {Job.objects.count()}')
        self.stdout.write(f'  • Total Applications: {Application.objects.count()}')
        self.stdout.write(f'  • Total Interviews: {Interview.objects.count()}')
        
        placed_count = Application.objects.filter(status='Selected').count()
        total_students = Student.objects.count()
        placement_percentage = (placed_count / total_students * 100) if total_students > 0 else 0
        
        self.stdout.write(f'  • Placed Students: {placed_count}')
        self.stdout.write(f'  • Placement %: {placement_percentage:.2f}%')
        
        avg_package = Company.objects.values_list('package', flat=True)
        if avg_package:
            avg = sum(avg_package) / len(avg_package)
            max_pkg = max(avg_package)
            min_pkg = min(avg_package)
            self.stdout.write(f'  • Average Package: {avg:.2f} LPA')
            self.stdout.write(f'  • Highest Package: {max_pkg:.2f} LPA')
            self.stdout.write(f'  • Lowest Package: {min_pkg:.2f} LPA')
