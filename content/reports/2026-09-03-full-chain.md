---
title: "Curvine full-chain daily test report - 2026-09-03"
linkTitle: "2026-09-03 full-chain"
date: 2026-09-03T00:00:00Z
weight: -20260903
tags: [full-chain, daily, no-go]
---

## Quality conclusion

### Executive summary

> [!CAUTION]
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 5 passed, 2 failed.

Blocking failures remain on daily and fuse. Finish attribution, fix, and targeted regression, then rerun the full-chain tests.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 5/7 passed | FAIL |
| Failure attribution | Failures classified | 2 failures | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failures are attributed to flaky coverage orchestration and an external git clone network error, not to demonstrated stable product regressions.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 12m 02s | passed | passed |
| integration | PASS | PASS | 11m 56s | passed | passed |
| daily | PASS | FAIL | 17m 07s | flaky | passed |
| fuse | PASS | FAIL | 6m 20s | environment_failure | passed |
| ltp | PASS | PASS | 49m 55s | passed | passed |
| csi | PASS | PASS | 0m 35s | passed | passed |
| perf-benchmark | NOT_RECORDED | PASS | 3m 57s | failed | passed |

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
| Create file | 23458.88 ops/s | 1.70 ms/op | 2.05 | 4.09 | 4.09 | 4.93 | 200000 | 0 | pass |
| Stat file | 70410.55 ops/s | 0.57 ms/op | 1.02 | 1.02 | 1.02 | 3.23 | 200000 | 0 | pass |
| Open file | 68937.42 ops/s | 0.58 ms/op | 1.02 | 1.02 | 1.02 | 2.29 | 200000 | 0 | pass |
| Rename file | 34447.82 ops/s | 1.15 ms/op | 2.05 | 3.75 | 3.75 | 3.75 | 200000 | 0 | pass |
| Delete file | 34447.86 ops/s | 1.15 ms/op | 2.05 | 4.09 | 4.09 | 4.79 | 200000 | 0 | pass |

#### FIO read/write (this run)

| ITEM | SPEED GiB/s | IOPS | AVG COST | P50 ms | P95 ms | P99 ms | MAX ms | SAMPLES | ERRORS | Status |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Sequential write 64KB | 1.73 | 28373.63 | 8.78 ms/op | 8.72 | 10.16 | 10.94 | 17.53 | 262144 | 0 | pass |
| Sequential read 64KB | 2.31 | 37914.96 | 6.22 ms/op | 5.80 | 10.94 | 12.91 | 24.72 | 262144 | 0 | pass |
| Random write 64KB | 1.81 | 29637.54 | 8.36 ms/op | 8.16 | 9.37 | 10.16 | 295.84 | 262144 | 0 | pass |
| Random read 64KB | 1.13 | 18526.08 | 13.47 ms/op | 13.30 | 16.71 | 18.74 | 76.59 | 262144 | 0 | pass |
| Sequential write 256KB | 2.81 | 11511.68 | 20.79 ms/op | 22.68 | 30.80 | 35.39 | 43.70 | 65536 | 0 | pass |
| Sequential read 256KB | 2.92 | 11963.49 | 19.68 ms/op | 21.63 | 26.35 | 29.49 | 60.05 | 65536 | 0 | pass |
| Random write 256KB | 2.52 | 10322.26 | 23.55 ms/op | 21.10 | 26.61 | 30.28 | 927.48 | 65536 | 0 | pass |
| Random read 256KB | 2.42 | 9892.23 | 24.97 ms/op | 24.77 | 30.28 | 33.42 | 46.11 | 65536 | 0 | pass |
| Sequential write 1MB | 3.65 | 3735.52 | 58.80 ms/op | 58.46 | 135.27 | 206.57 | 325.07 | 16384 | 0 | pass |
| Sequential read 1MB | 2.83 | 2894.19 | 79.60 ms/op | 88.60 | 101.19 | 104.33 | 187.22 | 16384 | 0 | pass |
| Random write 1MB | 3.03 | 3105.97 | 75.31 ms/op | 71.83 | 104.33 | 346.03 | 578.14 | 16384 | 0 | fail |
| Random read 1MB | 2.18 | 2227.60 | 110.51 ms/op | 111.67 | 125.30 | 131.60 | 205.51 | 16384 | 0 | pass |

## Failures and attribution

### Failure analysis

#### daily

- Goal: Daily unit tests and coverage collection
- Expected: All unit tests pass and coverage data is collected
- Actual: All 1440 nextest tests passed, but coverage collection timed out during llvm-cov rerun; one cluster-readiness timeout occurred in the coverage subprocess
- Impact: Blocks the full-chain quality gate
- Class: **flaky**
- Failure layer: **test**
- Root-cause confidence: medium
- Cleanup: **passed**
- Next step: Increase coverage timeout or retry on transient cluster readiness failures

#### fuse

- Goal: FUSE mount, file I/O, and FIO regression
- Expected: Mount is readable/writable; functional regression passes
- Actual: 53 of 54 FUSE tests passed; Test 16 git clone failed with HTTPS SSL read error
- Impact: Blocks the full-chain quality gate
- Class: **environment_failure**
- Failure layer: **test**
- Root-cause confidence: high
- Cleanup: **passed**
- Next step: Retry or mirror git clone when outbound HTTPS is unstable

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| daily profile | daily / daily | FAIL | profile failed | g-daily-coverage-timeout |
| fuse | fuse / fuse | FAIL | status failed | g-fuse-git-clone-network |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| daily | 1 | 0 | +1 | Profile-level failure after all named tests passed |
| fuse | 1 | 1 | +0 | Counts match |

### Common root-cause groups

Attribution coverage: **2/2 (100.0%)**.

#### P1 g-daily-coverage-timeout

- Profiles: daily
- Hypothesis: Coverage orchestration timed out while llvm-cov reran tests; intermittent MiniCluster readiness failure during coverage subprocess
- Recommendation: Increase coverage timeout; retry coverage on transient cluster readiness failures
- Unique logical failures: 1
- Model class: **flaky**; confidence: **medium**; Issue: **none**
- Verification: Daily profile completes ut-coverage with coverage output and exit 0
- daily profile (daily): profile failed

#### P1 g-fuse-git-clone-network

- Profiles: fuse
- Hypothesis: External HTTPS git clone failed with SSL EOF; FUSE filesystem tests otherwise passed
- Recommendation: Retry git clone or use a local mirror for Test 16 when outbound GitHub access is unstable
- Unique logical failures: 1
- Model class: **environment_failure**; confidence: **high**; Issue: **none**
- Verification: Fuse profile passes Test 16 when HTTPS to GitHub is stable
- fuse (fuse): status failed

### All failed cases

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| daily profile | daily / daily | FAIL | profile failed | g-daily-coverage-timeout |
| fuse | fuse / fuse | FAIL | status failed | g-fuse-git-clone-network |

## Follow-up

### Defects and fixes

- GitHub Issue: **not_required**
- GitHub PR: **pending_fix_review**

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Perf random write 1MB exceeded latency baseline ratio; gate is report-only.

### Next actions

| Priority | Role | Action | Done when |
| --- | --- | --- | --- |
| P0 | daily-owner | Stabilize coverage collection on the ordinary runner | daily profile passes with coverage collected |
| P0 | fuse-owner | Harden git clone test against transient network errors | fuse profile passes including Test 16 |
| P1 | perf-owner | Review random write 1MB latency vs baseline | Perf gate reviewed or baseline updated |
