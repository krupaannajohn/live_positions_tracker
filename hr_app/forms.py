from django import forms
from .models import HiringData

class HiringDataForm(forms.ModelForm):
    class Meta:
        model = HiringData
        fields = '__all__'

        labels = {
            'department' : 'Department',
            'vacancy_title' : 'Vacancy Title',
            'recruiter' : 'Name of the Recruiter',
            'source':'Source',
            'location': 'Location',
            'place_of_posting':'Place of Posting',
            'no_of_vacancies':'Number of Vacancies',
            'grade':'Grade',
            'type_hire':'Type of Hire',
            'cv_given' : 'Number of CVs given',
            'cv_shared' : 'Number of CV sets shared',
            'cv_shortlisted' : 'Number of CVs shortlisted',
            'candidates_interviewed' : 'Number of Candidates Interviewed',
            'candidates_finalround' : 'Number of Candidates shortlisted (Final Round)',
            'no_of_offers' : 'Number of offers',
            'status' : 'Status of Indent',
            'comments':'Comments' 
        }

    # Adding widgets for better UI
    date_req_received = forms.DateField(label='Date Request was Received',widget=forms.DateInput(attrs={'type': 'date'}), required = False)
    date_deltek_post = forms.DateField(label = 'Date of Deltek Post',widget=forms.DateInput(attrs={'type': 'date'}), required = False)
    date_round1_cvsent = forms.DateField(label = 'Date of CVs Sent (Round 1)', widget=forms.DateInput(attrs={'type': 'date'}), required = False)
    date_revert1 = forms.DateField(label = 'Date of First Revert', widget=forms.DateInput(attrs={'type': 'date'}), required = False)
    date_candidate_finalised = forms.DateField(label = 'Date of Candidate Finalization',widget=forms.DateInput(attrs={'type': 'date'}), required = False)

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    employee_id = forms.CharField(max_length=50, label='Employee ID')
    department = forms.CharField(max_length=100, label='Department')

