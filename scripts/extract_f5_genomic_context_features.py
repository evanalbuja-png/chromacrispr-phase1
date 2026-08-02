#!/usr/bin/env python3

import pandas as pd


INPUT = "data/interim/features/sgRNA_with_f2_f3_repressive.csv"

OUTPUT = "data/interim/features/f5_genomic_context_features.csv"


print("="*60)
print("ChromaCRISPR Phase 1")
print("Week 7 - F5 Genomic Context Features")
print("="*60)


df = pd.read_csv(
    INPUT,
    low_memory=False
)


print(f"\nInput rows: {len(df)}")


f5 = df[
    [
        "region_id",
        "chromosome",
        "coordinate",
        "start",
        "end",
        "strand",
        "gene_symbol",
        "gene_id",
        "dataset",
        "genome_build"
    ]
].copy()


print("\nCreating F5 features...")


# Gene availability

f5["has_gene_symbol"] = (
    f5["gene_symbol"]
    .notna()
    .astype(int)
)


# Strand availability

f5["strand_available"] = (
    f5["strand"]
    .notna()
    .astype(int)
)


# Relative position placeholder
# Will be updated with chromosome sizes later

f5["relative_position_placeholder"] = (
    f5["coordinate"]
)


print("\nF5 preview:")
print(f5.head())


print("\nMissing values:")
print(f5.isna().sum())


f5.to_csv(
    OUTPUT,
    index=False
)


print("\nSaved:")
print(OUTPUT)
