#!/usr/bin/env python3

import pandas as pd
import subprocess
import os


SGRNA_INPUT = (
    "data/interim/features/"
    "sgRNA_with_f2_f3_repressive.csv"
)

TSS_INPUT = (
    "data/reference/hg38/"
    "gencode_v49_TSS.tsv"
)

OUTPUT = (
    "data/interim/features/"
    "f5_tss_features.csv"
)


SGRNA_BED = "data/interim/f5_sgrna.bed"
TSS_BED = "data/interim/f5_tss.bed"


print("="*60)
print("ChromaCRISPR Phase 1")
print("F5.2 - TSS Context Features")
print("="*60)


# -----------------------
# Create sgRNA BED
# -----------------------

print("\nLoading sgRNA dataset...")

df = pd.read_csv(
    SGRNA_INPUT,
    low_memory=False
)

df["sgrna_id"] = range(len(df))


sgrna_bed = df[
    [
        "chromosome",
        "start_0based",
        "end_0based",
        "sgrna_id",
        "region_id"
    ]
].copy()


sgrna_bed.to_csv(
    SGRNA_BED,
    sep="\t",
    header=False,
    index=False
)


print(
    f"sgRNA BED entries: {len(sgrna_bed)}"
)


# -----------------------
# Create TSS BED
# -----------------------

print("\nLoading GENCODE TSS...")

tss = pd.read_csv(
    TSS_INPUT,
    sep="\t"
)


tss["start"] = tss["tss"] - 1
tss["end"] = tss["tss"]


tss_bed = tss[
    [
        "chromosome",
        "start",
        "end",
        "gene_name",
        "strand"
    ]
]


tss_bed.to_csv(
    TSS_BED,
    sep="\t",
    header=False,
    index=False
)

# Sort BED files for bedtools compatibility

print("\nSorting BED files...")

subprocess.run(
    [
        "sort",
        "-k1,1",
        "-k2,2n",
        SGRNA_BED
    ],
    stdout=open(
        SGRNA_BED + ".sorted",
        "w"
    ),
    check=True
)

subprocess.run(
    [
        "sort",
        "-k1,1",
        "-k2,2n",
        TSS_BED
    ],
    stdout=open(
        TSS_BED + ".sorted",
        "w"
    ),
    check=True
)

SGRNA_BED = SGRNA_BED + ".sorted"
TSS_BED = TSS_BED + ".sorted"

print("BED sorting completed.")


print(
    f"TSS BED entries: {len(tss_bed)}"
)


# -----------------------
# bedtools closest
# -----------------------

print("\nRunning bedtools closest...")


cmd = [
    "bedtools",
    "closest",
    "-a",
    SGRNA_BED,
    "-b",
    TSS_BED,
    "-d"
]


result = subprocess.run(
    cmd,
    capture_output=True,
    text=True,
    check=True
)


# Parse output

cols = [
    "chromosome",
    "start",
    "end",
    "sgrna_id",
    "region_id",
    "tss_chr",
    "tss_start",
    "tss_end",
    "nearest_tss_gene",
    "nearest_tss_strand",
    "nearest_tss_distance"
]


closest = pd.DataFrame(
    [
        x.split("\t")
        for x in result.stdout.strip().split("\n")
    ],
    columns=cols
)


closest["nearest_tss_distance"] = (
    closest["nearest_tss_distance"]
    .astype(int)
)


closest["within_promoter_2kb"] = (
    closest["nearest_tss_distance"]
    <= 2000
).astype(int)


features = closest[
    [
        "sgrna_id",
        "region_id",
        "nearest_tss_gene",
        "nearest_tss_strand",
        "nearest_tss_distance",
        "within_promoter_2kb"
    ]
]

# Resolve tied TSS assignments
duplicates = (
    features["sgrna_id"]
    .duplicated()
    .sum()
)

print(
    "\nTSS ties detected:",
    duplicates
)

features = (
    features
    .sort_values("sgrna_id")
    .drop_duplicates(
        "sgrna_id",
        keep="first"
    )
    .reset_index(drop=True)
)

features = features.sort_values(
    "sgrna_id"
).reset_index(drop=True)

print("\nFinal validation:")
print("Rows:", len(features))
print(
    "Unique sgrna_id:",
    features["sgrna_id"].nunique()
)

assert len(features) == 155454
assert features["sgrna_id"].nunique() == 155454

features.to_csv(
    OUTPUT,
    index=False
)


print("\nOutput:")
print(OUTPUT)

print("\nPreview:")
print(features.head())

print("\nDistance summary:")
print(
    features["nearest_tss_distance"]
    .describe()
)

print("\nCompleted.")

