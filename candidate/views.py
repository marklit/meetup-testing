from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from candidate.forms import CandidateForm


def create(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('created'))
    else:
        form = CandidateForm()
    
    return render(request, 'candidate.html', {
        'form': form,
    })


def created(request):
    return render(request, 'thanks.html')
