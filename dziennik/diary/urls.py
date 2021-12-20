
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from notebook.views import LaboratoryView, FirmLaboratoryView, AnalystView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', LaboratoryView.as_view(), name="index"),
    path('lab/<int:laboratory>/', FirmLaboratoryView.as_view(), name="lab_view"),
    path('analyst/<int:analyst_id>', AnalystView.as_view(), name="analyst_view")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
