from django.shortcuts import render
from .models import valorimedici
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.http import JsonResponse
import json
# Create your views here.

def calco(request):
    calco= valorimedici.objects.all()
    return render(request, 'calculator/index.html', {'calco':calco})

def pagina_dati(request):
    # Recupera i dati dalla sessione
    data = request.session.get('formData', {})
    return render(request, 'calculator/pagina_dati.html', {'data': data})

def salva_dati(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # Salva i dati nella sessione (o nel database, se preferisci)
        request.session['formData'] = data
        return JsonResponse({"message": "Dati salvati con successo!"})
    return JsonResponse({"error": "Richiesta non valida"}, status=400)
#



#def generate_pdf_report(request):
    # Crea un buffer per il PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # Crea il canvas per generare il PDF
    pdf_canvas = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Aggiungi il contenuto del PDF
    pdf_canvas.setFont("Helvetica", 12)
    pdf_canvas.drawString(100, height - 100, "Report con Immagini")

    # Percorso delle immagini caricate nel media root
    image_paths = [
        os.path.join(settings.MEDIA_ROOT, 'referto/page1.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page2.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page3.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page4.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page5.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page6.jpg'),
        os.path.join(settings.MEDIA_ROOT, 'referto/page7.jpg')
    ]

    # Aggiungi ogni immagine come pagina separata nel PDF
    for img_path in image_paths:
        pdf_canvas.drawImage(img_path, 100, height - 500, width=400, height=400)
        pdf_canvas.showPage()  # Aggiungi una nuova pagina

    # Salva il PDF
    pdf_canvas.save()
    return response
