---
title: "Curvine full-chain daily test report - 2026-09-06"
linkTitle: "2026-09-06 full-chain"
date: 2026-09-06T00:00:00Z
weight: -20260906
tags: [full-chain, daily, no-go]
---

## Quality conclusion

Release decision: **NO-GO**. Pipeline result: **FAIL**.

## Profile summary

| Profile | Result | Duration | Cleanup |
| --- | --- | --- | --- |
| fast | PASS | 1m 52s | PASSED |
| integration | PASS | 10m 58s | PASSED |
| daily | FAIL | 16m 55s | PASSED |
| fuse | FAIL | 2m 38s | PASSED |
| ltp | PASS | 48m 43s | PASSED |
| csi | PASS | 0m 35s | PASSED |
| perf-benchmark | PASS | 2m 07s | PASSED |

## Performance baseline comparison

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

## Failed cases

- daily profile
- FIO Sequential Write Test (256KB blocks)
- FIO Sequential Read Test (256KB blocks)
- FIO Random Write Test (256KB blocks)
- FIO Random Read Test (256KB blocks)
- FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write)
- fuse

## Publication note

This public report contains only sanitized test outcomes. Private execution evidence remains internal.
