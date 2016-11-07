from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from backend.models import *
from forms import *

import json


def demo_index(request):
    return render(request, 'demo_index.html', '')


def load_context():
    context = {}

    sidebar = [x.entry_name for x in MySideBar.objects.all()]
    context['sidebar'] = sidebar

    return context


def index(request):
    context = load_context()

    context['papers'] = len(MyPapers.objects.all())
    context['books'] = len(MyNotes.objects.filter(type=0))
    context['notes'] = len(MyNotes.objects.filter(type=1))

    return render(request, 'index.html', context)


def paper_lists(request):
    context = load_context()

    papers_list_objects = MyPapers.objects.all()
    papers_list = []

    for paper in papers_list_objects:
        paper_info = [paper.id, paper.name, paper.time, json.loads(paper.tag), paper.authors, paper.institutions,
                      paper.abstract]
        if paper.state == 0:
            color = "#3c8dbc"
            state_label = "already known"
        elif paper.state == 1:
            color = "#f39c12"
            state_label = "to be reread"
        else:
            color = "#f56954"
            state_label = "to be implemented"
        paper_info.insert(3, color)
        paper_info.insert(4, state_label)

        papers_list.append(paper_info)

    context['papers_list'] = papers_list

    return render(request, 'paper_lists.html', context)


def paper_detail(request, paper_id):
    context = load_context()

    paper_object = MyPapers.objects.filter(id=int(paper_id))[0]
    paper_info = [paper_object.id, paper_object.name, paper_object.time, json.loads(paper_object.tag),
                  paper_object.authors, paper_object.institutions, paper_object.abstract, paper_object.notes]

    if paper_object.state == 0:
        color = "#3c8dbc"
        state_label = "already known"
    elif paper_object.state == 1:
        color = "#f39c12"
        state_label = "to be reread"
    else:
        color = "#f56954"
        state_label = "to be implemented"
    paper_info.insert(3, color)
    paper_info.insert(4, state_label)

    context['paper_info'] = paper_info

    return render(request, 'paper_detail.html', context)


def paper_edit(request, paper_id):
    context = load_context()

    if paper_id == 'new':
        raw_state = [['selected', "already known"], ['', "to be reread"], ['', "to be implemented"]]
        raw_tag = [[tag, ''] for tag in context["sidebar"]]
        context['paper_info'] = ['new', 'todo', 'todo', raw_state, raw_tag, 'todo', 'todo', 'todo', 'todo']
        return render(request, 'paper_edit.html', context)

    paper_object = MyPapers.objects.filter(id=int(paper_id))[0]
    paper_info = [paper_object.id, paper_object.name, paper_object.time,
                  paper_object.authors, paper_object.institutions, paper_object.abstract, paper_object.notes]

    paper_state = [['', "already known"], ['', "to be reread"], ['', "to be implemented"]]
    paper_state[paper_object.state][0] = 'selected'
    paper_info.insert(3, paper_state)

    paper_tag = []
    for tag in context["sidebar"]:
        if tag in json.loads(paper_object.tag):
            paper_tag.append([tag, 'checked'])
        else:
            paper_tag.append([tag, ''])
    paper_info.insert(4, paper_tag)

    context['paper_info'] = paper_info

    return render(request, 'paper_edit.html', context)


def submit_paper_edit(request, paper_id):
    if paper_id == 'new':
        paper_object = MyPapers(time='', name='', authors='', institutions='', abstract='', notes='', state=0, tag='[]')
        paper_object.save()
    else:
        paper_object = MyPapers.objects.filter(id=int(paper_id))[0]

    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            # print form.cleaned_data
            paper_object.time = form.cleaned_data['time']
            paper_object.name = form.cleaned_data['title']
            paper_object.authors = form.cleaned_data['authors']
            paper_object.institutions = form.cleaned_data['institutions']
            paper_object.abstract = form.cleaned_data['abstract']
            paper_object.notes = form.cleaned_data['notes']
            state = form.cleaned_data['state']
            if state == 'already known':
                state = 0
            elif state == 'to be reread':
                state = 1
            else:
                state = 2
            paper_object.state = state
            paper_object.tag = form.cleaned_data['tags']

            paper_object.save()

    return HttpResponseRedirect('/paper_detail/' + str(paper_object.id))


def delete_paper(request, paper_id):
    paper_object = MyPapers.objects.filter(id=int(paper_id))[0]
    paper_object.delete()

    return HttpResponseRedirect('/paper_lists')