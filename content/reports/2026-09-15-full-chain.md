---
title: "Curvine full-chain daily test report - 2026-09-15"
linkTitle: "2026-09-15 full-chain"
date: 2026-09-15T00:00:00Z
weight: -20260915
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
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failed profiles require resolution before release.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 37s | passed | PASSED |
| integration | PASS | FAIL | 5m 08s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 14s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 44s | unknown_failure | PASSED |
| ltp | PASS | PASS | 50m 42s | passed | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 5m 30s | failed | PASSED |

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
| Create file | 23483.41 ops/s | 1.69 ms/op | 2.05 | 4.09 | 4.09 | 5.34 | 200000 | 0 | 21668.74 ops/s | +8.4% | 4.09 | +0.1% | pass |
| Stat file | 69346.69 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 2.69 | 200000 | 0 | 63487.48 ops/s | +9.2% | 2.05 | -50.1% | pass |
| Open file | 68221.21 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 3.01 | 200000 | 0 | 63113.20 ops/s | +8.1% | 2.05 | -50.1% | pass |
| Rename file | 32209.79 ops/s | 1.23 ms/op | 2.05 | 4.09 | 4.09 | 5.03 | 200000 | 0 | 30314.48 ops/s | +6.3% | 4.09 | +0.1% | pass |
| Delete file | 31833.34 ops/s | 1.24 ms/op | 2.05 | 4.09 | 4.09 | 4.37 | 200000 | 0 | 31231.33 ops/s | +1.9% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.74 | 28503.21 | 8.75 ms/op | 8.72 | 10.03 | 10.81 | 16.57 | 262144 | 0 | 1.71 | +1.7% | 10.94 | -1.2% | pass |
| Sequential read 64KB | 2.47 | 40435.60 | 6.03 ms/op | 5.73 | 10.03 | 12.39 | 47.17 | 262144 | 0 | 2.28 | +8.2% | 12.78 | -3.1% | pass |
| Random write 64KB | 1.74 | 28574.67 | 8.68 ms/op | 8.22 | 10.29 | 15.27 | 322.36 | 262144 | 0 | 1.77 | -1.5% | 10.29 | +48.4% | fail |
| Random read 64KB | 1.12 | 18316.38 | 13.23 ms/op | 13.04 | 16.45 | 19.01 | 42.08 | 262144 | 0 | 1.12 | -0.2% | 19.53 | -2.7% | pass |
| Sequential write 256KB | 3.00 | 12268.06 | 19.03 ms/op | 20.05 | 31.06 | 36.44 | 63.15 | 65536 | 0 | 2.73 | +9.7% | 36.44 | 0.0% | pass |
| Sequential read 256KB | 2.77 | 11358.06 | 20.77 ms/op | 22.94 | 27.39 | 29.23 | 44.78 | 65536 | 0 | 3.11 | -10.8% | 26.08 | +12.1% | pass |
| Random write 256KB | 2.80 | 11485.45 | 20.82 ms/op | 20.05 | 25.82 | 28.97 | 473.82 | 65536 | 0 | 2.51 | +11.7% | 30.28 | -4.3% | pass |
| Random read 256KB | 2.45 | 10036.14 | 24.36 ms/op | 24.25 | 29.75 | 33.16 | 49.99 | 65536 | 0 | 2.37 | +3.4% | 34.34 | -3.4% | pass |
| Sequential write 1MB | 3.45 | 3532.56 | 65.76 ms/op | 60.03 | 149.95 | 210.76 | 301.90 | 16384 | 0 | 3.45 | 0.0% | 191.89 | +9.8% | pass |
| Sequential read 1MB | 2.85 | 2919.98 | 79.09 ms/op | 87.56 | 102.24 | 108.53 | 170.48 | 16384 | 0 | 2.72 | +4.8% | 108.53 | 0.0% | pass |
| Random write 1MB | 3.16 | 3234.75 | 70.78 ms/op | 65.27 | 105.38 | 291.50 | 607.09 | 16384 | 0 | 3.09 | +2.2% | 229.64 | +26.9% | fail |
| Random read 1MB | 2.26 | 2318.05 | 104.67 ms/op | 105.38 | 117.96 | 125.30 | 172.69 | 16384 | 0 | 2.15 | +5.3% | 135.27 | -7.4% | pass |

## Failures and attribution

### Failure analysis

#### g-rustc-recursion-compile

- Class: **unknown_failure**
- Failure layer: **build**
- Root-cause confidence: **medium**
- Root cause: Rust compiler query recursion limit is exceeded while type-checking async test code in fallback_read_test and write_cache_test crates. Whether increased type complexity in curvine-tests or rustc 1.98 toolchain limits is the primary cause remains unproven.
- Recommendation: Bisect commits between last passing daily SHA and current main to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.

#### g-fuse-buffered-io-eio

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse buffered read/write on /curvine-fuse returns Input/output error during sustained or verified writes. This matches the pre-existing defect tracked in GitHub issue #1646 related to FuseConf mount CLI override generation.
- Recommendation: Review FuseConf-to-mount flag mapping in curvine-fuse mount CLI code introduced around e01cf918; restore correct buffered I/O behavior per open issue #1646 repair plan.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| integration profile | integration / integration | FAILED | profile failed | g-rustc-recursion-compile |
| daily profile | daily / daily | FAILED | profile failed | g-rustc-recursion-compile |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio |
| fuse | fuse / fuse | FAILED | "status": "failed" | g-fuse-buffered-io-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |
| integration | 1 | 1 | 0 |
| daily | 1 | 0 | 1 |
| fuse | 6 | 6 | 0 |

### Common root-cause groups

#### g-rustc-recursion-compile

- Model class: **unknown_failure**; confidence: **medium**
- Recommendation: Bisect commits between last passing daily SHA and current main to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.

#### g-fuse-buffered-io-eio

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Review FuseConf-to-mount flag mapping in curvine-fuse mount CLI code introduced around e01cf918; restore correct buffered I/O behavior per open issue #1646 repair plan.


## Follow-up

### Defects and fixes

- GitHub Issue: [1646](https://github.com/CurvineIO/curvine/issues/1646) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Bisect commits between last passing daily SHA and current main to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.
- Review FuseConf-to-mount flag mapping in curvine-fuse mount CLI code introduced around e01cf918; restore correct buffered I/O behavior per open issue #1646 repair plan.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
