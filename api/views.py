from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import *

from .models import *


@api_view(['GET'])
def api_overview(request):
    # return JsonResponse({"test": "API BASE POINT"})
    # return JsonResponse("API BASE POINT", safe=False)
    api_urls = {
        'Answer add': '/answer/',
        'Answer Read Update Delete': '/answer/<str:pk>/',
        'question add': '/question/',
        'question Read Update Delete': '/question/<str:pk>/',
        'Additional Question Category add': '/aqc/',
        'Additional Question Category Read Update Delete': '/aqc/<str:pk>/',
        'Section add': '/section/',
        'Section Read Update Delete': '/section/<str:pk>/',
        'SubSection add': '/subsection/',
        'SubSection Read Update Delete': '/subsection/<str:pk>/',
    }
    return Response(api_urls)


# # person model
# @api_view(['GET'])
# def person_list(request):
#     persons = Person.objects.all()
#     serializer = PersonSerializer(persons, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def person_details(request, person_id):
#     person = Person.objects.get(id=person_id)
#     serializer = PersonSerializer(person, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def person_create(request):
#     serializer = PersonSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def person_update(request, person_id):
#     person = Person.objects.get(id=person_id)
#     serializer = PersonSerializer(instance=person, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def person_delete(request, person_id):
#     person = Person.objects.get(id=person_id)
#     person.delete()
#     return Response("Deleted Successfully!")


# *** Answer model CRUD

# class AnswerView(APIView):
#     """
#     Create, Retrieve, update or delete a answer instance.
#     """
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Answer.objects.get(pk=pk)
#         except Answer.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         answer = self.get_object(pk)
#         serializer = AnswerSerializer(answer)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = AnswerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# #
#     def put(self, request, pk):
#         answer = self.get_object(pk)
#         serializer = AnswerSerializer(instance=answer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         answer = self.get_object(pk)
#         answer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# answer create
# @api_view(['POST'])
# def create_answer(request):
#     serializer = AnswerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # answer read
# @api_view(['GET'])
# def get_answer(self, request, pk):
#     answer = self.get_object(pk)
#     serializer = AnswerSerializer(answer)
#     return Response(serializer.data)
#
#
# # answer update
# @api_view(['POST'])
# def update_answer(self, request, pk):
#     answer = self.get_object(pk)
#     serializer = AnswerSerializer(instance=answer, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # answer delete
# @api_view(['DELETE'])
# def delete_answer(self, request, pk):
#     answer = self.get_object(pk)
#     answer.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# AdditionalQuestionCategory model CRUD
# AdditionalQuestionCategory create
# @api_view(['POST'])
# def create_additional_question_category(request):
#     serializer = AdditionalQuestionCategorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # answer read
# @api_view(['GET'])
# def get_additional_question_category(request, pk):
#     aqc = AdditionalQuestionCategory.objects.get(additionalQuestionCategoryID=pk)
#     serializer = AdditionalQuestionCategorySerializer(aqc)
#     print(serializer.data)
#     return Response(serializer.data)


# Answer views
class ListAllAndAddAnswers(ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class RetrieveUpdateDeleteAnswers(RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


# Question views
class ListAllAndAddQuestions(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class RetrieveUpdateDeleteQuestions(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# Additional Question Category views
class ListAllAndAddAdditionalQuestionCategories(ListCreateAPIView):
    queryset = AdditionalQuestionCategory.objects.all()
    serializer_class = AdditionalQuestionCategorySerializer


class RetrieveUpdateDeleteAdditionalQuestionCategory(RetrieveUpdateDestroyAPIView):
    queryset = AdditionalQuestionCategory.objects.all()
    serializer_class = AdditionalQuestionCategorySerializer


# Section views
class ListAllAndAddSections(ListCreateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class RetrieveUpdateDeleteSections(RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


# SubSection views
class ListAllAndAddSubSections(ListCreateAPIView):
    queryset = SubSection.objects.all()
    serializer_class = SubSectionSerializer


class RetrieveUpdateDeleteSubSections(RetrieveUpdateDestroyAPIView):
    queryset = SubSection.objects.all()
    serializer_class = SubSectionSerializer




