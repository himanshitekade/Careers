from django.contrib import admin
from .models import *
from django.utils import timezone
from django.forms import CheckboxSelectMultiple

# Register your models here.

#PrivilegesAdmin
class PrivilegesAdmin(admin.ModelAdmin):
    model = Privileges

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    list_display = ('privilege_name','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(Privileges, PrivilegesAdmin)


#RolesAdmin
class RolesAdmin(admin.ModelAdmin):
    model = Roles

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    list_display = ('role_name','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(Roles, RolesAdmin)


#TypeMasterCategoryAdmin
class TypeMasterCategoryAdmin(admin.ModelAdmin):
    model = TypeMasterCategory

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    list_display = ('category_name','value','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(TypeMasterCategory, TypeMasterCategoryAdmin)


#TypeMasterAdmin
class TypeMasterAdmin(admin.ModelAdmin):
    model = TypeMaster

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    list_display = ('name','value','category','sequence','parent_id','created_by', 'created_at', 'updated_by', 'updated_at')
   
    def category(self,obj):
        return obj.category.category_name
    
    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(TypeMaster, TypeMasterAdmin)


#UserDetailsAdmin
class UserDetailsAdmin(admin.ModelAdmin):
    model = UserDetails

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    formfield_overrides = {
            models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }

    list_display = ('username','skills','current_locations','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

    def username(self,obj):

        return obj.user.username

admin.site.register(UserDetails, UserDetailsAdmin)


#JobOpeningAdmin
class JobOpeningAdmin(admin.ModelAdmin):
    model = JobOpening

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    formfield_overrides = {
            models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        }

    list_display = ('job_title','department','job_type','job_location','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(JobOpening, JobOpeningAdmin)


#CompanyProfileAdmin
class CompanyProfileAdmin(admin.ModelAdmin):
    model = CompanyProfile

    def save_model(self, request, obj, form, change):
        
        if obj.created_by: 
            obj.updated_by_id = request.user.id
        else:
            obj.created_by_id = request.user.id
      
        super().save_model(request, obj, form, change)
    
    list_display = ('company_name','location','founded_date','created_by', 'created_at', 'updated_by', 'updated_at')

    def created_by(self,obj):
        if obj.created_by != None:
            return obj.created_by.username

    def updated_by(self,obj):
        if obj.updated_by != None:
            return obj.updated_by.username

admin.site.register(CompanyProfile, CompanyProfileAdmin)


admin.site.register(CandidateJob)


