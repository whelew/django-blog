from django.shortcuts import render, get_object_or_404
from .models import About


# Create your views here.
def about_me(request):
    about = About.objects.all().order_by('-updated_on').first()

    if not about:
        # Handle the case where no objects are found
        return render(request, "about/about_me.html", {"error": "No about information found."})

    return render(
        request,
        "about/about_me.html",
        {"about": about}
    )