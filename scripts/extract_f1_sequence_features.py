from pathlib import Path
import pandas as pd

INPUT = Path("data/interim/features/sgRNA_with_f2_f3_repressive.csv")

print("=" * 60)
print("ChromaCRISPR Phase 1")
print("Week 7 - F1 Sequence Feature Extraction")
print("=" * 60)

print(f"\nLoading dataset:\n{INPUT}")

df = pd.read_csv(INPUT, low_memory=False)

print("\nDataset loaded successfully.")

print(f"Rows    : {len(df):,}")
print(f"Columns : {len(df.columns)}")

if "guide_sequence" not in df.columns:
    raise ValueError("Column 'guide_sequence' not found.")

print("\nguide_sequence column detected.")

print("\nExample guide:")
print(df["guide_sequence"].iloc[0])

print("\nReady to compute F1 features.")

print("\nCreating F1 feature table...")

f1_df = df[["guide_sequence", "region_id"]].copy()

print("Done.")

print("\nComputing GC content...")

def gc_content(seq):
    seq = seq.upper()
    return (seq.count("G") + seq.count("C")) / len(seq)

f1_df["gc_content"] = f1_df["guide_sequence"].apply(gc_content)

print("Done.")

print("\nF1 table:")
print(f1_df.head())

print("\nGC content summary:")
print(f1_df["gc_content"].describe())

print("\nComputing additional sequence features...")

import subprocess
import re


def compute_rnafold_mfe(sequences):
    """
    Compute RNAfold minimum free energy (MFE)
    for multiple guide sequences using batch mode.
    """

    print("\nRunning RNAfold batch calculation...")
    print(f"Sequences to process: {len(sequences)}")

    input_data = "\n".join(sequences)

    result = subprocess.run(
        ["RNAfold", "--noPS"],
        input=input_data,
        text=True,
        capture_output=True,
        check=True
    )

    lines = result.stdout.strip().split("\n")

    mfe_values = {}

    for i in range(0, len(lines), 2):

        if i + 1 >= len(lines):
            break

        sequence = lines[i].strip()
        structure_line = lines[i + 1].strip()

        match = re.search(
            r"\(\s*(-?\d+\.\d+)\)",
            structure_line
        )

        if match:
            mfe_values[sequence.replace("U", "T")] = float(
                match.group(1)
            )

    print(
        f"RNAfold results obtained: {len(mfe_values)}"
    )

    return mfe_values

print("\nComputing RNAfold MFE...")

unique_guides = f1_df["guide_sequence"].unique()

mfe_dict = compute_rnafold_mfe(unique_guides)

f1_df["mfe_rnafold"] = (
    f1_df["guide_sequence"]
    .map(mfe_dict)
)

print("\nMFE summary:")
print(
    f1_df["mfe_rnafold"].describe()
)

def longest_run(seq, base):
    longest = 0
    current = 0

    for nt in seq.upper():
        if nt == base:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    return longest

f1_df["guide_length"] = f1_df["guide_sequence"].str.len()

f1_df["g_run_max"] = f1_df["guide_sequence"].apply(
    lambda s: longest_run(s, "G")
)

f1_df["poly_t_count"] = f1_df["guide_sequence"].str.count("TTTT")

print("Done.")

print("\nCurrent F1 columns:")
print(f1_df.columns.tolist())

print("\nPreview:")
print(f1_df.head())

print("\nValidation")

print("\nGuide length distribution:")
print(f1_df["guide_length"].value_counts().sort_index())

print("\nMaximum G homopolymer:")
print(f1_df["g_run_max"].describe())

print("\nGuides containing TTTT:")
print((f1_df["poly_t_count"] > 0).sum())

print("\nChecking guide length consistency...")

if "guide_length" in df.columns:
    computed_length = df["guide_sequence"].str.len()

    comparison = (
        pd.DataFrame({
            "dataset_length": df["guide_length"],
            "computed_length": computed_length
        })
    )

    valid = comparison.dropna()

    matches = (
        valid["dataset_length"].astype(int)
        == valid["computed_length"]
    ).sum()

    total = len(valid)

    print(f"Comparable guides : {total:,}")
    print(f"Matching lengths  : {matches:,}")
    print(f"Mismatches        : {total - matches:,}")

    if total != matches:
        print("\nExamples of mismatches:")

        mismatch = valid[
            valid["dataset_length"].astype(int) != valid["computed_length"]
        ].copy()

        mismatch["guide_sequence"] = (
            df.loc[mismatch.index, "guide_sequence"]
        )

        mismatch["dataset"] = (
            df.loc[mismatch.index, "dataset"]
        )

        print(
            mismatch[
                [
                    "dataset",
                    "guide_sequence",
                    "dataset_length",
                    "computed_length",
                ]
            ].head(20)
        )
else:
    print("guide_length column not present in original dataset.")

print("\n" + "="*60)
print("Final F1 validation")
print("="*60)

# Expected dataset size
expected_rows = len(df)

print(f"Expected rows : {expected_rows}")
print(f"F1 rows       : {len(f1_df)}")

if len(f1_df) != expected_rows:
    raise ValueError(
        "F1 dataframe row count does not match original dataset"
    )

# Check missing values
print("\nMissing values:")

missing = f1_df.isna().sum()

print(missing)

if missing.sum() > 0:
    raise ValueError(
        "Missing values detected in F1 features"
    )

# Export
output_file = (
    "data/interim/features/f1_sequence_features.csv"
)

print("\nSaving F1 feature table...")

f1_df.to_csv(
    output_file,
    index=False
)

print(f"Saved: {output_file}")

print("\nF1 extraction completed successfully.")