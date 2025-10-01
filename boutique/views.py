from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from .models import Produit
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def accueil(request):
    return render(request, 'boutique/accueil.html')


def categories(request):
    produits_liste = Produit.objects.all()
    paginator = Paginator(produits_liste, 8)  # Show 8 produits per page
    page_number = request.GET.get('page')
    produits = paginator.get_page(page_number)
    return render(request, 'boutique/categories.html', {'produits': produits})


def liste_produits(request):
    query = request.GET.get('q', '')
    produits_list = Produit.objects.all().order_by('-id')  # trié par ID décroissant

    if query:
        produits_list = produits_list.filter(
            Q(titre__icontains=query) | Q(description__icontains=query)
        )

    paginator = Paginator(produits_list, 4)  # 4 produits par page
    page_number = request.GET.get('page')
    produits = paginator.get_page(page_number)

    return render(request, 'boutique/categories.html', {
        'produits': produits,
        'query': query
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            message = form.cleaned_data['message']
            
            send_mail(
                f'Contact depuis le site : {nom}',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['thierry.toure67@gmail.com'],  # tu peux mettre ton email ici
                fail_silently=False,
            )
            
            messages.success(request, 'Merci ! Votre message a été envoyé.')
            form = ContactForm()  # réinitialise le formulaire
    else:
        form = ContactForm()
    
    return render(request, 'boutique/contact.html', {'form': form})
