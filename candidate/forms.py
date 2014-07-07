from django.forms import ModelForm

from candidate.models import Candidate


class CandidateForm(ModelForm):

    class Meta:
        model = Candidate
