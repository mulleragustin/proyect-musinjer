from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Socio
from .forms import SocioForm, GrupoFormSet, FiltroSocioForm
import openpyxl
from django.http import HttpResponse
from datetime import datetime
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
            try:
                socio.created_by = request.user
                socio = form.save()
                formset.instance = socio
                formset.save()
                return redirect('socios:socio_detail', socio_id=socio.socio_id)
            except IntegrityError:
                messages.error(request, 'El DNI o socio_id ya existe.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
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

		headers = ['Socio ID', 'DNI', 'Caracter', 'Apellido', 'Nombre', 'Sexo', 'Fecha de Nacimiento', 'Estado Civil', 'Dirección', 'Localidad', 'Celular', 'Teléfono', 'Email', 'Dependencia', 'Cargo', 'Función', 'Domicilio Laboral', 'Teléfono Laboral', 'Estado', 'Creado por', 'Modificado por', 'Fecha de Creación', 'Fecha de Actualización']
		sheet.append(headers)
		for socio in socios:
			row = [
				socio.socio_id,
				socio.dni,
				str(socio.caracter),  # Convertir a cadena de texto
				socio.apellido,
				socio.nombre,
				str(socio.sexo),  # Convertir a cadena de texto
				socio.fec_nac.strftime('%Y-%m-%d') if socio.fec_nac else '',
				str(socio.estado_civil),  # Convertir a cadena de texto
				socio.direccion,
				socio.localidad,
				socio.celular,
				socio.telefono,
				socio.email,
				socio.dependencia,
				socio.cargo,
				socio.funcion,
				socio.domicilio_laboral,
				socio.telefono_laboral,
				socio.estado,
				str(socio.created_by),  # Convertir a cadena de texto
				str(socio.modified_by),  # Convertir a cadena de texto
				socio.created_at.strftime('%Y-%m-%d %H:%M:%S') if socio.created_at else '',
				socio.updated_at.strftime('%Y-%m-%d %H:%M:%S') if socio.updated_at else ''
			]
			sheet.append(row)

		response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
		response['Content-Disposition'] = f'attachment; filename=socios-{datetime.now().strftime("%d")}-{datetime.now().strftime("%m")}-{datetime.now().strftime("%Y")}.xlsx'
		workbook.save(response)
		return response

	paginator = Paginator(socios, 10)
	page = request.GET.get('page')
	socios = paginator.get_page(page)

	return render(request, 'consulta.html', {'socios': socios, 'form': form})