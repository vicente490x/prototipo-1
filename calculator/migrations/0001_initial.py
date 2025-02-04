# Generated by Django 5.1.1 on 2024-10-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AltriEsami',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omoicisteina', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssettoDiabetologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glicemia', models.FloatField(blank=True, null=True)),
                ('insulina', models.FloatField(blank=True, null=True)),
                ('homa_test', models.FloatField(blank=True, null=True)),
                ('ir_test', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssettoLipidico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colesterolo_tot', models.FloatField(blank=True, null=True)),
                ('colesterolo_ldl', models.FloatField(blank=True, null=True)),
                ('colesterolo_hdl', models.FloatField(blank=True, null=True)),
                ('trigliceridi', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssettoMarziale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sideremia', models.FloatField(blank=True, null=True)),
                ('ferritina', models.FloatField(blank=True, null=True)),
                ('transferrina', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bilirubina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bilirubina_totale', models.FloatField(blank=True, null=True)),
                ('bilirubina_diretta', models.FloatField(blank=True, null=True)),
                ('bilirubina_indiretta', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EsameUrine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colore', models.CharField(blank=True, max_length=100, null=True)),
                ('aspetto', models.CharField(blank=True, max_length=100, null=True)),
                ('peso_specifico', models.FloatField(blank=True, null=True)),
                ('ph', models.FloatField(blank=True, null=True)),
                ('glucosio', models.FloatField(blank=True, null=True)),
                ('nitriti', models.CharField(blank=True, max_length=100, null=True)),
                ('proteine', models.FloatField(blank=True, null=True)),
                ('sangue', models.CharField(blank=True, max_length=100, null=True)),
                ('chetoni', models.FloatField(blank=True, null=True)),
                ('urobilinogeno', models.FloatField(blank=True, null=True)),
                ('bilirubina', models.FloatField(blank=True, null=True)),
                ('leucociti', models.CharField(blank=True, max_length=100, null=True)),
                ('esame_micro', models.TextField(blank=True, null=True)),
                ('note_u', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FunzionalitaEpatica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaminasi_got', models.FloatField(blank=True, null=True)),
                ('transaminasi_gpt', models.FloatField(blank=True, null=True)),
                ('gamma_gt', models.FloatField(blank=True, null=True)),
                ('fosfatasi_alcalina', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FunzioneRenale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('azotemia', models.FloatField(blank=True, null=True)),
                ('creatina', models.FloatField(blank=True, null=True)),
                ('uricemia', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobuliBianchi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baso', models.FloatField(blank=True, null=True)),
                ('eosi', models.FloatField(blank=True, null=True)),
                ('lymph', models.FloatField(blank=True, null=True)),
                ('mono', models.FloatField(blank=True, null=True)),
                ('neut', models.FloatField(blank=True, null=True)),
                ('wbc', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobuliBianchiPercentuale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neut1', models.FloatField(blank=True, null=True)),
                ('lymph1', models.FloatField(blank=True, null=True)),
                ('mono1', models.FloatField(blank=True, null=True)),
                ('eosi1', models.FloatField(blank=True, null=True)),
                ('baso1', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobuliRossi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htc', models.FloatField(blank=True, null=True)),
                ('hgb', models.FloatField(blank=True, null=True)),
                ('mch', models.FloatField(blank=True, null=True)),
                ('mchc', models.FloatField(blank=True, null=True)),
                ('mcv', models.FloatField(blank=True, null=True)),
                ('rbc', models.FloatField(blank=True, null=True)),
                ('rdw_sd', models.FloatField(blank=True, null=True)),
                ('rdw_cv', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IndiciFlogosi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ves', models.FloatField(blank=True, null=True)),
                ('pcr', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Minerali',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sodio', models.FloatField(blank=True, null=True)),
                ('potassio', models.FloatField(blank=True, null=True)),
                ('magnesio', models.FloatField(blank=True, null=True)),
                ('cloruri', models.FloatField(blank=True, null=True)),
                ('calcio', models.FloatField(blank=True, null=True)),
                ('fosforo', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('chronological_age', models.IntegerField()),
                ('cf', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Proteine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albuminemia', models.FloatField(blank=True, null=True)),
                ('proteine_totali', models.FloatField(blank=True, null=True)),
                ('pro_tot', models.FloatField(blank=True, null=True)),
                ('albumina', models.FloatField(blank=True, null=True)),
                ('alfa_1', models.FloatField(blank=True, null=True)),
                ('alfa_2', models.FloatField(blank=True, null=True)),
                ('beta_1', models.FloatField(blank=True, null=True)),
                ('beta_2', models.FloatField(blank=True, null=True)),
                ('gamma', models.FloatField(blank=True, null=True)),
                ('albumina_a', models.FloatField(blank=True, null=True)),
                ('alfa_1a', models.FloatField(blank=True, null=True)),
                ('alfa_2a', models.FloatField(blank=True, null=True)),
                ('beta_1a', models.FloatField(blank=True, null=True)),
                ('beta_2a', models.FloatField(blank=True, null=True)),
                ('gamma_a', models.FloatField(blank=True, null=True)),
                ('rapporto', models.CharField(blank=True, max_length=255, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('cmp', models.CharField(blank=True, max_length=255, null=True)),
                ('cm', models.CharField(blank=True, max_length=255, null=True)),
                ('beta2_picco_p', models.CharField(blank=True, max_length=255, null=True)),
                ('beta2_picco', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatoCoagulazione',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plt', models.FloatField(blank=True, null=True)),
                ('mpv', models.FloatField(blank=True, null=True)),
                ('p_lcr', models.FloatField(blank=True, null=True)),
                ('pct', models.FloatField(blank=True, null=True)),
                ('pdw', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StressOssidativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('droms', models.CharField(blank=True, max_length=255, null=True)),
                ('pat_test', models.CharField(blank=True, max_length=255, null=True)),
                ('osi', models.CharField(blank=True, max_length=255, null=True)),
                ('obri', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
