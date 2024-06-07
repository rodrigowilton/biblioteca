from django.shortcuts import render, redirect
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Livros, Categoria, Emprestimos
from .forms import CadastroLivro, CategoriaLivro



def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        status_categoria = request.GET.get('cadastro_categoria')
        livros = Livros.objects.filter(usuario = usuario)
        form = CadastroLivro()
        form.fields['usuario'].initial = request.session['usuario']
        form.fields['categoria'].queryset = Categoria.objects.filter(usuario = usuario)
        form_categoria = CategoriaLivro()

        return render(request,'home.html', {'livros' : livros, 'usuario_logado': request.session.get('usuario'),
                                            'form': form, 'status_categoria': status_categoria,'form_categoria': form_categoria})
    else:
        return redirect('/auth/login/?status=2')
    
    
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        if request.session.get('usuario') == livros.usuario.id:
            usuario = Usuario.objects.get(id=request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livros)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

            form_categoria = CategoriaLivro()

            return render(request, 'ver_livro.html',{'livro': livros, 'categoria_livro': categoria_livro, 'emprestimos': emprestimos,
                                                     'usuario_logado':request.session.get('usuario'),'form':form, 'form_categoria': form_categoria, 'id_livro': id })
        else:
            return HttpResponse('Esse livro não é seu')
    return redirect('/auth/login/?status=2')


def cadastrar_livro(request):
    if request.method == 'POST':
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/livro/home/')
        else:
            return HttpResponse("Dados Inválido")

def excluir_livro(request, id):
    livro = Livros.objects.get(id = id).delete()
    return redirect('/livro/home')


def cadastrar_categoria(request):
    if request.method == 'POST':
        form = CategoriaLivro(request.POST)
        if form.is_valid():
            id_usuario = request.session.get('usuario')
            nome = form.data['nome']
            descricao = form.data['descricao']
            user = request.session.get('usuario')
            if int(id_usuario) == int(user):
                categoria = Categoria(nome=nome, descricao=descricao, usuario_id=id_usuario)
                categoria.save()
                return redirect('/livro/home/?cadastro_categoria=1')
            else:
                return HttpResponse("Erro: Usuário inválido")
        else:
            return HttpResponse("Erro no formulário")
    else:
        return HttpResponse("Método inválido")