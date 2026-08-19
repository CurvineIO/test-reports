---
title: "Curvine full-chain daily test report - 2026-08-06"
linkTitle: "2026-08-06 full-chain"
date: 2026-08-06T00:00:00Z
weight: -20260806
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 6 passed, 1 failed.

A blocking failure exists. This revision is not releasable. Finish attribution, fix, and targeted regression, then rerun the full-chain tests.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 6/7 passed | FAIL |
| Failure attribution | Failures classified | 1 failure | pending per-item |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Route by failure class into product fix, harness fix, or environment work.

Unattributed failed profile: fuse.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 1m 35s | passed | passed |
| integration | PASS | PASS | 6m 08s | passed | passed |
| daily | PASS | PASS | 13m 31s | passed | passed |
| ltp | PASS | PASS | 48m 03s | passed | passed |
| csi | PASS | PASS | 0m 35s | passed | passed |
| perf-benchmark | NOT_RECORDED | PASS | 2m 04s | failed | passed |
| fuse | PASS | FAIL | 2m 56s | unknown_failure | passed |

### LTP

- Status: **completed**
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

#### Failed and abnormal cases

No TFAIL/TBROK parsed.

### Performance

> [!NOTE]
> Gate policy: **report only, non-blocking** for the full-chain result. Mark yellow/red vs baseline for human follow-up.

- Status: **failed**
- Gate mode: **report_only**

#### Metadata performance (this run)

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Create file | 21392.01 ops/s | 1.86 ms/op | 2.05 | 4.09 | 4.09 | 162.66 | 200000 | 0 | pass |
| Stat file | 63836.79 ops/s | 0.62 ms/op | 1.02 | 1.02 | 2.05 | 2.59 | 200000 | 0 | pass |
| Open file | 63916.00 ops/s | 0.62 ms/op | 1.02 | 1.02 | 2.05 | 2.43 | 200000 | 0 | pass |
| Rename file | 29170.42 ops/s | 1.36 ms/op | 2.05 | 4.09 | 4.09 | 5.01 | 200000 | 0 | pass |
| Delete file | 29501.85 ops/s | 1.35 ms/op | 2.05 | 4.09 | 4.09 | 4.28 | 200000 | 0 | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.70 | 27840.27 | 9.00 ms/op | 8.98 | 10.55 | 11.47 | 18.43 | 262144 | 0 | pass |
| Sequential read 64KB | 2.38 | 39044.38 | 6.13 ms/op | 5.73 | 10.55 | 12.39 | 20.34 | 262144 | 0 | pass |
| Random write 64KB | 1.77 | 28950.19 | 8.57 ms/op | 8.36 | 9.63 | 10.55 | 294.08 | 262144 | 0 | pass |
| Random read 64KB | 1.08 | 17776.09 | 13.49 ms/op | 13.30 | 16.91 | 20.05 | 50.87 | 262144 | 0 | pass |
| Sequential write 256KB | 2.71 | 11094.63 | 21.05 ms/op | 22.41 | 33.42 | 39.58 | 57.34 | 65536 | 0 | pass |
| Sequential read 256KB | 2.53 | 10361.42 | 22.97 ms/op | 25.03 | 28.44 | 30.02 | 52.41 | 65536 | 0 | degraded |
| Random write 256KB | 2.58 | 10585.69 | 22.49 ms/op | 21.63 | 28.18 | 31.33 | 440.01 | 65536 | 0 | pass |
| Random read 256KB | 2.38 | 9765.46 | 25.30 ms/op | 25.30 | 30.54 | 33.82 | 49.95 | 65536 | 0 | pass |
| Sequential write 1MB | 3.12 | 3196.25 | 68.41 ms/op | 59.51 | 156.24 | 265.29 | 352.43 | 16384 | 0 | fail |
| Sequential read 1MB | 2.93 | 2996.34 | 77.47 ms/op | 85.46 | 99.09 | 103.28 | 132.46 | 16384 | 0 | pass |
| Random write 1MB | 2.97 | 3044.22 | 78.36 ms/op | 73.92 | 112.72 | 274.73 | 529.95 | 16384 | 0 | degraded |
| Random read 1MB | 2.26 | 2314.78 | 105.69 ms/op | 106.43 | 119.01 | 126.35 | 187.02 | 16384 | 0 | pass |

#### Metadata performance baseline

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Create file | 21668.74 ops/s | 1.84 ms/op | 2.05 | 4.09 | 4.09 | 188.88 | 200000 | 0 |
| Stat file | 63487.48 ops/s | 0.63 ms/op | 1.02 | 1.02 | 2.05 | 2.57 | 200000 | 0 |
| Open file | 63113.20 ops/s | 0.63 ms/op | 1.02 | 1.02 | 2.05 | 2.53 | 200000 | 0 |
| Rename file | 30314.48 ops/s | 1.31 ms/op | 2.05 | 4.09 | 4.09 | 5.58 | 200000 | 0 |
| Delete file | 31231.33 ops/s | 1.27 ms/op | 2.05 | 4.09 | 4.09 | 4.89 | 200000 | 0 |

#### FIO read/write baseline

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Sequential write 64KB | 1.71 | 28084.85 | 8.89 ms/op | 8.85 | 10.29 | 10.94 | 16.58 | 262144 | 0 |
| Sequential read 64KB | 2.28 | 37433.10 | 6.31 ms/op | 5.87 | 10.81 | 12.78 | 25.90 | 262144 | 0 |
| Random write 64KB | 1.77 | 29011.07 | 8.48 ms/op | 8.29 | 9.50 | 10.29 | 274.42 | 262144 | 0 |
| Random read 64KB | 1.12 | 18325.34 | 13.46 ms/op | 13.30 | 16.91 | 19.53 | 57.97 | 262144 | 0 |
| Sequential write 256KB | 2.73 | 11187.44 | 20.83 ms/op | 22.41 | 31.85 | 36.44 | 66.49 | 65536 | 0 |
| Sequential read 256KB | 3.11 | 12750.19 | 17.71 ms/op | 19.01 | 23.99 | 26.08 | 61.98 | 65536 | 0 |
| Random write 256KB | 2.51 | 10267.27 | 23.24 ms/op | 20.84 | 26.87 | 30.28 | 985.88 | 65536 | 0 |
| Random read 256KB | 2.37 | 9700.41 | 25.17 ms/op | 25.03 | 30.54 | 34.34 | 67.33 | 65536 | 0 |
| Sequential write 1MB | 3.45 | 3530.27 | 62.65 ms/op | 60.03 | 145.75 | 191.89 | 422.44 | 16384 | 0 |
| Sequential read 1MB | 2.72 | 2784.50 | 85.32 ms/op | 93.85 | 105.38 | 108.53 | 165.07 | 16384 | 0 |
| Random write 1MB | 3.09 | 3164.16 | 74.79 ms/op | 72.88 | 105.38 | 229.64 | 481.01 | 16384 | 0 |
| Random read 1MB | 2.15 | 2202.15 | 111.52 ms/op | 112.72 | 127.40 | 135.27 | 220.57 | 16384 | 0 |

## Failures and attribution

### Failure analysis

#### fuse

- Goal: FUSE mount, file I/O, and FIO regression
- Expected: Mount is readable/writable; I/O semantics are correct; no EIO
- Actual: exit code **40**; sustained or preallocated writes returned EIO or ENOSPC while capacity still showed free space
- Impact: Blocks the full-chain quality gate; do not claim this capability until attribution is done
- Class: **unknown_failure**
- Failure layer: **test**
- Root-cause confidence: low
- Cleanup: **passed**
- Next step: fuse-owner completes attribution; file an Issue after a confirmed product regression, then fix, review, and open a PR

### Failed case summary

Body shows 6/6 cases; full list is under All failed cases.

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-write-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-write-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-write-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-write-eio |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-write-eio |
| fuse | fuse / fuse | FAILED | status failed | g-fuse-write-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| fuse | 6 | 6 | +0 | Counts match |

### Common root-cause groups

Attribution coverage: **6/6 (100.0%)**. Do not pre-cluster without evidence.

#### P1 g-fuse-write-eio

- Profiles: fuse
- Hypothesis: FUSE or backend storage returned EIO or ENOSPC on sustained or preallocated writes; worker and master error logs have not yet pinpointed a subsystem; confidence is medium
- Recommendation: Align the first FIO EIO and fallocate ENOSPC timestamps, check worker and master ERROR logs, and trace the FUSE write path and block allocation
- Unique logical failures: 6
- Model class: **unknown_failure**; confidence: **medium**; Issue: **needs_human**
- Verification: After the fix, rerun the fuse profile; the cases below plus fallocate and large-file dd must show no EIO or ENOSPC
- FIO Sequential Write Test (256KB blocks) (fuse): FIO Sequential Write test failed
- FIO Sequential Read Test (256KB blocks) (fuse): FIO Sequential Read test failed
- FIO Random Write Test (256KB blocks) (fuse): FIO Random Write test failed
- FIO Random Read Test (256KB blocks) (fuse): FIO Random Read test failed
- FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) (fuse): FIO Mixed Random Read/Write test failed

### All failed cases

Untruncated.

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-write-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-write-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-write-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-write-eio |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-write-eio |
| fuse | fuse / fuse | FAILED | status failed | g-fuse-write-eio |

## Follow-up

### Defects and fixes

- GitHub Issue: **needs_human**
- GitHub PR: **pending_fix_review**

Close-out bar: the Issue includes repro, expected/actual, impact, and acceptance; a PR is opened only after fix, tests, and review, and it must link the Issue on CurvineIO/curvine.

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Unattributed failed profile: fuse. Causes in this report are unverified hypotheses.

### Next actions

| Priority | Role | Action | Done when |
| --- | --- | --- | --- |
| P0 | fuse-owner | Finish attribution, file an Issue, fix, and run targeted regression | fuse passes; Issue and PR complete |
| P0 | test-owner | Rerun the full chain and update the report | All required profiles pass |
