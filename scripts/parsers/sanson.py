"""
Parser para Sanson et al. (2018)

Devuelve las anotaciones de las bibliotecas SetA y SetB
armonizadas al esquema común de ChromaCRISPR.
"""

from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

FILE = (
    ROOT
    / "data"
    / "raw"
    / "crispr_datasets"
    / "Sanson2018"
    / "41467_2018_7901_MOESM6_ESM.xlsx"
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


def _parse_sheet(sheet):

    df = pd.read_excel(FILE, sheet_name=sheet)

    out = pd.DataFrame(index=df.index)

    out["dataset"] = "Sanson2018"
    out["experiment"] = sheet

    out["guide_sequence"] = (
        df["sgRNA Sequence"]
        .astype(str)
        .str.upper()
        .str.replace(" ", "", regex=False)
    )

    out["gene_symbol"] = df["Annotated Gene Symbol"]

    out["gene_id"] = (
        df["Annotated Gene ID"]
        .astype(str)
    )

    out["chromosome"] = np.nan
    out["coordinate"] = np.nan
    out["strand"] = np.nan

    out["guide_length"] = out["guide_sequence"].str.len()

    # todavía no tenemos score
    out["score_raw"] = np.nan
    out["score_norm"] = np.nan

    out["score_type"] = "annotation_only"

    out["genome_build"] = "hg19"

    out["qc_pass"] = True

    return out[COMMON_COLUMNS]


def load():

    setA = _parse_sheet("SetA sgRNA annotations")
    setB = _parse_sheet("SetB sgRNA annotations")

    return pd.concat(
        [setA, setB],
        ignore_index=True,
    )