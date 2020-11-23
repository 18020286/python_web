from django.shortcuts import render
from django.views.generic import TemplateView

from hotel.models import Room


def home_view(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {
        'rooms_list': rooms,
        'nav': 'home'
    })


class SiteRoomView(TemplateView):
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        rooms = Room.objects.all()
        context = super().get_context_data(**kwargs)
        context['nav'] = 'room'
        context['rooms_list'] = rooms
        return context


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })
