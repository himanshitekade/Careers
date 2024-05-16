from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,JsonResponse,FileResponse
from django.views import View
from datetime import datetime, timedelta,timezone
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate,login
from .models import *
from .serializers import *  
import json
from django.db.models import Q
from .validate import *
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import json
from django.http import QueryDict
import os
import base64
from django.views import View


# Create your views here.

#UserDetails
class UserDetailsAPIView(APIView):
    def get(self, request, format=None):
        params = request.query_params
        user_details = UserDetails.objects.filter(status_code=1).order_by('-created_at').all()
        serializer = UserDetailsViewerSerializer(user_details, many=True)
        return Response(serializer.data)    

    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        serializer = UserDetailsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailsAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return UserDetails.objects.filter(status_code=1).get(pk=pk)
        except UserDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserDetailsViewerSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        request.data['updated_at'] = timezone.now()
        serializer = UserDetailsCreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_details = self.get_object(pk)
        user_details.status_code = False
        user_details.save()
        return Response("id {0} is deleted".format(user_details.id), status=status.HTTP_200_OK)        


# JobOpeningAPIView
class JobOpeningAPIView(APIView):
    def get(self, request, format=None):
        job_opening = JobOpening.objects.filter(status_code=1).order_by('-created_at').all()
        serializer = JobOpeningViewerSerializer(job_opening, many=True)
        return Response(serializer.data)    
    
    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        serializer = JobOpeningCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobOpeningAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return JobOpening.objects.filter(status_code=1).get(pk=pk)
        except JobOpening.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = JobOpeningViewerSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        request.data['updated_at'] = timezone.now()
        serializer = JobOpeningCreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        job_opening = self.get_object(pk)
        job_opening.status_code = False
        job_opening.save()
        return Response("id {0} is deleted".format(job_opening.id), status=status.HTTP_200_OK)




# CompanyProfileAPIView
class CompanyProfileAPIView(APIView):
    def get(self, request, format=None):
        company_profile = CompanyProfile.objects.filter(status_code=1).order_by('-created_at')[:1]
        serializer = CompanyProfileViewerSerializer(company_profile, many=True)
        return Response(serializer.data)    
    
    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        serializer = CompanyProfileCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyProfileAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return CompanyProfile.objects.filter(status_code=1).get(pk=pk)
        except CompanyProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CompanyProfileViewerSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        request.data['updated_at'] = timezone.now()
        serializer = CompanyProfileCreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        company_profile = self.get_object(pk)
        company_profile.status_code = False
        company_profile.save()
        return Response("id {0} is deleted".format(company_profile.id), status=status.HTTP_200_OK)        




#CandidateJob
class CandidateJobAPIView(APIView):
    def get(self, request, format=None):
        params = request.query_params
        candidate_job = CandidateJob.objects.filter(status_code=1).order_by('-created_at').all()
        serializer = CandidateJobViewerSerializer(candidate_job, many=True)
        return Response(serializer.data)    

    def post(self, request, format=None):
        request.data['created_at'] = timezone.now()
        serializer = CandidateJobCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CandidateJobAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return CandidateJob.objects.filter(status_code=1).get(pk=pk)
        except CandidateJob.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CandidateJobViewerSerializer(snippet)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        request.data['updated_at'] = timezone.now()
        serializer = CandidateJobCreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidate_job = self.get_object(pk)
        candidate_job.status_code = False
        candidate_job.save()
        return Response("id {0} is deleted".format(candidate_job.id), status=status.HTTP_200_OK)        


#UserApi
class UserApi(APIView):
    def post(self, request):
        data = request.data

        username = data.get('email')

        if username is not None:
            try:
                user = User.objects.create(username=email)
                user.save()

                return Response(
                {
                'message':"",
                'error':"",
                "user": username,
                }
            )
            except Exception as ex:

                return Response({
                'message':"user already exists!",
                'error':"",
                "user": username,
                })



#FetchAPIView
class FetchAPIView(APIView):
    def get(self, request, format=None):
        action = request.GET.get('action',None)
        api_response = requests.get("http://localhost:8000/api/jobopening")


        if action == "get_view_id":
            view_id = request.GET.get("view_id")

            api_response = requests.get(f"http://localhost:8000/api/jobopening/{view_id}")
            api_company_profile = requests.get(f"http://localhost:8000/api/companyprofile")

            api_get_data = requests.get("http://localhost:8000/api/jobopening")
            # print("api_get_data", api_get_data.text)

            job_titles_data = api_get_data.json()
            print("job_titles_data", job_titles_data)

            json_data = api_response.json()

            company_json_data = api_company_profile.json()
           
            context ={
            "json_data": json_data,
            "company_json_data":company_json_data,
            "view_id":view_id,
            "job_titles_data":job_titles_data
            }

            return render(request, 'jobopening_view.html', context)

        if action == "get_form":
            view_id = request.GET.get("view_id")
    
            context ={
            "redirect": "jobcards",
            "view_id":view_id

            }
            return render(request, 'apply_form.html', context)
            
        if api_response.status_code == 200:
            # Extract JSON content from the response object
            json_data = api_response.json()

        else:
            print("Error: Unable to fetch data from the API")
            return HttpResponse(status=api_response.status_code)

        context = {
        "json_data":json_data
        }
        return render(request, 'base.html', context)

    def post(self, request, format=None):
        print("Request Data:", request.data)
        
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        mobile = request.POST.get('mobile', None)
        attachment = request.FILES.get('attachment',None)
        gender = request.POST.get('gender', None)
        current_previous_company = request.POST.get('current_previous_company', None)
        date_of_birth = request.POST.get('date_of_birth', None)
        experience = request.POST.get('experience', None)
        expected_salary = request.POST.get('expected_salary', None)
        notice_period = request.POST.get('notice_period', None)
        linkedin_url = request.POST.get('linkedin_url', None)
        facebook_url = request.POST.get('facebook_url', None)
        instagram_url = request.POST.get('instagram_url', None)
        twitter_url = request.POST.get('twitter_url', None)


        job_list = request.POST.get('view_id', None)

        headers = {'Content-Type': 'application/json'}
        

        if CandidateJob.objects.filter(user__email=email).exists():
            email_id = User.objects.get(email=email)
            email_id = email_id.id

            candidate_job_id = CandidateJob.objects.get(user__email=email)
            candidate_id = candidate_job_id.id
            job_id = candidate_id

            var_job_list = [int(job_list)]

            for i in candidate_job_id.job_opening.all():
                var_job_list.append(int(i.id))

            patch_job_json_data = {
            "job_opening":var_job_list,
            "user":email_id

            }

            patch_job_json_data = json.dumps(patch_job_json_data)

            print("patch_job_json_data", patch_job_json_data)

            job_id_obj = requests.patch(f"http://localhost:8000/api/candidateinfo/{job_id}/", data=patch_job_json_data, headers=headers)
            print("job_id_obj", job_id_obj)

        else:
            user = User.objects.create_user(username=email, password='same123.456', 
            first_name=first_name,last_name=last_name, email=email)

            # Retrieve user ID
            user_id = user.id

            user_form_data = {
                "mobile": mobile,
                "date_of_birth": date_of_birth,
                "gender":gender,
                "linkedin_url": linkedin_url,
                "facebook_url": facebook_url,
                "instagram_url": instagram_url,
                "twitter_url": twitter_url,
                "user":user_id,
                "role":[1]
            }

            
            user_json_data = json.dumps(user_form_data)


            files = {}

            if attachment:
                file_content = attachment.read()
                original_file_name = attachment.name

                # Create a dictionary with file data
                files = {'attachment': (original_file_name, file_content)}

                # Make a single API request to save the user details and attachment
            response = requests.post("http://localhost:8000/api/userdetails", data=user_form_data, files=files)

            print("API response:", response.text)


            # user_response = requests.post("http://127.0.0.1:8000/api/userdetails", data=user_json_data, headers=headers)
            # print("user_response", user_response.text)

            # Create Job Form data dictionary
            job_form_data = {
                "experience": experience,
                "expected_salary": expected_salary,
                "notice_period": notice_period,
                "current_previous_company": current_previous_company,
                "job_opening":[int(job_list)],
                "user":user_id
            }

            job_json_data = json.dumps(job_form_data)

            response = requests.post("http://localhost:8000/api/candidateinfo", data=job_json_data,  headers=headers)

            print(response.text)

        return redirect('jobcards')


#CompanyInformationView       
class CompanyInformationView(View):
    def get(self,request, *args, **kwargs):
        action = request.GET.get('action',None)
        
        api_company_profile = requests.get(f"http://localhost:8000/api/companyprofile")
        print("api_company_profile", api_company_profile.text)

        company_json_data = api_company_profile.json()
        print("company_json_data", company_json_data)


        context ={
        "company_json_data":company_json_data
        }

        return render(request, 'company_info.html', context)
