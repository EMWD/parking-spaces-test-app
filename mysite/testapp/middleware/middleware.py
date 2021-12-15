
class FirstMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
    def __call__(self, request):
        response = self._get_response(request)
        print("Fist custom middleware is active")
        return response
        