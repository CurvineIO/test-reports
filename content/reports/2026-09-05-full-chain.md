---
title: "Curvine full-chain daily test report - 2026-09-05"
linkTitle: "2026-09-05 full-chain"
date: 2026-09-05T00:00:00Z
weight: -20260905
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 5 passed, 2 failed.

Blocking failures exist on the daily and fuse profiles. This revision is not releasable until the fuse product defect is fixed and the daily coverage gate is stabilized.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 5/7 passed | FAIL |
| Failure attribution | Failures classified | 2 failures | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. The fuse profile shows a pre-existing buffered I/O defect tracked in GitHub issue **1646**. The daily profile failed on a flaky coverage orchestration timeout after all unit tests passed.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 13s | passed | passed |
| integration | PASS | PASS | 10m 54s | passed | passed |
| daily | PASS | FAIL | 17m 03s | flaky | passed |
| fuse | PASS | FAIL | 3m 01s | pre_existing_failure | passed |
| ltp | PASS | PASS | 50m 02s | passed | passed |
| csi | PASS | PASS | 0m 35s | passed | passed |
| perf-benchmark | NOT_RECORDED | FAIL | 5m 30s | failed | passed |

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
| Create file | 23051.80 ops/s | 1.73 ms/op | 2.05 | 4.09 | 4.09 | 5.39 | 200000 | 0 | pass |
| Stat file | 69386.91 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 2.57 | 200000 | 0 | pass |
| Open file | 69147.83 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 1.55 | 200000 | 0 | pass |
| Rename file | 33343.98 ops/s | 1.19 ms/op | 2.05 | 3.50 | 3.50 | 3.50 | 200000 | 0 | pass |
| Delete file | 32418.22 ops/s | 1.22 ms/op | 2.05 | 4.09 | 4.09 | 4.30 | 200000 | 0 | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.71 | 27962.03 | 8.88 ms/op | 8.85 | 10.29 | 11.08 | 21.65 | 262144 | 0 | pass |
| Sequential read 64KB | 2.34 | 38375.64 | 6.28 ms/op | 6.00 | 10.16 | 12.39 | 19.99 | 262144 | 0 | pass |
| Random write 64KB | 1.80 | 29550.67 | 8.24 ms/op | 8.03 | 9.24 | 10.16 | 314.04 | 262144 | 0 | pass |
| Random read 64KB | 1.09 | 17882.80 | 13.83 ms/op | 13.70 | 17.17 | 19.53 | 63.31 | 262144 | 0 | pass |
| Sequential write 256KB | 2.81 | 11527.88 | 20.76 ms/op | 22.41 | 31.59 | 35.91 | 47.36 | 65536 | 0 | pass |
| Sequential read 256KB | 3.34 | 13699.00 | 16.71 ms/op | 16.71 | 23.46 | 25.30 | 45.21 | 65536 | 0 | pass |
| Random write 256KB | 2.51 | 10260.84 | 23.27 ms/op | 20.05 | 26.35 | 30.28 | 1182.31 | 65536 | 0 | pass |
| Random read 256KB | 2.36 | 9647.58 | 25.53 ms/op | 25.56 | 31.06 | 34.34 | 51.88 | 65536 | 0 | pass |
| Sequential write 1MB | 3.45 | 3537.90 | 63.61 ms/op | 55.84 | 158.33 | 278.92 | 559.43 | 16384 | 0 | fail |
| Sequential read 1MB | 2.69 | 2758.71 | 85.42 ms/op | 96.99 | 109.58 | 114.82 | 185.89 | 16384 | 0 | pass |
| Random write 1MB | 3.10 | 3171.51 | 72.07 ms/op | 68.68 | 112.72 | 283.12 | 461.26 | 16384 | 0 | degraded |
| Random read 1MB | 2.20 | 2253.96 | 108.71 ms/op | 109.58 | 124.26 | 129.50 | 205.44 | 16384 | 0 | pass |

## Failures and attribution

### Failure analysis

#### daily

- Goal: Full daily unit and coverage regression
- Expected: All unit tests pass and coverage collection completes
- Actual: All 1449 nextest tests passed; coverage step timed out with exit **124** during llvm-cov rerun
- Impact: Blocks the daily profile quality gate despite clean unit tests
- Class: **flaky**
- Failure layer: **test**
- Root-cause confidence: medium
- Cleanup: **passed**
- Next step: Increase coverage timeout or isolate MiniCluster startup from llvm-cov contention

#### fuse

- Goal: FUSE mount, file I/O, and FIO regression
- Expected: Mount is readable and writable; verified I/O completes without EIO
- Actual: Buffered writes return Input/output error after the first 256KB block; all five FIO sub-tests failed
- Impact: Blocks FUSE performance and durability validation
- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: high
- Cleanup: **passed**
- Next step: Fix tracked in GitHub issue **1646**

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| daily profile | daily / daily | FAILED | profile failed | g-daily-coverage-timeout |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio |
| FIO Mixed Random Read/Write Test | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio |
| fuse | fuse / fuse | FAILED | status failed | g-fuse-buffered-io-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| daily | 1 | 0 | +1 | Coverage orchestration failure not counted as named test case |
| fuse | 6 | 6 | +0 | Counts match |

### Common root-cause groups

Attribution coverage: **7/7 (100.0%)**.

#### P1 g-daily-coverage-timeout

- Profiles: daily
- Hypothesis: Coverage collection timed out during llvm-cov rerun; MiniCluster readiness failure in subprocess
- Recommendation: Increase coverage timeout or retry on transient cluster-readiness failures
- Unique logical failures: 1
- Model class: **flaky**; confidence: **medium**; Issue: **none**

#### P1 g-fuse-buffered-io-eio

- Profiles: fuse
- Hypothesis: curvine-fuse buffered writes return EIO after FuseConf mount CLI refactor
- Recommendation: Review mount option generation in curvine-fuse and curvine-config
- Unique logical failures: 6
- Model class: **pre_existing_failure**; confidence: **high**; Issue: **create_or_reuse** (GitHub **1646**)

## Follow-up

### Defects and fixes

- GitHub Issue: **1646** (open, reused)
- GitHub PR: **pending_fix_review**
- Multica repair task: **CUR-324** (blocked)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- The fuse EIO defect persists across multiple upstream commits.

### Next actions

| Priority | Role | Action | Done when |
| --- | --- | --- | --- |
| P0 | fuse-owner | Fix buffered I/O EIO per issue 1646 | fuse profile passes |
| P1 | test-owner | Stabilize daily coverage orchestration | daily profile passes with coverage.json |
| P0 | test-owner | Rerun the full chain after fixes | All required profiles pass |
