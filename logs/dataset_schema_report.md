# CRISPR Dataset Schema Report

# NIHMS1038673-supplement-TableS1.xlsx

Path: `/mnt/d/Documentos/Proyectos/ChromaCRISPR/data/raw/crispr_datasets/Gasperini2019/NIHMS1038673-supplement-TableS1.xlsx`

Sheets (2):
- A_Pilot_gRNA_library
- B_Pilot_145_enhancergene_pairs

---
## Sheet: A_Pilot_gRNA_library

Rows: 3,118

Columns: 6

|Column|dtype|Missing %|
|---|---|---|
|Spacer|object|0.00|
|Target_Site|object|0.00|
|chr.candidate_enhancer|object|28.13|
|start.candidate_enhancer|float64|28.13|
|stop.candidate_enhancer|float64|28.13|
|category|object|0.00|

### First five rows

| Spacer               | Target_Site   | chr.candidate_enhancer   |   start.candidate_enhancer |   stop.candidate_enhancer | category           |
|:---------------------|:--------------|:-------------------------|---------------------------:|--------------------------:|:-------------------|
| CAAGCTGGTTAAAAACCCCG | chr1.576      | chr1                     |                2.472e+06   |               2.47436e+06 | candidate_enhancer |
| GCAAAGTAGGTCTTTCCCAG | chr1.576      | chr1                     |                2.472e+06   |               2.47436e+06 | candidate_enhancer |
| GGCCCGCCAGGAAAGCTGCA | chr1.1432     | chr1                     |                8.25763e+06 |               8.25838e+06 | candidate_enhancer |
| TCCACGAAAAGTGATCCCCA | chr1.1432     | chr1                     |                8.25763e+06 |               8.25838e+06 | candidate_enhancer |
| TGATGAGTAACTCAGAGGAG | chr1.1488     | chr1                     |                8.96001e+06 |               8.96027e+06 | candidate_enhancer |

## Sheet: B_Pilot_145_enhancergene_pairs

Rows: 145

Columns: 8

|Column|dtype|Missing %|
|---|---|---|
|Target_Site|object|0.00|
|ENSG|object|0.00|
|target_gene_short|object|0.00|
|Diff_expression_test_raw_pval|float64|0.00|
|Diff_expression_test_fold_change|float64|0.00|
|chr.candidate_enhancer|object|0.00|
|start.candidate_enhancer|int64|0.00|
|stop.candidate_enhancer|int64|0.00|

### First five rows

| Target_Site   | ENSG            | target_gene_short   |   Diff_expression_test_raw_pval |   Diff_expression_test_fold_change | chr.candidate_enhancer   |   start.candidate_enhancer |   stop.candidate_enhancer |
|:--------------|:----------------|:--------------------|--------------------------------:|-----------------------------------:|:-------------------------|---------------------------:|--------------------------:|
| chr4.1626     | ENSG00000109255 | NMU                 |                    0            |                           0.206331 | chr4                     |                   56595855 |                  56596581 |
| chr4.1627     | ENSG00000109255 | NMU                 |                    0            |                           0.21781  | chr4                     |                   56596632 |                  56597095 |
| chrX.232      | ENSG00000205542 | TMSB4X              |                    0            |                           0.369964 | chrX                     |                   12973885 |                  12974748 |
| chrX.233      | ENSG00000205542 | TMSB4X              |                    0            |                           0.31626  | chrX                     |                   12974917 |                  12975383 |
| chr16.1866    | ENSG00000166501 | PRKCB               |                    1.77781e-121 |                           0.451848 | chr16                    |                   23833191 |                  23833694 |

# NIHMS1038673-supplement-TableS2.xlsx

Path: `/mnt/d/Documentos/Proyectos/ChromaCRISPR/data/raw/crispr_datasets/Gasperini2019/NIHMS1038673-supplement-TableS2.xlsx`

Sheets (3):
- Key
- S2A_AtScale_library_gRNA.cs
- B_AtScale_664_enhancergenepairs

---
## Sheet: Key

Rows: 19

Columns: 1

|Column|dtype|Missing %|
|---|---|---|
|Tab S2A | Annotated table of the gRNAs and candidate enhancers for the at-scale experiment, as well as all controls|object|5.26|

### First five rows

| Tab S2A | Annotated table of the gRNAs and candidate enhancers for the at-scale experiment, as well as all controls                                       |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Spacer | sequence of the 19 (for TSS controls) or 20 bp (for all else) spacer                                                                             |
| Target_Site | ID for targeted locus. Candidate enhancers’ IDs are derived from the original DHS peaks used to define theenhancersite (ENCODE ENCFF001UWQ) |
| chr.candidate_enhancer  | chromosomal location of candidate enhancers                                                                                     |
| start.candidate_enhancer | start coordinate of original DHS peak used to define candidate enhancer (hg19, ENCFF001UWQ)                                    |
| stop.candidate_enhancer |  stop coordinate of original DHS peak used to define candidate enhancer (hg19, ENCFF001UWQ)                                     |

## Sheet: S2A_AtScale_library_gRNA.cs

Rows: 13,189

Columns: 6

|Column|dtype|Missing %|
|---|---|---|
|Spacer|object|0.00|
|Target_Site|object|0.00|
|chr.candidate_enhancer|object|6.65|
|start.candidate_enhancer|float64|6.65|
|stop.candidate_enhancer|float64|6.65|
|Category|object|0.00|

### First five rows

| Spacer               | Target_Site   |   chr.candidate_enhancer |   start.candidate_enhancer |   stop.candidate_enhancer | Category   |
|:---------------------|:--------------|-------------------------:|---------------------------:|--------------------------:|:-----------|
| AATGAGGAGCAAACGAAAAT | control       |                      nan |                        nan |                       nan | NTC        |
| ACGAAATGTTTCATGACCAA | control       |                      nan |                        nan |                       nan | NTC        |
| ATAGATTTACGTTACTCTCT | control       |                      nan |                        nan |                       nan | NTC        |
| ATTAGCATCAGGTAGACTAA | control       |                      nan |                        nan |                       nan | NTC        |
| CCATAAAGAATTCGGTGTAG | control       |                      nan |                        nan |                       nan | NTC        |

## Sheet: B_AtScale_664_enhancergenepairs

Rows: 664

Columns: 11

|Column|dtype|Missing %|
|---|---|---|
|Target_Site|object|0.00|
|ENSG|object|0.00|
|target_gene_short|object|0.00|
|Diff_expression_test_raw_pval|float64|0.00|
|Diff_expression_test_fold_change|float64|0.00|
|Diff_expression_test_Empirical_pval|float64|0.00|
|Diff_expression_test_Empirical_adjusted_pval|float64|0.00|
|high_confidence_subset|bool|0.00|
|chr.candidate_enhancer|object|0.00|
|start.candidate_enhancer|int64|0.00|
|stop.candidate_enhancer|int64|0.00|

### First five rows

| Target_Site   | ENSG            | target_gene_short   |   Diff_expression_test_raw_pval |   Diff_expression_test_fold_change |   Diff_expression_test_Empirical_pval |   Diff_expression_test_Empirical_adjusted_pval | high_confidence_subset   | chr.candidate_enhancer   |   start.candidate_enhancer |   stop.candidate_enhancer |
|:--------------|:----------------|:--------------------|--------------------------------:|-----------------------------------:|--------------------------------------:|-----------------------------------------------:|:-------------------------|:-------------------------|---------------------------:|--------------------------:|
| chr2.2482     | ENSG00000115977 | AAK1                |                     0.00145157  |                           0.756542 |                           0.00271911  |                                      0.0986519 | True                     | chr2                     |                   69056234 |                  69056865 |
| chrX.2695     | ENSG00000101986 | ABCD1               |                     0.000735184 |                           0.669369 |                           0.00182457  |                                      0.0730137 | True                     | chrX                     |                  153250743 |                 153251468 |
| chr10.2252    | ENSG00000138316 | ADAMTS14            |                     2.14e-09    |                           0.447355 |                           0.000449245 |                                      0.0324977 | False                    | chr10                    |                   72426863 |                  72427518 |
| chr1.8461     | ENSG00000143382 | ADAMTSL4            |                     0.000115726 |                           0.667658 |                           0.0010443   |                                      0.0504136 | True                     | chr1                     |                  150517877 |                 150518596 |
| chr11.1006    | ENSG00000148926 | ADM                 |                     0.000588113 |                           0.309175 |                           0.00165117  |                                      0.0673358 | True                     | chr11                    |                    9573345 |                   9573973 |

# elife-19760-supp1-v2.xlsx

Path: `/mnt/d/Documentos/Proyectos/ChromaCRISPR/data/raw/crispr_datasets/Horlbeck2016/elife-19760-supp1-v2.xlsx`

Sheets (2):
- CRISPRi
- CRISPRa

---
## Sheet: CRISPRi

Rows: 18,380

Columns: 7

|Column|dtype|Missing %|
|---|---|---|
|gene symbol|object|0.00|
|chromosome|object|0.00|
|PAM genomic coordinate [hg19]|int64|0.00|
|strand targeted|object|0.00|
|sgRNA length (including PAM)|int64|0.00|
|sgRNA sequence|object|0.00|
|CRISPRi activity score [Horlbeck et al., eLife 2016]|float64|0.00|

### First five rows

| gene symbol   | chromosome   |   PAM genomic coordinate [hg19] | strand targeted   |   sgRNA length (including PAM) | sgRNA sequence        |   CRISPRi activity score [Horlbeck et al., eLife 2016] |
|:--------------|:-------------|--------------------------------:|:------------------|-------------------------------:|:----------------------|-------------------------------------------------------:|
| AARS          | chr16        |                        70323441 | +                 |                             24 | GCGCTCTGATTGGACGGAGCG |                                              0.0193204 |
| AARS          | chr16        |                        70323216 | +                 |                             24 | GCCCCAGGATCAGGCCCCGCG |                                              0.348892  |
| AARS          | chr16        |                        70323296 | +                 |                             24 | GGCCGCCCTCGGAGAGCTCTG |                                              0.912409  |
| AARS          | chr16        |                        70323318 | +                 |                             24 | GACGGCGACCCTAGGAGAGGT |                                              0.997242  |
| AARS          | chr16        |                        70323362 | +                 |                             24 | GGTGCAGCGGGCCCTTGGCGG |                                              0.962154  |

## Sheet: CRISPRa

Rows: 2,792

Columns: 7

|Column|dtype|Missing %|
|---|---|---|
|gene symbol|object|0.00|
|chromosome|object|0.00|
|PAM genomic coordinate [hg19]|int64|0.00|
|strand targeted|object|0.00|
|sgRNA length (including PAM)|int64|0.00|
|sgRNA sequence|object|0.00|
|CRISPRa activity score|float64|0.00|

### First five rows

| gene symbol   | chromosome   |   PAM genomic coordinate [hg19] | strand targeted   |   sgRNA length (including PAM) | sgRNA sequence        |   CRISPRa activity score |
|:--------------|:-------------|--------------------------------:|:------------------|-------------------------------:|:----------------------|-------------------------:|
| AHR           | chr7         |                        17337908 | +                 |                             24 | GacaactggtagacaacCAAT |              -0.00567068 |
| AHR           | chr7         |                        17337955 | +                 |                             24 | GACGGTGGGTCAGCTAACTTG |               0.0725472  |
| AHR           | chr7         |                        17338075 | +                 |                             23 | GTAAGGACGCCCCCCCCCGC  |               0.181175   |
| AHR           | chr7         |                        17338134 | +                 |                             24 | GATTCCATTCCGTCTTCCTTG |               0.185431   |
| AHR           | chr7         |                        17337989 | -                 |                             22 | GACCCACCGTCTCTCAAAC   |               0.0755291  |

# NIHMS1812939-supplement-11.xlsx

Path: `/mnt/d/Documentos/Proyectos/ChromaCRISPR/data/raw/crispr_datasets/Replogle2022/NIHMS1812939-supplement-11.xlsx`

Sheets (3):
- TabA_K562_day8_library
- TabB_K562_day6_library
- TabC_RPE1_day7_library

---
## Sheet: TabA_K562_day8_library

Rows: 11,294

Columns: 10

|Column|dtype|Missing %|
|---|---|---|
|unique sgRNA pair ID|object|0.00|
|gene|object|0.00|
|transcript|object|0.00|
|ensembl gene id|object|0.17|
|sgID_A|object|0.00|
|targeting sequence A|object|0.00|
|sgID_B|object|0.00|
|targeting sequence B|object|0.00|
|duplicated guide pair?|bool|0.00|
|either guide duplicated?|bool|0.00|

### First five rows

| unique sgRNA pair ID          | gene   | transcript   | ensembl gene id   | sgID_A                   | targeting sequence A   | sgID_B                   | targeting sequence B   | duplicated guide pair?   | either guide duplicated?   |
|:------------------------------|:-------|:-------------|:------------------|:-------------------------|:-----------------------|:-------------------------|:-----------------------|:-------------------------|:---------------------------|
| 0_A1BG_P1_ENSG00000121410     | A1BG   | P1           | ENSG00000121410   | A1BG_+_58858964.23-P1    | GCTCCGGGCGACGTGGAGTG   | A1BG_-_58858788.23-P1    | GGGGCACCCAGGAGCGGTAG   | False                    | False                      |
| 1_A1BG_P2_ENSG00000121410     | A1BG   | P2           | ENSG00000121410   | A1BG_-_58864840.23-P2    | GCCGGTGCAGTGAGTGTCTG   | A1BG_-_58864822.23-P2    | GATGATGGTCGCGCTCACTC   | False                    | False                      |
| 2_AAAS_P1P2_ENSG00000094914   | AAAS   | P1P2         | ENSG00000094914   | AAAS_-_53715438.23-P1P2  | GAGGACGAGTACGCGGTCCC   | AAAS_+_53715355.23-P1P2  | GCCTCGCCGTTTGTCCCTTG   | False                    | False                      |
| 3_AACS_P1P2_ENSG00000081760   | AACS   | P1P2         | ENSG00000081760   | AACS_+_125549983.23-P1P2 | GCGGCGGCGGCGGGGAACAA   | AACS_-_125550169.23-P1P2 | GCCCGGTCGGGAGGAGATCC   | False                    | False                      |
| 4_PRXL2C_P1P2_ENSG00000158122 | PRXL2C | P1P2         | ENSG00000158122   | AAED1_-_99417574.23-P1P2 | GGCGCGGCCATGACGCGGGG   | AAED1_+_99417525.23-P1P2 | GCGGTCACGCGGCAGGTTAG   | False                    | False                      |

## Sheet: TabB_K562_day6_library

Rows: 2,291

Columns: 10

|Column|dtype|Missing %|
|---|---|---|
|unique sgRNA pair ID|object|0.00|
|gene|object|0.00|
|transcript|object|0.00|
|ensembl gene id|object|0.13|
|sgID_A|object|0.00|
|targeting sequence A|object|0.00|
|sgID_B|object|0.00|
|targeting sequence B|object|0.00|
|duplicated guide pair?|bool|0.00|
|either guide duplicated?|bool|0.00|

### First five rows

| unique sgRNA pair ID             | gene     | transcript   | ensembl gene id   | sgID_A                       | targeting sequence A   | sgID_B                       | targeting sequence B   | duplicated guide pair?   | either guide duplicated?   |
|:---------------------------------|:---------|:-------------|:------------------|:-----------------------------|:-----------------------|:-----------------------------|:-----------------------|:-------------------------|:---------------------------|
| 2_AAAS_P1P2_ENSG00000094914      | AAAS     | P1P2         | ENSG00000094914   | AAAS_-_53715438.23-P1P2      | GAGGACGAGTACGCGGTCCC   | AAAS_+_53715355.23-P1P2      | GCCTCGCCGTTTGTCCCTTG   | False                    | False                      |
| 8_AAMP_P1P2_ENSG00000127837      | AAMP     | P1P2         | ENSG00000127837   | AAMP_+_219134851.23-P1P2     | GGTCGCGCAGAGCTGACTCT   | AAMP_+_219134841.23-P1P2     | GGCTGACTCTGGGAGGCGTT   | False                    | False                      |
| 10_AARS2_P1P2_ENSG00000124608    | AARS2    | P1P2         | ENSG00000124608   | AARS2_+_44281027.23-P1P2     | GAGTGGCAGCTGCAGCCCGG   | AARS2_+_44281044.23-P1P2     | GGCTACGATGGCAGCGTCAG   | False                    | False                      |
| 13_AARS_P1P2_ENSG00000090861     | AARS     | P1P2         | ENSG00000090861   | AARS_+_70323362.23-P1P2      | GTGCAGCGGGCCCTTGGCGG   | AARS_-_70323332.23-P1P2      | GAGGGCGGCCTACCTCTCCT   | False                    | False                      |
| 14_AASDHPPT_P1P2_ENSG00000149313 | AASDHPPT | P1P2         | ENSG00000149313   | AASDHPPT_+_105948405.23-P1P2 | GCGGACCTCGCCGCTATCTC   | AASDHPPT_+_105948450.23-P1P2 | GGGCACCAAGCAGAACCGTT   | False                    | True                       |

## Sheet: TabC_RPE1_day7_library

Rows: 2,688

Columns: 10

|Column|dtype|Missing %|
|---|---|---|
|unique sgRNA pair ID|object|0.00|
|gene|object|0.00|
|transcript|object|0.00|
|ensembl gene id|object|0.22|
|sgID_A|object|0.00|
|targeting sequence A|object|0.00|
|sgID_B|object|0.00|
|targeting sequence B|object|0.00|
|duplicated guide pair?|bool|0.00|
|either guide duplicated?|bool|0.00|

### First five rows

| unique sgRNA pair ID          | gene   | transcript   | ensembl gene id   | sgID_A                   | targeting sequence A   | sgID_B                   | targeting sequence B   | duplicated guide pair?   | either guide duplicated?   |
|:------------------------------|:-------|:-------------|:------------------|:-------------------------|:-----------------------|:-------------------------|:-----------------------|:-------------------------|:---------------------------|
| 2_AAAS_P1P2_ENSG00000094914   | AAAS   | P1P2         | ENSG00000094914   | AAAS_-_53715438.23-P1P2  | GAGGACGAGTACGCGGTCCC   | AAAS_+_53715355.23-P1P2  | GCCTCGCCGTTTGTCCCTTG   | False                    | False                      |
| 8_AAMP_P1P2_ENSG00000127837   | AAMP   | P1P2         | ENSG00000127837   | AAMP_+_219134851.23-P1P2 | GGTCGCGCAGAGCTGACTCT   | AAMP_+_219134841.23-P1P2 | GGCTGACTCTGGGAGGCGTT   | False                    | False                      |
| 9_AAR2_P1P2_ENSG00000131043   | AAR2   | P1P2         | ENSG00000131043   | AAR2_-_34824434.23-P1P2  | GTGGGGCGAGGCGGTGAGTG   | AAR2_+_34824488.23-P1P2  | GGACTCTGAGCCGAGAAGAG   | False                    | False                      |
| 10_AARS2_P1P2_ENSG00000124608 | AARS2  | P1P2         | ENSG00000124608   | AARS2_+_44281027.23-P1P2 | GAGTGGCAGCTGCAGCCCGG   | AARS2_+_44281044.23-P1P2 | GGCTACGATGGCAGCGTCAG   | False                    | False                      |
| 13_AARS_P1P2_ENSG00000090861  | AARS   | P1P2         | ENSG00000090861   | AARS_+_70323362.23-P1P2  | GTGCAGCGGGCCCTTGGCGG   | AARS_-_70323332.23-P1P2  | GAGGGCGGCCTACCTCTCCT   | False                    | False                      |

# 41467_2018_7901_MOESM6_ESM.xlsx

Path: `/mnt/d/Documentos/Proyectos/ChromaCRISPR/data/raw/crispr_datasets/Sanson2018/41467_2018_7901_MOESM6_ESM.xlsx`

Sheets (4):
- SetA raw reads
- SetB raw reads
- SetA sgRNA annotations
- SetB sgRNA annotations

---
## Sheet: SetA raw reads

Rows: 57,052

Columns: 8

|Column|dtype|Missing %|
|---|---|---|
|Supplementary Data 3. Dolcetto CRISPRi screening data|object|0.00|
|Unnamed: 1|object|0.00|
|Unnamed: 2|object|0.00|
|Unnamed: 3|object|0.00|
|Unnamed: 4|object|0.00|
|Unnamed: 5|object|0.00|
|Unnamed: 6|object|0.00|
|Unnamed: 7|object|0.00|

### First five rows

| Supplementary Data 3. Dolcetto CRISPRi screening data   | Unnamed: 1   | Unnamed: 2   | Unnamed: 3   | Unnamed: 4   | Unnamed: 5   | Unnamed: 6   | Unnamed: 7   |
|:--------------------------------------------------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|:-------------|
| nan                                                     | pDNA         | HT29         | HT29         | HT29         | A375         | A375         | A375         |
| sgRNA Sequence                                          | pDNA         | RepA         | RepB         | RepC         | RepA         | RepB         | RepC         |
| AAAAAAAAAATACTGAGAGA                                    | 503          | 264          | 231          | 275          | 483          | 608          | 337          |
| AAAAAAAAGAGGAGGGACGG                                    | 821          | 184          | 255          | 115          | 181          | 250          | 123          |
| AAAAAAAATTTCCTAGCGTG                                    | 304          | 61           | 148          | 207          | 213          | 319          | 247          |

## Sheet: SetB raw reads

Rows: 57,012

Columns: 8

|Column|dtype|Missing %|
|---|---|---|
|Unnamed: 0|object|0.00|
|pDNA|object|0.00|
|HT29|object|0.00|
|HT29.1|object|0.00|
|HT29.2|object|0.00|
|A375|object|0.00|
|A375.1|object|0.00|
|A375.2|object|0.00|

### First five rows

| Unnamed: 0           | pDNA   | HT29   | HT29.1   | HT29.2   | A375   | A375.1   | A375.2   |
|:---------------------|:-------|:-------|:---------|:---------|:-------|:---------|:---------|
| sgRNA Sequence       | pDNA   | RepA   | RepB     | RepC     | RepA   | RepB     | RepC     |
| AAAAAAAAAATTTCCTAGCG | 257    | 275    | 201      | 187      | 394    | 137      | 155      |
| AAAAAAAAAGCTGTGCGCAG | 417    | 433    | 474      | 340      | 445    | 270      | 498      |
| AAAAAAAACTGTCCCGCAAC | 623    | 746    | 734      | 640      | 1182   | 784      | 642      |
| AAAAAAAAGTGGTGGGGTGG | 986    | 1108   | 1014     | 772      | 1474   | 628      | 492      |

## Sheet: SetA sgRNA annotations

Rows: 57,050

Columns: 3

|Column|dtype|Missing %|
|---|---|---|
|sgRNA Sequence|object|0.00|
|Annotated Gene Symbol|object|0.00|
|Annotated Gene ID|object|0.00|

### First five rows

| sgRNA Sequence       | Annotated Gene Symbol   |   Annotated Gene ID |
|:---------------------|:------------------------|--------------------:|
| AAAAAAAAAATACTGAGAGA | GATA3                   |                2625 |
| AAAAAAAAGAGGAGGGACGG | ANKH                    |               56172 |
| AAAAAAAATTTCCTAGCGTG | SMARCAD1                |               56916 |
| AAAAAAACCAGCCTAGCTCG | JAG1                    |                 182 |
| AAAAAAACTGTCCCGCAACC | MAP1LC3C                |              440738 |

## Sheet: SetB sgRNA annotations

Rows: 57,011

Columns: 3

|Column|dtype|Missing %|
|---|---|---|
|sgRNA Sequence|object|0.00|
|Annotated Gene Symbol|object|0.00|
|Annotated Gene ID|object|0.00|

### First five rows

| sgRNA Sequence       | Annotated Gene Symbol   |   Annotated Gene ID |
|:---------------------|:------------------------|--------------------:|
| AAAAAAAAAATTTCCTAGCG | SMARCAD1                |               56916 |
| AAAAAAAAAGCTGTGCGCAG | LOC100129112            |           100129112 |
| AAAAAAAACTGTCCCGCAAC | MAP1LC3C                |              440738 |
| AAAAAAAAGTGGTGGGGTGG | LRRC70                  |           100130733 |
| AAAAAAAGAAAGAAACACAA | LRRC19                  |               64922 |

