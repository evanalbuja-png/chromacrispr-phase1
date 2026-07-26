## Week 6 - Step 1: F2 ATAC feature extraction - FINAL STATUS

Date: 2026-07-26

Status: COMPLETED AND APPROVED

Summary:
- Extracted numerical ATAC-seq features from deepTools computeMatrix output.
- Parsed deepTools metadata JSON after removing '@' prefix.
- Extracted:
  - ATAC_mean
  - ATAC_max
  - ATAC_p90
  - ATAC_sum

Integration strategy:
- Created region_id:
  chr:start-end
- Association performed using inner join.
- Deduplication of region_id applied before merging.

Deduplication results:
- ATAC matrix:
  - Original regions: 155005
  - Duplicated region_id: 15274
  - Unique regions: 139731

- BED:
  - Original regions: 155454
  - Duplicated region_id: 15290
  - Unique regions: 140164

Final integration:
- Matched regions: 139731
- Coverage over unique BED: 99.691%

Decision:
The duplicated region_id entries are accepted as expected behavior for the current high-density sgRNA dataset.
Potential causes:
- multiple guides mapping to identical coordinates
- overlapping sgRNA regions

Further investigation of duplicate origins is deferred to optional QC.

Output:
data/interim/features/f2_atac_features.csv

## Week 6 - Step 2: Coordinate offset correction

Date: 2026-07-26

Issue:
Initial F2 integration showed low coverage (12.212%).

Diagnosis:
Coordinate comparison between sgRNA_unified_FINAL.csv and F2 features identified a systematic -1 bp offset.

Cause:
CSV coordinates were interpreted as 1-based while BED/deepTools coordinates are 0-based.

Correction:
Created region_id using:
start = coordinate - 1
end = start + 1

Result:
F2 integration recalculated after coordinate normalization.
