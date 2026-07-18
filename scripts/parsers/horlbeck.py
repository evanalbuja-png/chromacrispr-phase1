"""
Parser para Horlbeck et al. (2016)

Salida:
DataFrame armonizado para ChromaCRISPR
"""

from pathlib import Path

import pandas as pd
import numpy as np


ROOT = Path(__file__).resolve().parents[2]

FILE = (
    ROOT
    / "data"
    / "raw"
    / "crispr_datasets"
    / "Horlbeck2016"
    / "elife-19760-supp1-v2.xlsx"
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


def _standardize(df, experiment, score_column):

    out = pd.DataFrame(index=df.index)

    out["dataset"] = "Horlbeck2016"
    out["experiment"] = experiment

    out["guide_sequence"] = (
        df["sgRNA sequence"]
        .astype(str)
        .str.upper()
        .str.replace(" ", "", regex=False)
    )

    out["gene_symbol"] = df["gene symbol"]

    out["gene_id"] = np.nan

    out["chromosome"] = df["chromosome"]

    out["coordinate"] = df["PAM genomic coordinate [hg19]"]

    out["strand"] = df["strand targeted"]

    out["guide_length"] = df["sgRNA length (including PAM)"]

    out["score_raw"] = df[score_column]

    mu = out["score_raw"].mean()
    sd = out["score_raw"].std()

    # Evitar división por cero
    if pd.isna(sd) or sd == 0:
        out["score_norm"] = 0.0
    else:
        out["score_norm"] = (out["score_raw"] - mu) / sd

    out["score_type"] = experiment

    out["genome_build"] = "hg19"

    out["qc_pass"] = True

    return out[COMMON_COLUMNS]


def load():

    crispri = pd.read_excel(FILE, sheet_name="CRISPRi")

    crispra = pd.read_excel(FILE, sheet_name="CRISPRa")

    crispri = _standardize(
        crispri,
        "CRISPRi",
        "CRISPRi activity score [Horlbeck et al., eLife 2016]",
    )

    crispra = _standardize(
        crispra,
        "CRISPRa",
        "CRISPRa activity score",
    )

    df = pd.concat(
        [crispri, crispra],
        ignore_index=True,
    )

    return df