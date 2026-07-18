#!/usr/bin/env python3

import pandas as pd


resolved = pd.read_csv(
    "logs/sanson_tss_resolution_final.tsv",
    sep="\t"
)


unresolved = pd.read_csv(
    "logs/window2kb_unresolved.tsv",
    sep="\t"
)

fantom = pd.read_csv(
    "logs/fantom5_resolved.tsv",
    sep="\t"
)


resolved_guides = set(
    fantom["guide_sequence"]
)


unresolved = unresolved[
    ~unresolved["guide_sequence"].isin(resolved_guides)
]

unresolved["coordinate_source"] = "NONE"
unresolved["guide_position"] = None
unresolved["tss_position"] = None
unresolved["offset"] = None
unresolved["crispri_region"] = False
unresolved["status"] = "unresolved"


unresolved = unresolved[
    [
        "gene_symbol",
        "guide_sequence",
        "coordinate_source",
        "guide_position",
        "tss_position",
        "offset",
        "crispri_region",
        "status"
    ]
]


final = pd.concat(
    [
        resolved,
        unresolved
    ],
    ignore_index=True
)


final.to_csv(
    "logs/sanson_tss_resolution_complete.tsv",
    sep="\t",
    index=False
)


print("===== Complete resolution =====")
print("Total:", len(final))

print("\nFuente:")
print(final["coordinate_source"].value_counts())

print("\nEstado:")
print(final["status"].value_counts())
