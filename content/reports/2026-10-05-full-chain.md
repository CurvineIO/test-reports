---
title: "Curvine full-chain daily test report - 2026-10-05"
linkTitle: "2026-10-05 full-chain"
date: 2026-10-05T00:00:00Z
weight: -20261005
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 2 passed, 4 failed.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 2/7 passed | FAIL |
| Failure attribution | Failures classified | 10 root-cause groups | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failed profiles require resolution before release.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 32s | passed | PASSED |
| integration | PASS | FAIL | 5m 12s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 28s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 4m 22s | unknown_failure | PASSED |
| ltp | PASS | FAIL | 38m 01s | unknown_failure | PASSED |
| csi | PASS | PASS | 0m 34s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 2m 38s | failed | PASSED |

### LTP

- Status: **COMPLETED_WITH_FAILURES**
- Suites completed: 7
- Suites remaining: 0
- Stats: 1112 passed / 17 real failed / 141 skipped / 0 report-consistency errors

| Suite | Status | Passed | Real failed | Skipped | Report errors | Return code |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| fs_perms_simple | passed | 18 | 0 | 0 | 0 | 0 |
| fsx | passed | 1 | 0 | 0 | 0 | 0 |
| fs_bind | passed | 1 | 0 | 0 | 0 | 0 |
| smoketest | passed | 12 | 0 | 1 | 0 | 0 |
| io | passed | 2 | 0 | 0 | 0 | 0 |
| fs-jfs | failed | 10 | 17 | 2 | 0 | 1 |
| syscalls-jfs | failed | 1068 | 0 | 138 | 0 | 1 |

### Performance

> [!NOTE]
> Gate policy: **report only, non-blocking** for the full-chain result. Mark yellow/red vs baseline for human follow-up.

- Status: **failed**
- Gate mode: **report_only**

#### Metadata performance (this run)

| ITEM | VALUE | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline VALUE | VALUE delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Create file | 9706.21 ops/s | 4.12 ms/op | 8.19 | 8.19 | 8.19 | 26.10 | 200000 | 0 | 21668.74 ops/s | -55.2% | 4.09 | +100.3% | fail |
| Stat file | 21461.69 ops/s | 1.86 ms/op | 2.05 | 2.05 | 4.09 | 4.49 | 200000 | 0 | 63487.48 ops/s | -66.2% | 2.05 | +99.8% | fail |
| Open file | 22330.60 ops/s | 1.79 ms/op | 2.05 | 2.05 | 4.09 | 4.15 | 200000 | 0 | 63113.20 ops/s | -64.6% | 2.05 | +99.8% | fail |
| Rename file | 16939.21 ops/s | 2.36 ms/op | 4.09 | 4.09 | 4.09 | 279.99 | 200000 | 0 | 30314.48 ops/s | -44.1% | 4.09 | +0.1% | fail |
| Delete file | 16766.15 ops/s | 2.39 ms/op | 4.09 | 4.09 | 4.09 | 4.66 | 200000 | 0 | 31231.33 ops/s | -46.3% | 4.09 | +0.1% | fail |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.71 | 28093.88 | 8.90 ms/op | 8.85 | 10.29 | 11.21 | 20.23 | 262144 | 0 | 1.71 | +0.3% | 10.94 | +2.4% | pass |
| Sequential read 64KB | 2.15 | 35158.80 | 6.97 ms/op | 6.46 | 11.99 | 14.35 | 29.35 | 262144 | 0 | 2.28 | -5.9% | 12.78 | +12.3% | pass |
| Random write 64KB | 1.76 | 28883.21 | 8.53 ms/op | 8.29 | 9.63 | 10.68 | 301.53 | 262144 | 0 | 1.77 | -0.4% | 10.29 | +3.8% | pass |
| Random read 64KB | 1.06 | 17336.42 | 14.34 ms/op | 14.22 | 17.69 | 19.79 | 50.72 | 262144 | 0 | 1.12 | -5.5% | 19.53 | +1.3% | pass |
| Sequential write 256KB | 2.76 | 11287.63 | 21.11 ms/op | 22.41 | 33.16 | 37.49 | 56.82 | 65536 | 0 | 2.73 | +0.9% | 36.44 | +2.9% | pass |
| Sequential read 256KB | 3.25 | 13309.50 | 16.97 ms/op | 17.69 | 22.68 | 24.51 | 35.76 | 65536 | 0 | 3.11 | +4.5% | 26.08 | -6.0% | pass |
| Random write 256KB | 2.57 | 10507.62 | 22.58 ms/op | 20.58 | 26.87 | 30.02 | 770.03 | 65536 | 0 | 2.51 | +2.2% | 30.28 | -0.9% | pass |
| Random read 256KB | 2.23 | 9150.52 | 26.63 ms/op | 26.61 | 32.11 | 35.39 | 55.42 | 65536 | 0 | 2.37 | -5.7% | 34.34 | +3.1% | pass |
| Sequential write 1MB | 3.36 | 3443.46 | 63.62 ms/op | 52.17 | 166.72 | 223.35 | 337.59 | 16384 | 0 | 3.45 | -2.5% | 191.89 | +16.4% | degraded |
| Sequential read 1MB | 2.87 | 2935.15 | 78.42 ms/op | 87.56 | 102.24 | 106.43 | 170.11 | 16384 | 0 | 2.72 | +5.4% | 108.53 | -1.9% | pass |
| Random write 1MB | 3.04 | 3116.01 | 72.91 ms/op | 65.27 | 110.62 | 358.61 | 679.08 | 16384 | 0 | 3.09 | -1.5% | 229.64 | +56.2% | fail |
| Random read 1MB | 2.15 | 2200.67 | 112.22 ms/op | 113.77 | 125.30 | 133.69 | 194.93 | 16384 | 0 | 2.15 | 0.0% | 135.27 | -1.2% | pass |

## Failures and attribution

### Failure analysis

#### g-daily-rustc-recursion-compile

- Class: **unknown_failure**
- Failure layer: **build**
- Root-cause confidence: **medium**
- Root cause: Rust compiler query recursion limit is exceeded while type-checking async test code in curvine-tests fallback_read_test and write_cache_test at 032c6dc5. Whether test refactor or toolchain limits is primary remains unproven.
- Recommendation: Bisect when daily compilation last passed; add recursion_limit attributes or refactor async helpers in curvine-tests, or adjust CI toolchain settings if environment-specific.

#### g-integration-compile-missing-summary

- Class: **harness_failure**
- Failure layer: **build**
- Root-cause confidence: **high**
- Root cause: Integration profile compilation failed on curvine-tests recursion-limit overflow; orchestration exit 40 reflects missing test_summary.json artifact, not a separate product runtime defect.
- Recommendation: Fix curvine-tests compilation (same build blocker as daily) so integration emits exactly one new test_summary.json after successful cargo test --no-run.

#### g-ltp-ftest-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: curvine-fuse read and readv paths return Input/output error errno=5 for ftest workloads on fs-jfs. Issue #1701 documents the defect; attributing it to any specific merged PR without bisect on 032c6dc5 would be speculative.
- Recommendation: Investigate curvine-fuse read/readv errno=5 on fs-jfs ftest workloads under GitHub issue #1701; add regression coverage after root cause is confirmed by bisect.

#### g-ltp-lftest-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: Likely the same worker Running-frame flush regression as ftest read EIO; write-path symptom on lftest01.
- Recommendation: Address alongside worker flush regression in issue #1701.

#### g-ltp-stream-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **medium**
- Root cause: stream04 reports direct fread Input/output error; stream01/03/05 failures follow in the same fs-jfs run. Likely related to curvine-fuse I/O errors tracked under issue #1701.
- Recommendation: Re-test stream cases after worker flush fix in issue #1701.

#### g-ltp-writetest-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **medium**
- Root cause: Likely verify failure caused by incomplete writes from the worker flush regression.
- Recommendation: Re-test writetest after worker flush fix in issue #1701.

#### g-ltp-inode-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: Likely the same worker flush regression manifesting on inode stress writes.
- Recommendation: Re-test inode02 after worker flush fix in issue #1701.

#### g-ltp-fs-di-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **medium**
- Root cause: Likely unable to create large test files because of the worker flush regression returning EIO on writes.
- Recommendation: Re-test fs_di after worker flush fix in issue #1701.

#### g-ltp-fs-fill-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: Likely the same worker flush regression blocking loop-device file creation on curvine-fuse.
- Recommendation: Re-test fs_fill after worker flush fix in issue #1701.

#### g-fuse-git-clone-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **medium**
- Root cause: Git clone to curvine-fuse fails with index.lock write Input/output error while fio passed. Likely related to curvine-fuse write-path instability tracked under issue #1701.
- Recommendation: Re-test git clone on curvine-fuse after worker flush fix in issue #1701.

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| integration profile | integration / integration | FAILED | profile failed | g-integration-compile-missing-summary |
| daily profile | daily / daily | FAILED | profile failed | g-daily-rustc-recursion-compile |
| fuse | fuse / fuse | FAILED | "status": "failed" | g-fuse-git-clone-eio-worker-flush |
| inode02 | fs-jfs / ltp | FAILED | inode02 1 TFAIL : inode02.c:851: Test failed | g-ltp-inode-eio-worker-flush |
| stream01 | fs-jfs / ltp | FAILED | stream01 1 TFAIL : stream01.c:92: bad contents in stream011.34421 / stream01 2 TFAIL : stream01.c:106: bad contents in stream012.34421 / stream01 3 TFAIL : stream01.c:115: Test failed. | g-ltp-stream-eio-worker-flush |
| stream03 | fs-jfs / ltp | FAILED | stream03 1 TFAIL : stream03.c:164: strlen(junk)=26: file pointer descrepancy 7 (pos=0) / stream03 2 TFAIL : stream03.c:175: Test failed in block0. / stream03 3 TFAIL : stream03.c:278: strlen(junk)=26: file pointer descrepancy 7 (opos=0) | g-ltp-stream-eio-worker-flush |
| stream04 | fs-jfs / ltp | FAILED | stream04 1 TFAIL : stream04.c:104: fread failed: Input/output error | g-ltp-stream-eio-worker-flush |
| stream05 | fs-jfs / ltp | FAILED | stream05 2 TFAIL : stream05.c:115: read did not read right number / stream05 3 TFAIL : stream05.c:119: read returned bad values / stream05 4 TFAIL : stream05.c:125: Test failed in block1. | g-ltp-stream-eio-worker-flush |
| ftest01 | fs-jfs / ltp | FAILED | ftest01 1 TFAIL : ftest01.c:343: Test[0]: read fail at 34000, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[1]: read fail at c6800, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[2]: read fail at 73800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest02 | fs-jfs / ltp | FAILED | ftest02 1 TBROK : ftest02.c:413: Test[2]: error 5 on read / ftest02 2 TBROK : ftest02.c:413: Remaining cases broken / ftest02 1 TBROK : ftest02.c:413: Test[1]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest03 | fs-jfs / ltp | FAILED | ftest03 1 TFAIL : ftest03.c:404: Test[0]: readv fail at ea000, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[1]: readv fail at 48800, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[2]: readv fail at 39000, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest04 | fs-jfs / ltp | FAILED | ftest04 1 TFAIL : ftest04.c:327: Test[1]: readv fail at 2b000, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[2]: readv fail at 5d800, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[0]: readv fail at 28000, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest05 | fs-jfs / ltp | FAILED | ftest05 1 TFAIL : ftest05.c:337: Test[0]: read fail at a7800: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[1]: read fail at 55800: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[2]: read fail at 21800: errno=EIO(5): Input/output error | g-ltp-ftest-eio-worker-flush |
| ftest06 | fs-jfs / ltp | FAILED | ftest06 1 TFAIL : ftest06.c:431: Test[0]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[1]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[4]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest07 | fs-jfs / ltp | FAILED | ftest07 1 TFAIL : ftest07.c:399: Test[0]: readv fail at 81000, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[1]: readv fail at 79000, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[2]: readv fail at 0, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest08 | fs-jfs / ltp | FAILED | ftest08 1 TFAIL : ftest08.c:340: Test[1]: readv fail at a0800x, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[2]: readv fail at 9c000x, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[0]: readv fail at 8e800x, errno = 5. | g-ltp-ftest-eio-worker-flush |
| lftest01 | fs-jfs / ltp | FAILED | lftest.c:55: TFAIL: write() failed: EIO (5) | g-ltp-lftest-eio-worker-flush |
| writetest01 | fs-jfs / ltp | FAILED | writetest 2 TFAIL : writetest.c:253: Verify: Failure | g-ltp-writetest-eio-worker-flush |
| fs_di | fs-jfs / ltp | FAILED | fs_di 10 TFAIL : ltpapicmd.c:188: Test Failed: Could not create testfile of size 30Mb | g-ltp-fs-di-eio-worker-flush |
| fs_fill | fs-jfs / ltp | FAILED | tst_device.c:335: TBROK: Failed to acquire device | g-ltp-fs-fill-eio-worker-flush |
| writetest | fs-jfs / ltp | TFAIL | writetest.c:253: Verify: Failure | g-ltp-writetest-eio-worker-flush |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta |
| --- | ---: | ---: | ---: |
| integration | 1 | 1 | 0 |
| daily | 1 | 0 | 1 |
| fuse | 1 | 1 | 0 |
| ltp | 18 | 18 | 0 |

### Common root-cause groups

#### g-daily-rustc-recursion-compile

- Model class: **unknown_failure**; confidence: **medium**
- Recommendation: Bisect when daily compilation last passed; add recursion_limit attributes or refactor async helpers in curvine-tests, or adjust CI toolchain settings if environment-specific.

#### g-integration-compile-missing-summary

- Model class: **harness_failure**; confidence: **high**
- Recommendation: Fix curvine-tests compilation (same build blocker as daily) so integration emits exactly one new test_summary.json after successful cargo test --no-run.

#### g-ltp-ftest-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Investigate curvine-fuse read/readv errno=5 on fs-jfs ftest workloads under GitHub issue #1701; add regression coverage after root cause is confirmed by bisect.

#### g-ltp-lftest-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Address alongside worker flush regression in issue #1701.

#### g-ltp-stream-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **medium**
- Recommendation: Re-test stream cases after worker flush fix in issue #1701.

#### g-ltp-writetest-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **medium**
- Recommendation: Re-test writetest after worker flush fix in issue #1701.

#### g-ltp-inode-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Re-test inode02 after worker flush fix in issue #1701.

#### g-ltp-fs-di-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **medium**
- Recommendation: Re-test fs_di after worker flush fix in issue #1701.

#### g-ltp-fs-fill-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Re-test fs_fill after worker flush fix in issue #1701.

#### g-fuse-git-clone-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **medium**
- Recommendation: Re-test git clone on curvine-fuse after worker flush fix in issue #1701.


## Follow-up

### Defects and fixes

- GitHub Issue: [1701](https://github.com/CurvineIO/curvine/issues/1701) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Bisect when daily compilation last passed; add recursion_limit attributes or refactor async helpers in curvine-tests, or adjust CI toolchain settings if environment-specific.
- Fix curvine-tests compilation (same build blocker as daily) so integration emits exactly one new test_summary.json after successful cargo test --no-run.
- Investigate curvine-fuse read/readv errno=5 on fs-jfs ftest workloads under GitHub issue #1701; add regression coverage after root cause is confirmed by bisect.
- Address alongside worker flush regression in issue #1701.
- Re-test stream cases after worker flush fix in issue #1701.
- Re-test writetest after worker flush fix in issue #1701.
- Re-test inode02 after worker flush fix in issue #1701.
- Re-test fs_di after worker flush fix in issue #1701.
- Re-test fs_fill after worker flush fix in issue #1701.
- Re-test git clone on curvine-fuse after worker flush fix in issue #1701.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
