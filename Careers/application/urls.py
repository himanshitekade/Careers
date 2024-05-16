from django.urls import path
from application import views
from .views import *


#Api's url
urlpatterns = [
    # path('', CompanyInformationView.as_view(), name='company-info'),
    path('', FetchAPIView.as_view(),name="jobcards"),
 	path('api/userdetails', UserDetailsAPIView.as_view(),name="userdetails-api"),
    path('api/userdetails/<int:pk>/', UserDetailsAPIViewDetail.as_view(),name="userdetails-details-api"),
    path('api/jobopening', JobOpeningAPIView.as_view(),name="jobopening-api"),
    path('api/jobopening/<int:pk>/', JobOpeningAPIViewDetail.as_view(),name="jobopening-details-api"),
    path('api/companyprofile', CompanyProfileAPIView.as_view(),name="companyprofile-api"),
    path('api/companyprofile/<int:pk>/', CompanyProfileAPIViewDetail.as_view(),name="companyprofile-details-api"),
    path('api/candidateinfo', CandidateJobAPIView.as_view(),name="candidateinfo-api"),
    path('api/candidateinfo/<int:pk>/', CandidateJobAPIViewDetail.as_view(),name="candidateinfo-details-api"),
    path('api/userapi', UserApi.as_view(),name="userapi"),

]
