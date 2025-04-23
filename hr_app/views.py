from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from .forms import HiringDataForm, LoginForm
from .models import HiringData

import openpyxl
import requests
import json
from datetime import datetime

def view_all_data(request):
    form_entries = HiringData.objects.all()
    return render(request, 'view_data.html', {'form_entries': form_entries})

def export_to_excel(request):
    # Create an Excel workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Hiring Data"

    # Add headers to the Excel sheet
    headers = ['S.No','Department','Vacancy Title','Recruiter','Source','Location','Place of Posting','Number of Hires','Grade','Type of Hire','Date Request was Received','Date of Deltek Post','Date when Round1 CVs sent','Date of first Revert','Date of Candidate Finalization','Number of CVs given','Number of CVs shared','Number of CVs shortlisted','Number of Candidates Interviewed','Number of Candidates in Final Round','Number of offer letters','Status', 'Comments']
    ws.append(headers)

    # Add data rows
    form_entries = HiringData.objects.all()
    for entry in form_entries:
        ws.append([
                entry.id,
                entry.department,
                entry.vacancy_title,
                entry.recruiter,
                entry.source,
                entry.location,
                entry.place_of_posting,
                entry.no_of_vacancies,
                entry.grade,
                entry.type_hire,
                entry.date_req_received,
                entry.date_deltek_post,
                entry.date_round1_cvsent,
                entry.date_revert1,
                entry.date_candidate_finalised,
                entry.cv_given,
                entry.cv_shared,
                entry.cv_shortlisted,
                entry.candidates_interviewed,
                entry.candidates_finalround,
                entry.no_of_offers,
                entry.status,
                entry.comments
        ])

    # Prepare the response
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=tracker_data.xlsx'
    wb.save(response)
    return response

# Hiring Form View

def update_indent(request, indent_no):
     # Fetch the existing data based on the unique indent_no
    indent = get_object_or_404(HiringData, indent_no=indent_no)

    # If the form is submitted with updated data
    if request.method == 'POST':
        form = HiringDataForm(request.POST, instance=indent)
        
        if form.is_valid():
            form.save()  # Save the updated data
            return redirect('recruiter')  # Redirect to recruiter page (change to appropriate success page)
    
    else:
        # If not POST, create form with the existing data
        form = HiringDataForm(instance=indent)

    return render(request, 'update_indent.html', {'form': form, 'indent_no': indent_no})

def update_indent_redirect(request):
    indent_no = request.GET.get('indent_no')  # Get the entered indent number
    if indent_no:
        return redirect('update_indent', indent_no=indent_no)  # Redirect to the update page
    else:
        return redirect('recruiter') 
    
def update_indent2(request, indent_no):   # for the independent one
     # Fetch the existing data based on the unique indent_no
    indent = get_object_or_404(HiringData, indent_no=indent_no)


    # If the form is submitted with updated data
    if request.method == 'POST':
        form = HiringDataForm(request.POST, instance=indent)
        
        if form.is_valid():
            form.save()  # Save the updated data
            return redirect('recruiter_dashboard')  # Redirect to recruiter page (change to appropriate success page)
    
    else:
        # If not POST, create form with the existing data
        form = HiringDataForm(instance=indent)

    return render(request, 'update_indent2.html', {'form': form, 'indent_no': indent_no})

def update_independent(request):
    indent_no = request.GET.get('indent_no')  # Get the entered indent number
    
    if indent_no:
        return redirect('update_indent2', indent_no=indent_no)  # Redirect to the update page
    else:
        return render(request, 'update_independent.html')  # Show the input form if no indent_no


# View for the hiring form (already created)
def hiring_form_view(request):
    if request.method == 'POST':
        form = HiringDataForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = HiringDataForm()
    
    return render(request, 'hiring_form.html', {'form': form})

# Login 
from django.shortcuts import render, redirect
import pandas as pd
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Get user input
        input_name = request.POST.get('Name')
        input_emp_id = request.POST.get('Emp_ID')
        input_department = request.POST.get('Department')
        
        # Read Excel file
        excel_path = 'excel_data/credentials.xlsx'
        df1 = pd.read_excel(excel_path)
        
        # Check if the input matches any row in the Excel file
        valid_user = df1[
            (df1['Name'] == input_name) &
            (df1['Emp_ID'] == int(input_emp_id)) &
            (df1['Department'] == input_department)
        ]

        if not valid_user.empty:
            # Successful login
            return redirect('recruiter')
        else:
            # Invalid credentials
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')
# Recruiter dashboard view

def recruiter_dashboard(request):
    departments = HiringData.objects.exclude(department__isnull=True).values_list('department', flat=True).distinct()
    return render(request, "recruiter_dashboard.html", {"departments": departments})
    
# Success View
def success_view(request):
    return render(request, 'success.html')

def homepage(request):
    return render(request, 'homepage.html')

# Recruiter view (Placeholder)
def recruiter(request):
    return render(request, 'recruiter.html')

# Business Stakeholder view (Placeholder)
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HiringData

"""def business_stakeholder_login(request): 
    if request.method == 'POST':
        # Read inputs
        name = request.POST.get('Name', '').strip().lower()
        emp_id = request.POST.get('Emp_ID', '').strip()
        department = request.POST.get('Department', '').strip().lower()

        # Validate Employee ID
        try:
            emp_id = int(emp_id)
        except ValueError:
            messages.error(request, 'Invalid Employee ID format.')
            return render(request, 'business_stakeholder.html')

        # Read Excel file
        df = pd.read_excel('excel_data/credentials_business.xlsx')

        # Check credentials
        if not df[(df['Name'].str.lower() == name) & (df['Emp_ID'] == emp_id) & (df['Department'].str.lower() == department)].empty:
            request.session['department'] = department  # Store session data
            return render(request,'business_dashboard.html')  # Redirect to dashboard
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'business_stakeholder.html')"""

from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd

def business_stakeholder_login(request):
    if request.method == 'POST':
        # Get user input
        input_name = request.POST.get('Name', '').strip().lower()
        input_emp_id = request.POST.get('Emp_ID', '').strip()
        input_department = request.POST.get('Department', '').strip().lower()

        # Read Excel file
        excel_path = 'excel_data/credentials_business.xlsx'
        df1 = pd.read_excel(excel_path)

        # Validate user credentials
        valid_user = df1[
            (df1['Name'].str.lower() == input_name) & 
            (df1['Emp_ID'] == int(input_emp_id)) & 
            (df1['Department'].str.lower() == input_department)
        ]

        if not valid_user.empty:
            # Store department in session
            request.session['department'] = input_department  
            return redirect('business_dashboard')  # Ensure this name matches your URL pattern

        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'business_stakeholder.html')  # Show login page if GET request or invalid login


"""def business_dashboard(request):
    department = request.session.get('department')
    if not department:
        return redirect('business_stakeholder_login')
    
    # Fetch hiring data
    hiring_data = list(HiringData.objects.filter(department=department).values())

    return render(request, "business_dashboard.html", {"hiring_data": hiring_data, "department": department})"""

def business_dashboard(request):
    department = request.session.get('department')

    if not department:
        return redirect('business_stakeholder_login')  # Redirect to login if not authenticated

    hiring_data = HiringData.objects.filter(department=department)
    
    return render(request, "business_dashboard.html", {"department": department, "hiring_data": hiring_data})

# Dashboards
# Recruiter

def delete_record(request, vacancy_title):
    HiringData.objects.filter(vacancy_title=vacancy_title).delete()
    return redirect('homepage')

from django.http import JsonResponse
def hiring_data_api(request, department=None):
    if department:
        data = HiringData.objects.filter(department=department).values()
    else:
        data = HiringData.objects.all().values()
    
    return JsonResponse(list(data), safe=False)


# HR Metrics
from django.http import JsonResponse
from django.db.models import Sum, Count, Avg, F, ExpressionWrapper, fields
from .models import HiringData  # Assuming this is your model

"""def hr_metrics(request):
    total_hires = HiringData.objects.aggregate(total_hires=Sum("no_of_hires"))["total_hires"] or 0
    total_offers = HiringData.objects.aggregate(total_offers=Sum("no_of_offers"))["total_offers"] or 0

    hiring_success_rate = (total_hires / total_offers) * 100 if total_offers > 0 else 0

    # Average time to hire (date_req_received → date_candidate_finalised)
    avg_time_to_hire = HiringData.objects.exclude(date_candidate_finalised=None).annotate(
        hiring_days=ExpressionWrapper(
            F("date_candidate_finalised") - F("date_req_received"),
            output_field=fields.DurationField()
        )
    ).aggregate(avg_days=Avg("hiring_days"))["avg_days"]

    avg_time_to_hire = avg_time_to_hire.days if avg_time_to_hire else 0  # Convert timedelta to days

    # Offer Acceptance Rate
    offer_acceptance_rate = (total_hires / total_offers) * 100 if total_offers > 0 else 0

    # Conversion Rates
    cv_given = HiringData.objects.aggregate(total=Sum("cv_given"))["total"] or 0
    cv_shared = HiringData.objects.aggregate(total=Sum("cv_shared"))["total"] or 0
    cv_shortlisted = HiringData.objects.aggregate(total=Sum("cv_shortlisted"))["total"] or 0
    interviewed = HiringData.objects.aggregate(total=Sum("candidates_interviewed"))["total"] or 0
    final_round = HiringData.objects.aggregate(total=Sum("candidates_finalround"))["total"] or 0

    return JsonResponse({
        "total_hires": total_hires,
        "total_offers": total_offers,
        "hiring_success_rate": round(hiring_success_rate, 2),
        "avg_time_to_hire": avg_time_to_hire,
        "offer_acceptance_rate": round(offer_acceptance_rate, 2),
        "cv_given": cv_given,
        "cv_shared": cv_shared,
        "cv_shortlisted": cv_shortlisted,
        "interviewed": interviewed,
        "final_round": final_round,
    })

def hr_metrics_page(request):
    return render(request, "hr_metrics.html")

"""

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Avg, ExpressionWrapper, F, fields
from .models import HiringData

from django.http import JsonResponse
from django.db.models import Sum, Avg, F
from .models import HiringData  # Make sure this model exists

def hr_metrics(request):
    total_vacancies = HiringData.objects.aggregate(total_vacancies=Sum("no_of_vacancies"))["total_vacancies"] or 0
    total_offers = HiringData.objects.aggregate(total_offers=Sum("no_of_offers"))["total_offers"] or 0
    avg_time_to_hire = HiringData.objects.exclude(date_candidate_finalised=None).annotate(
        hiring_days=F("date_candidate_finalised") - F("date_req_received")
    ).aggregate(avg_days=Avg("hiring_days"))["avg_days"]
    avg_time_to_hire = avg_time_to_hire.days if avg_time_to_hire else 0
    cv_given = HiringData.objects.aggregate(total_given=Sum("cv_given"))["total_given"] or 0
    cv_shared = HiringData.objects.aggregate(total_shared=Sum("cv_shared"))["total_shared"] or 0
    cv_shortlisted = HiringData.objects.aggregate(total_shortlisted=Sum("cv_shortlisted"))["total_shortlisted"] or 0
    candidates_interviewed = HiringData.objects.aggregate(total_interviewed=Sum("candidates_interviewed"))["total_interviewed"] or 0

    return JsonResponse({
        "total_vacancies": total_vacancies,
        "total_offers": total_offers,
        "avg_time_to_hire": avg_time_to_hire,
        "cv_given" : cv_given,
        "cv_shared" : cv_shared,
        "cv_shortlisted" : cv_shortlisted,
        "candidates_interviewed": candidates_interviewed
    })

"""def hr_metrics_page(request):
    return render(request, "hr_metrics.html")"""
from .models import HiringData

def hr_metrics_page(request):
    all_indents = HiringData.objects.values('indent_no').distinct()
    return render(request, 'hr_metrics.html', {'all_indents': all_indents})


# Recruitment Funnel
from django.http import JsonResponse
from collections import Counter

"""def get_funnel_data(request):
    funnel_order = [
    "More CVs required",
    "CVs to be shared",
    "CVs shared",
    "Interview",
    "Candidate Finalized",
    "Hired",
    "On Hold (New Hire)",
    "On Hold"
]
    
    # Fetch counts of each status
    funnel_counts = {status: HiringData.objects.filter(status=status).count() for status in funnel_order}

    # Prepare data in correct order
    funnel_data = [{"label": status, "y": funnel_counts[status]} for status in funnel_order if funnel_counts[status] > 0]

    return JsonResponse({"funnel_data": funnel_data})
"""
"""def get_funnel_data(request):
    funnel_order = [
        "More CVs required",
        "CVs to be shared",
        "CVs shared",
        "Interview",
        "On Hold",
        "Candidate Finalized",
        "Hired",
        "On Hold (New Hire)",
    ]

    # Step 1: Fetch raw counts
    funnel_counts = {status: HiringData.objects.filter(status=status).count() for status in funnel_order}

    # Step 2: Make cumulative values (top-down)
    cumulative_counts = []
    cumulative_total = 0
    for status in funnel_order:
        cumulative_total += funnel_counts.get(status, 0)
        cumulative_counts.append({"label": status, "y": cumulative_total})
    return JsonResponse({"funnel_data": cumulative_counts})

def hr_metrics_dashboard(request):
    return render(request, "hr-metrics.html")

"""
"""def get_funnel_data(request):
    funnel_order = [
        "More CVs required",
        "CVs to be shared",
        "CVs shared",
        "Interview",
        "On Hold",
        "Candidate Finalized",
        "Hired",
        "On Hold (New Hire)"
    ]

    color_map = {
        "More CVs required": "#FFD700",
        "CVs to be shared": "#FFA500",
        "CVs shared": "#FF8C00",
        "Interview": "#00CED1",
        "On Hold": "#808080",
        "Candidate Finalized": "#7CFC00",
        "Hired": "#228B22",
        "On Hold (New Hire)": "#B22222"
    }

    funnel_counts = {status: HiringData.objects.filter(status=status).count() for status in funnel_order}

    funnel_data = [
        {
            "label": status,
            "y": funnel_counts.get(status, 0),
            "color": color_map.get(status, "#FFFFFF")
        }
        for status in funnel_order
    ]

    # No reverse needed unless your charting library requires it
    return JsonResponse({"funnel_data": funnel_data})
    """

from django.http import JsonResponse
from .models import HiringData

from django.db.models import Sum
from django.http import JsonResponse

def get_funnel_data(request):
    indent = request.GET.get('indent_no', None)

    color_map = {
        "CVs Given": "#FFD700",
        "CV sets Shared": "#FFA500",
        "CVs Shortlisted": "#FF8C00",
        "Interviewed": "#00CED1",
        "Final Round": "#7CFC00",
        "Offers": "#228B22"
    }

    # Base queryset
    queryset = HiringData.objects.all()
    if indent:
        queryset = queryset.filter(indent_no=indent)

    # Sum up each funnel field
    aggregate_data = queryset.aggregate(
        cvs_given=Sum("cv_given"),
        cvs_shared=Sum("cv_shared"),
        cvs_shortlisted=Sum("cv_shortlisted"),
        interviewed=Sum("candidates_interviewed"),
        final_round=Sum("candidates_finalround"),
        offers=Sum("no_of_offers")
    )

    # Construct funnel data points
    funnel_data = [
        {"label": "CVs Given", "y": aggregate_data["cvs_given"] or 0, "color": color_map["CVs Given"]},
        {"label": "CV sets Shared", "y": aggregate_data["cvs_shared"] or 0, "color": color_map["CV sets Shared"]},
        {"label": "CVs Shortlisted", "y": aggregate_data["cvs_shortlisted"] or 0, "color": color_map["CVs Shortlisted"]},
        {"label": "Interviewed", "y": aggregate_data["interviewed"] or 0, "color": color_map["Interviewed"]},
        {"label": "Final Round", "y": aggregate_data["final_round"] or 0, "color": color_map["Final Round"]},
        {"label": "Offers", "y": aggregate_data["offers"] or 0, "color": color_map["Offers"]},
    ]

    return JsonResponse({"funnel_data": funnel_data})

def get_indent_list(request):
    indents = HiringData.objects.values_list('indent_no', flat=True).distinct()
    return JsonResponse({"indents": list(indents)})

#-----------------------------------------------------------------------------------------------------------------

from django.http import JsonResponse
from .models import HiringData
from django.shortcuts import get_object_or_404

def gantt_chart_data_by_indent(request, indent_no):
    record = get_object_or_404(HiringData, indent_no=indent_no)
    
    phases = []
    
    if record.date_req_received:
        phases.append({
            "Task": "Request Received",
            "Start": record.date_req_received,
            "Finish": record.date_round1_cvsent or record.date_revert1 or record.date_candidate_finalised or record.date_req_received,
            "Resource": "Request Received"
        })

    if record.date_round1_cvsent:
        phases.append({
            "Task": "Round 1 CV Sent",
            "Start": record.date_round1_cvsent,
            "Finish": record.date_revert1 or record.date_candidate_finalised or record.date_round1_cvsent,
            "Resource": "CV Sent"
        })

    if record.date_revert1:
        phases.append({
            "Task": "Revert 1",
            "Start": record.date_revert1,
            "Finish": record.date_candidate_finalised or record.date_revert1,
            "Resource": "Revert"
        })

    if record.date_candidate_finalised:
        phases.append({
            "Task": "Candidate Finalised",
            "Start": record.date_candidate_finalised,
            "Finish": record.date_candidate_finalised,
            "Resource": "Finalised"
        })

    return JsonResponse(phases, safe=False)

