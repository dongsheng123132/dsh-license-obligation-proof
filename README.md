# dsh-license-obligation-proof

**Maintainer / Author：贺去病 (He Fangsheng / Dosen) · [hequbing.com](https://www.hequbing.com)**

Offline, deterministic evidence that every required compliance artifact for a **supplied** release decision was delivered: NOTICE, license text, source offer, source bundle, or modification notice. Inputs and reports contain hashes, obligation codes and bounded metadata only—never license bodies, copyright text, package source or secrets.

This is deliberately not another license scanner. [`dsh-license-guard`](https://github.com/uckkk/dsh-license-guard) already scans `node_modules`, normalizes SPDX identifiers and applies allow/deny policy. This plugin starts after scanning and expert review: it verifies that the declared component set, decisions, obligations, delivered artifact digests, distinct receipts and fresh zero-unresolved closure agree. It does not scan packages, normalize SPDX, interpret a license, or provide legal advice.

```sh
npm test
npm run check
node bin/dsh-license-obligation-proof.mjs verify examples/closed.json
```

DSH tools: `dsh_license_obligation_inspect` and `dsh_license_obligation_verify`. MCP exposes equivalent proof-only inline tools. Reports explicitly retain `provesComponentSetExhaustive: false` and `provesLegalCompliance: false`.

References: [SPDX License Expressions](https://spdx.github.io/spdx-spec/v2.3/SPDX-license-expressions/) and [OpenChain ISO/IEC 5230](https://openchainproject.org/license-compliance).

MIT licensed.
