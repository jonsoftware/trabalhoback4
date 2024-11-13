from .models import Funcionario, Falta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView



# views do Funcionario
class FuncionarioListView(ListView):
    model = Funcionario
    template_name= 'cadfun/funcionario_list.html'
    
class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = ["nome", "email", "telefone", "cargo", "data_de_admissao", "salario"]
    success_url = reverse_lazy("funcionario_list")

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = ["nome", "email", "telefone", "cargo", "data_de_admissao", "salario"]
    success_url = reverse_lazy('funcionario_list')
    
class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionario_list')
    

class FaltaListView(ListView):
    model = Falta
    template_name = 'cadfun/lista_faltas.html'
    context_object_name = 'faltas'

class FaltaCreateView(CreateView):
    model = Falta
    fields = ['data_falta', 'motivo', 'id_funcionario']
    template_name = 'cadfun/criar_falta.html'
    success_url = reverse_lazy('lista_faltas')

class FaltaUpdateView(UpdateView):
    model = Falta
    fields = ['data_falta', 'motivo', 'id_funcionario']
    template_name = 'cadfun/editar_falta.html'
    success_url = reverse_lazy('lista_faltas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        funcionario = self.object.id_funcionario 
        context['funcionario'] = funcionario
        return context

    def get_success_url(self):
        return reverse_lazy('lista_faltas')

class FaltaDeleteView(DeleteView):
    model = Falta
    template_name = 'cadfun/excluir_falta.html'
    success_url = reverse_lazy('lista_faltas')


class FuncionarioDetailView(DetailView):
    model = Funcionario
    template_name = 'cadfun/funcionario_profile.html'
    context_object_name = 'funcionario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        funcionario = self.get_object() 
        context['faltas'] = Falta.objects.filter(id_funcionario=funcionario)
        return context
