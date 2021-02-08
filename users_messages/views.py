from django.shortcuts import render
from main.models import UsersMessages
from django.core.paginator import Paginator


# Create your views here.
def messages_view(request):
    messages = UsersMessages.objects.filter(is_processed=False).order_by('sent_date')
    paginator = Paginator(messages, 5)
    page = request.GET.get('page')
    messages_page = paginator.get_page(page)
    return render(request, 'messages_view.html', {
        'items': messages_page,
    })
