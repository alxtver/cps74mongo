from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Comp, CompItems, Pki
from .forms import PkiForm, PartForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')  # if not logged in redirect to /
def ind(request):
    return render(request, 'app74/ind.html', {'is_home': 'active'})


def login(request):
    return render(request, 'app74/login.html')


@login_required(login_url='/login')
def logout():
    return redirect('department74/login.html')


@login_required(login_url='/login')
def comp(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if 'select' in request.POST:
            select = request.POST['select']
            if select == '':
                return render(request, 'app74/comp.html', {'form': form, 'is_comp': 'active'})
            comps = Comp.objects.filter(part_id=select)
            comps_serial = [c.serial_number for c in comps]
            items = CompItems.objects.filter(comp__serial_number__in=comps_serial)
            return render(request, 'app74/comp.html', {
                'form': form,
                'comps': comps,
                'items': items,
                'is_comp': 'active'})
    form = PartForm()

    return render(request, 'app74/comp.html', {'form': form, 'is_comp': 'active'})


@login_required(login_url='/login')
def components_list(request):
    pki = Pki.objects.filter(date_of_arrival__lte=timezone.now()).order_by('date_of_arrival')
    errors = []
    notfound = ''
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Введите поисковый запрос!')
            return render(request, 'app74/components_list.html', {'pki': pki,
                                                                         'is_pki': 'active'})
        elif len(q) > 50:
            errors.append('Много символов!')
        else:
            names = Pki.objects.filter(name__icontains=q)
            serials = Pki.objects.filter(serial_number__icontains=q)
            types = Pki.objects.filter(name_type__name_type__icontains=q)
            part_names = Pki.objects.filter(part_name__part_name__icontains=q)
            matches = list(serials) + list(names) + list(types) + list(part_names)
            if not matches:
                notfound = 'Ничего не найдено'
            return render(request, 'app74/components_list.html', {
                'matches': matches,
                'query': q,
                'notfound': notfound,
                'is_pki': 'active'})

    return render(request, 'app74/components_list.html', {'errors': errors,
                                                                 'pki': pki,
                                                                 'is_pki': 'active'})


def components_new(request):
    if request.method == "POST":
        form = PkiForm(request.POST)
        if form.is_valid():
            new_component = form.save()
            new_component.save()
            return redirect('/components/new/')
    else:
        form = PkiForm()
    return render(request, 'app74/components_new.html', context={'form': form})