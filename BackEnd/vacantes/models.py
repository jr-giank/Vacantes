from django.db import models

from .functions import image_upload_location, file_upload_location
from users.models import CustomUser

#Choices
tipo_trabajo_opciones = [
    ('TEMPORAL', 'Temporal'),
    ('INDEFINIDO', 'Indefinido')
]

forma_trabajo_opciones = [
    ('PRESENCIAL', 'Presencial'),
    ('HIBRIDO', 'Hibrido'),
    ('REMOTO', 'Remoto')
]

status_vacante_opciones = [
    ('A', 'ABIERTA'),
    ('C', 'CERRADA')
]

nivel_conocimiento_opciones = [
    ('A', 'Básico'),
    ('B', 'Intermedio'),
    ('C', 'Profesional'),
    ('D', 'Avanzado')
]

status_mensajes_opciones = [
    ('N', 'No leído'),
    ('V', 'Visto')
]

status_prueba_tecnica_opciones = [
    ('E', 'En curso'),
    ('F', 'Finalizada')
]

leido_prueba_tecnica_opciones = [
    ('N', 'No leído'),
    ('V', 'Visto')
]

status_solicitude_opciones = [
    ('A', 'Aplicado'),
    ('P', 'Prueba tecnica'),
    ('E', 'Para entrevista'),
    ('O', 'Entrevistado'),
    ('S', 'Seleccionado'),
    ('D', 'Descartado')
]

# Create your models here.
class Categoria(models.Model):
    
    nombre = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)
    direccion = models.CharField(max_length=90, blank=False, null=False)
    pais = models.CharField(max_length=30, blank=False, null=False)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    correo_vacantes = models.EmailField(max_length=60, blank=False, null=False)
    descripcion_empresa = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=13, blank=False, null=False) 
    url_web = models.URLField(blank=True, null=True)
    url_facebook = models.URLField(blank=True, null=True)
    url_instagram = models.URLField(blank=True, null=True)
    url_twitter = models.URLField(blank=True, null=True)
    foto = models.ImageField(upload_to=image_upload_location, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Vacante(models.Model):

    nombre_puesto = models.CharField(max_length=50, blank=False, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    status = models.CharField(max_length=7, choices=status_vacante_opciones, default='A')
    tipo_trabajo = models.CharField(max_length=10, choices=tipo_trabajo_opciones, default='TEMPORAL')
    forma_trabajo = models.CharField(max_length=10, choices=forma_trabajo_opciones, default='PRESENCIAL')
    experiencia = models.BooleanField(blank=False, null=False)
    responsabilidades_puesto = models.TextField(blank=True, null=True)
    requisitos_obligatorios = models.TextField(blank=False, null=False)
    requisitos_opcionales = models.TextField(blank=True, null=True)
    salario_min = models.IntegerField(blank=True, null=True)
    salario_max = models.IntegerField(blank=True, null=True)
    beneficios = models.TextField(blank=True, null=True)
    horario_trabajo = models.CharField(max_length=25, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True, blank=True, null=True)
    hora = models.TimeField(auto_now_add=True, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    hora_cierre = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_puesto} - {self.empresa}"

class Candidato(models.Model):

    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    mensage_presentacion = models.TextField(blank=True, null=True)
    correo_contacto = models.EmailField(max_length=60, blank=True, null=True)
    pais = models.CharField(max_length=56, blank=True, null=True)
    foto = models.ImageField(upload_to=image_upload_location, blank=True, null=True)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    nacimiento = models.DateField(blank=True, null=True)
    titulo_personal = models.CharField(max_length=60, blank=True, null=True)
    url_web = models.URLField(blank=True, null=True)
    url_facebook = models.URLField(blank=True, null=True)
    url_twitter = models.URLField(blank=True, null=True)
    url_instagram = models.URLField(blank=True, null=True)
    url_linkedin = models.URLField(blank=True, null=True)
    url_github = models.URLField(blank=True, null=True)
    url_telegram = models.URLField(blank=True, null=True)
    url_twitter = models.URLField(blank=True, null=True)
    cv_1 = models.FileField(upload_to=file_upload_location, blank=True, null=True)
    cv_2 = models.FileField(upload_to=file_upload_location, blank=True, null=True)
    cv1_nombre = models.CharField(max_length=50, blank=True, null=True)
    cv2_nombre = models.CharField(max_length=50, blank=True, null=True) 

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Solicitude(models.Model):
    
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    mensaje = models.TextField(blank=False, null=False)
    cv_url = models.URLField(default='http://127.0.0.1:8000/media/cv/f37aca8b-4b2b-11ed-8a6f-c80c0051d672-Nita_Ditch.pdf', blank=False, null=False)
    status = models.CharField(max_length=15, choices=status_solicitude_opciones, default='A')
    fecha = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.candidato} - {self.vacante}"

class VacantesGuardada(models.Model):

    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    fecha_guardado = models.DateField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return f'{self.vacante} - {self.usuario}'

class Proyecto(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    foto_proyecto = models.ImageField(upload_to=image_upload_location, blank=True, null=True) # Este campo no es URL porque aqui se debe subir la foto
    tecnologias_utilizadas = models.TextField(blank=False, null=False)
    fecha_creacion = models.DateField(blank=False, null=False)
    url_repositorio = models.URLField(blank=False, null=False)
    url_demo = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.candidato.nombre} - {self.nombre}'

class ExperienciaLaboralCandidato(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    nombre_puesto = models.CharField(max_length=50, blank=False, null=False)
    nombre_empresa = models.CharField(max_length=50, blank=False, null=False)
    responsabilidades = models.TextField(blank=False, null=False)
    fecha_inicio = models.DateField(blank=False, null=False)
    fecha_final = models.DateField(blank=False, null=False)

    def __str__(self):
        return f'{self.candidato.nombre} - {self.nombre_puesto}'

class TecnologiasCandidato(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    nombre_tecnologia = models.CharField(max_length=30, blank=False, null=False)
    nivel_conocimiento = models.CharField(max_length=7, choices=nivel_conocimiento_opciones, default='A')

    def __str__(self):
        return f'{self.candidato.nombre} - {self.nombre_tecnologia}'

class Mensaje(models.Model):

    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)
    texto = models.TextField(blank=False, null=False)
    fecha = models.DateField(auto_now_add=True, blank=False, null=False)
    motivo_mensaje = models.CharField(max_length=60, blank=False, null=False)
    status = models.CharField(max_length=8, choices=status_mensajes_opciones, default='N')

    def __str__(self):
        return f'{self.motivo_mensaje} - {self.usuario}'

class MensajesUsuariosDestino(models.Model):

    mensaje = models.ForeignKey(Mensaje, on_delete=models.CASCADE)
    usuario_destino = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return f'{self.usuario_destino}'

class PruebaTecnica(models.Model):
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60, blank=False, null=False)
    mandato = models.TextField(blank=False, null=False)
    tecnologias = models.TextField(blank=True, null=True)
    info_subida = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.vacante}'

class PruebaTecnicaAsignada(models.Model):
    
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    prueba = models.ForeignKey(PruebaTecnica, on_delete=models.CASCADE)
    fecha_limite = models.DateField(blank=False, null=False)
    fecha_asignacion = models.DateField(auto_now_add=True, blank=False, null=False)
    solucion = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=status_prueba_tecnica_opciones, default='E')
    leido = models.CharField(max_length=8, choices=leido_prueba_tecnica_opciones, default='N')

    def __str__(self):
        return f'{self.candidato} - {self.prueba}'

class AgendaEntrevista(models.Model):

    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    vacante = models.ForeignKey(Vacante, on_delete=models.CASCADE)
    room_id = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateField(blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)
    completa = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f'{self.candidato} - {self.vacante}'