"""
Parser para Gasperini et al. (2019)

Integra las bibliotecas Pilot y At-Scale con sus tablas de
enhancer-gene pairs usando Target_Site como clave.

Devuelve un DataFrame armonizado al esquema común de ChromaCRISPR.
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

TABLE_S1 = (
    ROOT
    / "data"
    / "raw"
    / "crispr_datasets"
    / "Gasperini2019"
    / "NIHMS1038673-supplement-TableS1.xlsx"
)

TABLE_S2 = (
    ROOT
    / "data"
    / "raw"
    / "crispr_datasets"
    / "Gasperini2019"
    / "NIHMS1038673-supplement-TableS2.xlsx"
)

COMMON_COLUMNS = [
    "dataset",
    "experiment",
    "guide_sequence",
    "gene_symbol",
    "gene_id",
    "chromosome",
    "coordinate",
    "strand",
    "guide_length",
    "score_raw",
    "score_norm",
    "score_type",
    "genome_build",
    "qc_pass",
]


def _standardize(df, experiment):
    """
    Convierte la biblioteca de sgRNAs de Gasperini
    al esquema estándar de ChromaCRISPR.

    En Semana 4 no incorporamos todavía las relaciones
    enhancer-gen; cada fila representa únicamente una sgRNA.
    """

    out = pd.DataFrame(index=df.index)

    out["dataset"] = "Gasperini2019"
    out["experiment"] = experiment

    out["guide_sequence"] = (
        df["Spacer"]
        .astype(str)
        .str.upper()
        .str.replace(" ", "", regex=False)
    )

    # Las relaciones enhancer-gen se añadirán en fases posteriores
    out["gene_symbol"] = np.nan
    out["gene_id"] = np.nan

    out["chromosome"] = df["chr.candidate_enhancer"]
    out["coordinate"] = df["start.candidate_enhancer"]

    out["strand"] = np.nan

    out["guide_length"] = out["guide_sequence"].str.len()

    out["score_raw"] = np.nan
    out["score_norm"] = np.nan

    out["score_type"] = "annotation_only"

    out["genome_build"] = "hg19"

    out["qc_pass"] = True

    return out[COMMON_COLUMNS]


def _load_experiment(workbook, library_sheet, experiment):

    library = pd.read_excel(
        workbook,
        sheet_name=library_sheet,
    )

    return _standardize(
        library,
        experiment,
    )


def load():
    """
    Devuelve Pilot + AtScale.
    """

    pilot = _load_experiment(
        TABLE_S1,
        "A_Pilot_gRNA_library",
        "Pilot",
    )

    atscale = _load_experiment(
        TABLE_S2,
        "S2A_AtScale_library_gRNA.cs",
        "AtScale",
    )

    return pd.concat(
        [
            pilot,
            atscale,
        ],
        ignore_index=True,
    )