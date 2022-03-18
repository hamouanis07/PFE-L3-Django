from django.conf import settings
from django.db import models

# Create your models here.
class person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    class Meta:
        abstract = True

ANNE_CHOICES = (
        (1, 'L1'),
        (2, 'L2'),
        (3, 'L3'),
        (4, 'M1 SITW'),
        (4, 'M1 RSD'),
        (4, 'M1 RESIM'),
        (4, 'M1 ADSI'),
        (4, 'M1 IIPE'),
        (5, 'M2 SITW'),
        (5, 'M2 RSD'),
        (5, 'M2 RESIM'),
        (5, 'M2 ADSI'),
        (5, 'M2 IIPE'),
        (10, 'D'),
)
SEMESTRE_CHOICES = (('1','s1'),('2','s2'))



class etudiant(person):
    parcour = models.IntegerField(choices=ANNE_CHOICES)
    numero = models.IntegerField(unique=True)
    def __str__(self):
        return self.nom



GRADE_CHOICES = (
        ('P', 'PES'),
        ('A', 'ASS'),
        ('M', 'MAB'),
        ('M', 'MAA'),
        ('M', 'MCB'),
        ('M', 'MCA'),
        ('P', 'PROF'),
)
class roles(models.Model):
    role = models.CharField(max_length=255)
    def __str__(self):
        return self.role

class Adminstration(person):
    roles = models.ForeignKey(roles,on_delete=models.CASCADE)
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES)

    def __str__(self):
        return self.nom

class Secretaire(person):
    pass


class matierre(models.Model):
    matierre = models.CharField(max_length=255)
    parcour = models.IntegerField(choices=ANNE_CHOICES)
    semstre = models.CharField(choices=SEMESTRE_CHOICES, max_length=1)
    coef = models.IntegerField()
    responsable = models.OneToOneField(Adminstration,on_delete=models.CASCADE)
    enseignant = models.ManyToManyField(Adminstration,related_name="prof")

    def __str__(self):
        return self.matierre


class note(models.Model):
    note_td = models.FloatField()
    note_tp = models.FloatField()
    note_cour = models.FloatField()
    note_examen = models.FloatField()
    moyenne = models.FloatField()
    matierre = models.OneToOneField(matierre,on_delete=models.CASCADE)
    etudiant = models.OneToOneField(etudiant,on_delete=models.CASCADE)

    def __str__(self):
        return self.etudiant.nom + '/' + self.matierre.matierre

    class Meta:
        unique_together = ('matierre', 'etudiant')

RECOURS_CHOICES = (
        ('1', 'changement de groupe'),
        ('2', 'changement des notes'),
)
ETATS_CHOICES = (
        ('1', 'ACCEPTÉ'),
        ('2', 'REFFUSÉ'),
        ('3', 'PAS DE DESSISION'),
)


class recours(models.Model):
    etudiant = models.ForeignKey(etudiant,on_delete=models.CASCADE)
    recours = models.CharField(choices=RECOURS_CHOICES, max_length=1)
    remarque = models.TextField()
    accepte = models.CharField(max_length=1,choices=ETATS_CHOICES)
    def __str__(self):
        return self.etudiant.nom

class Cpc(models.Model):
    semsetre = models.CharField(max_length=1,choices=SEMESTRE_CHOICES)
    parcour = models.IntegerField(choices=ANNE_CHOICES)
    responsable = models.OneToOneField(Adminstration,related_name="responsable",on_delete=models.CASCADE)
    date_cpc = models.CharField(max_length=20)
    def __str__(self):
        return str(self.get_parcour_display()) + '/' + str(self.get_semsetre_display())


class DocSigner(models.Model):
    nom_doc = models.CharField(max_length=200)
    url_doc = models.FileField(null=True, blank=True)
    destination = models.ForeignKey(Adminstration,on_delete=models.CASCADE,default='')

    def __str__(self):
        return str(self.nom_doc)
#etudiant
# nom et prenom  parcours anne en haut
# emploi du temp de semstre s1 et s2 static
# emploi du temp examen static
# listes des pv s1 et s2
# liste des profs responsable de la matiere
# la liste des recours

# enseignant
# nom prenom grade et profile
# filtrer les pv par anné et matiere
# emploi du temp static

#adjoint post graduation
# dossier dossier des doctorant static

# chef scolaritè:
# listed des etudiant pv de soutnance de chaque etudiant
# pv de delibiration pv #s1 et s2
# les document static chaque etudiant avec groupe

#responsable cpc
#pv cpc documetn static semstre
#pv matiere par module et semstre
#planing
# les recours

#responsable de domain
# voir les pv des matiere

#adjoin pedagogique
#planing de surviallance
#planing de soutnance

#chef de departement
#planing de doctorat
#document a signer


#resposable ed matiere
#voire et envoyè pv matiere au resposnsable d'ènutié
#

#responsable d'enitè
# voir et envoyè le pv d'enutè

#secretaire/
#consulte le planing de soutnance
#consulter pv matiere
#consulter planing cpc
#voir les justificatif absence
#voir les justificatif recour
#voir les fiche des voeux de matiere
