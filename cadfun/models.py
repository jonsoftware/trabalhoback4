from django.db import models

class Funcionario(models.Model):
    id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    setor = models.CharField(max_length=50)
    data_de_admissao = models.DateField()
    salario = models.FloatField()

    def __str__(self):
        return self.nome

class Falta(models.Model):
    id_falta = models.AutoField(primary_key=True)
    data_falta = models.DateField()
    motivo = models.CharField(max_length=255)
    id_funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='faltas')

    def __str__(self):
        return f"Falta de {self.id_funcionario.nome} em {self.data_falta}"