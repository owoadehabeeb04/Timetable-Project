import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'timetable_project.settings')
django.setup()

from timetable.models import Department, Level, Timetable

# Define sample data
departments = ['Computer Science', 'Cyber Security', 'Software Engineering', 'Communication Arts']
levels = ['100', '200', '300', '400']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
courses = {
    'Computer Science': [
        'Introduction to Programming', 'Data Structures', 'Operating Systems', 'Databases', 'Algorithms'
    ],
    'Cyber Security': [
        'Introduction to Cyber Security', 'Network Security', 'Cryptography', 'Ethical Hacking', 'Digital Forensics'
    ],
    'Software Engineering': [
        'Introduction to Software Engineering', 'Software Design Patterns', 'Agile Development', 'Web Development', 'Mobile App Development'
    ],
    'Communication Arts': [
        'Introduction to Communication', 'Mass Media', 'Public Speaking', 'Writing for Media', 'Digital Communication'
    ]
}
lecturers = ['Dr. Smith', 'Prof. Johnson', 'Dr. Adams', 'Dr. Brown', 'Prof. Davis']

# Clear existing data (optional)
Timetable.objects.all().delete()

# Add departments
for dept in departments:
    Department.objects.get_or_create(name=dept)

# Add levels
for lvl in levels:
    Level.objects.get_or_create(level=lvl)

# Populate timetable
for department_name in departments:
    department = Department.objects.get(name=department_name)
    for level_name in levels:
        level = Level.objects.get(level=level_name)
        for day in days:
            # Random number of lectures per day (0 to 3)
            lectures_per_day = random.randint(0, 3)
            for _ in range(lectures_per_day):
                time = f"{random.randint(8, 16):02}:00"  # Random hour between 08:00 and 16:00
                course = random.choice(courses[department_name])
                lecturer = random.choice(lecturers)
                Timetable.objects.create(
                    department=department,
                    level=level,
                    day=day,
                    time=time,
                    course=course,
                    lecturer=lecturer
                )

print("Timetable populated successfully!")
