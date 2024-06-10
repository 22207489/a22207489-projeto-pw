from django.shortcuts import render
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect




# Create your views here.
from .models import Curso, Areas_Cientifica, Disciplina, Projeto, Linguagens_de_Programacoe, Docente, CursoForm, Areas_CientificaForm, DisciplinaForm, ProjetoForm, Linguagens_de_ProgramacoeForm, DocenteForm


def edita_curso(user):
    return user.groups.filter(name = 'Cursos').exists()

# Index
def index_view(request):
    context = {
        'cursos': Curso.objects.all(),
        'is_editor' : edita_curso(request.user)
    }
    return render(request, "curso/index.html", context)









#Curso
def curso_view(request, curso_id):
    context = {
        'curso': Curso.objects.get(id=curso_id),
        'areas_cientificas': Areas_Cientifica.objects.filter(curso = Curso.objects.get(id=curso_id)),
        'is_editor' : edita_curso(request.user)
    }
    return render(request, "curso/curso.html", context)

@login_required
@user_passes_test(edita_curso)
def novo_curso_view(request):

    form = CursoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('curso:cursos')

    context = {'form': form}
    return render(request, 'editar/novo_curso.html', context)



@login_required
@user_passes_test(edita_curso)
def edita_curso_view(request,curso_id):
    curso_certo = Curso.objects.get(id=curso_id)

    if request.POST:
        form = CursoForm(request.POST or None, request.FILES, instance=curso_certo)
        if form.is_valid():
            form.save()
            return redirect('curso:curso', curso_id=curso_id)
    else:
        form = CursoForm(instance=curso_certo)  # cria formulário com dados da instância autor

    context = {'form': form, 'curso':curso_certo}
    return render(request, 'editar/edita_curso.html', context)





def apaga_curso_view(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    curso.delete()
    return redirect('curso:cursos')
#feito










#Area Cientifica
def area_cientifica_view(request, area_id):
    context = {
        'area': Areas_Cientifica.objects.get(id=area_id),
        'disciplinas':Disciplina.objects.filter(area_cientifica=Areas_Cientifica.objects.get(id=area_id)),
        'is_editor' : edita_curso(request.user)
    }
    return render(request, "curso/area.html", context)

@login_required
@user_passes_test(edita_curso)
def nova_area_view(request, curso_id):
    curso_certo = Curso.objects.get(id = curso_id)
    form = Areas_CientificaForm(request.POST or None, request.FILES)

    if form.is_valid():
        area = form.save(commit=False)
        area.curso = curso_certo
        area.save()
        return redirect('curso:curso', curso_id=curso_id)

    context = {'form': form}
    return render(request, 'editar/nova_area.html', context)

def apaga_area_view(request, area_id):
    area = Areas_Cientifica.objects.get(id=area_id)
    curso_id = area.curso.id
    area.delete()
    return redirect('curso:curso', curso_id=curso_id)







#Disciplina
def disciplina_view(request, disciplina_id):
    context = {
        'disciplina': Disciplina.objects.get(id = disciplina_id),
        'projetos':Projeto.objects.filter(disciplina = Disciplina.objects.get(id = disciplina_id)),
        'is_editor' : edita_curso(request.user)
        }
    return render(request, "curso/disciplina.html", context)

@login_required
@user_passes_test(edita_curso)
def nova_disciplina_view(request, area_id):
    area_certa = Areas_Cientifica.objects.get(id = area_id)
    form = DisciplinaForm(request.POST or None, request.FILES)

    if form.is_valid():
        disciplina = form.save(commit=False)
        disciplina.area_cientifica = area_certa
        disciplina.save()
        return redirect('curso:area', area_id=area_id)

    context = {'form': form}
    return render(request, 'editar/nova_disciplina.html', context)


@login_required
@user_passes_test(edita_curso)
def edita_disciplina_view(request,disciplina_id):
    disciplina_certa = Disciplina.objects.get(id=disciplina_id)

    if request.POST:
        form = DisciplinaForm(request.POST or None, request.FILES, instance=disciplina_certa)
        if form.is_valid():
            form.save()
            return redirect('curso:disciplina', disciplina_id=disciplina_id)
    else:
        form = DisciplinaForm(instance=disciplina_certa)  # cria formulário com dados da instância autor

    context = {'form': form, 'disciplina':disciplina_certa}
    return render(request, 'editar/edita_disciplina.html', context)

def apaga_disciplina_view(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    area_id = disciplina.area.id
    disciplina.delete()
    return redirect('curso:area', area_id=area_id)

#feito





#Projeto
def projeto_view(request, projeto_id):
    context = {
        'projeto': Projeto.objects.get(id=projeto_id),'is_editor' : edita_curso(request.user)}
    return render(request, "curso/projeto.html", context)

@login_required
@user_passes_test(edita_curso)
def novo_projeto_view(request,disciplina_id):
    disciplina_certa = Disciplina.objects.get(id = disciplina_id)
    form = ProjetoForm(request.POST or None, request.FILES)

    if form.is_valid():
        projeto = form.save(commit=False)
        projeto.disciplina = disciplina_certa
        projeto.save()
        return redirect('curso:disciplina', disciplina_id=disciplina_id)

    context = {'form': form}
    return render(request, 'editar/novo_projeto.html', context)

@login_required
@user_passes_test(edita_curso)
def edita_projeto_view(request, projeto_id):
    projeto_certo = Projeto.objects.get(id=projeto_id)

    if request.POST:
        form = ProjetoForm(request.POST or None, request.FILES, instance=projeto_certo)
        if form.is_valid():
            form.save()
            return redirect('curso:projeto', projeto_id=projeto_id)
    else:
        form = ProjetoForm(instance=projeto_certo)  # cria formulário com dados da instância autor

    context = {'form': form, 'projeto':projeto_certo}
    return render(request, 'editar/edita_projeto.html', context)

def apaga_projeto_view(request, projeto_id):
    projeto = Projeto.objects.get(id=projeto_id)
    disciplina_id = projeto.disciplina.id
    projeto.delete()
    return redirect('curso:disciplina', disciplina_id=disciplina_id)




#Linguagens de Programação
@login_required
@user_passes_test(edita_curso)
def nova_linguagem_view(request,projeto_id):
    form = Linguagens_de_ProgramacoeForm(request.POST or None, request.FILES)

    if form.is_valid():
        linguagem = form.save(commit=False)
        linguagem.save()
        return redirect('curso:projeto', projeto_id = projeto_id)

    context = {'form': form}
    return render(request, 'editar/nova_linguagem.html', context)







#Docentes
@login_required
@user_passes_test(edita_curso)
def novo_docente_view(request,disciplina_id):
    disciplina_certa = Disciplina.objects.get(id = disciplina_id)
    form = DocenteForm(request.POST or None, request.FILES)

    if form.is_valid():
        docente = form.save(commit=False)
        docente.disciplina = disciplina_certa
        docente.save()
        return redirect('curso:disciplina', disciplina_id=disciplina_id)

    context = {'form': form}
    return render(request, 'editar/novo_docente.html', context)









