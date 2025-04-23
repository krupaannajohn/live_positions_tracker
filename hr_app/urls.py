from django.urls import path, include
from .views import hiring_form_view, success_view, homepage, recruiter, update_indent, update_indent2, business_stakeholder_login, update_indent_redirect, update_independent, view_all_data, export_to_excel, login_view, delete_record, hiring_data_api, recruiter_dashboard, hr_metrics_page, business_dashboard, hr_metrics, get_funnel_data, gantt_chart_data_by_indent, get_indent_list
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_view, name='login'),
    path('view-data/', view_all_data, name='view_all_data'),
    path('export-excel/', export_to_excel, name='export_excel'),
    path('recruiter/', recruiter, name='recruiter'),
    path('hiring_form/', hiring_form_view, name='hiring_form'),
    path('update_indent_redirect/', update_indent_redirect, name='update_indent_redirect'),
    path('update_independent/', update_independent, name='update_independent'),  # for the independent one in the dashboard tab
    path('update_indent/<str:indent_no>/', update_indent, name='update_indent'),
    path('update_indent2/<str:indent_no>/', update_indent2, name='update_indent2'), 
    path('recruiter_dashboard/', recruiter_dashboard, name='recruiter_dashboard'),
    path('success/', success_view, name='success_page'),
    path('business_stakeholder/', business_stakeholder_login, name='business_stakeholder'),
    path("business_dashboard/", business_dashboard, name="business_dashboard"),
    path('delete/<str:vacancy_title>/', delete_record, name='delete_record'),
    path("api/hiring_data/", hiring_data_api, name="hiring_data_api"),  # Fetch all
    path("api/hiring_data/<str:department>/", hiring_data_api, name="hiring_data_api"),  # Fetch specific department
    path("hr-metrics/", hr_metrics, name="hr_metrics"),
    path("hr-dashboard/", hr_metrics_page, name="hr_metrics_page"),
    path("get-funnel-data/", get_funnel_data, name="get_funnel_data"),
    path('api/gantt/<str:indent_no>/', gantt_chart_data_by_indent, name='gantt-data-indent'),
    path('get-indents/', get_indent_list, name='get_indent_list'),
]
