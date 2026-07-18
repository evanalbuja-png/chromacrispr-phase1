from pathlib import Path

import numpy as np
import pandas as pd

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

ROOT = Path(__file__).resolve().parents[2]

FILE = (
    ROOT
    / "data/raw/crispr_datasets/Replogle2022"
    / "NIHMS1812939-supplement-11.xlsx"
)

def _expand_guides(df, experiment):

    records = []

    for suffix in ["A", "B"]:

        tmp = pd.DataFrame(index=df.index)

        tmp["dataset"] = "Replogle2022"

        tmp["experiment"] = experiment

        tmp["guide_sequence"] = (
            df[f"targeting sequence {suffix}"]
            .astype(str)
            .str.upper()
            .str.replace(" ", "", regex=False)
        )

        tmp["gene_symbol"] = df["gene"]

        tmp["gene_id"] = (
            df["ensembl gene id"]
            .astype(str)
        )

        tmp["chromosome"] = np.nan

        tmp["coordinate"] = np.nan

        tmp["strand"] = np.nan

        tmp["guide_length"] = (
            tmp["guide_sequence"]
            .str.len()
        )

        tmp["score_raw"] = np.nan

        tmp["score_norm"] = np.nan

        tmp["score_type"] = "paired_library"

        tmp["genome_build"] = "hg38"

        tmp["qc_pass"] = True

        records.append(
            tmp[COMMON_COLUMNS]
        )

    return pd.concat(records, ignore_index=True)

def load():

    tabs = {
        "K562_day8": "TabA_K562_day8_library",
        "K562_day6": "TabB_K562_day6_library",
        "RPE1_day7": "TabC_RPE1_day7_library",
    }

    dfs = []

    for experiment, sheet in tabs.items():

        df = pd.read_excel(
            FILE,
            sheet_name=sheet,
            engine="openpyxl",
        )

        dfs.append(
            _expand_guides(df, experiment)
        )

    return pd.concat(
        dfs,
        ignore_index=True
    )