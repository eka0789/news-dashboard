from django.shortcuts import redirect
from django.contrib import messages

class AdminOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        restricted_urls = [
            '/users/',          # list user
            '/users/create/',
            '/users/',          # edit/delete otomatis ter-cover
        ]

        # Cegah staff & user mengakses restricted URLs
        if not request.user.is_superuser:
            for url in restricted_urls:
                if request.path.startswith(url):
                    messages.error(request, "Anda tidak memiliki akses ke menu ini.")
                    return redirect("dashboard.index")

        return self.get_response(request)
