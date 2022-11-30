from django.urls import path
from . import views

urlpatterns = [
    # api overview
    path('', views.api_overview, name="api-overview"),

    # Answer urls
    path('answer/', views.ListAllAndAddAnswers.as_view()),
    path('answer/<str:pk>/', views.RetrieveUpdateDeleteAnswers.as_view()),

    # Question urls
    path('question/', views.ListAllAndAddQuestions.as_view()),
    path('question/<str:pk>/', views.RetrieveUpdateDeleteQuestions.as_view()),

    # AddAdditional Question Category urls
    path('aqc/', views.ListAllAndAddAdditionalQuestionCategories.as_view()),
    path('aqc/<str:pk>/', views.RetrieveUpdateDeleteAdditionalQuestionCategory.as_view()),

    # Section urls
    path('section/', views.ListAllAndAddSections.as_view()),
    path('section/<str:pk>/', views.RetrieveUpdateDeleteSections.as_view()),

    # SubSection urls
    path('subsection/', views.ListAllAndAddSubSections.as_view()),
    path('subsection/<str:pk>/', views.RetrieveUpdateDeleteSubSections.as_view()),
]
