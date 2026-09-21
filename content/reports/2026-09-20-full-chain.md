---
title: "Curvine full-chain daily test report - 2026-09-20"
linkTitle: "2026-09-20 full-chain"
date: 2026-09-20T00:00:00Z
weight: -20260920
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
| Failure attribution | Failures classified | 8 root-cause groups | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failed profiles require resolution before release.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 16s | passed | PASSED |
| integration | PASS | FAIL | 5m 13s | harness_failure | PASSED |
| daily | PASS | FAIL | 9m 18s | unknown_failure | PASSED |
| fuse | PASS | PASS | 5m 51s | passed | PASSED |
| ltp | PASS | FAIL | 37m 31s | unknown_failure | PASSED |
| csi | PASS | PASS | 0m 37s | passed | PASSED |
| perf-benchmark | NOT_RECORDED | FAILED | 5m 38s | failed | PASSED |

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
| Create file | 24303.01 ops/s | 1.64 ms/op | 2.05 | 4.09 | 4.09 | 4.52 | 200000 | 0 | 21668.74 ops/s | +12.2% | 4.09 | +0.1% | pass |
| Stat file | 71507.28 ops/s | 0.56 ms/op | 1.02 | 1.02 | 1.02 | 2.78 | 200000 | 0 | 63487.48 ops/s | +12.6% | 2.05 | -50.1% | pass |
| Open file | 69299.76 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 2.93 | 200000 | 0 | 63113.20 ops/s | +9.8% | 2.05 | -50.1% | pass |
| Rename file | 33230.68 ops/s | 1.19 ms/op | 2.05 | 3.71 | 3.71 | 3.71 | 200000 | 0 | 30314.48 ops/s | +9.6% | 4.09 | -9.2% | pass |
| Delete file | 33997.68 ops/s | 1.17 ms/op | 2.05 | 4.09 | 4.09 | 4.94 | 200000 | 0 | 31231.33 ops/s | +8.9% | 4.09 | +0.1% | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Baseline SPEED GiB/s | SPEED delta | Baseline P99 ms | P99 delta | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.70 | 27801.89 | 9.01 ms/op | 8.98 | 10.42 | 11.21 | 18.14 | 262144 | 0 | 1.71 | -0.8% | 10.94 | +2.4% | pass |
| Sequential read 64KB | 2.36 | 38618.74 | 6.25 ms/op | 5.87 | 10.42 | 12.78 | 24.55 | 262144 | 0 | 2.28 | +3.4% | 12.78 | 0.0% | pass |
| Random write 64KB | 1.75 | 28671.55 | 8.67 ms/op | 8.45 | 9.76 | 10.81 | 290.91 | 262144 | 0 | 1.77 | -1.1% | 10.29 | +5.1% | pass |
| Random read 64KB | 1.09 | 17897.45 | 13.53 ms/op | 13.43 | 16.71 | 19.01 | 42.46 | 262144 | 0 | 1.12 | -2.5% | 19.53 | -2.7% | pass |
| Sequential write 256KB | 2.68 | 10962.86 | 21.86 ms/op | 23.20 | 32.90 | 37.49 | 46.97 | 65536 | 0 | 2.73 | -2.0% | 36.44 | +2.9% | pass |
| Sequential read 256KB | 2.65 | 10837.77 | 21.87 ms/op | 23.99 | 27.66 | 29.23 | 48.94 | 65536 | 0 | 3.11 | -14.9% | 26.08 | +12.1% | pass |
| Random write 256KB | 2.60 | 10656.26 | 22.90 ms/op | 22.15 | 27.66 | 30.54 | 462.94 | 65536 | 0 | 2.51 | +3.7% | 30.28 | +0.9% | pass |
| Random read 256KB | 2.35 | 9643.32 | 25.07 ms/op | 25.03 | 30.28 | 33.82 | 51.29 | 65536 | 0 | 2.37 | -0.7% | 34.34 | -1.5% | pass |
| Sequential write 1MB | 3.07 | 3140.50 | 71.86 ms/op | 67.63 | 158.33 | 219.15 | 348.27 | 16384 | 0 | 3.45 | -11.1% | 191.89 | +14.2% | pass |
| Sequential read 1MB | 2.43 | 2492.62 | 96.48 ms/op | 105.38 | 113.77 | 117.96 | 210.85 | 16384 | 0 | 2.72 | -10.5% | 108.53 | +8.7% | pass |
| Random write 1MB | 2.85 | 2921.54 | 79.98 ms/op | 74.97 | 122.16 | 291.50 | 497.01 | 16384 | 0 | 3.09 | -7.7% | 229.64 | +26.9% | fail |
| Random read 1MB | 2.20 | 2253.34 | 110.32 ms/op | 111.67 | 123.21 | 129.50 | 178.98 | 16384 | 0 | 2.15 | +2.3% | 135.27 | -4.3% | pass |

## Failures and attribution

### Failure analysis

#### g-rustc-recursion-compile

- Class: **unknown_failure**
- Failure layer: **build**
- Root-cause confidence: **medium**
- Root cause: Rust compiler query recursion limit is exceeded while type-checking async test code in fallback_read_test and write_cache_test. Whether increased type complexity in curvine-tests or rustc 1.98 limits is primary remains unproven.
- Recommendation: Bisect commits between last passing daily compilation SHA and current main; add recursion_limit attributes or refactor async test helpers if product-side, or adjust toolchain settings if environment-specific.

#### g-ltp-ftest-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: The worker Running-frame flush change in write_handler.rs (PR #1694) likely regressed read/readv durability on curvine-fuse for ftest workloads. Failure persists on de580be3; narrowed bisect against LTP-clean SHA 04d988e3 is still required.
- Recommendation: Review flush-only Running frame handling in curvine-worker/src/worker/handler/write_handler.rs from PR #1694; add ftest read/readv regression coverage on curvine-fuse.

#### g-ltp-lftest-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **high**
- Root cause: Likely the same worker Running-frame flush regression as ftest read EIO; write-path symptom on lftest01.
- Recommendation: Address alongside PR #1694 write_handler flush regression in issue #1701.

#### g-ltp-stream-eio-worker-flush

- Class: **pre_existing_failure**
- Failure layer: **product**
- Root-cause confidence: **medium**
- Root cause: Likely cascade from the worker flush regression affecting stream I/O on curvine-fuse.
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

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| integration profile | integration / integration | FAILED | profile failed | g-rustc-recursion-compile |
| daily profile | daily / daily | FAILED | profile failed | g-rustc-recursion-compile |
| inode02 | fs-jfs / ltp | FAILED | inode02 1 TFAIL : inode02.c:851: Test failed | g-ltp-inode-eio-worker-flush |
| stream01 | fs-jfs / ltp | FAILED | stream01 1 TFAIL : stream01.c:92: bad contents in stream011.34412 / stream01 2 TFAIL : stream01.c:106: bad contents in stream012.34412 / stream01 3 TFAIL : stream01.c:115: Test failed. | g-ltp-stream-eio-worker-flush |
| stream03 | fs-jfs / ltp | FAILED | stream03 1 TFAIL : stream03.c:164: strlen(junk)=26: file pointer descrepancy 7 (pos=0) / stream03 2 TFAIL : stream03.c:175: Test failed in block0. / stream03 3 TFAIL : stream03.c:278: strlen(junk)=26: file pointer descrepancy 7 (opos=0) | g-ltp-stream-eio-worker-flush |
| stream04 | fs-jfs / ltp | FAILED | stream04 1 TFAIL : stream04.c:104: fread failed: Input/output error | g-ltp-stream-eio-worker-flush |
| stream05 | fs-jfs / ltp | FAILED | stream05 2 TFAIL : stream05.c:115: read did not read right number / stream05 3 TFAIL : stream05.c:119: read returned bad values / stream05 4 TFAIL : stream05.c:125: Test failed in block1. | g-ltp-stream-eio-worker-flush |
| ftest01 | fs-jfs / ltp | FAILED | ftest01 1 TFAIL : ftest01.c:343: Test[0]: read fail at 9800, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[1]: read fail at f4800, errno = 5. / ftest01 1 TFAIL : ftest01.c:343: Test[2]: read fail at 6a800, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest02 | fs-jfs / ltp | FAILED | ftest02 1 TBROK : ftest02.c:413: Test[0]: error 5 on read / ftest02 2 TBROK : ftest02.c:413: Remaining cases broken / ftest02 1 TBROK : ftest02.c:413: Test[3]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest03 | fs-jfs / ltp | FAILED | ftest03 1 TFAIL : ftest03.c:404: Test[0]: readv fail at b6000, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[1]: readv fail at 8e000, errno = 5. / ftest03 1 TFAIL : ftest03.c:404: Test[2]: readv fail at a7000, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest04 | fs-jfs / ltp | FAILED | ftest04 1 TFAIL : ftest04.c:327: Test[0]: readv fail at 64000, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[2]: readv fail at 3f800, errno = 5. / ftest04 1 TFAIL : ftest04.c:327: Test[3]: readv fail at a4000, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest05 | fs-jfs / ltp | FAILED | ftest05 1 TFAIL : ftest05.c:337: Test[0]: read fail at 86000: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[1]: read fail at 26800: errno=EIO(5): Input/output error / ftest05 1 TFAIL : ftest05.c:337: Test[2]: read fail at 68800: errno=EIO(5): Input/output error | g-ltp-ftest-eio-worker-flush |
| ftest06 | fs-jfs / ltp | FAILED | ftest06 1 TFAIL : ftest06.c:431: Test[2]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[0]: error 5 on read / ftest06 1 TFAIL : ftest06.c:431: Test[1]: error 5 on read | g-ltp-ftest-eio-worker-flush |
| ftest07 | fs-jfs / ltp | FAILED | ftest07 1 TFAIL : ftest07.c:399: Test[0]: readv fail at e3000, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[1]: readv fail at 88800, errno = 5. / ftest07 1 TFAIL : ftest07.c:399: Test[2]: readv fail at dc000, errno = 5. | g-ltp-ftest-eio-worker-flush |
| ftest08 | fs-jfs / ltp | FAILED | ftest08 1 TFAIL : ftest08.c:430: Test[0]: writev fail at e1000x xfr -1, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[2]: readv fail at 35800x, errno = 5. / ftest08 1 TFAIL : ftest08.c:340: Test[3]: readv fail at 83800x, errno = 5. | g-ltp-ftest-eio-worker-flush |
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
| ltp | 18 | 18 | 0 |

### Common root-cause groups

#### g-rustc-recursion-compile

- Model class: **unknown_failure**; confidence: **medium**
- Recommendation: Bisect commits between last passing daily compilation SHA and current main; add recursion_limit attributes or refactor async test helpers if product-side, or adjust toolchain settings if environment-specific.

#### g-ltp-ftest-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Review flush-only Running frame handling in curvine-worker/src/worker/handler/write_handler.rs from PR #1694; add ftest read/readv regression coverage on curvine-fuse.

#### g-ltp-lftest-eio-worker-flush

- Model class: **pre_existing_failure**; confidence: **high**
- Recommendation: Address alongside PR #1694 write_handler flush regression in issue #1701.

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


## Follow-up

### Defects and fixes

- GitHub Issue: [1701](https://github.com/CurvineIO/curvine/issues/1701) (open, reused)

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Report-only performance regressions still require human follow-up.

### Next actions

- Bisect commits between last passing daily compilation SHA and current main; add recursion_limit attributes or refactor async test helpers if product-side, or adjust toolchain settings if environment-specific.
- Review flush-only Running frame handling in curvine-worker/src/worker/handler/write_handler.rs from PR #1694; add ftest read/readv regression coverage on curvine-fuse.
- Address alongside PR #1694 write_handler flush regression in issue #1701.
- Re-test stream cases after worker flush fix in issue #1701.
- Re-test writetest after worker flush fix in issue #1701.
- Re-test inode02 after worker flush fix in issue #1701.
- Re-test fs_di after worker flush fix in issue #1701.
- Re-test fs_fill after worker flush fix in issue #1701.
- Rerun the full chain after fixes and require all release gates to pass.

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
