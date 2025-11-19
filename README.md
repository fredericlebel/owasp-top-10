# owasp-top-10

[![Tests](https://github.com/fredericlebel/owasp-top-10/actions/workflows/tests.yml/badge.svg)](https://github.com/fredericlebel/owasp-top-10/actions/workflows/tests.yml)

code owasp-top-10-2025-labs.code-workspace

## 📊 Matrice globale — OWASP Top 10 (2025)

Cette matrice reflète l’avancement des PoC vulnérables et sécurisés pour chaque CWE lié à l’OWASP Top 10:2025.

---

### 🟥 A01 — Broken Access Control
| CWE                                                          | PoC                                                                                                          | Nom                                                        | Vulnérable | Sécurisé | Tests |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- | ---------- | -------- | ----- |
| [CWE‑22](https://cwe.mitre.org/data/definitions/22.html)     | [PoC](./a01-broken-access-control/cwe-22-path-traversal-flask/)                                              | Path Traversal                                             | ✅          | ✅        | ✅     |
| [CWE‑200](https://cwe.mitre.org/data/definitions/200.html)   | [PoC](./a01-broken-access-control/cwe-200-exposure-of-sensitive-information-to-an-unauthorized-actor-flask/) | Exposure of Sensitive Information to an Unauthorized Actor | ❌          | ❌        | ❌     |
| [CWE‑639](https://cwe.mitre.org/data/definitions/639.html)   | [PoC](./a01-broken-access-control/cwe-639-authorization-bypass-through-user-controlled-key-flask/)           | Authorization Bypass Through User-Controlled Key           | ❌          | ❌        | ❌     |
| [CWE-1275](https://cwe.mitre.org/data/definitions/1275.html) | [PoC](./a01-broken-access-control/cwe-1275-sensitive-cookie-with-improper-samesite-attribute-flask/)         | Sensitive Cookie with Improper SameSite Attribute          | ❌          | ❌        | ❌     |