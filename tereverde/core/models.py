from django.db import models

# 1. Modelo de Parque 

class Parque(models.Model):
     
    TIPO_CHOICES = (
        ('NACIONAL', 'Parque Nacional da Serra dos Órgãos'),
        ('ESTADUAL', 'Parque Estadual dos Três Picos'),
        ('MUNICIPAL', 'Parque Natural Municipal Montanhas de Teresópolis'),
    )

    nome = models.CharField(
        max_length=200, 
        choices=TIPO_CHOICES,
        unique=True,
        verbose_name="Nome Oficial do Parque"
    )
    descricao_geral = models.TextField(
        verbose_name="Descrição Geral",
        help_text="Foco em geografia, limites e importância."
    )
    altitude_media = models.IntegerField(
        null=True, 
        blank=True, 
        verbose_name="Altitude Média (m)"
    )
    horario_funcionamento = models.CharField(
        max_length=255, 
        verbose_name="Horário de Funcionamento/Temporada"
    )
    
    class Meta:
        verbose_name = "Parque"
        verbose_name_plural = "Parques"

    def __str__(self):
        return self.get_nome_display()
