# Generated by Django 5.1.1 on 2024-10-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_valorimedici_delete_altriesami_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valorimedici',
            name='albumina',
            field=models.FloatField(blank=True, null=True, verbose_name='Albumina (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='albumina_a',
            field=models.FloatField(blank=True, null=True, verbose_name='Albumina (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='albuminemia',
            field=models.FloatField(blank=True, null=True, verbose_name='Albuminemia (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='alfa_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Alfa 1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='alfa_1a',
            field=models.FloatField(blank=True, null=True, verbose_name='Alfa 1 (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='alfa_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Alfa 2 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='alfa_2a',
            field=models.FloatField(blank=True, null=True, verbose_name='Alfa 2 (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='aspetto',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Aspetto'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='azotemia',
            field=models.FloatField(blank=True, null=True, verbose_name='Azotemia (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='baso',
            field=models.FloatField(blank=True, null=True, verbose_name='BASO'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='baso1',
            field=models.FloatField(blank=True, null=True, verbose_name='Baso1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta2_picco',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Beta2 picco'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta2_picco_p',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Beta2 picco P'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta_1',
            field=models.FloatField(blank=True, null=True, verbose_name='Beta 1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta_1a',
            field=models.FloatField(blank=True, null=True, verbose_name='Beta 1 (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta_2',
            field=models.FloatField(blank=True, null=True, verbose_name='Beta 2 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='beta_2a',
            field=models.FloatField(blank=True, null=True, verbose_name='Beta 2 (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='bilirubina',
            field=models.FloatField(blank=True, null=True, verbose_name='Bilirubina (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='bilirubina_diretta',
            field=models.FloatField(blank=True, null=True, verbose_name='Bilirubina Diretta (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='bilirubina_indiretta',
            field=models.FloatField(blank=True, null=True, verbose_name='Bilirubina Indiretta (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='bilirubina_totale',
            field=models.FloatField(blank=True, null=True, verbose_name='Bilirubina Totale (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='calcio',
            field=models.FloatField(blank=True, null=True, verbose_name='CALCIO (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='cf',
            field=models.CharField(max_length=16, unique=True, verbose_name='CF'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='chetoni',
            field=models.FloatField(blank=True, null=True, verbose_name='Chetoni (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='chronological_age',
            field=models.IntegerField(verbose_name='Chronological Age'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='cloruri',
            field=models.FloatField(blank=True, null=True, verbose_name='CLORURI (mEq/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='cm',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CM'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='cmp',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CMp'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='colesterolo_hdl',
            field=models.FloatField(blank=True, null=True, verbose_name='Colesterolo HDL (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='colesterolo_ldl',
            field=models.FloatField(blank=True, null=True, verbose_name='Colesterolo LDL (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='colesterolo_tot',
            field=models.FloatField(blank=True, null=True, verbose_name='Colesterolo Tot (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='colore',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Colore'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='creatina',
            field=models.FloatField(blank=True, null=True, verbose_name='Creatina (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='date_of_birth',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='droms',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='dROMS (Radicali Liberi)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='eosi',
            field=models.FloatField(blank=True, null=True, verbose_name='EOSI'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='eosi1',
            field=models.FloatField(blank=True, null=True, verbose_name='EOSI1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='esame_micro',
            field=models.TextField(blank=True, null=True, verbose_name='Esame Micro'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='ferritina',
            field=models.FloatField(blank=True, null=True, verbose_name='FERRITINA (ng/ml)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='fosfatasi_alcalina',
            field=models.FloatField(blank=True, null=True, verbose_name='Fosfatasi Alcalina (U/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='fosforo',
            field=models.FloatField(blank=True, null=True, verbose_name='FOSFORO (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='gamma',
            field=models.FloatField(blank=True, null=True, verbose_name='Gamma (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='gamma_a',
            field=models.FloatField(blank=True, null=True, verbose_name='Gamma (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='gamma_gt',
            field=models.FloatField(blank=True, null=True, verbose_name='Gamma GT (U/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='glicemia',
            field=models.FloatField(blank=True, null=True, verbose_name='Glicemia (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='glucosio',
            field=models.FloatField(blank=True, null=True, verbose_name='Glucosio (mmol/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='hgb',
            field=models.FloatField(blank=True, null=True, verbose_name='HGB (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='homa_test',
            field=models.FloatField(blank=True, null=True, verbose_name='HOMA Test'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='htc',
            field=models.FloatField(blank=True, null=True, verbose_name='HTC (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='insulina',
            field=models.FloatField(blank=True, null=True, verbose_name='Insulina (μU/mL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='ir_test',
            field=models.FloatField(blank=True, null=True, verbose_name='IR Test'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='leucociti',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Leucociti (Leu/μL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='lymph',
            field=models.FloatField(blank=True, null=True, verbose_name='LYMPH'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='lymph1',
            field=models.FloatField(blank=True, null=True, verbose_name='LYMPH1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='magnesio',
            field=models.FloatField(blank=True, null=True, verbose_name='MAGNESIO (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mch',
            field=models.FloatField(blank=True, null=True, verbose_name='MCH (pg)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mchc',
            field=models.FloatField(blank=True, null=True, verbose_name='MCHC (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mcv',
            field=models.FloatField(blank=True, null=True, verbose_name='MCV (fL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mono',
            field=models.FloatField(blank=True, null=True, verbose_name='MONO'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mono1',
            field=models.FloatField(blank=True, null=True, verbose_name='MONO1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='mpv',
            field=models.FloatField(blank=True, null=True, verbose_name='MPV (fL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='neut',
            field=models.FloatField(blank=True, null=True, verbose_name='NEUT'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='neut1',
            field=models.FloatField(blank=True, null=True, verbose_name='NEUT1 (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='nitriti',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nitriti'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='note_u',
            field=models.TextField(blank=True, null=True, verbose_name='Note Urine'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='obri',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='OBRI (Oxidative Stress Index)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='omoicisteina',
            field=models.FloatField(blank=True, null=True, verbose_name='OMOICISTEINA (uuol/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='osi',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='OSI (Oxidative Stress Index)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='p_lcr',
            field=models.FloatField(blank=True, null=True, verbose_name='P_LCR (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='pat_test',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PAT Test (Potential Antioxidant Test)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='pcr',
            field=models.FloatField(blank=True, null=True, verbose_name='PCR (mg/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='pct',
            field=models.FloatField(blank=True, null=True, verbose_name='PCT (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='pdw',
            field=models.FloatField(blank=True, null=True, verbose_name='PDW (fL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='peso_specifico',
            field=models.FloatField(blank=True, null=True, verbose_name='Peso Specifico'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='ph',
            field=models.FloatField(blank=True, null=True, verbose_name='pH'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='plt',
            field=models.FloatField(blank=True, null=True, verbose_name='PLT (10^3/uL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='potassio',
            field=models.FloatField(blank=True, null=True, verbose_name='POTASSIO (mEq/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='pro_tot',
            field=models.FloatField(blank=True, null=True, verbose_name='Pro_tot (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='proteine',
            field=models.FloatField(blank=True, null=True, verbose_name='Proteine (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='proteine_totali',
            field=models.FloatField(blank=True, null=True, verbose_name='Proteine Totali (g/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='rapporto',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Rapporto'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='rbc',
            field=models.FloatField(blank=True, null=True, verbose_name='RBC (10^6/uL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='rdw_cv',
            field=models.FloatField(blank=True, null=True, verbose_name='RDW_CV (%)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='rdw_sd',
            field=models.FloatField(blank=True, null=True, verbose_name='RDW_SD (fL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='sangue',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sangue (ery/μL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='sideremia',
            field=models.FloatField(blank=True, null=True, verbose_name='SIDEREMIA (ug/dl)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='sodio',
            field=models.FloatField(blank=True, null=True, verbose_name='SODIO (mEq/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='transaminasi_got',
            field=models.FloatField(blank=True, null=True, verbose_name='Transaminasi GOT (U/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='transaminasi_gpt',
            field=models.FloatField(blank=True, null=True, verbose_name='Transaminasi GPT (U/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='transferrina',
            field=models.FloatField(blank=True, null=True, verbose_name='TRANSFERRINA (mg/dl)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='trigliceridi',
            field=models.FloatField(blank=True, null=True, verbose_name='Trigliceridi (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='uricemia',
            field=models.FloatField(blank=True, null=True, verbose_name='Uricemia (mg/dL)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='urobilinogeno',
            field=models.FloatField(blank=True, null=True, verbose_name='Urobilinogeno (umol/L)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='ves',
            field=models.FloatField(blank=True, null=True, verbose_name='VES (mm/h)'),
        ),
        migrations.AlterField(
            model_name='valorimedici',
            name='wbc',
            field=models.FloatField(blank=True, null=True, verbose_name='WBC'),
        ),
    ]
