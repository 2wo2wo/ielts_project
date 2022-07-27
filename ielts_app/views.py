from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import (
    Collection,    MatchingHeadingChoices,    Text,
    TrueFalse,    ParagraphMatching,     Part,     GivenKey,    SummaryCompletion,
    SentencePart, MultipleChoice, List, WholeList, ListSection,
    TableChoices, TablePart, TableCompletion, ChoicePart, MatchingSentence,
    GivenPart, FlowChart, FlowChartAnswer, Book, Checks
)

from .serializers import MatchingCollectionSerializer , BookSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.



class BookView(APIView):

    permission_classes = [IsAuthenticated]

    def get_heading_answers(self, collection):   #Matching Heading Text
        try:
            heading_answers = Text.objects.filter(belong_to_match=collection)
            solutions = [x.answer for x in heading_answers]
            return solutions
        except Text.DoesNotExist:
            return ''


    def true_false_answers(self, collection):   #True False answers
        try:
            true_false = TrueFalse.objects.filter(belong_true_false=collection)
            solutions = [x.answer for x in true_false]
            return solutions
        except TrueFalse.DoesNotExist:
            return ''


    def paragraph_matching_answers(self, collection): #statements which paragraph belongs
        try:
            paragraph_matching = ParagraphMatching.objects.filter(belong_paragraph_matching=collection)
            solutions = [x.answer for x in paragraph_matching]
            return solutions
        except ParagraphMatching.DoesNotExist:
            return ''

    def part_answers(self, collection):   # type given choices should fill gaps in text or sentence
        try:
            summary_completion = SummaryCompletion.objects.get(belong_text=collection)
            summary_parts_answers = Part.objects.filter(belong_summary=summary_completion)
            solutions = [x.answer for x in summary_parts_answers]
            return solutions
        except SummaryCompletion.DoesNotExist:
            return ''
                            #get answers from summary completion model

    def sentence_part_answers(self, collection):
        try:
            sentence_parts = SentencePart.objects.filter(belong_text=collection)
            solutions = [x.answer for x in sentence_parts]
            return solutions
        except SentencePart.DoesNotExist:
            return ''


    def multiple_choice_answers(self, collection):
        try:
            multiple_choices = MultipleChoice.objects.filter(belong_text=collection)
            solutions = [x.answer for x in multiple_choices ]
            return solutions
        except MultipleChoice.DoesNotExist:
            return ''


    def list_section_answers(self,collection):  #WholeListModel used smb statements
        try:
            whole_list = WholeList.objects.get(belong_text=collection)
            list_sections = ListSection.objects.filter(belong_list=whole_list)
            solutions = [x.answer for x in list_sections]
            return solutions
        except WholeList.DoesNotExist:
            return ''

    def given_part_answers(self, collection):  # sentence endings from lists # Given Part Model
        try:
            matching_sentence = MatchingSentence.objects.get(belong_coll=collection)
            given_parts = GivenPart.objects.filter(belong_sentence=matching_sentence)
            solutions = [x.answer for x in given_parts]
            return solutions
        except MatchingSentence.DoesNotExist:
            return ''

    def table_completions_answers(self, collection):  # table parts model
        try:
            table_completion = TableCompletion.objects.get(belong_table=collection)
            table_answers_all = TablePart.objects.filter(belong_table=table_completion)
            solutions = [x.answer for x in table_answers_all]
            return solutions
        except TableCompletion.DoesNotExist :
            return ''


    def flow_chart_answers(self, collection): # Flow charts
        try:
            flow_chart = FlowChart.objects.get(belong_flow=collection)
            flow_chart_answers_all = FlowChartAnswer.objects.filter(belong_flow=flow_chart)
            solutions = [x.answer for x in flow_chart_answers_all]
            return solutions
        except FlowChart.DoesNotExist :
            return ''

    def checks_answers(self,collection):
        try:
            checks = Checks.objects.filter(belong_collection=collection)
            solutions = [x.description for x in checks if x.answer == '+']

            return solutions
        except Checks.DoesNotExist:
            return ''



    def get_answers(self, collection):
        # answers = {
        #     "get_heading_answers": self.get_heading_answers(collection),
        #     "true_false_answers": self.true_false_answers(collection),
        #     "paragraph_matching_answers": self.paragraph_matching_answers(collection),
        #     "part_answers": self.part_answers(collection),
        #     "sentence_part_answers": self.sentence_part_answers(collection),
        #     "multiple_choice_answers": self.multiple_choice_answers(collection),
        #     "list_section_answers": self.list_section_answers(collection),
        #     "given_part_answers": self.given_part_answers(collection),
        #     "table_completions_answers": self.table_completions_answers(collection),
        #     "flow_chart_answers": self.flow_chart_answers(collection)
        # }
        answers = [
            self.get_heading_answers(collection),
            self.true_false_answers(collection),
            self.paragraph_matching_answers(collection),
            self.part_answers(collection),
            self.sentence_part_answers(collection),
            self.multiple_choice_answers(collection),
            self.list_section_answers(collection),
            self.given_part_answers(collection),
            self.table_completions_answers(collection),
            self.flow_chart_answers(collection)
        ]
        return answers



    def get_passage(self, book):
        try:
            collections = Collection.objects.filter(owner=book)
            answers1 = self.get_answers(collections[0])
            answers2 = self.get_answers(collections[1])
            answers3 = self.get_answers(collections[2])
            answers = [
                 answers1,
                 answers2,
                 answers3
            ]
            return answers
        except Book.DoesNotExist:
            return ''







    def get_book(self, pk):
        try:
            book = Book.objects.get(pk=pk)
            return self.get_passage(book)
        except Book.DoesNotExist:
            return ''





    def get(self, request, pk, format=None):
        books = Book.objects.get(pk=1)
        serializer = BookSerializer(books)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        list_answers = self.get_book(pk)

        a = [x for x in list_answers[0] if len(x) > 0]
        b = [y for y in list_answers[1] if len(y) > 0]
        c = [z for z in list_answers[2] if len(z) > 0]

        list = [*a,*b,*c]
        lis = []
        for i in list:
            for t in i:
                if t != '-':
                    lis.append(t)

        print(lis[12:24])


        return Response(lis)




