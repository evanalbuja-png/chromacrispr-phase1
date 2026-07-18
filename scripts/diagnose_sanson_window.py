#!/usr/bin/env python3

import pandas as pd
from pyfaidx import Fasta


def reverse_complement(seq):
    comp = str.maketrans(
        "ACGTacgt",
        "TGCAtgca"
    )
    return seq.translate(comp)[::-1]


sgrna_file = "data/interim/sgRNA_unified.csv"
tss_file = "data/reference/hg38/gencode_v49_TSS_nochr.tsv"
fasta_file = "data/reference/hg38/fasta/Homo_sapiens.GRCh38.primary_assembly.fa"
failed_file = "logs/failed_sanson.tsv"


sgrna = pd.read_csv(
    sgrna_file,
    low_memory=False
)

sgrna = sgrna[
    sgrna["dataset"] == "Sanson2018"
]


tss = pd.read_csv(
    tss_file,
    sep="\t"
)

tss_unique = (
    tss
    .drop_duplicates(
        subset=["gene_name"],
        keep=False
    )
)


merged = sgrna.merge(
    tss_unique[
        [
            "gene_name",
            "chromosome",
            "strand",
            "tss"
        ]
    ],
    left_on="gene_symbol",
    right_on="gene_name",
    how="left"
)


failed = pd.read_csv(
    failed_file,
    sep="\t"
)

failed = failed[
    failed["failure_type"] == "sequence_absent"
]


test = failed.merge(
    merged,
    on=["guide_sequence", "gene_symbol"],
    how="left"
)


fasta = Fasta(fasta_file)


WINDOW = 2000

results = []
resolved = []
unresolved = []

for _, row in test.iterrows():

    gene = row["gene_symbol"]
    guide = row["guide_sequence"]

    if pd.isna(row["tss"]):
        print(gene, "NO TSS")
        continue
    
    print(merged.columns.tolist())
    chrom = str(row["chromosome_y"])
    tss_pos = int(row["tss"])

    start = max(0, tss_pos - WINDOW)
    end = tss_pos + WINDOW

    seq = str(
        fasta[chrom][start:end]
    ).upper()

    rc = reverse_complement(guide)

    pos_fwd = seq.find(guide)
    pos_rev = seq.find(rc)


    if pos_fwd != -1:

        guide_position = start + pos_fwd

        offset = guide_position - tss_pos

        resolved.append({
            "gene_symbol": gene,
            "guide_sequence": guide,
            "guide_position": guide_position,
            "gencode_tss": tss_pos,
            "offset": offset
        })

        results.append({
            "gene_symbol": gene,
            "guide_sequence": guide,
            "guide_position": guide_position,
            "gencode_tss": tss_pos,
            "offset": offset
        })

        print(
            f"{gene}: match (+) offset {offset:+d}"
        )

    elif pos_rev != -1:

        guide_position = start + pos_rev

        offset = guide_position - tss_pos

        resolved.append({
            "gene_symbol": gene,
            "guide_sequence": guide,
            "guide_position": guide_position,
            "gencode_tss": tss_pos,
            "offset": offset
        })

        results.append({
            "gene_symbol": gene,
            "guide_sequence": guide,
            "guide_position": guide_position,
            "gencode_tss": tss_pos,
            "offset": offset
        })

        print(
            f"{gene}: match (-) offset {offset:+d}"
        )

    else:
        unresolved.append({
            "gene_symbol": gene,
            "guide_sequence": guide
        })

print("\n===== Resumen =====")
print("Resueltos:", len(resolved))
print("No resueltos:", len(unresolved))
print("Total:", len(resolved) + len(unresolved))

pd.DataFrame(resolved).to_csv(
    "logs/window2kb_resolved.tsv",
    sep="\t",
    index=False
)

pd.DataFrame(unresolved).to_csv(
    "logs/window2kb_unresolved.tsv",
    sep="\t",
    index=False
)

pd.DataFrame(results).to_csv(
    "logs/window2kb_resolved_positions.tsv",
    sep="\t",
    index=False
)
