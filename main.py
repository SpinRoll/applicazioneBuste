from flask import Flask, request, render_template
import PyPDF2

def Z00250(testo):
    indice_ferie = testo.find("Z00250")
    if indice_ferie != -1:
        parti = testo[indice_ferie:].split()
        #print(parti)
        if len(parti) >= 7:
            tasso_orario = parti[3]
            ore = parti[4]
            totale = parti[6]
            risultato = f"Ferie godute: Questo è il pagamento per le ferie che hai preso. Hai goduto di {ore} ore di ferie con un tasso orario di {tasso_orario}, per un totale di {totale}."

            return risultato
        else:
            return "La stringa 'Z00250 Ferie godute' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z00250 Ferie godute' nel testo."
def Z00001(testo):
    indice_retribuzione = testo.find("Z00001")
    if indice_retribuzione != -1:
        parti = testo[indice_retribuzione:].split()
        #print(parti)
        if len(parti) >= 7:
            tasso_orario = parti[2]
            ore = parti[3]
            totale = parti[5]
            risultato = f"Retribuzione: Questa è la tua retribuzione base. Hai lavorato {ore} ore con un tasso orario di {tasso_orario}, per un totale di {totale}."
            return risultato
        else:
            return "La stringa 'Z00001 Retribuzione' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z00001 Retribuzione' nel testo."
def Z40025(testo):
    indice_straordinario = testo.find("Z40025")
    if indice_straordinario != -1:
        parti = testo[indice_straordinario:].split()
        #print(parti)
        if len(parti) >= 7:
            tasso_orario = parti[3]
            ore = parti[4]
            totale = parti[6]
            risultato = f"Straordinario al 25%: Questo è il pagamento per le ore straordinarie che hai lavorato con un aumento del 25%. Hai lavorato {ore} ore straordinarie con un tasso orario di {tasso_orario}, per un totale di {totale}."
            return risultato
        else:
            return "La stringa 'Z40025 Straordinario 25%' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z40025 Straordinario 25%' nel testo."
def ZP0100(testo):
    indice_festivita = testo.find("ZP0100")
    if indice_festivita != -1:
        parti = testo[indice_festivita:].split()
        #print(parti)
        if len(parti) >= 4:
            ore = parti[3]
            risultato = f"Festività godute: Questo è il pagamento per le {ore} ore di festività che hai goduto."
            return risultato
        else:
            return "La stringa 'ZP0100 Festivita' godute' non è formattata come previsto."
    else:
        return "Non ho trovato 'ZP0100 Festivita' godute' nel testo."
def ZP9960(testo):
    indice_arrotondamento = testo.find("ZP9960")
    if indice_arrotondamento != -1:
        parti = testo[indice_arrotondamento:].split()
        #print(parti)
        if len(parti) >= 4:
            arrotondamento = parti[4]
            risultato = f"Arrotondamento del mese precedente: Questo è un arrotondamento di {arrotondamento} dal mese precedente."
            return risultato
        else:
            return "La stringa 'ZP9960 Arrotond. mese pr.' non è formattata come previsto."
    else:
        return "Non ho trovato 'ZP9960 Arrotond. mese pr.' nel testo."
def Z00000(testo):
    indice_contributo = testo.find("Z00000")
    if indice_contributo != -1:
        parti = testo[indice_contributo:].split()
        if len(parti) >= 5:
            imponibile = parti[3]
            percentuale = parti[5]
            totale = parti[6]
            risultato = f"Contributo IVS: Questo è il contributo per l’assicurazione generale obbligatoria per l’invalidità, la vecchiaia e i superstiti. Il contributo IVS è del {percentuale}% su un imponibile di {imponibile}, per un totale di {totale}."
            return risultato
        else:
            return "La stringa 'Z00000 Contributo IVS' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z00000 Contributo IVS' nel testo."
def Z00071(testo):
    indice_contributo = testo.find("Z00071")
    if indice_contributo != -1:
        parti = testo[indice_contributo:].split()
        if len(parti) >= 5:
            imponibile = parti[3]
            percentuale = parti[5]
            totale = parti[6]
            risultato = f"Contributo CIGS: Questo è il contributo per la Cassa Integrazione Guadagni Straordinaria. Il contributo CIGS è del {percentuale}% su un imponibile di {imponibile}, per un totale di {totale}."
            return risultato
        else:
            return "La stringa 'Z00071 Contributo CIGS' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z00071 Contributo CIGS' nel testo."
def Z31270(testo):
    indice_contributo = testo.find("Z31270")
    if indice_contributo != -1:
        parti = testo[indice_contributo:].split()
        if len(parti) >= 5:
            contributo = parti[7]
            risultato = f"Contributo METASALUTE: Questo è un contributo per l’assistenza sanitaria, che ammonta a {contributo}."
            return risultato
        else:
            return "La stringa 'Z31270 Contributo METASALUTE' non è formattata come previsto."
    else:
        return "Non ho trovato 'Z31270 Contributo METASALUTE' nel testo."
def F02000(testo):
    indice_irpef = testo.find("F02000")
    if indice_irpef != -1:
        parti = testo[indice_irpef:].split()
        if len(parti) >= 3:
            imponibile = parti[3]
            risultato = f"Imponibile IRPEF: Questo è l’importo del tuo reddito che è soggetto all’Imposta sul Reddito delle Persone Fisiche (IRPEF). L’imponibile IRPEF è di {imponibile}."
            return risultato
        else:
            return "La stringa 'F02000 Imponibile IRPEF' non è formattata come previsto."
    else:
        return "Non ho trovato 'F02000 Imponibile IRPEF' nel testo."
def F02010(testo):
    indice_irpef = testo.find("F02010")
    if indice_irpef != -1:
        parti = testo[indice_irpef:].split()

        if len(parti) >= 3:
            irpef_lorda = parti[3]
            risultato = f"IRPEF lorda: Questa è l’IRPEF calcolata sul tuo imponibile. L’IRPEF lorda è di {irpef_lorda}."
            return risultato
        else:
            return "La stringa 'F02010 IRPEF lorda' non è formattata come previsto."
    else:
        return "Non ho trovato 'F02010 IRPEF lorda' nel testo."
def F02500(testo):
    indice_detrazioni = testo.find("F02500")
    if indice_detrazioni != -1:
        parti = testo[indice_detrazioni:].split()
        if len(parti) >= 3:
            detrazioni = parti[3]
            risultato = f"Detrazioni per lavoratori dipendenti: Queste sono le detrazioni fiscali a cui hai diritto come lavoratore dipendente. Le detrazioni per lavoratori dipendenti sono di {detrazioni}."
            return risultato
        else:
            return "La stringa 'F02500 Detrazioni lav.dip.' non è formattata come previsto."
    else:
        return "Non ho trovato 'F02500 Detrazioni lav.dip.' nel testo."
def F03020(testo):
    indice_ritenute = testo.find("F03020")
    if indice_ritenute != -1:
        parti = testo[indice_ritenute:].split()


        if len(parti) >= 3:
            ritenute = parti[3]
            risultato = f"Ritenute IRPEF: Queste sono le ritenute d’acconto sull’IRPEF. Le ritenute IRPEF sono di {ritenute}."
            return risultato
        else:
            return "La stringa 'F03020 Ritenute IRPEF' non è formattata come previsto."
    else:
        return "Non ho trovato 'F03020 Ritenute IRPEF' nel testo."
def F09110(testo):
    indice_addizionale = testo.find("F09110")
    if indice_addizionale != -1:
        parti = testo[indice_addizionale:].split()

        if len(parti) >= 6:
            residuo = parti [4]
            regione = parti[5]
            anno = parti[7]
            addizionale = parti[6]
            risultato = f"Addizionale regionale: Questa è un’addizionale all’IRPEF a livello regionale. L’addizionale regionale per la {regione} per il {anno} è di {addizionale} su un totale di {residuo}."
            return risultato
        else:
            return "La stringa 'F09110 Addizionale regionale' non è formattata come previsto."
    else:
        return "Non ho trovato 'F09110 Addizionale regionale' nel testo."
def F09130(testo):
    indice_addizionale = testo.find("F09130")
    if indice_addizionale != -1:
        parti = testo[indice_addizionale:].split()

        if len(parti) >= 6:
            residuo = parti[4]
            comune = parti[5]
            anno = parti[8]
            addizionale = parti[7]
            risultato = f"Addizionale comunale: Questa è un’addizionale all’IRPEF a livello comunale. L’addizionale comunale per {comune} per il {anno} è di {addizionale} su un rimanente di {residuo}"
            return risultato
        else:
            return "La stringa 'F09130 Addizionale comunale' non è formattata come previsto."
    else:
        return "Non ho trovato 'F09130 Addizionale comunale' nel testo."
def TFR(testo):
    indice_tfr = testo.find("T.F.R.")
    if indice_tfr != -1:
        parti = testo[indice_tfr:].split()

        if len(parti) >= 2:
            retribuzione = parti[1]
            risultato = f"Retribuzione utile T.F.R.: Questa è la parte della tua retribuzione che contribuisce al TFR (Trattamento di Fine Rapporto). La retribuzione utile per il TFR è di {retribuzione}."
            return risultato
        else:
            return "La stringa 'Retribuzione utile T.F.R.' non è formattata come previsto."
    else:
        return "Non ho trovato 'Retribuzione utile T.F.R.' nel testo."
def Quota_TFR(testo):
    indice_quota = testo.find("Quota")
    if indice_quota != -1:
        parti = testo[indice_quota:].split()

        if len(parti) >= 2:
            quota = parti[2]
            risultato = f"Quota T.F.R.: Questa è la quota del TFR accumulata in questo periodo. La quota TFR è di {quota}."
            return risultato
        else:
            return "La stringa 'Quota T.F.R.' non è formattata come previsto."
    else:
        return "Non ho trovato 'Quota T.F.R.' nel testo."
def INAIL(testo):
    indice_inail = testo.find("INAIL")
    if indice_inail != -1:
        parti = testo[indice_inail:].split()
        if len(parti) >= 2:
            imponibile = parti[1]
            risultato = f"Imp. INAIL: Questo è l’imponibile per l’assicurazione contro gli infortuni sul lavoro gestita dall’INAIL. L’imponibile INAIL è di {imponibile}."
            return risultato
        else:
            return "La stringa 'Imp. INAIL' non è formattata come previsto."
    else:
        return "Non ho trovato 'Imp. INAIL' nel testo."
def RAL(testo):
    indice_inail = testo.find("INAIL")
    if indice_inail != -1:
        parti = testo[indice_inail:].split()
        if len(parti) >= 2:
            Tolgopunti = parti[1].replace('.', '').replace(',', '.')
            RAL = float(Tolgopunti)
            RAL = RAL * 13
            risultato = f"RAL: Rimborso Annuo Lordo annuale considerando 13 mensilità. La tua RAL annuale è di € {RAL}."
            return risultato
        else:
            return "La stringa 'Imp. INAIL' non è formattata come previsto. Non posso calcolare la RAL attuale"
    else:
        return "Non ho trovato 'Imp. INAIL' nel testo. Non posso calcolare la RAL attuale"
def Ferie(testo):
    righe = testo.split('\n')
    if len(righe) > 10:
        testo = '\n'.join(righe[10:])
    indice_ferie = testo.find("Ferie")
    if indice_ferie != -1:
        parti = testo[indice_ferie:].split()
        #print(parti)
        if len(parti) >= 5:
            saldo = parti[1]
            godute = parti[3]
            maturate = parti[4]
            risultato = f"Ferie: Questo è il saldo delle tue ore di ferie. Hai maturato {maturate} ore di ferie e ne hai godute {godute}, per un saldo di {saldo} ore."
            return risultato
        else:
            return "La stringa 'Ferie' non è formattata come previsto."
    else:
        return "Non ho trovato 'Ferie' nel testo."
def Permesso_PAR(testo):
    indice_permesso = testo.find("P.A.R")
    if indice_permesso != -1:
        parti = testo[indice_permesso:].split()
        if len(parti) >= 4:
            saldo = parti[1]
            goduto = parti[2]
            maturato = parti[3]
            risultato = f"Permesso P.A.R.: Questo è il saldo delle tue ore di permesso P.A.R. Hai maturato {maturato} ore di permesso P.A.R. e ne hai godute {goduto}, per un saldo di {saldo} ore."
            return risultato
        else:
            return "La stringa 'Permesso P.A.R.' non è formattata come previsto."
    else:
        return "Non ho trovato 'Permesso P.A.R.' nel testo."

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
                    'Retribuzione:': Z00001(testo),
                    'Ferie godute:': Z00250(testo),
                    'Straordinario al 25%:': Z40025(testo),
                    'Festività godute:': ZP0100(testo),
                    'Arrotondamento del mese precedente:': ZP9960(testo),
                    'Contributo IVS:': Z00000(testo),
                    'Contributo CIGS:': Z00071(testo),
                    'Contributo METASALUTE:': Z31270(testo),
                    'Imponibile IRPEF:': F02000(testo),
                    'FIRPEF lorda:': F02010(testo),
                    'Detrazioni per lavoratori dipendenti:': F02500(testo),
                    'Addizionale regionale:': F03020(testo),
                    'Addizionale comunale:': F09110(testo),
                    'Retribuzione utile T.F.R.:': F09130(testo),
                    'Retribuzione utile T.F.R.:': TFR(testo),
                    'Quota T.F.R.:': Quota_TFR(testo),
                    'Imp. INAIL:': INAIL(testo),
                    'Ferie:': Ferie(testo),
                    'Permesso P.A.R.:': Permesso_PAR(testo),
                    'RAL:': RAL(testo),

                    # Aggiungi qui le altre funzioni
                }
                return render_template('risultati.html', risultati=risultati)

    return render_template('carica.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
