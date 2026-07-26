## Week 6 - Step 1: F2 ATAC feature extraction (region_id association)

Date: 2026-07-26

- Changed ATAC-BED association method.
- Previous order-based matching rejected because:
  - ATAC regions: 155005
  - BED regions: 155454

- Implemented robust region_id matching:
  - Format: chr:start-end
  - Join type: inner join

Results:
- Matched regions: [reported by script]
- Discarded BED regions: 449 expected
- Coverage: [reported by script]

Generated:
data/interim/features/f2_atac_features.csv
