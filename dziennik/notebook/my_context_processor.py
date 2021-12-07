from django.utils import timezone
import django
def my_cp(request):
  ctx = {
    "now": django.utils.timezone.now(),
    "version": "1.0",
  }
  return ctx