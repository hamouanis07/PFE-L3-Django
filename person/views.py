from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, TemplateView, ListView

from person.models import DocSigner
from .forms import UserLoginForm,Enseingantloginform
from . import models




class Homepage(TemplateView):
    template_name = 'person/index.html'



class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'person/login.html'
    success_url = reverse_lazy('pfe:EtudiantEmploiDutemp')


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            try:
                etudiant = models.etudiant.objects.get(numero=username)
            except:
                return HttpResponse('etudiant n\'exist pas ')
            user = etudiant.user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.success_url)
                else:
                    return HttpResponse('etudiant n\'est pas active ')
            else:
                return HttpResponse('etudiant n\'exist pas ')
        else:
            return HttpResponse('Erreur')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('pfe:EtudiantEmploiDutemp')
        return super(LoginView, self).get(request,*args,**kwargs)

class LoginViewEnseingnant(FormView):
    form_class = Enseingantloginform
    template_name = 'person/login.html'
    success_url = reverse_lazy('pfe:Enseingnat')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password = form.cleaned_data.get("password")
            try:
                Adminstartion = models.Adminstration.objects.get(user=User.objects.get(username=username))
            except:
                return HttpResponse('enseingnant n\'exist pas ')
            user = Adminstartion.user
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(self.success_url)
                else:
                    return HttpResponse('etudiant n\'est pas active ')
            else:
                return HttpResponse('etudiant n\'exist pas ')
        else:
            return HttpResponse('Erreur')


class EtudiantEmploiDutemp(LoginRequiredMixin,TemplateView):
    template_name = 'person/etudiant_emploi_s1.html'

    def get_context_data(self, **kwargs):
        context = super(EtudiantEmploiDutemp, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            etudiant = models.etudiant.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(EtudiantEmploiDutemp, self).get(request,*args,**kwargs)

class EtudiantEmploiDutemps2(LoginRequiredMixin,TemplateView):
    template_name = 'person/etudiant_emploi_s2.html'

    def get_context_data(self, **kwargs):
        context = super(EtudiantEmploiDutemps2, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context


class EtudiantEmploiDutempexamens1(LoginRequiredMixin,TemplateView):
    template_name = 'person/etudiant_emploi_s2.html'

    def get_context_data(self, **kwargs):
        context = super(EtudiantEmploiDutempexamens1, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context


class EtudiantEmploiDutempexamens2(LoginRequiredMixin,TemplateView):
    template_name = 'person/etudiant_emploi_s2.html'

    def get_context_data(self, **kwargs):
        context = super(EtudiantEmploiDutempexamens2, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

class pvs1(LoginRequiredMixin,ListView):
    template_name = 'person/pvs1.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(pvs1, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(pvs1, self).get_queryset()

        qs = qs.filter(Q(etudiant=models.etudiant.objects.get(user=self.request.user)) and Q(
                matierre__semstre='1'
            ))
        return qs

class pvs2(LoginRequiredMixin,ListView):
    template_name = 'person/pvs1.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(pvs2, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(pvs2, self).get_queryset()

        qs = qs.filter(Q(etudiant=models.etudiant.objects.get(user=self.request.user)) and Q(
                matierre__semstre='2'
            ))
        return qs


class Recours(LoginRequiredMixin,ListView):
    template_name = 'person/recours.html'
    model = models.recours

    def get_context_data(self, **kwargs):
        context = super(Recours, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(Recours, self).get_queryset()
        qs = qs.filter(etudiant=models.etudiant.objects.get(user=self.request.user))
        return qs


class Matiereresponsable(LoginRequiredMixin,TemplateView):
    template_name = 'person/respoonsable.html'

    def get_context_data(self, **kwargs):
        context = super(Matiereresponsable, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        matierre = models.matierre.objects.filter(parcour=models.etudiant.objects.get(user=self.request.user).parcour)
        context['s1'] = matierre.filter(semstre='1')
        context['s2'] = matierre.filter(semstre='2')
        return context


class Enseingnat(LoginRequiredMixin,TemplateView):
    template_name = 'person/enseingant.html'

    def get_context_data(self, **kwargs):
        context = super(Enseingnat, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context


class ListEtudiantL1(LoginRequiredMixin,ListView):
    template_name = 'person/liste_etudiant.html'
    model = models.etudiant

    def get_context_data(self, **kwargs):
        context = super(ListEtudiantL1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(ListEtudiantL1, self).get_queryset()
        qs = qs.filter(Q(parcour=1))
        return qs


class ListEtudiantL2(LoginRequiredMixin,ListView):
    template_name = 'person/liste_etudiant.html'
    model = models.etudiant

    def get_context_data(self, **kwargs):
        context = super(ListEtudiantL2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(ListEtudiantL2, self).get_queryset()
        qs = qs.filter(Q(parcour=2))
        return qs


class ListEtudiantL3(LoginRequiredMixin,ListView):
    template_name = 'person/liste_etudiant.html'
    model = models.etudiant

    def get_context_data(self, **kwargs):
        context = super(ListEtudiantL3, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(ListEtudiantL3, self).get_queryset()
        qs = qs.filter(Q(parcour=3))
        return qs


class ListEtudiantM1(LoginRequiredMixin,ListView):
    template_name = 'person/liste_etudiant.html'
    model = models.etudiant

    def get_context_data(self, **kwargs):
        context = super(ListEtudiantM1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(ListEtudiantM1, self).get_queryset()
        qs = qs.filter(Q(parcour=4))
        return qs


class ListEtudiantM2(LoginRequiredMixin,ListView):
    template_name = 'person/liste_etudiant.html'
    model = models.etudiant

    def get_context_data(self, **kwargs):
        context = super(ListEtudiantM2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(ListEtudiantM2, self).get_queryset()
        qs = qs.filter(Q(parcour=5))
        return qs


def DocaSigner(request):
    file = DocSigner.objects.all()
    return render(request, 'person/listeDocument.html', {'doc': file})

class NoteEtudiantL1(LoginRequiredMixin,ListView):
    template_name = 'person/note_etudiant.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(NoteEtudiantL1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(NoteEtudiantL1, self).get_queryset()
        qs = qs.filter(Q(etudiant__parcour=1))
        return qs

class NoteEtudiantL2(LoginRequiredMixin,ListView):
    template_name = 'person/note_etudiant.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(NoteEtudiantL2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(NoteEtudiantL2, self).get_queryset()
        qs = qs.filter(Q(etudiant__parcour=2))
        return qs

class NoteEtudiantL3(LoginRequiredMixin,ListView):
    template_name = 'person/note_etudiant.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(NoteEtudiantL3, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(NoteEtudiantL3, self).get_queryset()
        qs = qs.filter(Q(etudiant__parcour=3))
        return qs

class NoteEtudiantM1(LoginRequiredMixin,ListView):
    template_name = 'person/note_etudiant.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(NoteEtudiantM1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(NoteEtudiantM1, self).get_queryset()
        qs = qs.filter(Q(etudiant__parcour=4))
        return qs

class NoteEtudiantM2(LoginRequiredMixin,ListView):
    template_name = 'person/note_etudiant.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(NoteEtudiantM2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(NoteEtudiantM2, self).get_queryset()
        qs = qs.filter(Q(etudiant__parcour=5))
        return qs



class ProfEmploiDutemp(LoginRequiredMixin,TemplateView):
    template_name = 'person/ens_emploi.html'

    def get_context_data(self, **kwargs):
        context = super(ProfEmploiDutemp, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(ProfEmploiDutemp, self).get(request,*args,**kwargs)


class ProfEmploiDutemp2(LoginRequiredMixin,TemplateView):
    template_name = 'person/ens_emploi2.html'

    def get_context_data(self, **kwargs):
        context = super(ProfEmploiDutemp2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(ProfEmploiDutemp2, self).get(request,*args,**kwargs)


class PlanningCPCs1(LoginRequiredMixin,TemplateView):
    template_name = 'person/planning_cpc_s1.html'

    def get_context_data(self, **kwargs):
        context = super(PlanningCPCs1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PlanningCPCs1, self).get(request,*args,**kwargs)


class PlanningCPCs2(LoginRequiredMixin,TemplateView):
    template_name = 'person/planning_cpc_s2.html'

    def get_context_data(self, **kwargs):
        context = super(PlanningCPCs2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PlanningCPCs2, self).get(request,*args,**kwargs)

class PlanningPedagogique(LoginRequiredMixin,TemplateView):
    template_name = 'person/planning_pedagogique.html'

    def get_context_data(self, **kwargs):
        context = super(PlanningPedagogique, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PlanningPedagogique, self).get(request,*args,**kwargs)

class PlanningSurveillenceS1(LoginRequiredMixin,TemplateView):
    template_name = 'person/planning_surveillence_s1.html'

    def get_context_data(self, **kwargs):
        context = super(PlanningSurveillenceS1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PlanningSurveillenceS1, self).get(request,*args,**kwargs)

class PlanningSurveillenceS2(LoginRequiredMixin,TemplateView):
    template_name = 'person/planning_surveillence_s2.html'

    def get_context_data(self, **kwargs):
        context = super(PlanningSurveillenceS2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PlanningSurveillenceS2, self).get(request,*args,**kwargs)

class PvCpcS1(LoginRequiredMixin,TemplateView):
    template_name = 'person/pv_cpc_s1.html'

    def get_context_data(self, **kwargs):
        context = super(PvCpcS1, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PvCpcS1, self).get(request,*args,**kwargs)

class PvCpcS2(LoginRequiredMixin,TemplateView):
    template_name = 'person/pv_cpc_s2.html'

    def get_context_data(self, **kwargs):
        context = super(PvCpcS2, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PvCpcS2, self).get(request,*args,**kwargs)


class PvMatiere(LoginRequiredMixin,TemplateView):
    template_name = 'person/pv_matiere.html'

    def get_context_data(self, **kwargs):
        context = super(PvMatiere, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(PvMatiere, self).get(request,*args,**kwargs)


class DepPlanningCpc(LoginRequiredMixin,TemplateView):
    template_name = 'person/dep_planning_cpc.html'

    def get_context_data(self, **kwargs):
        context = super(DepPlanningCpc, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(DepPlanningCpc, self).get(request,*args,**kwargs)


class RecoursNote(LoginRequiredMixin,ListView):
    template_name = 'person/recours_note.html'
    model = models.recours

    def get_context_data(self, **kwargs):
        context = super(RecoursNote, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(RecoursNote, self).get_queryset()
        qs = qs.filter(recours='2')
        return qs

class RecoursGroupe(LoginRequiredMixin,ListView):
    template_name = 'person/recours_groupe.html'
    model = models.recours

    def get_context_data(self, **kwargs):
        context = super(RecoursGroupe, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(RecoursGroupe, self).get_queryset()
        qs = qs.filter(recours='1')
        return qs


class pvs2(LoginRequiredMixin,ListView):
    template_name = 'person/pvs1.html'
    model = models.note

    def get_context_data(self, **kwargs):
        context = super(pvs2, self).get_context_data()
        context['etudiant'] = models.etudiant.objects.get(user=self.request.user)
        return context

    def get_queryset(self):
        qs = super(pvs2, self).get_queryset()

        qs = qs.filter(Q(etudiant=models.etudiant.objects.get(user=self.request.user)) and Q(
                matierre__semstre='2'
            ))
        return qs

class FicheDeVoeuxMaster(LoginRequiredMixin,TemplateView):
    template_name = 'person/fiche_de_voeux_master.html'

    def get_context_data(self, **kwargs):
        context = super(FicheDeVoeuxMaster, self).get_context_data()
        context['enseingnat'] = models.Adminstration.objects.get(user=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        try:
            enseignant = models.Adminstration.objects.get(user=self.request.user)
        except:
            raise Http404
        return super(FicheDeVoeuxMaster, self).get(request,*args,**kwargs)

