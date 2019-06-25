from django.shortcuts import render, redirect, HttpResponse
from .models import AgileCard, AgileCardForm
from django.contrib.auth.decorators import login_required


@login_required
def cards(request):
    if request.method == 'POST':
        new_card = AgileCardForm(request.POST)
        new_card.save()
        return redirect('/')
    else:
        active_cards = AgileCard.objects.filter(active=True).order_by('-modified_at')
        context = {'todo': active_cards.filter(state='TODO').order_by('-modified_at'),
                   'in_progress': active_cards.filter(state='IN_PROGRESS').order_by('-modified_at'),
                   'done': active_cards.filter(state='DONE'),
                   'new_card': AgileCardForm()}
        return render(request, 'cards.html', context)


@login_required
def update(request, id=0, state=''):
    card = AgileCard.objects.get(id=id)
    if card and state:
        card.state = state
        card.save()
        return redirect('/')
    else:
        return HttpResponse('card not found or state not provided')


@login_required
def delete(request, id=0):
    card = AgileCard.objects.get(id=id)
    if card:
        card.active = False
        card.save()
        return redirect('/')
    else:
        return HttpResponse('card not found')

@login_required
def edit(request, id):
    card = AgileCard.objects.get(id=id)
    if request.method == 'POST':
        card.content = request.POST['content']
        card.state = request.POST['state']
        card.save()
        return redirect('/')
    else:
        context = {
            'card': card
        }
        return render(request, 'edit_card.html', context)
