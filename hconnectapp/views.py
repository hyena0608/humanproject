from django.shortcuts import render, redirect, get_object_or_404
from account.models import CustomUser, Hobby
from .models import Contest, Party
from django.utils import timezone

# Create your views here.

def main(request):
    Contests = Contest.objects.all()
    Parties = Party.objects.all()
    return render(request, 'main.html', {'Contests': Contests, 'Parties': Parties})

def profiles(request):
    CustomUsers = CustomUser.objects.all()
    Hobbys = Hobby.objects.all()
    return render(request, 'profiles.html', {'CustomUsers': CustomUsers, 'Hobbys': Hobbys})

def contest(request):
    Contests = Contest.objects.all()
    return render(request, 'contest.html', {'Contests': Contests})

def party(request):
    Parties = Party.objects.all()
    return render(request, 'party.html', {'Parties': Parties})

def newcontest(request):
    return render(request, 'newcontest.html')

def createcontest(request):
    new_contest = Contest()
    new_contest.title = request.POST['title']
    new_contest.contents = request.POST['contexts']
    new_contest.pub_date = timezone.now()
    new_contest.image = request.FILES['image']
    new_contest.save()
    return redirect('contest')

def newparty(request):
    return render(request, 'newparty.html')

def createparty(request):
    new_party = Party()
    new_party.title = request.POST['title']
    new_party.contents = request.POST['contexts']
    new_party.pub_date = timezone.now()
    new_party.image = request.FILES['image']
    new_party.save()
    return redirect('party')

def notice(request):
    return render(request, 'notice.html')
