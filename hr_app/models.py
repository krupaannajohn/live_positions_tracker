from django.db import models
from django.contrib.auth.models import AbstractUser



class HiringData(models.Model):
    updated_at = models.DateTimeField(auto_now=True) 
    indent_no = models.CharField(max_length=255)
    
    # Corrected department choices format
    DEPARTMENT_CHOICES = [
        ("Administration", "Administration"),
        ("Appliance Division", "Appliance Division"),
        ("Brand & Communications", "Brand & Communications"),
        ("Category Strategy & NBI", "Category Strategy & NBI"),
        ("Civil & MEP", "Civil & MEP"),
        ("Corporate Manufacturing Services", "Corporate Manufacturing Services"),
        ("Customer Service", "Customer Service"),
        ("ECDI Service", "ECDI Service"),
        ("Electromechanical Division", "Electromechanical Division"),
        ("Electronics Division", "Electronics Division"),
        ("Emerging Channels & Digital Initiatives", "Emerging Channels & Digital Initiatives"),
        ("Finance & Accounts", "Finance & Accounts"),
        ("Go To Market", "Go To Market"),
        ("Human Resources", "Human Resources"),
        ("Industrial Design", "Industrial Design"),
        ("IT & Systems", "IT & Systems"),
        ("Legal", "Legal"),
        ("Marketing", "Marketing"),
        ("Mechanical & Electrical Division", "Mechanical & Electrical Division"),
        ("New Product Development", "New Product Development"),
        ("Quality", "Quality"),
        ("R&D (Electronics Division)", "R&D (Electronics Division)"), 
        ("Strategy", "Strategy"),
        ("Supply Chain Management", "Supply Chain Management"),
        ("Wires & Cables Division", "Wires & Cables Division")
    ]
    department = models.CharField(max_length=255, choices=DEPARTMENT_CHOICES)

    vacancy_title = models.CharField(max_length=255)
    recruiter = models.CharField(max_length=255)

    SOURCE_CHOICES = [
        ('Naukri', 'Naukri'),
        ('Linkedin', 'Linkedin'),
        ('Employee Referrals', 'Employee Referrals'),
        ('Others', 'Others'),
    ]
    source = models.CharField(max_length=255, choices=SOURCE_CHOICES, blank = True, null = True)

    LOCATION_CHOICES = [
    ('Ahmedabad', 'Ahmedabad'),
    ('Bangalore', 'Bangalore'),
    ('Bhopal', 'Bhopal'),
    ('Bhubhaneshwar', 'Bhubhaneshwar'),
    ('Chandigarh', 'Chandigarh'),
    ('Chavady Factory', 'Chavady Factory'),
    ('Chennai', 'Chennai'),
    ('Coimbatore', 'Coimbatore'),
    ('Dehradun', 'Dehradun'),
    ('Delhi', 'Delhi'),
    ('Faridabad', 'Faridabad'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Ghaziabad Lab', 'Ghaziabad Lab'),
    ('Gurugram', 'Gurugram'),
    ('Gurugram Corporate', 'Gurugram Corporate'),
    ('Gurugram SB', 'Gurugram SB'),
    ('GUTS Haridwar', 'GUTS Haridwar'),
    ('GUTS Hyderabad', 'GUTS Hyderabad'),
    ('Guwahati', 'Guwahati'),
    ('Haridwar', 'Haridwar'),
    ('Hubli', 'Hubli'),
    ('Hyderabad', 'Hyderabad'),
    ('Indore', 'Indore'),
    ('Jaipur', 'Jaipur'),
    ('Jammu', 'Jammu'),
    ('Jodhpur', 'Jodhpur'),
    ('Kanpur', 'Kanpur'),
    ('Kashipur Factory', 'Kashipur Factory'),
    ('Kashmir', 'Kashmir'),
    ('Kochi Corporate', 'Kochi Corporate'),
    ('Kochi R&D', 'Kochi R&D'),
    ('Kochi R&D Dsir', 'Kochi R&D Dsir'),
    ('Kolkata', 'Kolkata'),
    ('Lucknow', 'Lucknow'),
    ('Ludhiana', 'Ludhiana'),
    ('Madurai', 'Madurai'),
    ('Mumbai', 'Mumbai'),
    ('Nagpur', 'Nagpur'),
    ('Patna', 'Patna'),
    ('Perundurai', 'Perundurai'),
    ('Pune', 'Pune'),
    ('Raipur', 'Raipur'),
    ('Ranchi', 'Ranchi'),
    ('Roorkee Factory', 'Roorkee Factory'),
    ('Sikkim Unit 2', 'Sikkim Unit 2'),
    ('Sikkim Unit 3', 'Sikkim Unit 3'),
    ('Srinagar', 'Srinagar'),
    ('Udupi', 'Udupi'),
    ('VCPL Patnagar', 'VCPL Patnagar'),
    ('Vijayawada', 'Vijayawada'),
    ('Others', 'Others')
    ]
    location = models.CharField(max_length=255, choices=LOCATION_CHOICES)

    place_of_posting = models.CharField(max_length=255, blank = True, null = True)
    no_of_vacancies = models.PositiveIntegerField()

    GRADE_CHOICES = [
        ('J', 'Junior'),
        ('E', 'Executive'),
        ('O', 'Officer'),
        ('M', 'Manager'),
        ('C', 'Chief'),
    ]
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)

    TYPE_HIRE_CHOICES = [
        ('New Hire', 'New Hire'),
        ('Replacement', 'Replacement'),
    ]
    type_hire = models.CharField(max_length=20, choices=TYPE_HIRE_CHOICES)

    date_req_received = models.DateField()
    date_deltek_post = models.DateField(blank = True, null = True)
    date_round1_cvsent = models.DateField()
    date_revert1 = models.DateField(blank = True, null = True)
    date_candidate_finalised = models.DateField(blank = True, null = True)

    cv_given = models.PositiveIntegerField(blank = True, null = True)
    cv_shared = models.PositiveIntegerField(blank = True, null = True)
    cv_shortlisted = models.PositiveIntegerField(blank = True, null = True)
    candidates_interviewed = models.PositiveIntegerField(blank = True, null = True)
    candidates_finalround = models.PositiveIntegerField(blank = True, null = True)
    no_of_offers = models.PositiveIntegerField(blank = True, null = True)

    STATUS_CHOICES = [
        ('Candidate Finalized', 'Candidate Finalized'),
        ('CVs shared', 'CVs shared'),
        ('CVs to be shared', 'CVs to be shared'),
        ('More CVs required', 'More CVs required'),
        ('Interview', 'Interview'),
        ('On Hold', 'On Hold'),
        ('On Hold (New Hire)', 'On Hold (New Hire)'),
        ('Hired','Hired')
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)

    comments = models.CharField(max_length=2000, blank=True, null=True) 

def __str__(self):
    return f"{self.indent_no} - {self.vacancy_title} ({self.department})"

