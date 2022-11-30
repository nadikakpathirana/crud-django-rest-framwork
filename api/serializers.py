from rest_framework import serializers

from crud.utils import get_or_none
from .models import Answer, AdditionalQuestionCategory, Question, Section, SubSection


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.Serializer):
    questionID = serializers.IntegerField()
    questionOrderNumber = serializers.IntegerField(required=False)
    questionTitle = serializers.CharField(required=False)

    answerType = serializers.CharField(required=False)
    answersMCQ = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Answer.objects.all())

    userResponse_MCQ = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Answer.objects.all())
    userResponse_text = serializers.CharField(required=False)
    userResponse_bool = serializers.BooleanField(required=False)
    userResponse_number = serializers.IntegerField(required=False)
    userResponse_float = serializers.FloatField(required=False)

    metricUnitMain = serializers.CharField(required=False)
    metricUnitSub = serializers.CharField(required=False)

    imperialUnitMain = serializers.CharField(required=False)
    imperialUnitSub = serializers.CharField(required=False)

    isRequired = serializers.BooleanField(required=False)

    subQuestions = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Question.objects.all())

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.questionOrderNumber = validated_data.get('questionOrderNumber', instance.questionOrderNumber)
        instance.questionTitle = validated_data.get('questionTitle', instance.questionTitle)

        instance.answerType = validated_data.get('answerType', instance.answerType)
        instance.answersMCQ = validated_data.get('answersMCQ', instance.answersMCQ)

        instance.userResponse_MCQ = validated_data.get('userResponse_MCQ', instance.userResponse_MCQ)
        instance.userResponse_text = validated_data.get('userResponse_text', instance.userResponse_text)
        instance.userResponse_bool = validated_data.get('userResponse_bool', instance.userResponse_bool)
        instance.userResponse_number = validated_data.get('userResponse_number', instance.userResponse_number)
        instance.userResponse_float = validated_data.get('userResponse_float', instance.userResponse_float)
        instance.save()
        return instance


class AdditionalQuestionCategorySerializer(serializers.Serializer):
    additionalQuestionCategoryID = serializers.IntegerField()
    additionalQuestionCategoryOrderNumber = serializers.IntegerField(required=False)
    additionalQuestionCategoryTitle = serializers.CharField(required=False)
    additionalQuestions = serializers.PrimaryKeyRelatedField(many=True, read_only=False,
                                                             queryset=Question.objects.all())

    def create(self, validated_data):
        aqc_obj = AdditionalQuestionCategory(
            additionalQuestionCategoryTitle=validated_data["additionalQuestionCategoryTitle"],
            additionalQuestionCategoryOrderNumber=validated_data["additionalQuestionCategoryTitle"]
        )

        for pk in validated_data["additionalQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                aqc_obj.additionalQuestions.add(q_obj)

        aqc_obj.save()
        return aqc_obj

    def update(self, instance, validated_data):
        instance.additionalQuestionCategoryOrderNumber = validated_data.get('additionalQuestionCategoryOrderNumber',
                                                                            instance.additionalQuestionCategoryOrderNumber)
        instance.additionalQuestionCategoryTitle = validated_data.get('additionalQuestionCategoryTitle',
                                                                      instance.additionalQuestionCategoryTitle)
        for pk in validated_data["additionalQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                if q_obj not in instance.additionalQuestions:
                    instance.additionalQuestions.add(q_obj)
        instance.save()
        return instance


class SectionSerializer(serializers.Serializer):
    sectionID = serializers.IntegerField()
    sectionOrderNumber = serializers.IntegerField(required=False)

    sectionTitle = serializers.CharField(required=False)
    sectionDescription = serializers.CharField(required=False)
    sectionInfo = serializers.CharField(required=False)

    isAnsweredToSection = serializers.BooleanField(required=False)
    isSectionSelectedCurrently = serializers.BooleanField(required=False)
    isExpanded = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sectionOrderNumber = validated_data.get('sectionOrderNumber', instance.sectionOrderNumber)

        instance.sectionTitle = validated_data.get('sectionTitle', instance.sectionTitle)
        instance.sectionDescription = validated_data.get('sectionDescription', instance.sectionDescription)
        instance.sectionInfo = validated_data.get('answersMCQ', instance.sectionInfo)

        instance.isAnsweredToSection = validated_data.get('isAnsweredToSection', instance.isAnsweredToSection)
        instance.isAnsweredToSection = validated_data.get('isAnsweredToSection', instance.isAnsweredToSection)
        instance.isAnsweredToSection = validated_data.get('isAnsweredToSection', instance.isAnsweredToSection)
        instance.save()
        return instance


class SubSectionSerializer(serializers.Serializer):
    subSectionID = serializers.IntegerField()
    subSectionOrderNumber = serializers.IntegerField(required=False)

    sectionID = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Section.objects.all())

    subSectionTitle = serializers.CharField(required=False)
    subSectionDescription = serializers.CharField(required=False)
    subSectionInfo = serializers.CharField(required=False)
    SubSectionImage = serializers.ImageField(required=False)

    isAnsweredToSubSection = serializers.BooleanField(required=False)
    isSubSectionSelectedCurrently = serializers.BooleanField(required=False)

    commonQuestions = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Question.objects.all())
    additionalQuestions = serializers.PrimaryKeyRelatedField(many=True, read_only=False,
                                                             queryset=Question.objects.all())
    additionalQuestionsCategories = serializers.PrimaryKeyRelatedField(many=True, read_only=False,
                                                                       queryset=AdditionalQuestionCategory.objects.all())

    def create(self, validated_data):
        sub_obj = SubSection(
            subSectionOrderNumber=validated_data["subSectionOrderNumber"],
            sectionID=validated_data["sectionID"],
            subSectionTitle=validated_data["subSectionTitle"],
            subSectionDescription=validated_data["subSectionDescription"],
            subSectionInfo=validated_data["subSectionInfo"],
            isAnsweredToSubSection=validated_data["isAnsweredToSubSection"],
            isSubSectionSelectedCurrently=validated_data["isSubSectionSelectedCurrently"]
        )

        for pk in validated_data["commonQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                sub_obj.commonQuestions.add(q_obj)

        for pk in validated_data["additionalQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                sub_obj.additionalQuestions.add(q_obj)

        for pk in validated_data["additionalQuestionsCategories"]:
            aqc_obj = get_or_none(AdditionalQuestionCategory, questionID=pk)
            if aqc_obj is not None:
                sub_obj.additionalQuestions.add(aqc_obj)

        sub_obj.save()
        return sub_obj

    def update(self, instance, validated_data):
        instance.subSectionOrderNumber = validated_data.get('subSectionOrderNumber', instance.subSectionOrderNumber)

        instance.sectionID = validated_data.get('sectionID', instance.sectionID)

        instance.subSectionTitle = validated_data.get('subSectionTitle', instance.subSectionTitle)
        instance.subSectionDescription = validated_data.get('subSectionDescription', instance.subSectionDescription)
        instance.subSectionInfo = validated_data.get('subSectionInfo', instance.subSectionInfo)

        instance.isAnsweredToSubSection = validated_data.get('isAnsweredToSubSection', instance.isAnsweredToSubSection)
        instance.isSubSectionSelectedCurrently = validated_data.get('isSubSectionSelectedCurrently',
                                                                    instance.isSubSectionSelectedCurrently)

        for pk in validated_data["commonQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                if q_obj not in instance.commonQuestions:
                    instance.commonQuestions.add(q_obj)

        for pk in validated_data["additionalQuestions"]:
            q_obj = get_or_none(Question, questionID=pk)
            if q_obj is not None:
                if q_obj not in instance.additionalQuestions:
                    instance.additionalQuestions.add(q_obj)

        for pk in validated_data["additionalQuestionsCategories"]:
            q_obj = get_or_none(AdditionalQuestionCategory, questionID=pk)
            if q_obj is not None:
                if q_obj not in instance.additionalQuestionsCategories:
                    instance.additionalQuestionsCategories.add(q_obj)

        instance.save()
        return instance
