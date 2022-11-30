from django.db import models

AnswerType = (
    (u'mcq', 'mcq'),
    (u'text', 'text'),
    (u'bool', 'bool'),
    (u'number', 'number'),
    (u'float', 'float'),
    (u'date', 'date'),
    (u'file', 'file'),
    (u'photo', 'photo'),
    (u'answerMCQ_dropDown', 'answerMCQ_dropDown')
)


class Answer(models.Model):

    class Meta:
        app_label = 'api'

    answerID = models.IntegerField(primary_key=True, db_index=True)
    answerOrderNumber = models.IntegerField(blank=True, null=True)
    answerTitle = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return str(self.answerID)+"."+self.answerTitle


class Question(models.Model):

    class Meta:
        app_label = 'api'

    questionID = models.IntegerField(primary_key=True, db_index=True)
    questionOrderNumber = models.IntegerField(blank=True, null=True)
    questionTitle = models.CharField(max_length=256, blank=True, null=True)

    answerType = models.CharField(max_length=50, choices=AnswerType, blank=True, null=True)
    answersMCQ = models.ManyToManyField(Answer, blank=True, related_name="mcq_answerID_set")

    userResponse_MCQ = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE,
                                         related_name="response_answerID_set")
    userResponse_text = models.CharField(max_length=256, blank=True, null=True)
    userResponse_bool = models.BooleanField(blank=True, null=True)
    userResponse_number = models.IntegerField(blank=True, null=True)
    userResponse_float = models.FloatField(blank=True, null=True)

    metricUnitMain = models.CharField(max_length=256, blank=True, null=True)
    metricUnitSub = models.CharField(max_length=256, blank=True, null=True)

    imperialUnitMain = models.CharField(max_length=256, blank=True, null=True)
    imperialUnitSub = models.CharField(max_length=256, blank=True, null=True)

    isRequired = models.BooleanField(blank=True, null=True)

    subQuestions = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="subQuestions_list")

    def __str__(self):
        return str(self.questionID)+"."+self.questionTitle


class AdditionalQuestionCategory(models.Model):

    class Meta:
        app_label = 'api'

    additionalQuestionCategoryID = models.IntegerField(primary_key=True, db_index=True)
    additionalQuestionCategoryOrderNumber = models.IntegerField(blank=True, null=True)

    additionalQuestionCategoryTitle = models.CharField(max_length=256, blank=True, null=True)
    additionalQuestions = models.ManyToManyField(Question, blank=True)

    def __str__(self):
        return str(self.additionalQuestionCategoryID)+"."+self.additionalQuestionCategoryTitle


class Section(models.Model):

    class Meta:
        app_label = 'api'

    sectionID = models.IntegerField(primary_key=True, db_index=True)
    sectionOrderNumber = models.IntegerField(blank=True, null=True)

    sectionTitle = models.CharField(max_length=256, blank=True, null=True)
    sectionDescription = models.TextField(blank=True, null=True)
    sectionInfo = models.TextField(blank=True, null=True)

    isAnsweredToSection = models.BooleanField(blank=True, null=True)
    isSectionSelectedCurrently = models.BooleanField(blank=True, null=True)
    isExpanded = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return str(self.sectionID)+"."+self.sectionTitle


class SubSection(models.Model):

    class Meta:
        app_label = 'api'

    subSectionID = models.IntegerField(primary_key=True, db_index=True)
    subSectionOrderNumber = models.IntegerField(blank=True, null=True)
    # ***
    sectionID = models.ForeignKey(Section, null=True, blank=True, on_delete=models.CASCADE)

    subSectionTitle = models.CharField(max_length=256, blank=True, null=True)
    subSectionDescription = models.TextField(blank=True, null=True)
    subSectionInfo = models.TextField(blank=True, null=True)
    SubSectionImage = models.ImageField(blank=True, null=True)

    isAnsweredToSubSection = models.BooleanField(blank=True, null=True)
    isSubSectionSelectedCurrently = models.BooleanField(blank=True, null=True)

    commonQuestions = models.ManyToManyField(Question, blank=True, related_name="common_questionID_set")

    additionalQuestions = models.ManyToManyField(Question, blank=True, related_name="additional_questionID_set")

    additionalQuestionsCategories = models.ManyToManyField(AdditionalQuestionCategory, blank=True)

    def __str__(self):
        return str(self.subSectionID)+"."+self.subSectionTitle



