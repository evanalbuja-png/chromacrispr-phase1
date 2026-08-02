## Week 7 - F1 Sequence Features Extraction

Date:
2026-08-02

## Objective

Extract and integrate sequence-level features (F1) from the main sgRNA dataset.

Input dataset:

data/interim/features/sgRNA_with_f2_f3_repressive.csv


Rows processed:

155,454 sgRNAs


## Generated features

The following sequence features were extracted:

- GC content
- guide length
- RNAfold minimum free energy (MFE)
- maximum G homopolymer length
- poly-T motif count


## RNAfold calculation

ViennaRNA RNAfold 2.7.2 was used.

Calculation mode:

Batch processing of unique guide sequences.


Unique sequences processed:

150,311


Results obtained:

150,311


Final coverage:

155,454 / 155,454 guides


## Guide length validation

The original dataset_length column was evaluated.

A total of 21,172 mismatches were detected.

All mismatches corresponded to Horlbeck2016.

Observed pattern:

dataset_length = sequence_length + 3


This was interpreted as guide + PAM length.

Decision:

guide_length was calculated exclusively from guide_sequence length.


## Final output

Generated file:

data/interim/features/f1_sequence_features.csv


Columns:

- guide_sequence
- region_id
- gc_content
- mfe_rnafold
- guide_length
- g_run_max
- poly_t_count


Validation:

Rows preserved:
155,454 / 155,454

Missing values:
0


Status:

F1 Sequence Features completed.
