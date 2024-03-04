from django.db import models
from datetime import datetime, timedelta



# Create your models here.

class Clinica(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    responsables = models.ManyToManyField('usuarios.CustomUser', related_name='clinicas_responsables', blank=True)
    logo = models.ImageField(upload_to='clinicas/', blank=True, null=True)
    correo_electronico = models.EmailField(max_length=255, null=True, blank=True)
    equipamiento = models.CharField(max_length=255, null=True, blank=True)
    numero_consultorios = models.IntegerField(null=True)
    lunes = models.BooleanField(default=False)
    martes = models.BooleanField(default=False)
    miercoles = models.BooleanField(default=False)
    jueves = models.BooleanField(default=False)
    viernes = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)

    MUNICIPIOS = [
        ('AMAXAC DE GUERRERO', 'AMAXAC DE GUERRERO'),
        ('ACUAMANALA DE MIGUEL HIDALGO', 'ACUAMANALA DE MIGUEL HIDALGO'),
        ('ALTLANCA', 'ALTLANCA'),
        ('AMAXAC DE GUERRERO', 'AMAXAC DE GUERRERO'),
        ('APIZACO', 'APIZACO'),
        ('ATLANGATEPEC', 'ATLANGATEPEC'),
        ('BENITO JUÁREZ', 'BENITO JUÁREZ'),
        ('CALPULALPAN', 'CALPULALPAN'),
        ('CHIAUTEMPAN', 'CHIAUTEMPAN'),
        ('CONTLA DE JUAN CUAMATZI', 'CONTLA DE JUAN CUAMATZI'),
        ('CUAPIAXTLA', 'CUAPIAXTLA'),
        ('CUAXOMULCO', 'CUAXOMULCO'),
        ('EL CARMEN TEQUEXQUITLA', 'EL CARMEN TEQUEXQUITLA'),
        ('EMILIANO ZAPATA', 'EMILIANO ZAPATA'),
        ('ESPAÑITA', 'ESPAÑITA'),
        ('HUAMANTLA', 'HUAMANTLA'),
        ('HUEYOTLIPAN', 'HUEYOTLIPAN'),
        ('IXTACUIXTLA DE MARIANO MATAMOROS', 'IXTACUIXTLA DE MARIANO MATAMOROS'),
        ('IXTENCO', 'IXTENCO'),
        ('LA MAGDALENA TLALTELULCO', 'LA MAGDALENA TLALTELULCO'),
        ('LÁZARO CÁRDENAS', 'LÁZARO CÁRDENAS'),
        ('MAZATECOCHCO DE JOSÉ MARÍA MORELOS', 'MAZATECOCHCO DE JOSÉ MARÍA MORELOS'),
        ('MUÑOZ DE DOMINGO ARENAS', 'MUÑOZ DE DOMINGO ARENAS'),
        ('NANACAMILPA DE MARIANO ARISTA', 'NANACAMILPA DE MARIANO ARISTA'),
        ('NATIVITAS', 'NATIVITAS'),
        ('PANOTLA', 'PANOTLA'),
        ('PAPALOTLA DE XICOHTÉNCATL', 'PAPALOTLA DE XICOHTÉNCATL'),
        ('SAN DAMIÁN TEXOLOC', 'SAN DAMIÁN TEXOLOC'),
        ('SAN FRANCISCO TETLANOHCAN', 'SAN FRANCISCO TETLANOHCAN'),
        ('SAN JERÓNIMO ZACUALPAN', 'SAN JERÓNIMO ZACUALPAN'),
        ('SAN JOSÉ TEACALCO', 'SAN JOSÉ TEACALCO'),
        ('SAN JUAN HUACTZINCO', 'SAN JUAN HUACTZINCO'),
        ('SAN LORENZO AXOCOMANITLA', 'SAN LORENZO AXOCOMANITLA'),
        ('SAN LUCAS TECOPILCO', 'SAN LUCAS TECOPILCO'),
        ('SAN PABLO DEL MONTE', 'SAN PABLO DEL MONTE'),
        ('SANCTORUM DE LÁZARO CÁRDENAS', 'SANCTORUM DE LÁZARO CÁRDENAS'),
        ('SANTA ANA NOPALUCAN', 'SANTA ANA NOPALUCAN'),
        ('SANTA APOLONIA TEACALCO', 'SANTA APOLONIA TEACALCO'),
        ('SANTA CATARINA AYOMETLA', 'SANTA CATARINA AYOMETLA'),
        ('SANTA CRUZ QUILEHTLA', 'SANTA CRUZ QUILEHTLA'),
        ('SANTA CRUZ TLAXCALA', 'SANTA CRUZ TLAXCALA'),
        ('SANTA ISABEL XILOXOXTLA', 'SANTA ISABEL XILOXOXTLA'),
        ('TEOLOCHOLCO', 'TEOLOCHOLCO'),
        ('TEPETITLA DE LARDIZÁBAL', 'TEPETITLA DE LARDIZÁBAL'),
        ('TETLA DE LA SOLIDARIDAD', 'TETLA DE LA SOLIDARIDAD'),
        ('TETLATLAHUCA', 'TETLATLAHUCA'),
        ('TLAXCALA', 'TLAXCALA'),
        ('TLAXCO', 'TLAXCO'),
        ('TOTOLAC', 'TOTOLAC'),
        ('TOCATLÁN', 'TOCATLÁN'),
        ('TZOMPANTEPEC', 'TZOMPANTEPEC'),
        ('XALOZTOC', 'XALOZTOC'),
        ('XALTOCAN', 'XALTOCAN'),
        ('YAUHQUEMEHCAN', 'YAUHQUEMEHCAN'),
        ('ZACATELCO', 'ZACATELCO'),
        ('ZITLALTEPEC DE TRINIDAD SÁNCHEZ SANTOS', 'ZITLALTEPEC DE TRINIDAD SÁNCHEZ SANTOS'),
    ]

    municipio = models.CharField(choices=MUNICIPIOS, max_length=50, null=True)

    def generar_horas_entre(self):
        hora_actual = datetime.combine(datetime.today(), self.hora_inicio)
        hora_fin = datetime.combine(datetime.today(), self.hora_fin)

        horas_entre = []
        while hora_actual <= hora_fin:
            horas_entre.append(hora_actual.time())
            hora_actual += timedelta(minutes=60)

        return horas_entre
    
    def dias_true(self):
        dias_true = []
        if self.lunes:
            dias_true.append('lunes')
        if self.martes:
            dias_true.append('martes')
        if self.miercoles:
            dias_true.append('miércoles')
        if self.jueves:
            dias_true.append('jueves')
        if self.viernes:
            dias_true.append('viernes')
        if self.sabado:
            dias_true.append('sábado')
        return dias_true
    
    def get_responsables_list(self):
        return self.responsables.all()

    def __str__(self):
        return self.nombre