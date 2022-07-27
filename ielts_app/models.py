from django.db import models

# Create your models here.

#Collection of Questions to the Text


class Author(models.Model):
    name = models.CharField("author's name", max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField("book name", max_length=255)
    owner_book = models.ForeignKey(Author,
                                   on_delete=models.CASCADE,
                                   related_name='passage',
                                   null=True
                                   )

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    owner = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='passage',
        null=True
    )

    def __str__(self):
        return self.name[:10]

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''

# Matching Heading Part


class Text(models.Model):
    text = models.TextField()
    head_letter = models.CharField(max_length=1)
    answer = models.CharField("Answer", max_length=4, null=True)
    belong_to_match = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='texts'
    )

    def __str__(self):
        return self.text[:10]


class MatchingHeadingChoices(models.Model):
    given_choice = models.CharField(max_length=255)
    belong_tomatch = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='collections'
    )

    def __str__(self):
        return self.given_choice[:10]


#True False Questions Part


class TrueFalse(models.Model):
    description = models.CharField(max_length=255, null=True)

    ANSWER_CHOICES = [
        ("True", 'True'),
        ("False", 'False'),
        ("Not Given", 'Not Given'),
    ]

    answer = models.CharField(
        max_length=16,
        choices=ANSWER_CHOICES,
        null=True
    )
    belong_true_false = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='true_false',
        null=True
            )

    def __str__(self):
        return self.description

# Paragraph matching Part


class ParagraphMatching(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=1, null=True)
    belong_paragraph_matching = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='paragraphs',
        null=True
    )

    def __str__(self):
        return self.description

# Summary Completion


class SummaryCompletion(models.Model):
    name = models.CharField(max_length=255, null=True)
    belong_text = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='summary_completions',
        null=True
    )

    def __str__(self):
        return self.name


class Part(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=1, null=True)
    belong_summary = models.ForeignKey(
        SummaryCompletion,
        models.CASCADE,
        related_name='summary_parts',
        null=True
    )

    def __str__(self):
        return self.description


class GivenKey(models.Model):
    key_letter = models.CharField(max_length=1, null=True)
    key_descrp = models.CharField(max_length=255, null=True)
    belong_part = models.ForeignKey(
        SummaryCompletion,
        models.CASCADE,
        related_name='summary_choices',
        null=True
    )

    def __str__(self):
        return self.key_letter

# Sentence Part can be used for Short Answers


class SentencePart(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=255, null=True)
    belong_text = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='sentence_completions',
        null=True
    )

    def __str__(self):
        return self.description

# Multiple  Choices


class MultipleChoice(models.Model):

    ANSWER_CHOICES = [
        ("A", 'A'),
        ("B", 'B'),
        ("C", 'C'),
        ("D", 'D'),
    ]

    description = models.CharField(max_length=255,null=True)
    a_key = models.CharField(max_length=255,null=True)
    b_key = models.CharField(max_length=255,null=True)
    c_key = models.CharField(max_length=255,null=True)
    d_key = models.CharField(max_length=255,null=True)
    answer = models.CharField(
        max_length=1,
        choices=ANSWER_CHOICES,
        null=True
    )
    belong_text = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='multiple_choices',
        null=True
    )

    def __str__(self):
        return self.description

# List Selection can be used Author's statements


class WholeList(models.Model):
    name = models.CharField(max_length=255, null=True)
    belong_text = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='list_selections',
        null=True
    )

    def __str__(self):
        return self.name


class List(models.Model):
    description = models.CharField(max_length=255, null=True)
    belong_list = models.ForeignKey(
        WholeList,
        models.CASCADE,
        related_name='list_choices',
        null=True
    )

    def __str__(self):
        return self.description


class ListSection(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=1, null=True)
    belong_list = models.ForeignKey(
        WholeList,
        models.CASCADE,
        related_name='list_texts',
        null=True
    )

    def __str__(self):
        return self.description

# Matching Sentence Endings


class MatchingSentence(models.Model):
    name = models.CharField(max_length=255, null=True)
    belong_coll = models.ForeignKey(
        Collection,
        null=True,
        on_delete=models.CASCADE,
        related_name='matching_sentences'
    )
    def __str__(self):
        return self.name


class GivenPart(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=1, null=True)
    belong_sentence = models.ForeignKey(
        MatchingSentence,
        models.CASCADE,
        related_name='given_parts',
        null=True
    )

    def __str__(self):
        return self.description


class ChoicePart(models.Model):
    key_descrp = models.CharField(max_length=255, null=True)
    belong_sentence = models.ForeignKey(
        MatchingSentence,
        models.CASCADE,
        related_name='choice_parts',
        null=True
    )

    def __str__(self):
        return self.key_descrp

# Table Completion


class TableCompletion(models.Model):
    heading = models.CharField(max_length=255, null=True)
    belong_table = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='tables',
        null=True
    )

    def __str__(self):
        return self.heading


class TablePart(models.Model):
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(max_length=64, null=True)
    belong_table = models.ForeignKey(
        TableCompletion,
        models.CASCADE,
        related_name='table_parts',
        null=True
    )

    def __str__(self):
        return self.description


class TableChoices(models.Model):
    choice = models.CharField(max_length=255, null=True)
    belong_table = models.ForeignKey(
        TableCompletion,
        models.CASCADE,
        related_name='table_choices',
        null=True
    )

    def __str__(self):
        return self.answer

# Flow Chart


class FlowChart(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    belong_flow = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='flow_charts',
        null=True
    )

    def __str__(self):
        return self.description

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ''


class FlowChartAnswer(models.Model):
    answer = models.CharField('answer', max_length=128)
    belong_flow = models.ForeignKey(
        FlowChart,
        models.CASCADE,
        related_name='flow_answers',
        null=True
    )

    def __str__(self):
        return self.answer

 # Choosing from checkboxes lists

class Checks(models.Model):
    ANSWER_CHOICES = [
        ("+", '+'),
        ("--", '--'),

    ]
    description = models.CharField(max_length=255, null=True)
    answer = models.CharField(
        max_length=10,
        choices=ANSWER_CHOICES,
        null=True
    )
    belong_collecton = models.ForeignKey(
        Collection,
        models.CASCADE,
        related_name='check_questions',
        null=True
    )


    def __str__(self):
        return self.description

