# calculator/models.py

from django.db import models

class ReportImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reports/')

class valorimedici(models.Model):
    # Personal Information
    name = models.CharField(max_length=100, verbose_name="Name")
    surname = models.CharField(max_length=100, verbose_name="Surname")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    chronological_age = models.IntegerField(verbose_name="Chronological Age")
    cf = models.CharField(max_length=16, unique=True, verbose_name="CF")

    # Globuli Bianchi
    baso = models.FloatField(null=True, blank=True, verbose_name="BASO")
    eosi = models.FloatField(null=True, blank=True, verbose_name="EOSI")
    lymph = models.FloatField(null=True, blank=True, verbose_name="LYMPH")
    mono = models.FloatField(null=True, blank=True, verbose_name="MONO")
    neut = models.FloatField(null=True, blank=True, verbose_name="NEUT")
    wbc = models.FloatField(null=True, blank=True, verbose_name="WBC")

    # Globuli Bianchi %
    neut1 = models.FloatField(null=True, blank=True, verbose_name="NEUT1 (%)")
    lymph1 = models.FloatField(null=True, blank=True, verbose_name="LYMPH1 (%)")
    mono1 = models.FloatField(null=True, blank=True, verbose_name="MONO1 (%)")
    eosi1 = models.FloatField(null=True, blank=True, verbose_name="EOSI1 (%)")
    baso1 = models.FloatField(null=True, blank=True, verbose_name="Baso1 (%)")

    # Globuli Rossi
    htc = models.FloatField(null=True, blank=True, verbose_name="HTC (%)")
    hgb = models.FloatField(null=True, blank=True, verbose_name="HGB (g/dL)")
    mch = models.FloatField(null=True, blank=True, verbose_name="MCH (pg)")
    mchc = models.FloatField(null=True, blank=True, verbose_name="MCHC (g/dL)")
    mcv = models.FloatField(null=True, blank=True, verbose_name="MCV (fL)")
    rbc = models.FloatField(null=True, blank=True, verbose_name="RBC (10^6/uL)")
    rdw_sd = models.FloatField(null=True, blank=True, verbose_name="RDW_SD (fL)")
    rdw_cv = models.FloatField(null=True, blank=True, verbose_name="RDW_CV (%)")

    # Funzione Renale
    azotemia = models.FloatField(null=True, blank=True, verbose_name="Azotemia (mg/dL)")
    creatina = models.FloatField(null=True, blank=True, verbose_name="Creatina (mg/dL)")
    uricemia = models.FloatField(null=True, blank=True, verbose_name="Uricemia (mg/dL)")

    # Stato della Coagulazione
    plt = models.FloatField(null=True, blank=True, verbose_name="PLT (10^3/uL)")
    mpv = models.FloatField(null=True, blank=True, verbose_name="MPV (fL)")
    p_lcr = models.FloatField(null=True, blank=True, verbose_name="P_LCR (%)")
    pct = models.FloatField(null=True, blank=True, verbose_name="PCT (%)")
    pdw = models.FloatField(null=True, blank=True, verbose_name="PDW (fL)")

    # Assetto Lipidico
    colesterolo_tot = models.FloatField(null=True, blank=True, verbose_name="Colesterolo Tot (mg/dL)")
    colesterolo_ldl = models.FloatField(null=True, blank=True, verbose_name="Colesterolo LDL (mg/dL)")
    colesterolo_hdl = models.FloatField(null=True, blank=True, verbose_name="Colesterolo HDL (mg/dL)")
    trigliceridi = models.FloatField(null=True, blank=True, verbose_name="Trigliceridi (mg/dL)")

    # Minerali
    sodio = models.FloatField(null=True, blank=True, verbose_name="SODIO (mEq/L)")
    potassio = models.FloatField(null=True, blank=True, verbose_name="POTASSIO (mEq/L)")
    magnesio = models.FloatField(null=True, blank=True, verbose_name="MAGNESIO (mg/dL)")
    cloruri = models.FloatField(null=True, blank=True, verbose_name="CLORURI (mEq/L)")
    calcio = models.FloatField(null=True, blank=True, verbose_name="CALCIO (mg/dL)")
    fosforo = models.FloatField(null=True, blank=True, verbose_name="FOSFORO (mg/dL)")

    # Assetto Marziale
    sideremia = models.FloatField(null=True, blank=True, verbose_name="SIDEREMIA (ug/dl)")
    ferritina = models.FloatField(null=True, blank=True, verbose_name="FERRITINA (ng/ml)")
    transferrina = models.FloatField(null=True, blank=True, verbose_name="TRANSFERRINA (mg/dl)")

    # Assetto Diabetologico
    glicemia = models.FloatField(null=True, blank=True, verbose_name="Glicemia (mg/dL)")
    insulina = models.FloatField(null=True, blank=True, verbose_name="Insulina (μU/mL)")
    homa_test = models.FloatField(null=True, blank=True, verbose_name="HOMA Test")
    ir_test = models.FloatField(null=True, blank=True, verbose_name="IR Test")

    # Proteine
    albuminemia = models.FloatField(null=True, blank=True, verbose_name="Albuminemia (g/dL)")
    proteine_totali = models.FloatField(null=True, blank=True, verbose_name="Proteine Totali (g/dL)")
    pro_tot = models.FloatField(null=True, blank=True, verbose_name="Pro_tot (%)")
    albumina = models.FloatField(null=True, blank=True, verbose_name="Albumina (%)")
    alfa_1 = models.FloatField(null=True, blank=True, verbose_name="Alfa 1 (%)")
    alfa_2 = models.FloatField(null=True, blank=True, verbose_name="Alfa 2 (%)")
    beta_1 = models.FloatField(null=True, blank=True, verbose_name="Beta 1 (%)")
    beta_2 = models.FloatField(null=True, blank=True, verbose_name="Beta 2 (%)")
    gamma = models.FloatField(null=True, blank=True, verbose_name="Gamma (%)")
    albumina_a = models.FloatField(null=True, blank=True, verbose_name="Albumina (g/dL)")
    alfa_1a = models.FloatField(null=True, blank=True, verbose_name="Alfa 1 (g/dL)")
    alfa_2a = models.FloatField(null=True, blank=True, verbose_name="Alfa 2 (g/dL)")
    beta_1a = models.FloatField(null=True, blank=True, verbose_name="Beta 1 (g/dL)")
    beta_2a = models.FloatField(null=True, blank=True, verbose_name="Beta 2 (g/dL)")
    gamma_a = models.FloatField(null=True, blank=True, verbose_name="Gamma (g/dL)")
    rapporto = models.CharField(max_length=255, null=True, blank=True, verbose_name="Rapporto")
    note = models.TextField(null=True, blank=True, verbose_name="Note")
    cmp = models.CharField(max_length=255, null=True, blank=True, verbose_name="CMp")
    cm = models.CharField(max_length=255, null=True, blank=True, verbose_name="CM")
    beta2_picco_p = models.CharField(max_length=255, null=True, blank=True, verbose_name="Beta2 picco P")
    beta2_picco = models.CharField(max_length=255, null=True, blank=True, verbose_name="Beta2 picco")

    # Funzionalità Epatica
    transaminasi_got = models.FloatField(null=True, blank=True, verbose_name="Transaminasi GOT (U/L)")
    transaminasi_gpt = models.FloatField(null=True, blank=True, verbose_name="Transaminasi GPT (U/L)")
    gamma_gt = models.FloatField(null=True, blank=True, verbose_name="Gamma GT (U/L)")
    fosfatasi_alcalina = models.FloatField(null=True, blank=True, verbose_name="Fosfatasi Alcalina (U/L)")

    # Bilirubina
    bilirubina_totale = models.FloatField(null=True, blank=True, verbose_name="Bilirubina Totale (mg/dL)")
    bilirubina_diretta = models.FloatField(null=True, blank=True, verbose_name="Bilirubina Diretta (mg/dL)")
    bilirubina_indiretta = models.FloatField(null=True, blank=True, verbose_name="Bilirubina Indiretta (mg/dL)")

    # Indici di Flogosi
    ves = models.FloatField(null=True, blank=True, verbose_name="VES (mm/h)")
    pcr = models.FloatField(null=True, blank=True, verbose_name="PCR (mg/L)")

    # Altri Esami
    omoicisteina = models.FloatField(null=True, blank=True, verbose_name="OMOICISTEINA (uuol/L)")

    # Esame delle Urine
    colore = models.CharField(max_length=100, null=True, blank=True, verbose_name="Colore")
    aspetto = models.CharField(max_length=100, null=True, blank=True, verbose_name="Aspetto")
    peso_specifico = models.FloatField(null=True, blank=True, verbose_name="Peso Specifico")
    ph = models.FloatField(null=True, blank=True, verbose_name="pH")
    glucosio = models.FloatField(null=True, blank=True, verbose_name="Glucosio (mmol/L)")
    nitriti = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nitriti")
    proteine = models.FloatField(null=True, blank=True, verbose_name="Proteine (mg/dL)")
    sangue = models.CharField(max_length=100, null=True, blank=True, verbose_name="Sangue (ery/μL)")
    chetoni = models.FloatField(null=True, blank=True, verbose_name="Chetoni (mg/dL)")
    urobilinogeno = models.FloatField(null=True, blank=True, verbose_name="Urobilinogeno (umol/L)")
    bilirubina = models.FloatField(null=True, blank=True, verbose_name="Bilirubina (mg/dL)")
    leucociti = models.CharField(max_length=100, null=True, blank=True, verbose_name="Leucociti (Leu/μL)")
    esame_micro = models.TextField(null=True, blank=True, verbose_name="Esame Micro")
    note_u = models.TextField(null=True, blank=True, verbose_name="Note Urine")

    # Stress Ossidativo
    droms = models.CharField(max_length=255, null=True, blank=True, verbose_name="dROMS (Radicali Liberi)")
    pat_test = models.CharField(max_length=255, null=True, blank=True, verbose_name="PAT Test (Potential Antioxidant Test)")
    osi = models.CharField(max_length=255, null=True, blank=True, verbose_name="OSI (Oxidative Stress Index)")
    obri = models.CharField(max_length=255, null=True, blank=True, verbose_name="OBRI (Oxidative Stress Index)")

    def __str__(self):
        return f"{self.name} {self.surname} - {self.date_of_birth}"
