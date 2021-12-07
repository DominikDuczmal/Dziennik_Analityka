
from django.contrib import admin
from django.urls import path
from notebook.views import LaboratoryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LaboratoryView.as_view(), name="index")

]
