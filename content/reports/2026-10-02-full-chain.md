---
title: "Curvine full-chain daily test report - 2026-10-02"
linkTitle: "2026-10-02 full-chain"
date: 2026-10-02T00:00:00Z
weight: -20261002
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
| fast | PASS | PASS | 12m 42s | passed | PASSED |
| integration | PASS | FAIL | 5m 17s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 28s | unknown_failure | PASSED |
| fuse | PASS | FAIL | 4m 35s | unknown_failure | PASSED |
| ltp | PASS | FAIL | 37m 55s | unknown_failure | PASSED |
| csi | PASS | PASS | 0m 36s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 2m 42s | failed | PASSED |

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
| Create file | 10247.21 ops/s | 3.90 ms/op | 4.09 | 8.19 | 8.19 | 153.27 | 200000 | 0 | 21668.74 ops/s | -52.7% | 4.09 | +100.3% | fail |
| Stat file | 23544.93 ops/s | 1.70 ms/op | 2.05 | 2.05 | 2.05 | 4.09 | 200000 | 0 | 63487.48 ops/s | -62.9% | 2.05 | -0.1% | fail |
| Open file | 22661.97 ops/s | 1.76 ms/op | 2.05 | 2.05 | 4.09 | 4.26 | 200000 | 0 | 63113.20 ops/s | -64.1% | 2.05 | +99.8% | fail |
| Rename file | 16974.72 ops/s | 2.36 ms/op | 4.09 | 4.09 | 4.09 | 4.81 | 200000 | 0 | 30314.48 ops/s | -44.0% | 4.09 | +0.1% | fail |
| Delete file | 17032.68 ops/s | 2.35 ms/op | 4.09 | 4.09 | 4.09 | 4.98 | 200000 | 0 | 31231.33 ops/s | -45.5% | 4.09 | +0.1% | fail |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.67 | 27355.11 | 9.13 ms/op | 9.11 | 10.94 | 12.12 | 19.28 | 262144 | 0 | 1.71 | -2.4% | 10.94 | +10.8% | pass |
| Sequential read 64KB | 1.78 | 29224.53 | 7.42 ms/op | 6.65 | 13.43 | 15.40 | 28.17 | 262144 | 0 | 2.28 | -21.8% | 12.78 | +20.5% | degraded |
| Random write 64KB | 1.67 | 27343.69 | 9.00 ms/op | 8.72 | 10.42 | 12.52 | 298.07 | 262144 | 0 | 1.77 | -5.7% | 10.29 | +21.6% | degraded |
| Random read 64KB | 1.09 | 17860.87 | 13.95 ms/op | 13.83 | 17.43 | 19.79 | 51.54 | 262144 | 0 | 1.12 | -2.7% | 19.53 | +1.3% | pass |
| Sequential write 256KB | 2.46 | 10059.25 | 23.32 ms/op | 24.25 | 35.91 | 44.83 | 65.25 | 65536 | 0 | 2.73 | -10.0% | 36.44 | +23.0% | degraded |
| Sequential read 256KB | 2.48 | 10143.32 | 24.00 ms/op | 25.56 | 28.97 | 30.80 | 49.91 | 65536 | 0 | 3.11 | -20.4% | 26.08 | +18.1% | degraded |
| Random write 256KB | 2.35 | 9637.65 | 24.87 ms/op | 23.20 | 31.59 | 36.96 | 757.69 | 65536 | 0 | 2.51 | -6.3% | 30.28 | +22.1% | degraded |
| Random read 256KB | 2.30 | 9401.23 | 26.11 ms/op | 26.08 | 31.33 | 34.34 | 44.56 | 65536 | 0 | 2.37 | -3.2% | 34.34 | 0.0% | pass |
| Sequential write 1MB | 2.92 | 2988.15 | 70.34 ms/op | 64.23 | 187.70 | 287.31 | 568.04 | 16384 | 0 | 3.45 | -15.4% | 191.89 | +49.7% | fail |
| Sequential read 1MB | 2.41 | 2464.50 | 98.52 ms/op | 104.33 | 115.87 | 128.45 | 185.79 | 16384 | 0 | 2.72 | -11.5% | 108.53 | +18.4% | degraded |
| Random write 1MB | 2.48 | 2544.49 | 91.41 ms/op | 83.36 | 152.04 | 476.05 | 853.99 | 16384 | 0 | 3.09 | -19.6% | 229.64 | +107.3% | fail |
| Random read 1MB | 2.18 | 2230.94 | 110.13 ms/op | 111.67 | 124.26 | 131.60 | 210.10 | 16384 | 0 | 2.15 | +1.3% | 135.27 | -2.7% | pass |

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
| stream01 | fs-jfs / ltp | FAILED | stream01 1 TFAIL : stream01.c:92: bad contents in stream011.34416 / stream01 2 TFAIL : stream01.c:106: bad contents in stream012.34416 / stream01 3 TFAIL : stream01.c:115: Test failed. | g-ltp-stream-eio-worker-flush |
| stream03 | fs-jfs / ltp | FAILED | stream03 1 TFAIL : stream03.c:164: strlen(junk)=26: file pointer descrepancy 7 (pos=0) / stream03 2 TFAIL : stream03.c:175: Test failed in block0. / stream03 3 TFAIL : stream03.c:278: strlen(junk)=26: file pointer descrepancy 7 (opos=0) | g-ltp-stream-eio-worker-flush |
| stream04 | fs-jfs / ltp | FAILED | stream04 1 TFAIL : stream04.c:104: fread failed: Input/output error | g-ltp-stream-eio-worker-flush |
| stream05 | fs-jfs / ltp | FAILED | stream05 2 TFAIL : stream05.c:115: read did not read right number / stream05 3 TFAIL : stream05.c:119: read returned bad values / stream05 4 TFAIL : stream05.c:125: Test failed in block1. | g-ltp-stream-eio-worker-flush |
| ftest01 | fs-jfs / ltp | FAILED | ftest01 1 TFAIL : ftest01.c:343: Test[0]: read fail at cc000, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[1]: read fail at 81000, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[2]: read fail at 8f800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest02 | fs-jfs / ltp | FAILED | ftest02 1 TBROK : ftest02.c:413: Test[2]: error 5 on read / ftest02 2 TBROK : ftest02.c:413: Remaining cases broken / ftest02 1 TBROK : ftest02.c:413: Test[0]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest03 | fs-jfs / ltp | FAILED | ftest03 1 TFAIL : ftest03.c:404: Test[0]: readv fail at 46800, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[1]: readv fail at 3e800, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[2]: readv fail at e1800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest04 | fs-jfs / ltp | FAILED | ftest04 1 TFAIL : ftest04.c:413: Test[0]: writev fail at 16800 xfr -1, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[3]: readv fail at c4800, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[2]: readv fail at b7800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest05 | fs-jfs / ltp | FAILED | ftest05 1 TFAIL : ftest05.c:337: Test[0]: read fail at 7800: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[1]: read fail at 78800: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[2]: read fail at 7800: errno=EIO(5): Input/output error | g-ltp-ftest-eio-worker-flush |
| ftest06 | fs-jfs / ltp | FAILED | ftest06 1 TFAIL : ftest06.c:431: Test[1]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[4]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[2]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest07 | fs-jfs / ltp | FAILED | ftest07 1 TFAIL : ftest07.c:399: Test[0]: readv fail at ee800, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[1]: readv fail at 21800, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[2]: readv fail at e5800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest08 | fs-jfs / ltp | FAILED | ftest08 1 TFAIL : ftest08.c:340: Test[2]: readv fail at 88000x, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[0]: readv fail at 69000x, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[1]: readv fail at 53000x, errno = 5. | g-ltp-ftest-eio-worker-flush |
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
