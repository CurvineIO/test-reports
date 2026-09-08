---
title: "Curvine full-chain daily test report - 2026-09-08"
linkTitle: "2026-09-08 full-chain"
date: 2026-09-08T00:00:00Z
weight: -20260908
tags: [full-chain, daily, go]
---

## Quality conclusion

### Executive summary

> [!NOTE]
> Release decision: **GO**. Pipeline **PASS**; ran 7 profiles, 6 passed, 0 failed.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 6/7 passed | PASS |
| Failure attribution | Failures classified | 0 root-cause groups | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run passed all release gates.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 09s | passed | PASSED |
| integration | PASS | PASS | 12m 52s | passed | PASSED |
| daily | PASS | PASS | 20m 29s | passed | PASSED |
| fuse | PASS | PASS | 5m 25s | passed | PASSED |
| ltp | PASS | PASS | 49m 39s | passed | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 3m 51s | failed | PASSED |

### LTP

- Status: **COMPLETED**
- Suites completed: 7
- Suites remaining: 0
- Stats: 1129 passed / 0 real failed / 141 skipped / 0 report-consistency errors

| Suite | Status | Passed | Real failed | Skipped | Report errors | Return code |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| fs_perms_simple | passed | 18 | 0 | 0 | 0 | 0 |
| fsx | passed | 1 | 0 | 0 | 0 | 0 |
| fs_bind | passed | 1 | 0 | 0 | 0 | 0 |
| smoketest | passed | 12 | 0 | 1 | 0 | 0 |
| io | passed | 2 | 0 | 0 | 0 | 0 |
| fs-jfs | passed | 27 | 0 | 2 | 0 | 0 |
| syscalls-jfs | passed | 1068 | 0 | 138 | 0 | 0 |

### Performance

> [!NOTE]
> Gate policy: **report only, non-blocking** for the full-chain result. Mark yellow/red vs baseline for human follow-up.

- Status: **failed**
- Gate mode: **report_only**

#### Metadata performance (this run)

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline VALUE | VALUE delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Create file | 23174.62 ops/s | 1.72 ms/op | 2.05 | 4.09 | 4.09 | 5.12 | 200000 | 0 | 21668.74 ops/s | +6.9% | 4.09 | +0.1% | pass |
| Stat file | 68329.76 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 2.26 | 200000 | 0 | 63487.48 ops/s | +7.6% | 2.05 | -50.1% | pass |
| Open file | 66247.78 ops/s | 0.60 ms/op | 1.02 | 1.02 | 2.05 | 2.44 | 200000 | 0 | 63113.20 ops/s | +5.0% | 2.05 | -0.1% | pass |
| Rename file | 32603.86 ops/s | 1.22 ms/op | 2.05 | 4.09 | 4.09 | 4.16 | 200000 | 0 | 30314.48 ops/s | +7.6% | 4.09 | +0.1% | pass |
| Delete file | 31985.44 ops/s | 1.24 ms/op | 2.05 | 4.09 | 4.09 | 4.36 | 200000 | 0 | 31231.33 ops/s | +2.4% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.72 | 28136.10 | 8.85 ms/op | 8.85 | 10.29 | 11.08 | 17.75 | 262144 | 0 | 1.71 | +0.4% | 10.94 | +1.2% | pass |
| Sequential read 64KB | 2.26 | 37067.87 | 6.37 ms/op | 6.00 | 10.42 | 12.52 | 20.90 | 262144 | 0 | 2.28 | -0.8% | 12.78 | -2.1% | pass |
| Random write 64KB | 1.77 | 29046.43 | 8.48 ms/op | 8.29 | 9.50 | 10.42 | 291.59 | 262144 | 0 | 1.77 | +0.2% | 10.29 | +1.3% | pass |
| Random read 64KB | 1.14 | 18716.55 | 13.07 ms/op | 12.91 | 16.19 | 18.48 | 50.52 | 262144 | 0 | 1.12 | +2.0% | 19.53 | -5.4% | pass |
| Sequential write 256KB | 2.72 | 11134.22 | 21.17 ms/op | 22.94 | 32.11 | 36.44 | 50.56 | 65536 | 0 | 2.73 | -0.4% | 36.44 | 0.0% | pass |
| Sequential read 256KB | 2.84 | 11638.43 | 20.41 ms/op | 22.94 | 27.13 | 28.70 | 45.74 | 65536 | 0 | 3.11 | -8.6% | 26.08 | +10.1% | pass |
| Random write 256KB | 2.61 | 10705.00 | 22.23 ms/op | 21.10 | 27.13 | 30.28 | 485.70 | 65536 | 0 | 2.51 | +4.1% | 30.28 | 0.0% | pass |
| Random read 256KB | 2.48 | 10162.20 | 24.27 ms/op | 24.25 | 29.23 | 32.11 | 48.72 | 65536 | 0 | 2.37 | +4.7% | 34.34 | -6.5% | pass |
| Sequential write 1MB | 3.18 | 3257.26 | 69.71 ms/op | 61.60 | 168.82 | 198.18 | 344.73 | 16384 | 0 | 3.45 | -7.8% | 191.89 | +3.3% | pass |
| Sequential read 1MB | 2.85 | 2917.90 | 79.11 ms/op | 87.56 | 101.19 | 106.43 | 173.08 | 16384 | 0 | 2.72 | +4.8% | 108.53 | -1.9% | pass |
| Random write 1MB | 2.96 | 3029.03 | 77.64 ms/op | 73.92 | 107.48 | 346.03 | 569.03 | 16384 | 0 | 3.09 | -4.3% | 229.64 | +50.7% | fail |
| Random read 1MB | 2.25 | 2305.66 | 105.50 ms/op | 106.43 | 120.06 | 130.55 | 176.75 | 16384 | 0 | 2.15 | +4.7% | 135.27 | -3.5% | pass |

## Failures and attribution

### Failure analysis

### Failed case summary

No named test failures were reported.

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |

### Common root-cause groups

No root-cause groups were required.

## Follow-up

### Defects and fixes

- GitHub Issue: none

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Continue monitoring the full-chain results.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
