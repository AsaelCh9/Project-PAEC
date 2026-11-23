from django.shortcuts import render

def inicio(request):
    contexto = {
        'materiales_verdes': [
            'Restos de frutas y verduras',
            'Posos de cafe y bolsitas de te (sin grapas)',
            'Cascaras de huevo trituradas',
            'Cesped recien cortado y plantas verdes',
        ],
        'materiales_marrones': [
            'Hojas secas y ramas pequeñas',
            'Carton y papel sin tinta brillante (troceado)',
            'Aserrin o virutas de madera mo tratada',
            'Paja o heno seco',
        ],
        'no_compostar': [
            'Carnes, huesos y pescados (atraen plagas),'
            'Lacteos, aceites y grasas',
            'Heces de perros o gatos',
            'Plasticos, metales o vidrios',
        ]
    }
    return render(request, 'guia/inicio.html', contexto)