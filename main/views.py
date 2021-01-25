from django.shortcuts import render


def main(request):
    page_title = "Restaurant — Index"
    # В {} передаём переменные (контекст) в разметку
    return render(request, 'index.html', {'page_title': page_title})

