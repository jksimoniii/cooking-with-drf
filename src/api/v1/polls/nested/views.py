from api.v1.polls import views


class QuestionNestedChoiceView(views.ChoiceViewSet):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(question=self.kwargs.get('question_pk'))
