from django.shortcuts import render
from .models import Banda, Album, Musica,BandaForm, AlbumForm, MusicaForm
from django.contrib.auth.decorators import login_required, user_passes_test



def edita_banda(user):
    return user.groups.filter(name = 'Bandas').exists()



from django.shortcuts import redirect

def index_view(request):
    context = {
        'bandas': Banda.objects.all().order_by('nome'),
        'is_editor' : edita_banda(request.user),
    }
    return render(request, "bandasNovas/index.html", context)




#Banda--------------------------------------------------------------------------------------------------------------------------------------------
def banda_view(request, banda_id):
    context = {
        'banda': Banda.objects.get(id=banda_id),
        'albums':Album.objects.filter(banda=Banda.objects.get(id=banda_id)),
        'is_editor' : edita_banda(request.user),

    }
    return render(request, "bandasNovas/banda.html", context)

@login_required
@user_passes_test(edita_banda)
def nova_banda_view(request):

    form = BandaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandasNovas:bandas')

    context = {'form': form}
    return render(request, 'editar/nova_banda.html', context)


@login_required
@user_passes_test(edita_banda)
def edita_banda_view(request,banda_id):
    banda_certa = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda_certa)
        if form.is_valid():
            form.save()
            return redirect('bandasNovas:banda', banda_id=banda_id)
    else:
        form = BandaForm(instance=banda_certa)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda_certa}
    return render(request, 'editar/edita_banda.html', context)



def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandasNovas:bandas')
#Feito--------------------------------------------------------------------------------------------------------------------------------------------









#Album--------------------------------------------------------------------------------------------------------------------------------------------
def album_view(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'musicas': Musica.objects.filter(album = Album.objects.get(id=album_id)),
        'is_editor' : edita_banda(request.user),
    }
    return render(request, "bandasNovas/album.html", context)






@login_required
@user_passes_test(edita_banda)
def novo_album_view(request, banda_id):
    banda_certa = Banda.objects.get(id = banda_id)
    form = AlbumForm(request.POST or None, request.FILES)

    if form.is_valid():
        album = form.save(commit=False)
        album.banda = banda_certa
        album.save()
        return redirect('bandasNovas:banda', banda_id=banda_id)

    context = {'form': form}
    return render(request, 'editar/novo_album.html', context)





@login_required
@user_passes_test(edita_banda)
def edita_album_view(request,album_id):
    album_certo = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=album_certo)
        if form.is_valid():
            form.save()
            return redirect('bandasNovas:album', album_id=album_id)
    else:
        form = AlbumForm(instance=album_certo)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album_certo}
    return render(request, 'editar/edita_album.html', context)




def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    banda_id = album.banda.id
    album.delete()
    return redirect('bandasNovas:banda', banda_id=banda_id)
#Feito--------------------------------------------------------------------------------------------------------------------------------------------







#Musica--------------------------------------------------------------------------------------------------------------------------------------------

def musica_view(request, musica_id):
    context = {
        'musica': Musica.objects.get(id=musica_id),
        'is_editor' : edita_banda(request.user),
    }
    return render(request, "bandasNovas/musica.html", context)


@login_required
@user_passes_test(edita_banda)
def nova_musica_view(request, album_id):
    album_certo = Album.objects.get(id = album_id)
    form = MusicaForm(request.POST or None, request.FILES)

    if form.is_valid():
        musica = form.save(commit=False)
        musica.album = album_certo
        musica.save()
        return redirect('bandasNovas:album', album_id=album_id)

    context = {'form': form}
    return render(request, 'editar/nova_musica.html', context)

@login_required
@user_passes_test(edita_banda)
def edita_musica_view(request,musica_id):
    musica_certa = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica_certa)
        if form.is_valid():
            form.save()
            return redirect('bandasNovas:musica', musica_id=musica_id)
    else:
        form = MusicaForm(instance=musica_certa)  # cria formulário com dados da instância autor

    context = {'form': form, 'musica':musica_certa}
    return render(request, 'editar/edita_musica.html', context)



def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    album_id = musica.album.id
    musica.delete()
    return redirect('bandasNovas:album', album_id=album_id)
#Feito--------------------------------------------------------------------------------------------------------------------------------------------














