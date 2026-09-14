---
title: "Curvine full-chain daily test report - 2026-09-12"
linkTitle: "2026-09-12 full-chain"
date: 2026-09-12T00:00:00Z
weight: -20260912
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
| fast | PASS | PASS | 12m 31s | passed | PASSED |
| integration | PASS | FAIL | 5m 07s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 07s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 12s | unknown_failure | PASSED |
| ltp | PASS | PASS | 49m 42s | passed | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | PASSED | 5m 29s | passed | PASSED |

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

- Status: **passed**
- Gate mode: **report_only**

#### Metadata performance (this run)

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline VALUE | VALUE delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Create file | 23112.09 ops/s | 1.72 ms/op | 2.05 | 4.09 | 4.09 | 4.60 | 200000 | 0 | 21668.74 ops/s | +6.7% | 4.09 | +0.1% | pass |
| Stat file | 71711.99 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 2.63 | 200000 | 0 | 63487.48 ops/s | +13.0% | 2.05 | -50.1% | pass |
| Open file | 68931.50 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 3.42 | 200000 | 0 | 63113.20 ops/s | +9.2% | 2.05 | -50.1% | pass |
| Rename file | 32706.40 ops/s | 1.22 ms/op | 2.05 | 4.01 | 4.01 | 4.01 | 200000 | 0 | 30314.48 ops/s | +7.9% | 4.09 | -2.0% | pass |
| Delete file | 32228.14 ops/s | 1.23 ms/op | 2.05 | 4.09 | 4.09 | 4.59 | 200000 | 0 | 31231.33 ops/s | +3.2% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.74 | 28459.88 | 8.81 ms/op | 8.85 | 10.16 | 10.94 | 17.23 | 262144 | 0 | 1.71 | +1.6% | 10.94 | 0.0% | pass |
| Sequential read 64KB | 2.30 | 37740.28 | 6.34 ms/op | 6.13 | 10.29 | 12.39 | 22.45 | 262144 | 0 | 2.28 | +1.0% | 12.78 | -3.1% | pass |
| Random write 64KB | 1.81 | 29735.03 | 8.40 ms/op | 8.22 | 9.37 | 10.16 | 290.43 | 262144 | 0 | 1.77 | +2.5% | 10.29 | -1.3% | pass |
| Random read 64KB | 1.09 | 17910.90 | 13.16 ms/op | 13.04 | 16.58 | 19.27 | 50.36 | 262144 | 0 | 1.12 | -2.4% | 19.53 | -1.3% | pass |
| Sequential write 256KB | 2.82 | 11566.54 | 20.49 ms/op | 21.63 | 31.85 | 37.49 | 45.55 | 65536 | 0 | 2.73 | +3.4% | 36.44 | +2.9% | pass |
| Sequential read 256KB | 2.77 | 11328.61 | 20.88 ms/op | 22.94 | 26.35 | 27.92 | 45.38 | 65536 | 0 | 3.11 | -11.1% | 26.08 | +7.0% | pass |
| Random write 256KB | 2.71 | 11102.15 | 21.74 ms/op | 21.10 | 26.87 | 30.02 | 453.64 | 65536 | 0 | 2.51 | +8.0% | 30.28 | -0.9% | pass |
| Random read 256KB | 2.46 | 10068.52 | 24.52 ms/op | 24.51 | 29.75 | 33.16 | 49.61 | 65536 | 0 | 2.37 | +3.7% | 34.34 | -3.4% | pass |
| Sequential write 1MB | 3.36 | 3443.46 | 66.61 ms/op | 58.98 | 145.75 | 204.47 | 327.90 | 16384 | 0 | 3.45 | -2.5% | 191.89 | +6.6% | pass |
| Sequential read 1MB | 2.53 | 2590.77 | 92.24 ms/op | 101.19 | 113.77 | 117.96 | 198.49 | 16384 | 0 | 2.72 | -7.0% | 108.53 | +8.7% | pass |
| Random write 1MB | 3.13 | 3208.77 | 72.60 ms/op | 69.73 | 110.62 | 242.22 | 559.23 | 16384 | 0 | 3.09 | +1.4% | 229.64 | +5.5% | pass |
| Random read 1MB | 2.34 | 2399.88 | 102.10 ms/op | 103.28 | 114.82 | 125.30 | 180.77 | 16384 | 0 | 2.15 | +9.0% | 135.27 | -7.4% | pass |

## Failures and attribution

### Failure analysis

#### g-rustc-recursion-compile

- Class: **unknown_failure**
- Failure layer: **build**
- Root-cause confidence: **medium**
- Root cause: Rust compiler query recursion limit is exceeded while type-checking async test code in fallback_read_test and write_cache_test crates. Whether increased type complexity in curvine-tests or rustc 1.98 toolchain limits is the primary cause remains unproven.
- Recommendation: Bisect commits between last passing daily SHA and ae330604 to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.

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
- Recommendation: Bisect commits between last passing daily SHA and ae330604 to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.

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

- Bisect commits between last passing daily SHA and ae330604 to identify async test changes that increased type depth. If product-side, add recursion_limit attributes or refactor test helpers; if toolchain-specific, adjust rustc settings in the build environment.
- Review FuseConf-to-mount flag mapping in curvine-fuse mount CLI code introduced around e01cf918; restore correct buffered I/O behavior per open issue #1646 repair plan.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
