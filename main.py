from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        lettore = PyPDF2.PdfReader(file)

        # Estrai il testo da ogni pagina
        for pagina in lettore.pages:
            testo = pagina.extract_text()
            indice_inizio = testo.find('**Z00001')

            # Se i dati sono presenti, estrai solo la parte di testo che ti interessa
            if indice_inizio != -1:
                testo = testo[indice_inizio:]
                risultati = {
                    'Z00001': Z00001(testo),
                    'Z00250': Z00250(testo),
                    # Aggiungi qui le altre funzioni
                }
                return render_template('risultati.html', risultati=risultati)

    return render_template('carica.html')

if __name__ == '__main__':
    app.run(debug=True)
