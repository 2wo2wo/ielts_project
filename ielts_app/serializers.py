from rest_framework import serializers
from .models import (
    Collection,    MatchingHeadingChoices,     Text,
    TrueFalse,    ParagraphMatching,     Part,     GivenKey,    SummaryCompletion,
    SentencePart, MultipleChoice, List, WholeList, ListSection,
    ChoicePart, GivenPart, MatchingSentence, TablePart,
    TableCompletion, TableChoices, FlowChart, FlowChartAnswer,
    Book,

)

#Heading Matchin ser
class MatchingTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('head_letter', 'text',)


class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchingHeadingChoices
        fields = ('given_choice',)

# True, False, Not Given ser or Yes, No, Not Given
class TrueFalsesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrueFalse
        fields = ('description',)


# Paragraph matching Part
class ParagraphMatchingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParagraphMatching
        fields = ('description',)

# Summary Completion

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = (
            'description',
        )


class GivenKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = GivenKey
        fields = (
            'key_letter',
            'key_descrp',
        )


class SummaryCompletionSerializer(serializers.ModelSerializer):
    summary_parts = PartSerializer(many=True)
    summary_choices = GivenKeySerializer(many=True)

    class Meta:
        model = SummaryCompletion
        fields = (
            'name',
            'summary_parts',
            'summary_choices',
        )



# Sentence Part
class SentencePartSerializer(serializers.ModelSerializer):

    class Meta:
        model = SentencePart
        fields = (
            'description',

        )
#  Multiple Choices


class MultipleChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoice
        fields = (
            'description',
            'a_key',
            'b_key',
            'c_key',
            'd_key',
        )


# List Selection

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = (
            'description',
        )

class ListSelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListSection
        fields = (
            'description',
        )


class WholeListSerializer(serializers.ModelSerializer):
    list_texts = ListSelectionSerializer(many=True)
    list_choices = ListSerializer(many=True)

    class Meta:
        model = WholeList
        fields =(
            'name',
            'list_texts',
            'list_choices'
        )

# Matching Sentence


class ChoicePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoicePart
        fields = (
            'key_descrp',

        )


class GivenPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = GivenPart
        fields = (
            'description',
        )


class MatchingSentenceSerializer(serializers.ModelSerializer):
    given_parts = GivenPartSerializer(many=True)
    choice_parts = ChoicePartSerializer(many=True)

    class Meta:
        model = MatchingSentence
        fields = (
            'name',
            'given_parts',
            'choice_parts'

        )

# Table Part


class TablePartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablePart
        fields = (
            'description',
        )

class TableChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableChoices
        fields = (
            'choice'
        )

class TableCompletionSerializer(serializers.ModelSerializer):
    table_parts = TablePartSerializer(many=True)
    table_choices = TableChoiceSerializer(many=True)
    class Meta:
        model = TableCompletion
        fields = (
            'heading',
            'table_parts',
            'table_choices',
        )

# Flow Charts is also True Diagram Completion Questions

class FlowAnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlowChartAnswer
        fields = (
            'answer',
        )

class FlowChartSerializers(serializers.ModelSerializer):

    class Meta:
        model = FlowChart
        fields = (
            'description',
            'get_image_url',
        )

# Overall

class MatchingCollectionSerializer(serializers.ModelSerializer):

    collections = ChoicesSerializer(many=True)
    texts = MatchingTextSerializer(many=True)
    true_false = TrueFalsesSerializer(many=True)
    paragraphs = ParagraphMatchingSerializer(many=True)
    summary_completions = SummaryCompletionSerializer(many=True)
    sentence_completions = SentencePartSerializer(many=True)
    multiple_choices = MultipleChoicesSerializer(many=True)
    list_selections = WholeListSerializer(many=True)
    matching_sentences = MatchingSentenceSerializer(many=True)
    tables = TableCompletionSerializer(many=True)
    flow_charts = FlowChartSerializers(many=True)

    class Meta:
        model = Collection
        fields = (
            'id',
            'name',
            'get_image_url',
            'texts',
            'true_false',
            'paragraphs',
            'summary_completions',
            'sentence_completions',
            'multiple_choices',
            'list_selections',
            'matching_sentences',
            'tables',
            'flow_charts',
            'collections',
        )
        read_only_fields = ('id',)

class BookSerializer(serializers.ModelSerializer):
    passage = MatchingCollectionSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'passage'
        )
