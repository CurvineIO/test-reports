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
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 4 passed, 3 failed.

Blocking failures were found in integration, daily, and fuse. This revision is not releasable until the attributed product defects are fixed and targeted regression completes.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 4/7 passed | FAIL |
| Failure attribution | Failures classified | 3 failed profiles | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Two root-cause groups were identified: a new master resize lock-scope regression and a pre-existing curvine-fuse buffered I/O EIO defect.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 15s | passed | passed |
| integration | PASS | FAIL | 12m 40s | unknown_failure | passed |
| daily | PASS | FAIL | 20m 35s | unknown_failure | passed |
| fuse | PASS | FAIL | 3m 07s | unknown_failure | passed |
| ltp | PASS | PASS | 49m 32s | passed | passed |
| csi | PASS | PASS | 0m 35s | passed | passed |
| perf-benchmark | NOT_RECORDED | PASS | 5m 45s | failed | passed |

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
| Create file | 23370.78 ops/s | 1.70 ms/op | 2.05 | 4.09 | 4.09 | 5.25 | 200000 | 0 | pass |
| Stat file | 71017.91 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 3.18 | 200000 | 0 | pass |
| Open file | 69220.37 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 1.93 | 200000 | 0 | pass |
| Rename file | 32239.33 ops/s | 1.23 ms/op | 2.05 | 3.96 | 3.96 | 3.96 | 200000 | 0 | pass |
| Delete file | 31892.21 ops/s | 1.24 ms/op | 2.05 | 4.09 | 4.09 | 4.30 | 200000 | 0 | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.67 | 27406.59 | 9.08 ms/op | 9.11 | 10.55 | 11.47 | 22.83 | 262144 | 0 | pass |
| Sequential read 64KB | 2.56 | 41896.12 | 5.83 ms/op | 5.54 | 9.63 | 11.73 | 23.26 | 262144 | 0 | pass |
| Random write 64KB | 1.72 | 28233.06 | 8.73 ms/op | 8.59 | 9.90 | 11.08 | 294.43 | 262144 | 0 | pass |
| Random read 64KB | 1.17 | 19185.01 | 12.90 ms/op | 12.78 | 16.06 | 18.74 | 42.47 | 262144 | 0 | pass |
| Sequential write 256KB | 2.47 | 10113.58 | 23.34 ms/op | 24.25 | 33.82 | 38.01 | 53.76 | 65536 | 0 | pass |
| Sequential read 256KB | 3.10 | 12681.11 | 17.94 ms/op | 19.53 | 23.99 | 25.82 | 38.95 | 65536 | 0 | pass |
| Random write 256KB | 2.32 | 9500.72 | 25.39 ms/op | 23.20 | 29.49 | 32.64 | 862.72 | 65536 | 0 | pass |
| Random read 256KB | 2.55 | 10443.98 | 23.84 ms/op | 23.72 | 28.97 | 33.16 | 53.08 | 65536 | 0 | pass |
| Sequential write 1MB | 3.12 | 3193.76 | 73.65 ms/op | 64.75 | 156.24 | 238.03 | 339.16 | 16384 | 0 | degraded |
| Sequential read 1MB | 3.74 | 3834.31 | 59.35 ms/op | 54.79 | 76.02 | 84.41 | 116.92 | 16384 | 0 | pass |
| Random write 1MB | 2.40 | 2456.74 | 95.47 ms/op | 78.12 | 119.01 | 977.27 | 1589.17 | 16384 | 0 | fail |
| Random read 1MB | 2.27 | 2323.64 | 105.57 ms/op | 106.43 | 119.01 | 126.35 | 182.86 | 16384 | 0 | pass |

## Failures and attribution

### Failure analysis

#### integration and daily

- Goal: server integration and daily unit-test regression
- Expected: all nextest cases pass
- Actual: resize_does_not_hold_fs_lock_while_waiting_worker_manager failed because MasterFilesystem resize keeps the fs_dir write lock while waiting on worker_manager
- Impact: blocks integration and daily quality gates
- Class: **product_regression**
- Failure layer: **product**
- Root-cause confidence: high
- Cleanup: **passed**
- GitHub Issue: **1671**

#### fuse

- Goal: FUSE mount, file I/O, and FIO regression
- Expected: mount is readable and writable without EIO
- Actual: all five FIO sub-tests failed with Input/output error on buffered writes
- Impact: blocks FUSE validation
- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: high
- Cleanup: **passed**
- GitHub Issue: **1646**

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| resize_does_not_hold_fs_lock_while_waiting_worker_manager | resize_lock_scope_test / curvine-server | FAILED | resize must not keep fs_dir locked while waiting on worker_manager | g-resize-fs-dir-lock-regression |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio |
| FIO Mixed Random Read/Write Test (256KB blocks) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio |
| fuse | fuse / fuse | FAILED | fio and fuse sub-tests failed | g-fuse-buffered-io-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| integration | 1 | 1 | +0 | Counts match |
| daily | 1 | 1 | +0 | Counts match |
| fuse | 6 | 6 | +0 | Counts match |

### Common root-cause groups

Attribution coverage: **8/8 (100.0%)**.

#### P0 g-resize-fs-dir-lock-regression

- Profiles: integration, daily
- Hypothesis: MasterFilesystem resize holds fs_dir write lock while blocking on worker_manager after the inode-id resize refactor
- Recommendation: release fs_dir before worker_manager.remove_blocks while preserving inode-id validation
- Unique logical failures: 1
- Model class: **product_regression**; confidence: **high**; Issue: **create_or_reuse** (GitHub **1671**)
- Verification: resize_lock_scope_test passes; integration and daily profiles pass

#### P1 g-fuse-buffered-io-eio

- Profiles: fuse
- Hypothesis: curvine-fuse buffered writes return Input/output error after FuseConf mount CLI refactor
- Recommendation: restore correct buffered I/O mount options
- Unique logical failures: 6
- Model class: **pre_existing_failure**; confidence: **high**; Issue: **create_or_reuse** (GitHub **1646**)
- Verification: FIO and FUSE regression suites pass without EIO

## Follow-up

### Defects and fixes

- GitHub Issue **1671**: new product regression for resize lock scope
- GitHub Issue **1646**: reused open pre-existing FUSE EIO defect
- Multica fix task **CUR-344**: assigned for issue **1671**, promoted to todo
- GitHub PR: **pending_fix_review**

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- The FUSE EIO defect remains open and blocks fuse profile until fixed.

### Next actions

| Priority | Role | Action | Done when |
| --- | --- | --- | --- |
| P0 | master-owner | Fix resize lock scope regression | integration and daily pass; PR for issue 1671 |
| P1 | fuse-owner | Fix buffered FUSE EIO defect | fuse profile passes; PR for issue 1646 |
| P0 | test-owner | Rerun the full chain after fixes | All required profiles pass |
