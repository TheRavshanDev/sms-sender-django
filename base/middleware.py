
class TestMiddleware:
    def __init__(self, get_response: callable):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("Response bo'lishidan oldin bajariladigan amallar")
        response = self.get_response(request, *args, **kwargs)
        print("Response'dan keyin bajariladigan amallar")
        return response