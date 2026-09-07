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

- Status: **DEGRADED**
- Gate mode: **REPORT_ONLY**

The performance gate is report-only. Higher throughput is better; lower P99 latency is better.

| Benchmark | Current | Baseline | Difference | Current P99 | Baseline P99 | P99 difference | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Create file | 23097.31 ops/s | 21668.74 ops/s | +6.6% better | 4.09 ms | 4.09 ms | +0.1% worse | PASS |
| Stat file | 71578.65 ops/s | 63487.48 ops/s | +12.7% better | 1.02 ms | 2.05 ms | -50.1% better | PASS |
| Open file | 69457.74 ops/s | 63113.20 ops/s | +10.1% better | 1.02 ms | 2.05 ms | -50.1% better | PASS |
| Rename file | 32699.97 ops/s | 30314.48 ops/s | +7.9% better | 4.09 ms | 4.09 ms | +0.1% worse | PASS |
| Delete file | 32370.10 ops/s | 31231.33 ops/s | +3.6% better | 4.09 ms | 4.09 ms | +0.1% worse | PASS |
| Sequential write|65536 | 1.67 GiB/s | 1.71 GiB/s | -2.4% worse | 11.47 ms | 10.94 ms | +4.8% worse | PASS |
| Sequential read|65536 | 2.28 GiB/s | 2.28 GiB/s | 0.0% | 12.65 ms | 12.78 ms | -1.0% better | PASS |
| Random write|65536 | 1.73 GiB/s | 1.77 GiB/s | -2.0% worse | 10.68 ms | 10.29 ms | +3.8% worse | PASS |
| Random read|65536 | 1.03 GiB/s | 1.12 GiB/s | -8.3% worse | 20.32 ms | 19.53 ms | +4.0% worse | PASS |
| Sequential write|262144 | 2.59 GiB/s | 2.73 GiB/s | -5.2% worse | 37.49 ms | 36.44 ms | +2.9% worse | PASS |
| Sequential read|262144 | 2.53 GiB/s | 3.11 GiB/s | -18.8% worse | 30.54 ms | 26.08 ms | +17.1% worse | DEGRADED |
| Random write|262144 | 2.47 GiB/s | 2.51 GiB/s | -1.6% worse | 32.11 ms | 30.28 ms | +6.1% worse | PASS |
| Random read|262144 | 2.17 GiB/s | 2.37 GiB/s | -8.3% worse | 36.44 ms | 34.34 ms | +6.1% worse | PASS |
| Sequential write|1048576 | 3.03 GiB/s | 3.45 GiB/s | -12.1% worse | 200.28 ms | 191.89 ms | +4.4% worse | PASS |
| Sequential read|1048576 | 2.15 GiB/s | 2.72 GiB/s | -21.1% worse | 127.40 ms | 108.53 ms | +17.4% worse | DEGRADED |
| Random write|1048576 | 2.77 GiB/s | 3.09 GiB/s | -10.3% worse | 261.10 ms | 229.64 ms | +13.7% worse | PASS |
| Random read|1048576 | 2.13 GiB/s | 2.15 GiB/s | -0.9% worse | 137.36 ms | 135.27 ms | +1.5% worse | PASS |

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
