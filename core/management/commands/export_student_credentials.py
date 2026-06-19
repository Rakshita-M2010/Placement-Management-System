from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import csv
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Export all student credentials to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='student_credentials.csv',
            help='Output file name (default: student_credentials.csv)'
        )

    def handle(self, *args, **options):
        output_file = options['output']
        
        # Get all student users (non-staff)
        students = User.objects.filter(is_staff=False).order_by('username')
        
        if not students.exists():
            self.stdout.write(self.style.ERROR('❌ No students found in the database.'))
            return
        
        # Create the file in the project root
        file_path = output_file
        
        try:
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['S.No', 'Username/Email', 'Email', 'Password', 'Full Name']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for idx, student in enumerate(students, 1):
                    writer.writerow({
                        'S.No': idx,
                        'Username/Email': student.username,
                        'Email': student.email,
                        'Password': f"{student.first_name}{student.last_name}@123",
                        'Full Name': student.get_full_name() or student.username
                    })
            
            file_size = os.path.getsize(file_path)
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Successfully exported {students.count()} student credentials to "{file_path}"'
                )
            )
            self.stdout.write(self.style.SUCCESS(f'📊 File size: {file_size} bytes'))
            self.stdout.write(self.style.WARNING('\n⚠️  WARNING: Keep this file secure as it contains login credentials!'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error creating file: {str(e)}'))
