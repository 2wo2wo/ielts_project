from django.contrib import admin
from .models import (
    Collection,    MatchingHeadingChoices,     Text,
    TrueFalse,    ParagraphMatching,     Part,     GivenKey,    SummaryCompletion,
    SentencePart, MultipleChoice, List, WholeList, ListSection,
    TableChoices, TablePart, TableCompletion, ChoicePart, MatchingSentence,
    GivenPart, FlowChart, FlowChartAnswer, Book, Author, Checks

)
# Register your models here.

# Register your models here.
admin.site.register(Author)
admin.site.register(Collection)
admin.site.register(MatchingHeadingChoices)
admin.site.register(Text)
admin.site.register(TrueFalse)
admin.site.register(ParagraphMatching)
admin.site.register(Part)
admin.site.register(GivenKey)
admin.site.register(SummaryCompletion)
admin.site.register(SentencePart)
admin.site.register(MultipleChoice)
admin.site.register(List)
admin.site.register(ListSection)
admin.site.register(WholeList)
admin.site.register(TableChoices)
admin.site.register(TablePart)
admin.site.register(TableCompletion)
admin.site.register(ChoicePart)
admin.site.register(MatchingSentence)
admin.site.register(GivenPart)
admin.site.register(FlowChart)
admin.site.register(FlowChartAnswer)
admin.site.register(Book)
admin.site.register(Checks)
