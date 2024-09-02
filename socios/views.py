from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Socio
from .forms import SocioForm, GrupoFormSet, FiltroSocioForm
import openpyxl
from django.http import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def socio_create_update(request, socio_id=None):
	if socio_id:
		socio = get_object_or_404(Socio, pk=socio_id)
	else:
		socio = Socio()
	
	if request.method == 'POST':
		form = SocioForm(request.POST, instance=socio)
		formset = GrupoFormSet(request.POST, instance=socio)
		if form.is_valid() and formset.is_valid():
			socio = form.save(user=request.user)
			formset.instance = socio
			formset.save()
			return redirect('socios:socio_detail', socio_id=socio.socio_id)
	else:
		form = SocioForm(instance=socio)
		formset = GrupoFormSet(instance=socio)

	return render(request, 'socios.html', {'form': form, 'formset': formset})

@login_required
def socio_delete(request, socio_id):
    socio = get_object_or_404(Socio, pk=socio_id)
    socio.delete()
    return redirect(reverse('home'))

@login_required
def socio_detail(request, socio_id):
	socio = get_object_or_404(Socio, pk=socio_id)
	return render(request, 'socio_detail.html', {'socio': socio})

@login_required
def socio_list(request):
	form = FiltroSocioForm(request.GET)
	socios = Socio.objects.all()
	
	if request.GET and form.is_valid():
		if form.cleaned_data['socio_id']:
			socios = socios.filter(socio_id=form.cleaned_data['socio_id'])
		if form.cleaned_data['dni']:
			socios = socios.filter(dni=form.cleaned_data['dni'])
		if form.cleaned_data['apellido']:
			socios = socios.filter(apellido__icontains=form.cleaned_data['apellido'])
		if form.cleaned_data['nombre']:
			socios = socios.filter(nombre__icontains=form.cleaned_data['nombre'])
		if form.cleaned_data['estado']:
			socios = socios.filter(estado=form.cleaned_data['estado'])
	
	if request.GET.get('formato') == 'excel':
		workbook = openpyxl.Workbook()
		sheet = workbook.active
		sheet.title = 'Socios' + datetime.now().strftime('%Y%m%d')

		headers = ['Socio ID', 'DNI', 'Apellido', 'Nombre', 'Localidad', 'Teléfono']
		sheet.append(headers)
		for socio in socios:
			sheet.append([socio.socio_id, socio.dni, socio.apellido, socio.nombre, socio.localidad, socio.telefono])

		response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		response['Content-Disposition'] = 'attachment; filename=socios.xlsx'
		workbook.save(response)
		return response

	paginator = Paginator(socios, 1)
	page = request.GET.get('page')
	socios = paginator.get_page(page)

	return render(request, 'consulta.html', {'socios': socios, 'form': form})