console.log("Il file app.js è caricato correttamente");
if (window.jspdf && window.jspdf.jsPDF) {
    console.log("jsPDF caricato correttamente");
} else {
    console.error("Errore: jsPDF non è stato caricato.");
}

const containerInput = document.getElementById('containerInput');
const generateBtn = document.getElementById('generate');

const dataField = {
    "Personal Information": {
        "Name": "",
        "Surname": "",
        "Date_of_Birth": "DD/MM/YYYY",
        "Chronological_Age": "years",
        "CF": ""
    },
    "Globuli Bianchi": {
        "BASO": "",
        "EOSI": "",
        "LYMPH": "",
        "MONO": "",
        "NEUT": "",
        "WBC":  ""
    },
    "Globuli Bianchi%": {
        "NEUT1": "%",
        "LYMPH1":"%",
        "MONO1":"%",
        "EOSI1":"%",
        "Baso1": "%"
    },
    "Globuli Rossi": {
        "HTC": "%",
        "HGB":"g/dL",
        "MCH":"pg",
        "MCHC":"g/dL",
        "MCV": "fL",
        "RBC":  "10^6/uL",
        "RDW_SD":"fL",
        "RDW_CV":"%"
    },
    "Funzione Renale": {
        "Azotemia": "mg/dL",
        "Creatina": "mg/dL",
        "Uricemia": "mg/dL"
    },
    "Stato della Coagulazione": {
        "PLT": "10^3/uL",
        "MPV": "fL",
        "P_LCR": "%",
        "PCT": "%",
        "PDW": "fL"
    },
    "Assetto Lipidico": {
        "Colesterolo_Tot": "mg/dL",
        "Colesterolo_LDL": "mg/dL",
        "Colesterolo_HDL": "mg/dL",
        "Trigliceridi": "mg/dL"
    },
    "Minerali": {
        "SODIO": "mEq/L",
        "POTASSIO": "mEq/L",
        "MAGNESIO": "mg/dL",
        "CLORURI": "mEq/L",
        "CALCIO": "mg/dL",
        "FOSFORO": "mg/dL"
    },
    "AssettoMarziale":{
        "SIDEREMIA": "ug/dl",
        "FERRITINA": "ng/ml",
        "TRANSFERRINA": "mg/dl"
    },
    "Assetto Diabetologico": {
        "Glicemia": "mg/dL",
        "Insulina": "μU/mL",
        "HOMA_Test": "",
        "IR_TEST": ""
    },
    "Proteine": {
        "Albuminemia": "g/dL",
        "Proteine_Totali": "g/dL",
        "Pro_tot": "%",
        "Albumina": "%",
        "Alfa_1": "%",
        "Alfa_2": "%",
        "Beta_1": "%",
        "Beta_2": "%",
        "Gamma": "%",
        "AlbuminaA": "g/dL",
        "Alfa_1A": "g/dL",
        "Alfa_2A": "g/dL",
        "Beta_1A": "g/dL",
        "Beta_2A": "g/dL",
        "GammaA": "g/dL",
        "Rapporto_": "",
        "note": "",
        "CMp": "",
        "CM": "",
        "Beta2_piccoP": "",
        "Beta2_picco": ""
    },
    "Funzionalità Epatica": {
        "Transaminasi_GOT": "U/L",
        "Transaminasi_GPT": "U/L",
        "Gamma_GT": "U/L",
        "Fosfatasi_Alcalina": "U/L"
    },
    "Bilirubina": {
        "Bilirubina_Totale": "mg/dL",
        "Bilirubina_Diretta": "mg/dL",
        "Bilirubina_Indiretta": "mg/dL"
    },
    "Indici di Flogosi": {
        "VES": "mm/h",
        "PCR": "mg/L"
    },
    "Altri Esami": {
        "OMOICISTEINA": "uuol/L"
    },
    "Esame delle Urine": {
        "Colore": "",
        "Aspetto": "",
        "Peso_Specifico": "",
        "pH": "",
        "Glucosio": "mmol/L",
        "Nitriti": "",
        "Proteine": "mg/dL",
        "Sangue": "ery/μL",
        "Chetoni": "mg/dL",
        "Urobilinogeno": "umol/L",
        "Bilirubina": "mg/dL",
        "Leucociti": "Leu/μL",
        "EsameMicro":"",
        "NoteU":""
    },
    "Stress Ossidativo": {
        "dROMS": "Radicali Liberi",
        "PAT_Test": "Potential Antioxidant Test",
        "OSI": "Oxidative Stress Index",
        "OBRI": "Oxidative Stress Index"
    }
};

// Funzione per popolare dinamicamente tutte le sezioni e campi
for (const key in dataField) {
    const sectionDiv = document.createElement('div');
    const sectionTitle = document.createElement('h3');
    sectionTitle.textContent = key;
    sectionDiv.appendChild(sectionTitle);

    for (const el in dataField[key]) {
        const fieldDiv = document.createElement('div');
        const label = document.createElement('label');
        label.textContent = el;

        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = dataField[key][el];
        input.classList.add(el.replace(/\s+/g, '-'));

        fieldDiv.appendChild(label);
        fieldDiv.appendChild(input);
        sectionDiv.appendChild(fieldDiv);
    }
    containerInput.appendChild(sectionDiv);
}

function clearInputFields() {
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input => {
        input.value = '';
    });
}

document.getElementById('generate').addEventListener('click', () => {
    console.log("Pulsante cliccato, inizio `calculateAndSave`");
    openVisualizzaPage();
    calculateAndSave();
});

function openVisualizzaPage() {
    window.open('/visualizza/', '_blank');
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Funzioni di calcolo dell'età biologica
function adjustAgeObri(obriIndex) {
    if (obriIndex === null) return 0;
    if (obriIndex >= 0.8 && obriIndex <= 1.2) return 0; 
    if (obriIndex >= 1.3 && obriIndex <= 1.7) return 2; 
    if (obriIndex >= 1.8 && obriIndex <= 2.2) return 5; 
    if (obriIndex > 2.2) return 10; 
    return 0;
}
function adjustAgeDRoms(dRoms) {
    if (dRoms === null) return 0;
    if (dRoms >= 250 && dRoms <= 300) return 0;
    if (dRoms >= 301 && dRoms <= 320) return 1; 
    if (dRoms >= 321 && dRoms <= 340) return 1;
    if (dRoms >= 341 && dRoms <= 400) return 3; 
    if (dRoms > 400) return 6; 
    return 0;
}
function adjustAgeAAEpa(aaEpa) {
    if (aaEpa === null) return 0;
    if (aaEpa >= 1 && aaEpa <= 3) return 0; 
    if (aaEpa > 3 && aaEpa <= 15) return 2; 
    if (aaEpa > 15) return 4; 
    return 0;
}
function adjustAgeAADha(aaDha) {
    if (aaDha === null) return 0;
    if (aaDha >= 1.6 && aaDha <= 3.6) return 0; 
    if (aaDha > 3.6 && aaDha <= 4.3) return 2; 
    if (aaDha > 4.3) return 4; 
    return 0;
}
function adjustAgeHoma(homaTest) {
    if (homaTest === null) return 0;
    if (homaTest >= 0.23 && homaTest <= 2.5) return 0; 
    return 5; 
}
function adjustAgeCardio(cardiovascularRisk) {
    if (cardiovascularRisk === null) return 0;
    if (cardiovascularRisk < 3) return 0; 
    if (cardiovascularRisk >= 3 && cardiovascularRisk <= 20) return 2; 
    return 5; 
}
function adjustAgeOsi(osi) {
    if (osi === null) return 0;
    if (osi >= 0 && osi <= 40) return 0; 
    if (osi >= 41 && osi <= 65) return 2; 
    if (osi >= 66 && osi <= 120) return 5; 
    return 10; 
}
function adjustAgePat(pat) {
    if (pat === null) return 0;
    if (pat < 1800) return 10; 
    if (pat >= 1800 && pat < 2700) return 5; 
    if (pat >= 2700 && pat < 2270) return 2; 
    if (pat >= 2270 && pat < 2800) return 0; 
    return -5; 
}
function adjustAgeExams(exams) {
    const normalValues = {
        'BASO': [0, 2.5],
        'EOSI': [0, 7],
        'LYMPH': [15, 45],
        'MONO': [0, 10],
        'NEUT': [45, 70],
        'BASO1': [0, 2.5],
        'EOSI1': [0, 7],
        'LYMPH1': [15, 45],
        'MONO1': [0, 10],
        'NEUT1': [45, 70],
        'WBC': [4.0, 10.0],
        'HCT': [38, 48],
        'HGB': [12, 16],
        'MCH': [27, 32],
        'MCHC': [32, 37],
        'MCV': [82, 98],
        'RBC': [4.0, 5.5],
        'RDW_SD': [38.0, 48.0],
        'RDW_CV': [11.0, 15.0],
        'AZOTEMIA': [16.6, 48.5],
        'CREATININA': [0.5, 0.9],
        'PLT': [150, 450],
        'MPV': [9.1, 12.3],
        'PDW': [10, 16],
        'COLESTEROLO_TOT': [0, 200],
        'COLESTEROLO_HDL': [0, 100],
        'COLESTEROLO_LDL': [45, 65],
        'TRIGLICERIDI': [0, 150],
        'SODIO': [136, 145],
        'POTASSIO': [3.5, 5.1],
        'MAGNESIO': [1.6, 2.6],
        'CLORURI': [98, 107],
        'CALCIO': [8.6, 10.0],
        'FOSFORO': [0.8, 1.5],
        'SIDEREMIA': [37, 150],
        'FERRITINA': [13, 150],
        'TRANSFERRINA': [270, 360],
        'GLICEMIA': [70, 105],
        'INSULINA': [3, 16],
        'HOMA TEST': [0.23, 2.5],
        'ALBUMINEMIA': [3.50, 5.20],
        'TRANSAMINASI_GOT': [0, 31],
        'TRANSAMINASI_GPT': [0, 38],
        'GAMMA GT': [8, 31],
        'FOSFATASI_ALCALINA': [100, 290],
        'VES': [0, 20],
        'PCR': [0, 5],
        'OMOICISTEINA': [5, 15],
        'PESO SPECIFICO': [1000, 1030],
        'PH': [5.0, 9.0],
        'GLUCOSIO': [0, 5],
        'PROTEINE': [0, 0.15],
        'SANGUE': [0, 0],
        'CHETONI': [0, 0.5],
        'BILIRUBINA': [0, 17],
        'UROBILINOGENO': [0, 17],
        'LEUCOCITI': [0, 15],
        'IR_TEST': [0, 1],
        'Proteine_tot': [6.6, 8.7],
        'Albumina': [52.7, 67.4],
        'Alfa1': [3.6, 8.0],
        'Alfa2': [6.4, 11.5],
        'Beta1': [5.2, 8.3],
        'Beta2': [2.2, 8.0],
        'Gamma': [8.7, 18.0],
        'Albumina*': [3.48, 5.86],
        'Alfa1A': [0.24, 0.70],
        'Alfa2A': [0.42, 1.0],
        'Beta1A': [0.34, 0.72],
        'Beta2A': [0.15, 0.70],
        'GammaA': [0.57, 1.56],
        'Rapporto_A': [1.20, 2.06],
    };

    let ageAdjustment = 0;
    for (const exam in exams) {
        const value = exams[exam];
        if (value === null) continue;
        const normalRange = normalValues[exam];
        if (normalRange && !(value >= normalRange[0] && value <= normalRange[1])) {
            ageAdjustment += 1; 
        }
    }
    return ageAdjustment;
}

// Funzione principale per calcolare l'età biologica
function calculateBiologicalAge(Chronological_Age, obriIndex, dRoms, aaEpa, aaDha, homaTest, osi, pat, exams) {
    let biologicalAge = Chronological_Age;

    biologicalAge += adjustAgeObri(obriIndex);
    biologicalAge += adjustAgeDRoms(dRoms);
    biologicalAge += adjustAgeAAEpa(aaEpa);
    biologicalAge += adjustAgeAADha(aaDha);
    biologicalAge += adjustAgeHoma(homaTest);
    biologicalAge += adjustAgeOsi(osi);
    biologicalAge += adjustAgePat(pat);
    biologicalAge += adjustAgeExams(exams);

    return biologicalAge;
}

async function calculateAndSave() {
    try {
        console.log("Chiamata a calculateAndSave iniziata");
        const inputs = document.querySelectorAll('input');
        const data = {};

        inputs.forEach(input => {
            const className = input.className;
            if (className) {
                data[className.replace(/-/g, '_')] = input.value;
            }
        });

        await generatePDFReport(data);

         console.log("Generazione PDF completata, eseguo reindirizzamento");
 
         // Reindirizza alla pagina di visualizzazione

        const Chronological_Age = parseFloat(data["Chronological_Age"]) || 0;
        const obriIndex = parseFloat(data["OBRI"]) || null;
        const dRoms = parseFloat(data["D-ROMS"]) || null;
        const aaEpa = parseFloat(data["aa_epa"]) || null;
        const aaDha = parseFloat(data["aa_dha"]) || null;
        const homaTest = parseFloat(data["HOMA_Test"]) || null;
        const osi = parseFloat(data["OSI-Index"]) || null;
        const pat = parseFloat(data["PAT Test"]) || null;

        const exams = {};
        const examElements = document.getElementsByClassName("exam-entry");
        for (const examElement of examElements) {
            const examName = examElement.name;
            exams[examName] = parseFloat(examElement.value) || null;
        }

        const biologicalAge = calculateBiologicalAge(
            Chronological_Age,
            obriIndex,
            dRoms,
            aaEpa,
            aaDha,
            homaTest,
            osi,
            pat,
            exams
        );

        data.BiologicalAge = biologicalAge;
        data.OlderThanChronologicalAge = biologicalAge > Chronological_Age ? 1 : 0;

        

        alert(`Calculated Biological Age: ${biologicalAge.toFixed(2)} years`);
    } catch (e) {
        console.error("Error: ", e);
        alert("An unexpected error occurred. Please check your input values.");
    }
}

async function generatePDFReport(data) {
    console.log("Inizio generazione PDF");

    if (!window.jspdf || !window.jspdf.jsPDF) {
        console.error("jsPDF non caricato correttamente");
        return;
    }

    const { jsPDF } = window.jspdf;
    const pdf = new jsPDF();

    const pageWidth = pdf.internal.pageSize.getWidth();
    const pageHeight = pdf.internal.pageSize.getHeight();

    const images = [
        '/media/referto/page1.jpg',
        '/media/referto/page2.jpg',
        '/media/referto/page3.jpg',
        '/media/referto/page4.jpg',
        '/media/referto/page5.jpg',
        '/media/referto/page6.jpg',
        '/media/referto/page7.jpg'
    ];

    function loadImage(imgSrc) {
        return new Promise((resolve, reject) => {
            const img = new Image();
            img.src = imgSrc;
            img.onload = () => resolve(img);
            img.onerror = (error) => reject(error);
        });
    }

    async function createPDF() {
        for (let i = 0; i < images.length; i++) {
            try {
                const img = await loadImage(images[i]);
                let imgWidth = pageWidth;
                let imgHeight = (img.height / img.width) * imgWidth;

                if (imgHeight > pageHeight) {
                    const scaleFactor = pageHeight / imgHeight;
                    imgHeight *= scaleFactor;
                    imgWidth *= scaleFactor;
                }

                if (i > 0) {
                    pdf.addPage();
                }

                pdf.addImage(img, 'JPEG', 0, 0, imgWidth, imgHeight);
                const addText = (text, x, y, fontSize = 12, color = [0, 0, 0]) => {
                    if (text !== undefined && text !== null) { // Controlla che il testo esista e non sia null
                        pdf.setFontSize(fontSize);
                        pdf.setTextColor(...color);
                        pdf.text(text.toString(), x, y);
                    }
                };

                // Aggiungi il testo in base alla pagina corrente
                if (i === 0) {
                    addText(data.Name, 110, 58);
                    addText(data.Surname, 120, 58);
                    addText(data.Date_of_Birth, 110, 65);
                    addText(data.Chronological_Age, 50, 71);
                    addText(data.CF, 110, 71);
                    addText(data.BASO, 90, 97);
                    addText(data.EOSI, 90, 104);
                    addText(data.LYMPH, 90, 111);
                    addText(data.MONO, 90, 118);
                    addText(data.NEUT, 90, 124);
                    addText(data.WBC, 90, 130);
                    addText(data.NEUT1, 90, 137);
                    addText(data.LYMPH1, 90, 144);
                    addText(data.MONO1, 90, 151);
                    addText(data.EOSI1, 90, 158);
                    addText(data.Baso1, 90, 164);
                    addText(data.HTC, 90, 184);
                    addText(data.HGB, 90, 191);
                    addText(data.MCH, 90, 197);
                    addText(data.MCHC, 90, 204);
                    addText(data.MCV, 90, 210);
                    addText(data.RBC, 90, 217);
                    addText(data.RDW_SD, 90, 224);
                    addText(data.RDW_CV, 90, 230);
                    addText(data.Azotemia, 90, 250);
                    addText(data.Creatina, 90, 260);
                }
                if (i === 1) {
                    addText(data.Uricemia, 90, 60);
                    addText(data.PLT, 90, 93);
                    addText(data.MPV, 90, 100);
                    addText(data.P_LCR, 90, 106);
                    addText(data.PCT, 90, 112);
                    addText(data.PDW, 90, 118);
                    addText(data.Colesterolo_Tot, 90, 140);
                    addText(data.Colesterolo_LDL, 90, 147);
                    addText(data.Colesterolo_HDL, 90, 156);
                    addText(data.Trigliceridi, 90, 173);
                    addText(data.SODIO, 90, 197);
                    addText(data.POTASSIO, 90, 203);
                    addText(data.MAGNESIO, 90, 210);
                    addText(data.CLORURI, 90, 217);
                    addText(data.CALCIO, 90, 224);
                    addText(data.FOSFORO, 90, 230);
                    addText(data.SIDEREMIA, 90, 255);
                    addText(data.FERRITINA, 90, 265);
                    addText(data.TRANSFERRINA, 90, 274);
                }
                if (i === 2) {
                    addText(data.Glicemia, 90, 37);
                    addText(data.Insulina, 90, 44);
                    addText(data.HOMA_Test, 90, 50);
                    addText(data.IR_TEST, 90, 62);
                    addText(data.Albuminemia, 90, 84);
                    addText(data.Proteine_Totali, 90, 91);
                    addText(data.Pro_tot , 90, 103);
                    addText(data.Albumina, 90, 109);
                    addText(data.Alfa_1, 90, 114);
                    addText(data.Alfa_2, 90, 119);
                    addText(data.Beta_1, 90, 125);
                    addText(data.Beta_2, 90, 130);
                    addText(data.Gamma, 90, 135);
                    addText(data.AlbuminaA, 90, 141);
                    addText(data.Alfa_1A, 90, 146);
                    addText(data.Alfa_2A, 90, 152);
                    addText(data.Beta_1A, 90, 157);
                    addText(data.Beta_2A, 90, 163);
                    addText(data.GammaA, 90, 168);
                    addText(data.Rapporto_, 90, 174);
                    addText(data.note, 90, 180);
                    addText(data.CMp, 90, 186);
                    addText(data.CM, 90, 190);
                    addText(data.Beta2_piccoP, 90, 196);
                    addText(data.Beta2_picco, 90, 201);
                    addText(data.Transaminasi_GOT, 90, 223);
                    addText(data.Transaminasi_GPT, 90, 233);
                    addText(data.Gamma_GT, 90, 243);
                    addText(data.Fosfatasi_Alcalina, 90, 252);
                    addText(data.Bilirubina_Totale, 90, 265);
                    addText(data.Bilirubina_Diretta, 90, 270);
                    addText(data.Bilirubina_Indiretta, 90, 275);
                }
                if (i === 3) {
                    addText(data.VES, 90, 43);
                    addText(data.PCR, 90, 49);
                }
                if (i === 4) {
                    addText(data.OMOICISTEINA, 90, 37);
                    addText(data.Colore, 90, 57);
                    addText(data.Aspetto, 90, 63);
                    addText(data.Peso_Specifico, 90, 70);
                    addText(data.pH, 90, 76);
                    addText(data.Glucosio, 90, 83);
                    addText(data.Nitriti, 90, 90);
                    addText(data.Proteine, 90, 97);
                    addText(data.Sangue, 90, 103);
                    addText(data.Chetoni, 90, 110);
                    addText(data.Urobilinogeno, 90, 116);
                    addText(data.Bilirubina, 90, 123);
                    addText(data.Leucociti, 90, 129);
                    addText(data.EsameMicro, 90, 136);
                    addText(data.NoteU, 90, 142);

                }
                if (i === 5) {
                    addText(data.Name, 110, 35);
                    addText(data.Surname, 120, 35);
                    addText(data.Date_of_Birth, 110, 41);
                    addText(data.Chronological_Age, 50, 48);
                    addText(data.CF, 110, 48);
                    addText(data.dROMS, 90, 75);
                    addText(data.PAT_Test, 90, 102);
                    addText(data.OSI, 90, 125);
                    addText(data.OBRI,90, 145);
                }
                if (i === 6) {
                    /*non ci sono campi da inserire nella pagina */
                }
            } catch (error) {
                console.error("Errore nel caricamento dell'immagine: ", error);
            }
        }

        pdf.save('report_multipagina.pdf');
        await new Promise(resolve => setTimeout(resolve, 2000));
        console.log("Attendo prima di reindirizzare");
    }

    createPDF();
}
