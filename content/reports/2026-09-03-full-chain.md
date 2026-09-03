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
> Release decision: **NO-GO**. Pipeline **FAIL**; ran 7 profiles, 4 passed, 3 failed.

A blocking failure exists. This revision is not releasable. Finish attribution, fix, and targeted regression, then rerun the full-chain tests.

### Quality gates

| Gate | Criterion | Actual | Verdict |
| --- | --- | --- | --- |
| Full-chain result | All required profiles passed | 4/7 passed | FAIL |
| Failure attribution | Failures classified | 3 profiles, 9 cases | PASS |
| Resource cleanup | All profile cleanups succeeded | 7/7 | PASS |

### Conclusion

This full-chain run did not pass. Failures are attributed to environment isolation and test orchestration timing, not confirmed product regressions.

## Test results

### Profile summary

| Profile | Preflight | Result | Duration | Class | Cleanup |
| --- | --- | --- | --- | --- | --- |
| fast | PASS | PASS | 11m 58s | passed | passed |
| integration | PASS | FAIL | 12m 00s | environment_failure | passed |
| daily | PASS | FAIL | 17m 13s | environment_failure | passed |
| fuse | PASS | FAIL | 3m 51s | harness_failure | passed |
| ltp | PASS | PASS | 50m 48s | passed | passed |
| csi | PASS | PASS | 0m 35s | passed | passed |
| perf-benchmark | NOT_RECORDED | PASS | 1m 52s | skipped | passed |

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

- Status: **skipped**
- Gate mode: **report_only**

## Failures and attribution

### Failure analysis

#### integration and daily

- Goal: Server and client integration plus daily unit and coverage regression
- Expected: All nextest cases pass with isolated configuration
- Actual: Four unit tests failed in both profiles with hostname and block-store assertion errors
- Impact: Blocks the full-chain quality gate for ordinary-runner profiles
- Class: **environment_failure**
- Failure layer: **test**
- Root-cause confidence: high
- Cleanup: **passed**
- Next step: Unset hostname override env vars in the ordinary runner or clear them inside affected unit tests

#### fuse

- Goal: FUSE mount, file I/O, and FIO regression
- Expected: FIO and FUSE regression complete after cluster restart
- Actual: FIO preparation skipped because the mount was not ready within 10 seconds; all 55 FUSE regression checks passed afterward
- Impact: Profile marked failed even though FUSE functional tests were green
- Class: **harness_failure**
- Failure layer: **test**
- Root-cause confidence: high
- Cleanup: **passed**
- Next step: Align FIO mount wait with the FUSE phase or do not fail the profile when only FIO prep times out

### Failed case summary

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| cluster_conf::tests::trims_whitespace_in_hostname_config | lib / curvine-config | FAILED | assertion left equals right failed | g-config-hostname-env |
| tests::get_conf_loads_from_discovered_config | bin/curvine-server / curvine-server | FAILED | assertion left equals right failed | g-config-hostname-env |
| worker::block::block_store::tests::remove_deallocate_error_keeps_block_for_retry | lib / curvine-worker | FAILED | assertion failed result is_err | g-block-store-root-tests |
| worker::block::block_store::tests::async_remove_deallocate_error_keeps_block_for_retry | lib / curvine-worker | FAILED | assertion failed result is_err | g-block-store-root-tests |
| fuse profile | fuse / fuse | FAILED | profile failed after FIO skipped | g-fuse-fio-mount-timeout |

### Failed case reconciliation

| Profile | Reported failures | Source failures | Delta | Notes |
| --- | ---: | ---: | ---: | --- |
| integration | 4 | 4 | +0 | Counts match |
| daily | 4 | 4 | +0 | Counts match |
| fuse | 1 | 0 | +1 | FIO stage failure counted as profile failure while named FUSE cases passed |

### Common root-cause groups

Attribution coverage: **9/9 (100.0%)**.

#### P1 g-config-hostname-env

- Profiles: integration, daily
- Hypothesis: CURVINE_MASTER_HOSTNAME from the test runner overwrites TOML hostname values during config load
- Recommendation: Unset hostname override env vars in the ordinary nextest profile or clear them inside affected unit tests
- Unique logical failures: 2
- Model class: **environment_failure**; confidence: **high**; Issue: **none**
- Verification: Hostname config unit tests pass with CURVINE_MASTER_HOSTNAME unset
- cluster_conf::tests::trims_whitespace_in_hostname_config (integration, daily): assertion left equals right failed
- tests::get_conf_loads_from_discovered_config (integration, daily): assertion left equals right failed

#### P1 g-block-store-root-tests

- Profiles: integration, daily
- Hypothesis: Block store tests rely on chmod permission denial that root bypasses in the ordinary runner
- Recommendation: Mock deallocate failure or skip chmod-based tests when running as root
- Unique logical failures: 2
- Model class: **environment_failure**; confidence: **high**; Issue: **none**
- Verification: Block store retry tests pass when permission denial is effective or tests are skipped for root
- worker::block::block_store::tests::remove_deallocate_error_keeps_block_for_retry (integration, daily): assertion failed result is_err
- worker::block::block_store::tests::async_remove_deallocate_error_keeps_block_for_retry (integration, daily): assertion failed result is_err

#### P1 g-fuse-fio-mount-timeout

- Profiles: fuse
- Hypothesis: FIO prep aborts on a 10 second mount wait while FUSE regression passes after mount becomes ready
- Recommendation: Increase FIO mount wait or decouple profile status from skipped FIO when FUSE tests pass
- Unique logical failures: 1
- Model class: **harness_failure**; confidence: **high**; Issue: **none**
- Verification: Fuse profile completes with FIO executed or passes when only FIO prep times out and FUSE regression is green
- fuse profile (fuse): profile failed after FIO skipped

### All failed cases

| Case | Suite / Package | Status | Key error | Root group |
| --- | --- | --- | --- | --- |
| cluster_conf::tests::trims_whitespace_in_hostname_config | lib / curvine-config | FAILED | assertion left equals right failed | g-config-hostname-env |
| tests::get_conf_loads_from_discovered_config | bin/curvine-server / curvine-server | FAILED | assertion left equals right failed | g-config-hostname-env |
| worker::block::block_store::tests::remove_deallocate_error_keeps_block_for_retry | lib / curvine-worker | FAILED | assertion failed result is_err | g-block-store-root-tests |
| worker::block::block_store::tests::async_remove_deallocate_error_keeps_block_for_retry | lib / curvine-worker | FAILED | assertion failed result is_err | g-block-store-root-tests |
| fuse profile | fuse / fuse | FAILED | profile failed after FIO skipped | g-fuse-fio-mount-timeout |

## Follow-up

### Defects and fixes

- GitHub Issue: **not_required**
- GitHub PR: **not_required**

### Risks

- A subset of green profiles does not override a full-chain NO-GO.
- Environment and orchestration fixes are still required before release.

### Next actions

| Priority | Role | Action | Done when |
| --- | --- | --- | --- |
| P0 | test-owner | Fix ordinary-runner env isolation for hostname and root-sensitive unit tests | integration and daily profiles pass |
| P0 | test-owner | Fix FIO mount wait orchestration in the fuse profile | fuse profile passes with FIO executed or correctly classified |
| P0 | test-owner | Rerun the full chain and update the report | All required profiles pass |
