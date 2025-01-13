import time
from django.core.cache import cache
from django.http import JsonResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        now = time.time()
        request_count = cache.get(ip, [])
        request_count = [timestamp for timestamp in request_count if now - timestamp <= 100]
        if len(request_count) >= 1:
            return JsonResponse(
                {"error": "Too many requests"}, status=429
            )
        request_count.append(now)
        cache.set(ip, request_count, timeout=100)
        response = self.get_response(request)
        response['Limit-Remaining'] = 10 - len(request_count)
        return response

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        return x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
