from django.db import models

LABORATORY = (
    (1, "Organic"),
    (2, 'Non Organic'),
    (3, 'Research and development'),
    (4, 'Quality Control')
)

class Supervisor(models.Model):
    name = models.CharField(max_length=64, verbose_name='Laboratorium')
    supervisor_name = models.CharField(max_length=64, verbose_name='Nazwisko Kierownika')

    def __str__(self):
        return f'{self.name} - {self.supervisor_name}'

class Analyst(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    laboratory = models.IntegerField(choices=LABORATORY)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

class Confirmation(models.Model):
    analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE)
    day = models.DateField()
    present = models.BooleanField(null=True)

class AnalystNotice(models.Model):
    subject = models.CharField(max_length=254, verbose_name='Temat Analizy/Badania')
    content = models.TextField(verbose_name='Notatki z przeprowadzonego eksperymentu')
    from_analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE, verbose_name='Analityk')
    photos = models.ImageField(upload_to='photos', null=True, blank=True)
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name='Data wysłania')

class AnalystMessage(models.Model):
    subject = models.CharField(max_length=254, verbose_name='Temat wiadomości')
    content = models.TextField(verbose_name='Treść wiadomości')
    from_analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE, verbose_name='Od')
    to_supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='Do')
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name='Data wysłania')

class SupervisorMessage(models.Model):
    subject = models.CharField(max_length=254, verbose_name='Temat wiadomości')
    content = models.TextField(verbose_name='Treść wiadomości')
    from_supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, verbose_name='Kierownik')
    to_analyst = models.ForeignKey(Analyst, on_delete=models.CASCADE, verbose_name='Do')
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name='Data wysłania')