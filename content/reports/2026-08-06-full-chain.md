---
title: "Curvine 全链路每日测试报告 - 2026-08-06"
date: 2026-08-06T00:00:00Z
tags: [full-chain, daily, no-go]
---

# Curvine 全链路每日测试报告 - 2026-08-06

## 质量结论

### 执行摘要

> 发布决策：**NO-GO**。流水线结果 **FAIL**；执行 7 个 profile，6 个通过，1 个失败。

存在阻断性失败，当前提交不得作为可发布版本；需完成归因、修复和定向回归后重新执行全链路测试。

### 质量门禁

|门禁|标准|实际|结论|
|:----|:----|:----|:----|
|全链路结果|所有必跑 profile 通过|6/7 通过|FAIL|
|失败归因|失败项已分类|1 个失败|待逐项确认|
|资源清理|所有 profile cleanup 成功|7/7|PASS|

### 结论

本次全链路测试未通过，按失败分类进入产品修复、Harness 修复或环境治理。

未完成归因的 profile：fuse。

## 测试结果

### Profile 汇总

|Profile|Preflight|结果|耗时|分类|Cleanup|
|:----|:----|:----|:----|:----|:----|
|fast|PASS|PASS|1m 35s|passed|passed|
|integration|PASS|PASS|6m 08s|passed|passed|
|daily|PASS|PASS|13m 31s|passed|passed|
|ltp|PASS|PASS|48m 03s|passed|passed|
|csi|PASS|PASS|0m 35s|passed|passed|
|perf-benchmark|NOT_RECORDED|PASS|2m 04s|failed|passed|
|fuse|PASS|FAIL|2m 56s|unknown_failure|passed|

### LTP

* 状态：`completed`
* 已完成 suite：7
* 待运行 suite：0
* 测试统计：1129 passed / 0 real failed / 141 skipped / 0 report-consistency errors

|Suite|状态|Passed|Real failed|Skipped|Report errors|Return code|
|:----|:----|:----|:----|:----|:----|:----|
|fs_perms_simple|passed|18|0|0|0|0|
|fsx|passed|1|0|0|0|0|
|fs_bind|passed|1|0|0|0|0|
|smoketest|passed|12|0|1|0|0|
|io|passed|2|0|0|0|0|
|fs-jfs|passed|27|0|2|0|0|
|syscalls-jfs|passed|1068|0|138|0|0|

#### 失败与异常用例

未解析到 TFAIL/TBROK。

### 性能基准

> 门禁策略：**仅报告，不阻断** 全链路结果；低于 baseline 时标黄/标红供人工跟进。

* 状态：`failed`
* 门禁模式：`report_only`

#### 元数据性能（本次）

|ITEM|VALUE|AVG COST|P50(ms)|P95(ms)|P99(ms)|MAX(ms)|SAMPLES|ERRORS|状态|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|Create file|21392.01 ops/s|1.86 ms/op|2.05|4.09|4.09|162.66|200000|0|pass|
|Stat file|63836.79 ops/s|0.62 ms/op|1.02|1.02|2.05|2.59|200000|0|pass|
|Open file|63916.00 ops/s|0.62 ms/op|1.02|1.02|2.05|2.43|200000|0|pass|
|Rename file|29170.42 ops/s|1.36 ms/op|2.05|4.09|4.09|5.01|200000|0|pass|
|Delete file|29501.85 ops/s|1.35 ms/op|2.05|4.09|4.09|4.28|200000|0|pass|

#### FIO 读写性能（本次）

|ITEM|SPEED(GiB/s)|IOPS|AVG COST|P50(ms)|P95(ms)|P99(ms)|MAX(ms)|SAMPLES|ERRORS|状态|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|Sequential write (64KB)|1.70|27840.27|9.00 ms/op|8.98|10.55|11.47|18.43|262144|0|pass|
|Sequential read (64KB)|2.38|39044.38|6.13 ms/op|5.73|10.55|12.39|20.34|262144|0|pass|
|Random write (64KB)|1.77|28950.19|8.57 ms/op|8.36|9.63|10.55|294.08|262144|0|pass|
|Random read (64KB)|1.08|17776.09|13.49 ms/op|13.30|16.91|20.05|50.87|262144|0|pass|
|Sequential write (256KB)|2.71|11094.63|21.05 ms/op|22.41|33.42|39.58|57.34|65536|0|pass|
|Sequential read (256KB)|2.53|10361.42|22.97 ms/op|25.03|28.44|30.02|52.41|65536|0|degraded|
|Random write (256KB)|2.58|10585.69|22.49 ms/op|21.63|28.18|31.33|440.01|65536|0|pass|
|Random read (256KB)|2.38|9765.46|25.30 ms/op|25.30|30.54|33.82|49.95|65536|0|pass|
|Sequential write (1MB)|3.12|3196.25|68.41 ms/op|59.51|156.24|265.29|352.43|16384|0|fail|
|Sequential read (1MB)|2.93|2996.34|77.47 ms/op|85.46|99.09|103.28|132.46|16384|0|pass|
|Random write (1MB)|2.97|3044.22|78.36 ms/op|73.92|112.72|274.73|529.95|16384|0|degraded|
|Random read (1MB)|2.26|2314.78|105.69 ms/op|106.43|119.01|126.35|187.02|16384|0|pass|

#### 元数据性能基准

|ITEM|VALUE|AVG COST|P50(ms)|P95(ms)|P99(ms)|MAX(ms)|SAMPLES|ERRORS|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|Create file|21668.74 ops/s|1.84 ms/op|2.05|4.09|4.09|188.88|200000|0|
|Stat file|63487.48 ops/s|0.63 ms/op|1.02|1.02|2.05|2.57|200000|0|
|Open file|63113.20 ops/s|0.63 ms/op|1.02|1.02|2.05|2.53|200000|0|
|Rename file|30314.48 ops/s|1.31 ms/op|2.05|4.09|4.09|5.58|200000|0|
|Delete file|31231.33 ops/s|1.27 ms/op|2.05|4.09|4.09|4.89|200000|0|

#### FIO 读写性能基准

|ITEM|SPEED(GiB/s)|IOPS|AVG COST|P50(ms)|P95(ms)|P99(ms)|MAX(ms)|SAMPLES|ERRORS|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|Sequential write (64KB)|1.71|28084.85|8.89 ms/op|8.85|10.29|10.94|16.58|262144|0|
|Sequential read (64KB)|2.28|37433.10|6.31 ms/op|5.87|10.81|12.78|25.90|262144|0|
|Random write (64KB)|1.77|29011.07|8.48 ms/op|8.29|9.50|10.29|274.42|262144|0|
|Random read (64KB)|1.12|18325.34|13.46 ms/op|13.30|16.91|19.53|57.97|262144|0|
|Sequential write (256KB)|2.73|11187.44|20.83 ms/op|22.41|31.85|36.44|66.49|65536|0|
|Sequential read (256KB)|3.11|12750.19|17.71 ms/op|19.01|23.99|26.08|61.98|65536|0|
|Random write (256KB)|2.51|10267.27|23.24 ms/op|20.84|26.87|30.28|985.88|65536|0|
|Random read (256KB)|2.37|9700.41|25.17 ms/op|25.03|30.54|34.34|67.33|65536|0|
|Sequential write (1MB)|3.45|3530.27|62.65 ms/op|60.03|145.75|191.89|422.44|16384|0|
|Sequential read (1MB)|2.72|2784.50|85.32 ms/op|93.85|105.38|108.53|165.07|16384|0|
|Random write (1MB)|3.09|3164.16|74.79 ms/op|72.88|105.38|229.64|481.01|16384|0|
|Random read (1MB)|2.15|2202.15|111.52 ms/op|112.72|127.40|135.27|220.57|16384|0|

## 失败与归因

### 失败分析

#### fuse

* 测试目标：FUSE 挂载、文件 I/O 与 FIO 回归
* 预期结果：挂载可读写，I/O 语义正确且无 EIO
* 实际结果：exit code `40`；持续或预分配写入出现 EIO/ENOSPC，容量查询仍显示有空闲空间
* 业务影响：阻断全链路质量门禁；归因完成前不可宣称该能力可用
* 分类：`unknown_failure`
* 失败层：`test`
* 根因置信度：低
* Cleanup：`passed`
* 下一步：由 fuse-owner 完成归因；确认产品回归后建 Issue，修复并审查通过后再提 PR

### 失败用例摘要

正文展示 6/6 条；全量见「全部失败用例」。

|用例|Suite/Package|状态|关键错误|根因组|
|:----|:----|:----|:----|:----|
|FIO Sequential Write Test (256KB blocks)|fio / fuse|FAIL|FIO Sequential Write test failed|g-fuse-write-eio|
|FIO Sequential Read Test (256KB blocks)|fio / fuse|FAIL|FIO Sequential Read test failed|g-fuse-write-eio|
|FIO Random Write Test (256KB blocks)|fio / fuse|FAIL|FIO Random Write test failed|g-fuse-write-eio|
|FIO Random Read Test (256KB blocks)|fio / fuse|FAIL|FIO Random Read test failed|g-fuse-write-eio|
|FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write)|fio / fuse|FAIL|FIO Mixed Random Read/Write test failed|g-fuse-write-eio|
|fuse|fuse / fuse|FAILED|status failed|g-fuse-write-eio|

### 失败用例对账

|Profile|报告失败数|源失败数|差异|解释|
|:----|:----|:----|:----|:----|
|fuse|6|6|+0|数量一致|

### 共性根因组

归因覆盖率：**6/6（100.0%）**。无证据前不做预聚类。

#### [P1] g-fuse-write-eio

* Profiles：fuse
* 根因语义：假设 FUSE 或后端存储在持续写入、预分配写入时返回 EIO/ENOSPC；worker/master 错误日志尚未定位到具体子系统，置信度中等
* 建议：对齐首次 FIO EIO 与 fallocate ENOSPC 的时间点，核对 worker/master ERROR，并追踪 FUSE 写路径与块分配
* 唯一逻辑失败：6
* 模型分类：`unknown_failure`；置信度：`medium`；Issue：`needs_human`
* 验证方案：修复后重跑 fuse profile，下列用例及 fallocate、大文件 dd 均应无 EIO/ENOSPC
* `FIO Sequential Write Test (256KB blocks)`（fuse）：FIO Sequential Write test failed
* `FIO Sequential Read Test (256KB blocks)`（fuse）：FIO Sequential Read test failed
* `FIO Random Write Test (256KB blocks)`（fuse）：FIO Random Write test failed
* `FIO Random Read Test (256KB blocks)`（fuse）：FIO Random Read test failed
* `FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write)`（fuse）：FIO Mixed Random Read/Write test failed

### 全部失败用例

不截断。

|用例|Suite/Package|状态|关键错误|根因组|
|:----|:----|:----|:----|:----|
|FIO Sequential Write Test (256KB blocks)|fio / fuse|FAIL|FIO Sequential Write test failed|g-fuse-write-eio|
|FIO Sequential Read Test (256KB blocks)|fio / fuse|FAIL|FIO Sequential Read test failed|g-fuse-write-eio|
|FIO Random Write Test (256KB blocks)|fio / fuse|FAIL|FIO Random Write test failed|g-fuse-write-eio|
|FIO Random Read Test (256KB blocks)|fio / fuse|FAIL|FIO Random Read test failed|g-fuse-write-eio|
|FIO Mixed Random Read/Write Test (256KB blocks, 70% read, 30% write)|fio / fuse|FAIL|FIO Mixed Random Read/Write test failed|g-fuse-write-eio|
|fuse|fuse / fuse|FAILED|status failed|g-fuse-write-eio|

## 闭环

### 缺陷与修复

* GitHub Issue：`needs_human`
* GitHub PR：`pending_fix_review`

闭环标准：Issue 含复现步骤、预期/实际、影响、验收；PR 仅在修复、测试和审查通过后创建，并关联 Issue。

### 风险

* 局部 profile 通过不能替代全链路 NO-GO。
* 未完成归因的 profile：fuse。文中原因仅为待验证假设。

### 后续行动

|优先级|角色|行动|完成标准|
|:----|:----|:----|:----|
|P0|fuse-owner|完成归因、建 Issue、修复并定向回归|`fuse` 通过，Issue/PR 完整|
|P0|测试负责人|重跑全链路并更新报告|必跑 profile 全部通过|
