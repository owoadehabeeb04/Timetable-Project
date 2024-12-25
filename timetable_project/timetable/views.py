from django.shortcuts import render
from .forms import TimetableForm
from .models import Timetable, Department, Level
from datetime import date

from django.shortcuts import render, redirect

def landing_page(request):
    # Render the landing page
    return render(request, 'timetable/landing.html')


def timetable_view(request):
    # Default values for department and level
    department_name = request.GET.get('department', 'Computer Science')  # Default department
    level_name = request.GET.get('level', '100')  # Default level

    # Fetch department and level from the database
    department = Department.objects.get(name=department_name)
    level = Level.objects.get(level=level_name)
    timetable_entries = Timetable.objects.filter(department=department, level=level)

    # Structure timetable by day and time slots
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    time_slots = ['8:00-10:00', '10:00-12:00', '12:00-2:00', '2:00-4:00', '4:00-6:00']
    timetable = {day: [None] * len(time_slots) for day in days}

    for entry in timetable_entries:
        time_index = time_slots.index(entry.time) if entry.time in time_slots else None
        if time_index is not None:
            timetable[entry.day][time_index] = {
                'course': entry.course,
                'lecturer': entry.lecturer,
                'venue': entry.venue if hasattr(entry, 'venue') else "N/A"
            }

    # Handle POST request for the form submission
    if request.method == "POST":
        form = TimetableForm(request.POST)
        if form.is_valid():
            department = form.cleaned_data['department']
            level = form.cleaned_data['level']
            timetables = Timetable.objects.filter(department=department, level=level)
            return render(request, 'timetable/result.html', {'timetables': timetables})
    else:
        form = TimetableForm()

    # Context for rendering the timetable page
    context = {
        'department': department_name,
        'level': level_name,
        'current_date': date.today().strftime('%d %B, %Y'),
        'timetable': timetable,
        'form': form,
    }

    return render(request, 'timetable/home.html', context)
