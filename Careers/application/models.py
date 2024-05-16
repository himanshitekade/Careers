from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ObjectManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status_code=1)

#Base
class Base(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_creator_name",null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="%(app_label)s_%(class)s_editor_name",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    status_code = models.BooleanField(default=1)
    activity_status = models.BooleanField(default=1)
    tenant_id = models.IntegerField(null=True, blank=True)
    objects = ObjectManager()

    class Meta:
        abstract = True

#Privileges
class Privileges(Base):
    privilege_name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.privilege_name

#Roles
class Roles(Base):
    role_name = models.CharField(max_length=100, blank=True, null=True)
    privilege = models.ManyToManyField(Privileges)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.role_name

#TypeMasterCategory
class TypeMasterCategory(Base):
    category_name = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.category_name

#TypeMaster 
class TypeMaster(Base):
    name = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    category = models.ForeignKey(TypeMasterCategory, on_delete = models.CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    sequence = models.IntegerField(default=0, blank=True, null=True)
    parent_id = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name

#UserDetails
class UserDetails(Base):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    role = models.ManyToManyField(Roles)
    mobile = PhoneNumberField(blank=True, null=True)
    attachment = models.FileField(upload_to = 'userdetails_attachment/', blank=True, null=True)
    skills = models.CharField(max_length=500, blank=True, null=True)
    is_candidate = models.BooleanField(default=False)
    current_locations = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    linkedin_url = models.URLField(max_length=500,blank=True, null=True)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    user_image = models.ImageField(upload_to='user_image/',blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    facebook_url = models.URLField(max_length=500,blank=True, null=True)
    instagram_url = models.URLField(max_length=500,blank=True, null=True)
    twitter_url = models.URLField(max_length=500,blank=True, null=True)
    
    def __str__(self):
        return self.user.username

#JobOpening
class JobOpening(Base):
    job_title = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    assignment_required = models.CharField(max_length=100, blank=True, null=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    job_location = models.CharField(max_length=200, blank=True, null=True)
    required_experience = models.CharField(max_length=100, blank=True, null=True)
    no_of_vacancy = models.IntegerField(default=0, blank=True, null=True)
    min_salary = models.FloatField(default=0, blank=True, null=True)
    max_salary = models.FloatField(default=0, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    job_requirement = models.TextField(blank=True, null=True)
    text_field_1 = models.CharField(max_length=100, blank=True, null=True)
    text_field_2 = models.CharField(max_length=100, blank=True, null=True)
    int_field_1 = models.IntegerField(default=0, blank=True, null=True)
    int_field_2 = models.IntegerField(default=0, blank=True, null=True)
    float_field_1 = models.FloatField(default=0,blank=True, null=True)
    float_field_2 = models.FloatField(default=0,blank=True, null=True)
    datetime_field_1 = models.DateTimeField(blank=True, null=True)
    datetime_field_2 = models.DateTimeField(blank=True, null=True)
     
    def __str__(self):
        return self.job_title


#CompanyProfile
class CompanyProfile(Base):
	company_name = models.CharField(max_length=200, blank=True, null=True)
	logo = models.FileField(upload_to='CompanyProfile_attachment',blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	founded_date = models.DateField(blank=True, null=True)
	location = models.CharField(max_length=200, blank=True, null=True)
	contact_information = PhoneNumberField(blank=True, null=True)
	website = models.CharField(max_length=250, blank=True, null=True)
	facebook_url = models.CharField(max_length=250, blank=True, null=True)
	instagram_url = models.CharField(max_length=250, blank=True, null=True)
	linkedin_url = models.CharField(max_length=250, blank=True, null=True)
	industry = models.CharField(max_length=100, blank=True, null=True)
	number_of_employees = models.IntegerField(default=0, blank=True, null=True)
	revenue = models.IntegerField(default=0, blank=True, null=True)
	text_field_1 = models.CharField(max_length=100, blank=True, null=True)
	text_field_2 = models.CharField(max_length=100, blank=True, null=True)
	int_field_1 = models.IntegerField(default=0, blank=True, null=True)
	int_field_2 = models.IntegerField(default=0, blank=True, null=True)
	float_field_1 = models.CharField(max_length=100, blank=True, null=True)
	float_field_2 = models.CharField(max_length=100, blank=True, null=True)
	datetime_field_1 = models.DateTimeField(blank=True, null=True)
	datetime_field_2 = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.company_name


#CandidateJob
class CandidateJob(Base):
	job_opening = models.ManyToManyField(JobOpening)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	notice_period = models.IntegerField(default=0, blank=True, null=True)
	current_previous_company = models.CharField(max_length=100, blank=True, null=True)
	expected_salary = models.IntegerField(default=0, blank=True, null=True)
	experience = models.IntegerField(default=0, blank=True, null=True)
	text_field_1 = models.CharField(max_length=100, blank=True, null=True)
	text_field_2 = models.CharField(max_length=100, blank=True, null=True)
	int_field_1 = models.IntegerField(default=0, blank=True, null=True)
	int_field_2 = models.IntegerField(default=0, blank=True, null=True)
	float_field_1 = models.CharField(max_length=100, blank=True, null=True)
	float_field_2 = models.CharField(max_length=100, blank=True, null=True)
	datetime_field_1 = models.DateTimeField(blank=True, null=True)
	datetime_field_2 = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.user.username


#ProfessionalDetails
class ProfessionalDetails(Base):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    profile_name = models.CharField(max_length=100, blank=True, null=True)
    organization_name = models.CharField(max_length=200, blank=True, null=True)
    previously_worked = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_responsibilities = models.CharField(max_length=500, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    text_field_1 = models.CharField(max_length=100, blank=True, null=True)
    text_field_2 = models.CharField(max_length=100, blank=True, null=True)
    int_field_1 = models.IntegerField(default=0, blank=True, null=True)
    int_field_2 = models.IntegerField(default=0, blank=True, null=True)
    float_field_1 = models.FloatField(default=0,blank=True, null=True)
    float_field_2 = models.FloatField(default=0,blank=True, null=True)
    datetime_field_1 = models.DateTimeField(blank=True, null=True)
    datetime_field_2 = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.user.username


#UserEducation
class UserEducation(Base):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	education_type = models.CharField(max_length=100, blank=True, null=True)
	passing_year = models.IntegerField(default=0, blank=True, null=True)
	board_name = models.CharField(max_length=200, blank=True, null=True)
	specialization = models.CharField(max_length=200, blank=True, null=True)
	percentage = models.IntegerField(default=0, blank=True, null=True)
	marksheet = models.FileField(upload_to='usereducation_attachment',blank=True, null=True)
	additional_qualification = models.CharField(max_length=500, blank=True, null=True)
	comments = models.CharField(max_length=500, blank=True, null=True)
	text_field_1 = models.CharField(max_length=100, blank=True, null=True)
	text_field_2 = models.CharField(max_length=100, blank=True, null=True)
	int_field_1 = models.IntegerField(default=0, blank=True, null=True)
	int_field_2 = models.IntegerField(default=0, blank=True, null=True)
	float_field_1 = models.CharField(max_length=100, blank=True, null=True)
	float_field_2 = models.CharField(max_length=100, blank=True, null=True)
	datetime_field_1 = models.DateTimeField(blank=True, null=True)
	datetime_field_2 = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.user.username


#UserDocuments
class UserDocuments(Base):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	doc_name = models.CharField(max_length=100, blank=True, null=True)
	attachment = models.FileField(upload_to='UserDocuments_attachment',blank=True, null=True)
	text_field_1 = models.CharField(max_length=100, blank=True, null=True)
	text_field_2 = models.CharField(max_length=100, blank=True, null=True)
	int_field_1 = models.IntegerField(default=0, blank=True, null=True)
	int_field_2 = models.IntegerField(default=0, blank=True, null=True)
	float_field_1 = models.CharField(max_length=100, blank=True, null=True)
	float_field_2 = models.CharField(max_length=100, blank=True, null=True)
	datetime_field_1 = models.DateTimeField(blank=True, null=True)
	datetime_field_2 = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.user.username