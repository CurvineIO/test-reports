---
title: "Curvine full-chain daily test report - 2026-09-06"
linkTitle: "2026-09-06 full-chain"
date: 2026-09-06T00:00:00Z
weight: -20260906
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 4 passed, 2 failed, 1 degraded.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 4/7 passed | FAIL |
| Failure attribution | Failures classified | 2 root-cause groups | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failed profiles require resolution before release.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 1m 52s | passed | PASSED |
| integration | PASS | PASS | 10m 58s | passed | PASSED |
| daily | PASS | FAIL | 16m 55s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 2m 38s | unknown_failure | PASSED |
| ltp | PASS | PASS | 48m 43s | passed | PASSED |
| csi | PASS | PASS | 0m 35s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | DEGRADED | 2m 07s | degraded | PASSED |

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

- Status: **degraded**
- Gate mode: **report_only**

#### Metadata performance (this run)

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Create file | 23097.31 ops/s | 1.73 ms/op | 2.05 | 4.09 | 4.09 | 163.60 | 200000 | 0 | pass |
| Stat file | 71578.65 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 1.19 | 200000 | 0 | pass |
| Open file | 69457.74 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 2.49 | 200000 | 0 | pass |
| Rename file | 32699.97 ops/s | 1.21 ms/op | 2.05 | 4.09 | 4.09 | 4.22 | 200000 | 0 | pass |
| Delete file | 32370.10 ops/s | 1.23 ms/op | 2.05 | 4.09 | 4.09 | 4.39 | 200000 | 0 | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.67 | 27349.40 | 9.12 ms/op | 9.11 | 10.55 | 11.47 | 17.34 | 262144 | 0 | pass |
| Sequential read 64KB | 2.28 | 37353.09 | 6.55 ms/op | 6.19 | 10.42 | 12.65 | 22.61 | 262144 | 0 | pass |
| Random write 64KB | 1.73 | 28413.61 | 8.72 ms/op | 8.59 | 9.76 | 10.68 | 326.94 | 262144 | 0 | pass |
| Random read 64KB | 1.03 | 16821.36 | 14.64 ms/op | 14.48 | 18.22 | 20.32 | 39.44 | 262144 | 0 | pass |
| Sequential write 256KB | 2.59 | 10604.53 | 22.51 ms/op | 24.25 | 32.64 | 37.49 | 53.60 | 65536 | 0 | pass |
| Sequential read 256KB | 2.53 | 10343.43 | 22.96 ms/op | 25.03 | 28.70 | 30.54 | 55.31 | 65536 | 0 | degraded |
| Random write 256KB | 2.47 | 10115.14 | 23.66 ms/op | 23.20 | 28.97 | 32.11 | 444.19 | 65536 | 0 | pass |
| Random read 256KB | 2.17 | 8899.51 | 27.44 ms/op | 27.39 | 33.16 | 36.44 | 56.87 | 65536 | 0 | pass |
| Sequential write 1MB | 3.03 | 3105.97 | 75.62 ms/op | 70.78 | 152.04 | 200.28 | 362.41 | 16384 | 0 | pass |
| Sequential read 1MB | 2.15 | 2197.42 | 115.08 ms/op | 115.87 | 122.16 | 127.40 | 212.11 | 16384 | 0 | degraded |
| Random write 1MB | 2.77 | 2839.02 | 83.35 ms/op | 82.31 | 116.92 | 261.10 | 512.36 | 16384 | 0 | pass |
| Random read 1MB | 2.13 | 2181.62 | 113.86 ms/op | 114.82 | 127.40 | 137.36 | 199.54 | 16384 | 0 | pass |

## Failures and attribution

### Failure analysis

#### g-daily-coverage-timeout

- Class: **flaky**
- Failure layer: **test**
- Root-cause confidence: **medium**
- Root cause: The daily profile passed all 1449 nextest unit tests, but the ut-coverage orchestration step timed out (exit 124) while cargo-llvm-cov re-ran tests for coverage. This points to intermittent resource or timing pressure during the coverage subprocess rather than a demonstrated stable product defect at ad604155.
- Recommendation: Increase coverage collection timeout or isolate llvm-cov rerun from runner load; retry coverage on transient timeout; investigate whether ordinary runner compile pressure during parallel crate builds causes coverage step to exceed its limit.

#### g-fuse-buffered-io-eio

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse mount option generation from FuseConf (introduced in e01cf918) appears to mis-apply or omit settings required for buffered read/write, causing user I/O on /curvine-fuse to fail with Input/output error. Mount and metadata operations succeed, but sustained or verified writes fail deterministically. This is a pre-existing product defect still open as GitHub issue #1646.
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| daily profile | daily / daily | FAILED | profile failed | g-daily-coverage-timeout |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio |
| fuse | fuse / fuse | FAILED | "status": "failed" | g-fuse-buffered-io-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |
| daily | 1 | 0 | 1 |
| fuse | 6 | 6 | 0 |

### Common root-cause groups

#### g-daily-coverage-timeout

- Model class: **flaky**; confidence: **medium**
- Recommendation: Increase coverage collection timeout or isolate llvm-cov rerun from runner load; retry coverage on transient timeout; investigate whether ordinary runner compile pressure during parallel crate builds causes coverage step to exceed its limit.

#### g-fuse-buffered-io-eio

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.


## Follow-up

### Defects and fixes

- GitHub Issue: [1646](https://github.com/CurvineIO/curvine/issues/1646) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Increase coverage collection timeout or isolate llvm-cov rerun from runner load; retry coverage on transient timeout; investigate whether ordinary runner compile pressure during parallel crate builds causes coverage step to exceed its limit.
- Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
