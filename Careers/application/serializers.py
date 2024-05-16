from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


#UserDetails
class UserDetailsViewerSerializer(serializers.ModelSerializer):

	class Meta:
		depth = 1
		model = UserDetails
		fields = ['id','user','user_id',  
		'mobile','attachment','skills', 'is_candidate', 'current_locations',
		'date_of_birth','linkedin_url', 'middle_name', 'user_image','gender'
		,'facebook_url','instagram_url','twitter_url','created_by',
		'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 


class UserDetailsCreateSerializer(serializers.ModelSerializer):

	created_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='creator_name', required=False)
	updated_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='editor_name', required=False)
	user_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(), required=False)
	# role_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset = Roles.objects.all(), required=False)

	class Meta:
		model = UserDetails
		fields = ['id','user','user_id', 
		'mobile','attachment','skills', 'is_candidate', 'current_locations',
		'date_of_birth','linkedin_url', 'middle_name', 'user_image','gender'
		,'facebook_url','instagram_url','twitter_url','created_by',
		'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at',
		'activity_status', 'tenant_id'] 



#JobOpening
class JobOpeningViewerSerializer(serializers.ModelSerializer):

	class Meta:
		depth = 1
		model = JobOpening
		fields = ['id','job_title','department','job_description','assignment_required',
		'job_type','job_location','required_experience','no_of_vacancy','min_salary',
		'max_salary','deadline','job_requirement','text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 


class JobOpeningCreateSerializer(serializers.ModelSerializer):

	created_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='creator_name', required=False)
	updated_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='editor_name', required=False)

	class Meta:
		model = JobOpening
		fields = ['id','job_title','department','job_description','assignment_required',
		'job_type','job_location','required_experience','no_of_vacancy','min_salary',
		'max_salary','deadline','job_requirement','text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id']  



#CompanyProfile
class CompanyProfileViewerSerializer(serializers.ModelSerializer):

	class Meta:
		depth = 1
		model = CompanyProfile
		fields = ['id','company_name', 'logo', 'description', 'founded_date',
		'location', 'contact_information', 'website', 'facebook_url', 'instagram_url',
		'linkedin_url', 'industry', 'number_of_employees', 'revenue',
		'text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 


class CompanyProfileCreateSerializer(serializers.ModelSerializer):

	created_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='creator_name', required=False)
	updated_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='editor_name', required=False)

	class Meta:
		model = CompanyProfile
		fields = ['id','company_name', 'logo', 'description', 'founded_date',
		'location', 'contact_information', 'website', 'facebook_url', 'instagram_url',
		'linkedin_url', 'industry', 'number_of_employees', 'revenue',
		'text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 



#CandidateJob
class CandidateJobViewerSerializer(serializers.ModelSerializer):

	class Meta:
		depth = 1
		model = CandidateJob
		fields = ['id', 'job_opening','user','user_id',
		'notice_period','current_previous_company', 'expected_salary','experience',
		'text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 


class CandidateJobCreateSerializer(serializers.ModelSerializer):

	created_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='creator_name', required=False)
	updated_by_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(),source='editor_name', required=False)
	user_id = serializers.PrimaryKeyRelatedField(many=False, write_only=True, queryset = User.objects.all(), required=False)
	job_opening_id = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset = JobOpening.objects.all(), required=False)

	class Meta:
		model = CandidateJob
		fields = ['id', 'job_opening', 'job_opening_id', 'user','user_id',
		'notice_period','current_previous_company', 'expected_salary','experience',
		'text_field_1','text_field_2','int_field_1',
		'int_field_2','float_field_1','float_field_2','datetime_field_1','datetime_field_2',
		'created_by', 'created_by_id', 'updated_by','updated_by_id', 'created_at','updated_at','activity_status',
		'tenant_id'] 
