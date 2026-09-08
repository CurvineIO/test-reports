---
title: "Curvine full-chain daily test report - 2026-09-07"
linkTitle: "2026-09-07 full-chain"
date: 2026-09-07T00:00:00Z
weight: -20260907
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
| fast | PASS | PASS | 12m 15s | passed | PASSED |
| integration | PASS | FAIL | 12m 40s | unknown_failure | PASSED |
| daily | PASS | FAIL | 20m 35s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 07s | unknown_failure | PASSED |
| ltp | PASS | PASS | 49m 32s | passed | PASSED |
| csi | PASS | PASS | 0m 35s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 5m 45s | failed | PASSED |

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
| Create file | 23370.78 ops/s | 1.70 ms/op | 2.05 | 4.09 | 4.09 | 5.25 | 200000 | 0 | 21668.74 ops/s | +7.9% | 4.09 | +0.1% | pass |
| Stat file | 71017.91 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 3.18 | 200000 | 0 | 63487.48 ops/s | +11.9% | 2.05 | -50.1% | pass |
| Open file | 69220.37 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 1.93 | 200000 | 0 | 63113.20 ops/s | +9.7% | 2.05 | -50.1% | pass |
| Rename file | 32239.33 ops/s | 1.23 ms/op | 2.05 | 3.96 | 3.96 | 3.96 | 200000 | 0 | 30314.48 ops/s | +6.3% | 4.09 | -3.1% | pass |
| Delete file | 31892.21 ops/s | 1.24 ms/op | 2.05 | 4.09 | 4.09 | 4.30 | 200000 | 0 | 31231.33 ops/s | +2.1% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.67 | 27406.59 | 9.08 ms/op | 9.11 | 10.55 | 11.47 | 22.83 | 262144 | 0 | 1.71 | -2.2% | 10.94 | +4.8% | pass |
| Sequential read 64KB | 2.56 | 41896.12 | 5.83 ms/op | 5.54 | 9.63 | 11.73 | 23.26 | 262144 | 0 | 2.28 | +12.2% | 12.78 | -8.2% | pass |
| Random write 64KB | 1.72 | 28233.06 | 8.73 ms/op | 8.59 | 9.90 | 11.08 | 294.43 | 262144 | 0 | 1.77 | -2.6% | 10.29 | +7.6% | pass |
| Random read 64KB | 1.17 | 19185.01 | 12.90 ms/op | 12.78 | 16.06 | 18.74 | 42.47 | 262144 | 0 | 1.12 | +4.6% | 19.53 | -4.0% | pass |
| Sequential write 256KB | 2.47 | 10113.58 | 23.34 ms/op | 24.25 | 33.82 | 38.01 | 53.76 | 65536 | 0 | 2.73 | -9.6% | 36.44 | +4.3% | pass |
| Sequential read 256KB | 3.10 | 12681.11 | 17.94 ms/op | 19.53 | 23.99 | 25.82 | 38.95 | 65536 | 0 | 3.11 | -0.5% | 26.08 | -1.0% | pass |
| Random write 256KB | 2.32 | 9500.72 | 25.39 ms/op | 23.20 | 29.49 | 32.64 | 862.72 | 65536 | 0 | 2.51 | -7.6% | 30.28 | +7.8% | pass |
| Random read 256KB | 2.55 | 10443.98 | 23.84 ms/op | 23.72 | 28.97 | 33.16 | 53.08 | 65536 | 0 | 2.37 | +7.6% | 34.34 | -3.4% | pass |
| Sequential write 1MB | 3.12 | 3193.76 | 73.65 ms/op | 64.75 | 156.24 | 238.03 | 339.16 | 16384 | 0 | 3.45 | -9.6% | 191.89 | +24.0% | degraded |
| Sequential read 1MB | 3.74 | 3834.31 | 59.35 ms/op | 54.79 | 76.02 | 84.41 | 116.92 | 16384 | 0 | 2.72 | +37.7% | 108.53 | -22.2% | pass |
| Random write 1MB | 2.40 | 2456.74 | 95.47 ms/op | 78.12 | 119.01 | 977.27 | 1589.17 | 16384 | 0 | 3.09 | -22.4% | 229.64 | +325.6% | fail |
| Random read 1MB | 2.27 | 2323.64 | 105.57 ms/op | 106.43 | 119.01 | 126.35 | 182.86 | 16384 | 0 | 2.15 | +5.5% | 135.27 | -6.6% | pass |

## Failures and attribution

### Failure analysis

#### g-fuse-buffered-io-eio

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse mount option generation from FuseConf (introduced in e01cf918) appears to mis-apply or omit settings required for buffered read/write, causing user I/O on /curvine-fuse to fail with Input/output error. Mount and metadata operations succeed, but sustained or verified writes fail deterministically. This is a pre-existing product defect still open as GitHub issue #1646.
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.

#### g-resize-fs-dir-lock-regression

- Class: **product_regression**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: Commit dc637c67 (PR #1663, feat(master): add inode id to resize and assign worker RPCs) refactored MasterFilesystem::resize to acquire fs_dir.write() at function entry and retain it while calling worker_manager.write().remove_blocks() and building the FileBlocks response. This violates the lock-scope contract established by PR #670 and tested by resize_lock_scope_test.rs, which requires resize to release fs_dir before blocking on worker_manager.
- Recommendation: Restore the narrow lock scope in MasterFilesystem::resize: release fs_dir before acquiring worker_manager for remove_blocks, then re-acquire only as needed to build the response (or build the response before releasing fs_dir but after remove_blocks completes without holding fs_dir during worker_manager acquisition). Ensure resize_lock_scope_test passes.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| resize_does_not_hold_fs_lock_while_waiting_worker_manager | resize_lock_scope_test / curvine-server | FAILED | called `Result::unwrap()` on an `Err` value: PoisonError { .. } | g-resize-fs-dir-lock-regression |
| resize_does_not_hold_fs_lock_while_waiting_worker_manager | resize_lock_scope_test / curvine-server | FAILED | called `Result::unwrap()` on an `Err` value: PoisonError { .. } | g-resize-fs-dir-lock-regression |
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
| daily | 1 | 1 | 0 |
| fuse | 6 | 6 | 0 |

### Common root-cause groups

#### g-fuse-buffered-io-eio

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.

#### g-resize-fs-dir-lock-regression

- Model class: **product_regression**; confidence: **high**
- Recommendation: Restore the narrow lock scope in MasterFilesystem::resize: release fs_dir before acquiring worker_manager for remove_blocks, then re-acquire only as needed to build the response (or build the response before releasing fs_dir but after remove_blocks completes without holding fs_dir during worker_manager acquisition). Ensure resize_lock_scope_test passes.


## Follow-up

### Defects and fixes

- GitHub Issue: [1671](https://github.com/CurvineIO/curvine/issues/1671) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.
- Restore the narrow lock scope in MasterFilesystem::resize: release fs_dir before acquiring worker_manager for remove_blocks, then re-acquire only as needed to build the response (or build the response before releasing fs_dir but after remove_blocks completes without holding fs_dir during worker_manager acquisition). Ensure resize_lock_scope_test passes.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
