from django.shortcuts import render, get_object_or_404, redirect
from WebShop.models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemFrom

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'core/detail.html', {
        'item': item,
        'related_items': related_items,
    })

@login_required()
def new(request):
    if request.method == 'POST':
        form = NewItemFrom(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemFrom()

    return render(request, 'core/form.html', {
        'form': form,
        'title': 'New item',
    })