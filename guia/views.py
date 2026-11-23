from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ConsultaComposta
from .forms import ConsultaForm, CalculadoraForm

def inicio(request):
    resultado_calculadora = None
    calc_form = CalculadoraForm()
    consulta_form = ConsultaForm()

    if request.method == 'POST':
        # Procesar la calculadora
        if 'btn_calcular' in request.POST:
            calc_form = CalculadoraForm(request.POST)
            if calc_form.is_valid():
                verdes = calc_form.cleaned_data['cantidad_verdes']
                resultado_calculadora = {
                    'verdes': verdes,
                    'marrones': round(verdes * 2.5, 2), # Proporción ideal 2.5:1
                    'agua_estimada': round(verdes * 0.2, 2)
                }

        # Procesar nueva duda
        elif 'btn_preguntar' in request.POST:
            consulta_form = ConsultaForm(request.POST)
            if consulta_form.is_valid():
                consulta_form.save()
                messages.success(request, '¡Tu duda ha sido enviada! Pronto aparecerá respondida aquí.')
                return redirect('inicio')

    consultas = ConsultaComposta.objects.all()[:5] # Últimas 5 consultas

    contexto = {
        'materiales_verdes': [
            'Restos de frutas y verduras',
            'Posos de café y bolsitas de té (sin grapas)',
            'Cáscaras de huevo trituradas',
            'Césped recién cortado y plantas verdes',
        ],
        'materiales_marrones': [
            'Hojas secas y ramas pequeñas',
            'Cartón y papel sin tinta brillante (troceado)',
            'Aserrín o virutas de madera no tratada',
            'Paja o heno seco',
        ],
        'no_compostar': [
            'Carnes, huesos y pescados (atraen plagas)',
            'Lácteos, aceites y grasas',
            'Heces de perros o gatos',
            'Plásticos, metales o vidrios',
        ],
        'calc_form': calc_form,
        'resultado_calculadora': resultado_calculadora,
        'consulta_form': consulta_form,
        'consultas': consultas,
    }
    return render(request, 'guia/inicio.html', contexto)