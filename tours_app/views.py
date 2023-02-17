from django.shortcuts import render, redirect

from tours_app.forms import header_form, banner_form, footer_form, team_form
from tours_app.models import header_back, banner_back, footer_back, our_team


def travel_index(request):
    header = header_back.objects.all()
    banner = banner_back.objects.all()
    footer = footer_back.objects.all()
    team = our_team.objects.all()
    return render(request, 'index.html', dict(header=header, footer=footer, banner=banner, team=team))


def travel_destinations(request):
    return render(request, 'destinations.html')


def travel_elements(request):
    return render(request, 'elements.html')


def travel_news(request):
    return render(request, 'news.html')


def travel_contact(request):
    return render(request, 'contact.html')


def header_details(request, did):
    header = header_back.objects.get(id=did)
    return render(request, 'tours_header.html', {'header': header})


def header_update(request, id):
    item = header_back.objects.get(id=id)
    hfb_form = header_form(request.POST or None, request.FILES, instance=item)
    if hfb_form.is_valid():
        hfb_form.save()
        return redirect('/')
    return render(request, 'hfb_update.html', {'form': hfb_form, 'item': item})


def banner_update(request, id):
    item = banner_back.objects.get(id=id)
    form = header_form(request.POST or None, request.FILES, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'hfb_update.html', {'form': form, 'item': item})


def footer_update(request, id):
    item = footer_back.objects.get(id=id)
    form = header_form(request.POST or None, request.FILES, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'hfb_update.html', {'form': form, 'item': item})


def our_team_update(request, id):
    item = our_team.objects.get(id=id)
    form = team_form(request.POST or None, request.FILES, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'team_tours_update.html', {'form': form, 'item': item})
