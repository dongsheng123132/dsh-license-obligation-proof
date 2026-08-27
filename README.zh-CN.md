# dsh-license-obligation-proof

离线、确定性的许可证义务闭合证据层：核验 supplied 发布决策要求的 NOTICE、许可证文本、源码提供、源码包或修改说明是否逐项交付。输入和报告只保留哈希、义务代码与有界元数据，不包含许可证正文、版权文字、包源码或秘密。

它不是第二个许可证扫描器。`dsh-license-guard` 已扫描 `node_modules`、归一化 SPDX 并执行 allow/deny 门禁；本插件从扫描与专家判断之后开始，只复算组件全集、决策、义务、交付制品哈希、独立回执和新鲜零未结闭合。它不扫描、不解释许可证，也不提供法律意见。

DSH 工具为 `dsh_license_obligation_inspect` 与 `dsh_license_obligation_verify`，MCP 提供等价的只验证工具。报告明确保留 `provesComponentSetExhaustive: false` 与 `provesLegalCompliance: false`。
