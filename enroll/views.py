from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistation
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.

class AddShowView(TemplateView):
    template_name='enroll/addandshow.html'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        fm=StudentRegistation()
        stud=User.objects.all()
        context={'stu':stud,'form':fm}
        return context
    def post(self,request):
        fm=StudentRegistation(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm=StudentRegistation()
            return HttpResponseRedirect('/mohd/')



# this class will update/edit

class UpdateView(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistation(instance=pi)
        return render(request,'enroll/update.html' ,{'form':fm})
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=StudentRegistation(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return render(request,'enroll/update.html' ,{'form':fm})

# this class will delete

class DeleteView(RedirectView):
    url='/mohd/'
    def get_redirect_url(self,*args,**kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)

