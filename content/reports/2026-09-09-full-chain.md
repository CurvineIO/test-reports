---
title: "Curvine full-chain daily test report - 2026-09-09"
linkTitle: "2026-09-09 full-chain"
date: 2026-09-09T00:00:00Z
weight: -20260909
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 4 passed, 2 failed.

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
| fast | PASS | PASS | 12m 07s | passed | PASSED |
| integration | PASS | PASS | 12m 06s | passed | PASSED |
| daily | PASS | FAIL | 20m 12s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 02s | unknown_failure | PASSED |
| ltp | PASS | PASS | 49m 15s | passed | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 5m 41s | failed | PASSED |

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
| Create file | 23168.30 ops/s | 1.72 ms/op | 2.05 | 4.09 | 4.09 | 4.57 | 200000 | 0 | 21668.74 ops/s | +6.9% | 4.09 | +0.1% | pass |
| Stat file | 69786.89 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 2.93 | 200000 | 0 | 63487.48 ops/s | +9.9% | 2.05 | -50.1% | pass |
| Open file | 69180.89 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 1.25 | 200000 | 0 | 63113.20 ops/s | +9.6% | 2.05 | -50.1% | pass |
| Rename file | 33539.96 ops/s | 1.19 ms/op | 2.05 | 3.61 | 3.61 | 3.61 | 200000 | 0 | 30314.48 ops/s | +10.6% | 4.09 | -11.6% | pass |
| Delete file | 32920.34 ops/s | 1.21 ms/op | 2.05 | 4.09 | 4.09 | 4.68 | 200000 | 0 | 31231.33 ops/s | +5.4% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.67 | 27320.90 | 9.15 ms/op | 9.11 | 10.55 | 11.47 | 24.58 | 262144 | 0 | 1.71 | -2.5% | 10.94 | +4.8% | pass |
| Sequential read 64KB | 2.32 | 37958.88 | 6.39 ms/op | 5.93 | 11.21 | 13.17 | 28.65 | 262144 | 0 | 2.28 | +1.6% | 12.78 | +3.1% | pass |
| Random write 64KB | 1.73 | 28389.00 | 8.72 ms/op | 8.59 | 9.76 | 10.68 | 292.65 | 262144 | 0 | 1.77 | -2.1% | 10.29 | +3.8% | pass |
| Random read 64KB | 1.05 | 17225.92 | 14.04 ms/op | 13.96 | 17.43 | 19.53 | 56.85 | 262144 | 0 | 1.12 | -6.1% | 19.53 | 0.0% | pass |
| Sequential write 256KB | 2.53 | 10359.79 | 23.00 ms/op | 24.51 | 32.90 | 37.49 | 47.83 | 65536 | 0 | 2.73 | -7.4% | 36.44 | +2.9% | pass |
| Sequential read 256KB | 3.22 | 13183.67 | 17.37 ms/op | 18.22 | 24.51 | 27.13 | 58.05 | 65536 | 0 | 3.11 | +3.5% | 26.08 | +4.0% | pass |
| Random write 256KB | 2.45 | 10051.53 | 24.21 ms/op | 23.46 | 28.97 | 31.85 | 476.79 | 65536 | 0 | 2.51 | -2.2% | 30.28 | +5.2% | pass |
| Random read 256KB | 2.31 | 9471.89 | 25.98 ms/op | 25.82 | 31.33 | 34.34 | 46.24 | 65536 | 0 | 2.37 | -2.4% | 34.34 | 0.0% | pass |
| Sequential write 1MB | 3.31 | 3388.62 | 64.64 ms/op | 58.46 | 135.27 | 179.31 | 287.72 | 16384 | 0 | 3.45 | -4.1% | 191.89 | -6.6% | pass |
| Sequential read 1MB | 3.22 | 3294.59 | 69.32 ms/op | 77.07 | 91.75 | 94.90 | 140.92 | 16384 | 0 | 2.72 | +18.3% | 108.53 | -12.6% | pass |
| Random write 1MB | 2.61 | 2667.97 | 85.52 ms/op | 73.92 | 117.96 | 784.33 | 1347.35 | 16384 | 0 | 3.09 | -15.7% | 229.64 | +241.5% | fail |
| Random read 1MB | 2.32 | 2378.28 | 104.32 ms/op | 105.38 | 117.96 | 128.45 | 183.40 | 16384 | 0 | 2.15 | +8.0% | 135.27 | -5.0% | pass |

## Failures and attribution

### Failure analysis

#### g-fuse-buffered-io-eio

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse mount option generation from FuseConf (introduced in e01cf918) appears to mis-apply or omit settings required for buffered read/write, causing user I/O on /curvine-fuse to fail with Input/output error. Mount and metadata operations succeed, but sustained or verified writes fail deterministically. This is a pre-existing product defect still open as GitHub issue #1646.
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.

#### g-raft-propose-apply-timeout-flaky

- Class: **flaky**
- Failure layer: **test**
- Root-cause confidence: **medium**
- Root cause: The propose_response_waits_until_committed_entry_is_applied unit test uses a 3-second timeout for apply to start after propose. Under load or slow Raft election timing (log shows ~14 seconds before election began), the committed entry may not reach BlockingApplyAppStorage within the timeout window. Daily passed on the immediately prior run at 5ecf8ca2, suggesting intermittent timing sensitivity rather than a deterministic product defect on 39069ae2.
- Recommendation: If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from intermittent timeout without stable reproduction across commits.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| propose_response_waits_until_committed_entry_is_applied | raft_node_test / curvine-raft | FAILED | thread 'propose_response_waits_until_committed_entry_is_applied' (29715) panicked at crates/metadata/curvine-raft/tests/raft_node_test.rs:615:14: | g-raft-propose-apply-timeout-flaky |
| FIO Sequential Write Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Write test failed | g-fuse-buffered-io-eio |
| FIO Sequential Read Test (256KB blocks) | fio / fuse | FAIL | FIO Sequential Read test failed | g-fuse-buffered-io-eio |
| FIO Random Write Test (256KB blocks) | fio / fuse | FAIL | FIO Random Write test failed | g-fuse-buffered-io-eio |
| FIO Random Read Test (256KB blocks) | fio / fuse | FAIL | FIO Random Read test failed | g-fuse-buffered-io-eio |
| FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write) | fio / fuse | FAIL | FIO Mixed Random Read/Write test failed | g-fuse-buffered-io-eio |
| fuse | fuse / fuse | FAILED | "status": "failed" | g-fuse-buffered-io-eio |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |
| daily | 1 | 1 | 0 |
| fuse | 6 | 6 | 0 |

### Common root-cause groups

#### g-fuse-buffered-io-eio

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.

#### g-raft-propose-apply-timeout-flaky

- Model class: **flaky**; confidence: **medium**
- Recommendation: If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from intermittent timeout without stable reproduction across commits.


## Follow-up

### Defects and fixes

- GitHub Issue: [1646](https://github.com/CurvineIO/curvine/issues/1646) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.
- If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from intermittent timeout without stable reproduction across commits.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
