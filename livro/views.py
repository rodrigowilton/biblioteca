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

        usuarios = Usuario.objects.all()

        return render(request,'home.html', {'livros' : livros, 'usuario_logado': request.session.get('usuario'),
                                            'form': form, 'status_categoria': status_categoria,'form_categoria': form_categoria,
                                            'usuarios':usuarios})
    else:
        return redirect('/auth/login/?status=2')


def ver_livros(request, id):
    if request.session.get('usuario'):
        livro = Livros.objects.get(id=id)
        if request.session.get('usuario') == livro.usuario.id:
            usuario = Usuario.objects.get(id=request.session['usuario'])
            categoria_livro = Categoria.objects.filter(usuario = request.session.get('usuario'))
            emprestimos = Emprestimos.objects.filter(livro = livro)
            form = CadastroLivro()
            form.fields['usuario'].initial = request.session['usuario']
            form.fields['categoria'].queryset = Categoria.objects.filter(usuario=usuario)

            form_categoria = CategoriaLivro()
            usuarios =  Usuario.objects.all()

            livros = Livros.objects.filter(usuario_id = request.session.get('usuario'))

            return render(request, 'ver_livro.html',{'livro': livro, 'categoria_livro': categoria_livro, 'emprestimos': emprestimos,
                                                     'usuario_logado':request.session.get('usuario'),'form':form, 'form_categoria': form_categoria,
                                                     'id_livro': id, 'livros':livros, 'usuarios':usuarios })
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


def cadastrar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
        
        if nome_emprestado_anonimo:
            emprestimo = Emprestimos(nome_emprestado_anonimo=nome_emprestado_anonimo,
                                 livro_id=livro_emprestado)
        else:
            emprestimo = Emprestimos(nome_emprestado_id=nome_emprestado,
                                     livro_id=livro_emprestado)
        emprestimo.save()
        

    return HttpResponse("Emprestado com sucesso")