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
| fast | PASS | PASS | 12m 23s | passed | PASSED |
| integration | PASS | PASS | 12m 05s | passed | PASSED |
| daily | PASS | FAIL | 20m 39s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 3m 38s | unknown_failure | PASSED |
| ltp | PASS | PASS | 50m 05s | passed | PASSED |
| csi | PASS | PASS | 0m 35s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 1m 58s | failed | PASSED |

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
| Create file | 23407.32 ops/s | 1.70 ms/op | 2.05 | 4.09 | 4.09 | 158.56 | 200000 | 0 | 21668.74 ops/s | +8.0% | 4.09 | +0.1% | pass |
| Stat file | 70594.64 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 3.06 | 200000 | 0 | 63487.48 ops/s | +11.2% | 2.05 | -50.1% | pass |
| Open file | 70275.83 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 1.79 | 200000 | 0 | 63113.20 ops/s | +11.3% | 2.05 | -50.1% | pass |
| Rename file | 32871.07 ops/s | 1.20 ms/op | 2.05 | 3.57 | 3.57 | 3.57 | 200000 | 0 | 30314.48 ops/s | +8.4% | 4.09 | -12.8% | pass |
| Delete file | 32472.27 ops/s | 1.22 ms/op | 2.05 | 4.09 | 4.09 | 4.81 | 200000 | 0 | 31231.33 ops/s | +4.0% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.74 | 28466.07 | 8.76 ms/op | 8.72 | 10.29 | 11.08 | 18.01 | 262144 | 0 | 1.71 | +1.6% | 10.94 | +1.2% | pass |
| Sequential read 64KB | 2.48 | 40598.42 | 5.91 ms/op | 5.60 | 9.90 | 12.12 | 24.00 | 262144 | 0 | 2.28 | +8.7% | 12.78 | -5.1% | pass |
| Random write 64KB | 1.81 | 29691.24 | 8.31 ms/op | 8.09 | 9.24 | 9.90 | 328.16 | 262144 | 0 | 1.77 | +2.4% | 10.29 | -3.8% | pass |
| Random read 64KB | 1.12 | 18415.45 | 13.43 ms/op | 13.30 | 16.91 | 19.27 | 54.83 | 262144 | 0 | 1.12 | +0.4% | 19.53 | -1.3% | pass |
| Sequential write 256KB | 2.96 | 12116.10 | 19.32 ms/op | 20.58 | 30.54 | 35.91 | 48.83 | 65536 | 0 | 2.73 | +8.4% | 36.44 | -1.4% | pass |
| Sequential read 256KB | 2.56 | 10469.01 | 22.66 ms/op | 25.56 | 28.97 | 31.06 | 55.85 | 65536 | 0 | 3.11 | -17.8% | 26.08 | +19.1% | degraded |
| Random write 256KB | 2.79 | 11437.35 | 21.07 ms/op | 20.05 | 25.30 | 28.44 | 510.28 | 65536 | 0 | 2.51 | +11.2% | 30.28 | -6.1% | pass |
| Random read 256KB | 2.39 | 9775.66 | 24.74 ms/op | 24.77 | 30.28 | 32.90 | 47.31 | 65536 | 0 | 2.37 | +0.7% | 34.34 | -4.2% | pass |
| Sequential write 1MB | 3.51 | 3596.93 | 61.40 ms/op | 60.03 | 139.46 | 181.40 | 280.45 | 16384 | 0 | 3.45 | +1.8% | 191.89 | -5.5% | pass |
| Sequential read 1MB | 3.03 | 3099.51 | 73.78 ms/op | 76.02 | 96.99 | 102.24 | 173.82 | 16384 | 0 | 2.72 | +11.3% | 108.53 | -5.8% | pass |
| Random write 1MB | 3.05 | 3121.36 | 75.24 ms/op | 68.68 | 103.28 | 497.03 | 753.29 | 16384 | 0 | 3.09 | -1.4% | 229.64 | +116.4% | fail |
| Random read 1MB | 2.23 | 2280.62 | 108.82 ms/op | 109.58 | 122.16 | 128.45 | 174.27 | 16384 | 0 | 2.15 | +3.6% | 135.27 | -5.0% | pass |

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
- Root cause: The propose_response_waits_until_committed_entry_is_applied unit test uses a 3-second timeout for apply to start after propose. Under load or slow Raft election timing (log shows 16 seconds before election began), the committed entry may not reach BlockingApplyAppStorage within the timeout window. Same SHA passed on the immediately prior daily run, suggesting intermittent timing sensitivity rather than a deterministic product defect.
- Recommendation: If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from a single flaky occurrence on a passing SHA.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| propose_response_waits_until_committed_entry_is_applied | raft_node_test / curvine-raft | FAILED | thread 'propose_response_waits_until_committed_entry_is_applied' (29699) panicked at crates/metadata/curvine-raft/tests/raft_node_test.rs:615:14: | g-raft-propose-apply-timeout-flaky |
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
- Recommendation: If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from a single flaky occurrence on a passing SHA.


## Follow-up

### Defects and fixes

- GitHub Issue: [1646](https://github.com/CurvineIO/curvine/issues/1646) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Review e01cf918 changes in curvine-fuse/src/cli/mount_args.rs and crates/common/curvine-config/src/fuse_conf.rs ClientConfCliOverrides generation; compare effective mount flags against eb76f94a and restore correct buffered I/O behavior.
- If failures recur, increase the wait_started timeout in raft_node_test.rs or investigate Raft election/apply latency under parallel test load. No product code change warranted from a single flaky occurrence on a passing SHA.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
