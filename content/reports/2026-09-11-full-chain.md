---
title: "Curvine full-chain daily test report - 2026-09-11"
linkTitle: "2026-09-11 full-chain"
date: 2026-09-11T00:00:00Z
weight: -20260911
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 3 passed, 3 failed.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 3/7 passed | FAIL |
| Failure attribution | Failures classified | 2 root-cause groups | PASS |
| Resource cleanup | All profile cleanups succeeded | 6/7 | FAIL |

### Conclusion

This full-chain run did not pass. Failed profiles require resolution before release.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 28s | passed | PASSED |
| integration | PASS | FAIL | 5m 07s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 14s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 41s | runner_infrastructure_failure | FAILED |
| ltp | PASS | PASS | 49m 54s | passed | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 7m 39s | failed | PASSED |

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
| Create file | 23049.70 ops/s | 1.73 ms/op | 2.05 | 4.09 | 4.09 | 6.50 | 200000 | 0 | 21668.74 ops/s | +6.4% | 4.09 | +0.1% | pass |
| Stat file | 68805.77 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 2.91 | 200000 | 0 | 63487.48 ops/s | +8.4% | 2.05 | -50.1% | pass |
| Open file | 67769.47 ops/s | 0.59 ms/op | 1.02 | 1.02 | 1.80 | 1.80 | 200000 | 0 | 63113.20 ops/s | +7.4% | 2.05 | -12.4% | pass |
| Rename file | 32382.44 ops/s | 1.22 ms/op | 2.05 | 4.09 | 4.09 | 4.67 | 200000 | 0 | 30314.48 ops/s | +6.8% | 4.09 | +0.1% | pass |
| Delete file | 32735.81 ops/s | 1.21 ms/op | 2.05 | 4.09 | 4.09 | 4.78 | 200000 | 0 | 31231.33 ops/s | +4.8% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.71 | 28069.81 | 8.89 ms/op | 8.85 | 10.29 | 11.08 | 18.98 | 262144 | 0 | 1.71 | +0.2% | 10.94 | +1.2% | pass |
| Sequential read 64KB | 2.19 | 35821.81 | 6.52 ms/op | 6.13 | 10.55 | 12.78 | 32.47 | 262144 | 0 | 2.28 | -4.1% | 12.78 | 0.0% | pass |
| Random write 64KB | 1.80 | 29487.51 | 8.42 ms/op | 8.22 | 9.50 | 10.29 | 272.99 | 262144 | 0 | 1.77 | +1.7% | 10.29 | 0.0% | pass |
| Random read 64KB | 1.05 | 17258.81 | 13.92 ms/op | 13.83 | 17.43 | 20.58 | 78.75 | 262144 | 0 | 1.12 | -5.9% | 19.53 | +5.4% | pass |
| Sequential write 256KB | 2.89 | 11831.74 | 20.26 ms/op | 22.15 | 31.06 | 35.91 | 43.88 | 65536 | 0 | 2.73 | +5.8% | 36.44 | -1.4% | pass |
| Sequential read 256KB | 2.42 | 9901.19 | 24.71 ms/op | 26.08 | 28.97 | 30.28 | 49.63 | 65536 | 0 | 3.11 | -22.3% | 26.08 | +16.1% | degraded |
| Random write 256KB | 2.59 | 10623.44 | 22.44 ms/op | 21.63 | 26.87 | 30.28 | 453.63 | 65536 | 0 | 2.51 | +3.3% | 30.28 | 0.0% | pass |
| Random read 256KB | 2.28 | 9323.66 | 26.10 ms/op | 26.08 | 31.59 | 34.34 | 56.06 | 65536 | 0 | 2.37 | -4.0% | 34.34 | 0.0% | pass |
| Sequential write 1MB | 3.47 | 3557.87 | 63.28 ms/op | 67.63 | 137.36 | 164.63 | 305.72 | 16384 | 0 | 3.45 | +0.7% | 191.89 | -14.2% | pass |
| Sequential read 1MB | 2.52 | 2580.16 | 91.84 ms/op | 99.09 | 113.77 | 121.11 | 175.18 | 16384 | 0 | 2.72 | -7.4% | 108.53 | +11.6% | pass |
| Random write 1MB | 3.00 | 3070.46 | 77.41 ms/op | 73.92 | 108.53 | 295.70 | 558.28 | 16384 | 0 | 3.09 | -3.0% | 229.64 | +28.8% | fail |
| Random read 1MB | 2.09 | 2136.11 | 114.39 ms/op | 115.87 | 128.45 | 135.27 | 178.41 | 16384 | 0 | 2.15 | -3.0% | 135.27 | 0.0% | pass |

## Failures and attribution

### Failure analysis

#### g-rustc-recursion-compile

- Class: **unknown_failure**
- Failure layer: **build**
- Root-cause confidence: **medium**
- Root cause: Rust compiler query recursion limit is exceeded while type-checking async test code in fallback_read_test and write_cache_test crates. Whether this is a new product regression from increased type complexity on a858336e or a toolchain/environment sensitivity is not yet proven; prior daily runs at earlier SHAs passed compilation.
- Recommendation: Bisect a858336e against the last passing daily SHA to identify commits that increased async type depth in curvine-tests. If confirmed product-side, add recursion_limit attributes or refactor async test helpers; if toolchain-specific, pin or adjust rustc settings in the build image.

#### g-fuse-buffered-io-eio-cleanup-blocked

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse buffered read/write on /curvine-fuse returns Input/output error during sustained or verified writes. This matches the pre-existing defect tracked in GitHub issue #1646. Cleanup failed after tests with 'could not remove owned worktree', blocking automated issue handoff for this run.
- Recommendation: Reuse existing repair track for GitHub issue #1646 (FuseConf mount CLI buffered I/O regression). No new issue from this run because cleanup did not succeed.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| integration profile | integration / integration | FAILED | profile failed | g-rustc-recursion-compile |
| daily profile | daily / daily | FAILED | profile failed | g-rustc-recursion-compile |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio-cleanup-blocked |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio-cleanup-blocked |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio-cleanup-blocked |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio-cleanup-blocked |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio-cleanup-blocked |
| fuse | fuse / fuse | FAILED | "status": "failed" | g-fuse-buffered-io-eio-cleanup-blocked |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |
| integration | 1 | 1 | 0 |
| daily | 1 | 0 | 1 |
| fuse | 6 | 6 | 0 |

### Common root-cause groups

#### g-rustc-recursion-compile

- Model class: **unknown_failure**; confidence: **medium**
- Recommendation: Bisect a858336e against the last passing daily SHA to identify commits that increased async type depth in curvine-tests. If confirmed product-side, add recursion_limit attributes or refactor async test helpers; if toolchain-specific, pin or adjust rustc settings in the build image.

#### g-fuse-buffered-io-eio-cleanup-blocked

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Reuse existing repair track for GitHub issue #1646 (FuseConf mount CLI buffered I/O regression). No new issue from this run because cleanup did not succeed.


## Follow-up

### Defects and fixes

- GitHub Issue: none

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Bisect a858336e against the last passing daily SHA to identify commits that increased async type depth in curvine-tests. If confirmed product-side, add recursion_limit attributes or refactor async test helpers; if toolchain-specific, pin or adjust rustc settings in the build image.
- Reuse existing repair track for GitHub issue #1646 (FuseConf mount CLI buffered I/O regression). No new issue from this run because cleanup did not succeed.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
