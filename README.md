# ChromaCRISPR Phase 1

## Estado del proyecto
Semana 1 - Configuración de infraestructura computacional

## Entorno
- WSL2 (Windows 11)
- Conda/Mamba
- Entorno dedicado: chromacrispr-phase1 (Python 3.10)

## Objetivo
Preparación de pipeline reproducible para:
- ATAC-seq / ChIP-seq (bigWig processing)
- Hi-C (cooler, hic2cool)
- Feature engineering genómico
- Machine Learning (XGBoost, SHAP, Optuna)

## Estructura
Pipeline reproducible basado en Snakemake.

Referencia: ChromaCRISPR Phase 1 Proposal

## Semana 3 - QC ENCODE + Hi-C inicializado (SO1 avance)

Durante la Semana 3 se realizó:

### QC de datos ENCODE K562

- Verificación de integridad de archivos BigWig.
- Evaluación de headers y cromosomas.
- Cálculo de estadísticas básicas de señal.
- Generación de reporte:


data/interim/qc_encode_report.md


### Preparación inicial Hi-C

Dataset:


4DNFITUOMFUQ.hic


Procesamiento:


hic2cool conversion
.cool generation
KR balancing


Resultado:


data/processed/hic_k562/4DNFITUOMFUQ.cool


Configuración:

- Resolución: 10 kb
- Formato: Cooler v3
- Cromosomas: 24

Esto completa el avance de SO1:
Dataset curation and harmonization.
