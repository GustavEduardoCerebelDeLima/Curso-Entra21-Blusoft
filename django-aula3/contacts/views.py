from django.shortcuts import render
from .models import Contact, Category


def index(request):
    contacts = Contact.objects.order_by('name')
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def see_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contacts/see_contact.html', {
        'contact': contact
    })


def see_family(request, contact_category):
    contact = Contact.objects.get(categories=contact_category).filter(
        categories=1
    )
    return render(request, 'contacts/see_family.html', {
        'contact': contact
    })


def see_friends(request, contact_category):
    contact = Contact.objects.get(categories=contact_category).filter(
        categories=2
    )
    return render(request, 'contacts/see_friends.html', {
        'contact': contact
    })


def see_company(request, contact_category):
    contact = Contact.objects.get(categories=contact_category).filter(
        categories=3
    )
    return render(request, 'contacts/see_company.html', {
        'contact': contact
    })


