from django.shortcuts import render, get_object_or_404, redirect
from .models import Floor
from .forms import ReviewForm

def floor_default(request):
    """Главная — редирект на первый этаж (number=1)."""
    first = Floor.objects.filter(number=1).first()
    if first:
        return redirect('reviews:floor_detail', number=first.number)
    # если нет этажей — перенаправим в админку
    return redirect('/admin/')

def floor_detail(request, number):
    floor = get_object_or_404(Floor, number=number)
    floors = Floor.objects.order_by('number')  # для панели кнопок
    # обработка формы отзыва
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.floor = floor
            rev.save()
            return redirect('reviews:floor_detail', number=number)
    else:
        form = ReviewForm()
    reviews = floor.reviews.all().order_by('-created_at')
    return render(request, 'reviews/floor.html', {
        'floor': floor,
        'floors': floors,
        'reviews': reviews,
        'form': form,
    })
