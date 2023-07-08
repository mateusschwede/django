from django.db import models

class Pet(models.Model):
    TIPO_PET = (
        ('Cão','Cão'),
        ('Gato','Gato'),
    )
    VACINADO = (
        (True,'Vacinado'),
        (False,'Não vacinado'),
    )
    ADOTADO = (
        (True,'Adotado'),
        (False,'Não adotado')
    )
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=4,choices=TIPO_PET)
    nascimento = models.DateField(auto_now_add=False)
    vacinado = models.BooleanField(default=False,choices=VACINADO)
    adotado = models.BooleanField(default=False,choices=ADOTADO)
    
    def __str__(self):
        return self.nome