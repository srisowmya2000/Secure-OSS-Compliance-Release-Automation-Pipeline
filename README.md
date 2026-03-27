# Secure OSS Compliance Pipeline

A secure DevSecOps CI/CD pipeline that automatically generates SBOMs, performs SAST/SCA/DAST checks, detects risky open-source licenses, and blocks releases using policy-as-code gates.

This project demonstrates how to **bake security and compliance into the software delivery lifecycle** so that every commit is checked before it becomes a release.

---

## 🚀 Why this project exists

Modern software pipelines do more than build code — they also need to verify:

- **Secrets are not accidentally committed**
- **Code does not contain insecure patterns**
- **Dependencies are visible and auditable**
- **Container images are free from critical vulnerabilities**
- **Open-source licenses are safe for commercial or closed-source use**
- **Releases are blocked when policy violations are detected**

This repository provides a practical reference implementation for **secure software supply chain controls** in CI/CD.

---

## 🧠 What this pipeline does

Every time a developer pushes code, the pipeline acts as a **security guard + compliance gate** for the application.

It automatically:

- Runs **secret scanning**
- Performs **static code analysis**
- Builds the application container
- Generates an **SBOM** (Software Bill of Materials)
- Scans the image for **vulnerabilities**
- Detects **license risks** (MIT / Apache / GPL / etc.)
- Enforces **policy-as-code rules**
- Performs **baseline DAST** against the running application
- Fails the build if critical risk or disallowed licenses are found

If all checks pass, the release can continue safely.

---

## 📸 Pipeline Architecture

<img width="2062" height="1690" alt="image" src="https://github.com/user-attachments/assets/406231b8-7464-4bf1-b5cf-6ac3ba39c4bf" />

---

## 🎯 Goals

- Continuous **SAST / SCA / DAST** with release gates
- **SBOM generation** on every build
- **License risk detection** for open-source dependencies
- **Policy-based build blocking** for critical issues
- **Auditability** with machine-readable security artifacts
- Foundation for **REST API + dashboard visibility per commit/release**

---

## 🔍 Problem Statement / Case Study

Security and license compliance are often treated as manual, late-stage checks.

That creates problems such as:

- vulnerable dependencies reaching production
- GPL-style license conflicts in proprietary products
- missing visibility into what ships in a release
- poor auditability for security reviews
- delayed remediation after release

This project demonstrates a **shift-left, auditable release pipeline** that gives developers early, actionable feedback and prevents unsafe builds from moving forward.

---

## ⚙️ Pipeline Stages

This pipeline includes **three core stages**:

1. **Static Scan**
2. **Build + Supply Chain Scan**
3. **DAST Scan**

---

## 🛡️ Stage 1: Static Scan

### 1. Gitleaks
Detects secrets accidentally committed into source code, such as:

- API keys
- passwords
- tokens
- private credentials

**Why it matters:** prevents secret leakage early in the pipeline.

### 2. Semgrep
Performs static code analysis to detect insecure coding patterns.

Examples:
- hardcoded credentials
- weak validation
- dangerous function usage
- insecure framework patterns

**Why it matters:** catches application security issues before build and release.

---

## 📦 Stage 2: Build + Supply Chain Security

### 1. Docker Build
Builds the application into a container image.

**Why it matters:** creates a consistent runtime artifact and eliminates "works on my machine" drift.

### 2. Syft
Generates an **SBOM (Software Bill of Materials)** for the application image.

Supported formats can include:
- SPDX
- CycloneDX

**Why it matters:** gives visibility into every package and dependency shipped in the release.

### 3. Trivy
Scans the built image for:

- known CVEs
- vulnerable packages
- license issues
- misconfigurations (if configured)

**Why it matters:** identifies both security and compliance risks in the release artifact.

### 4. Conftest + OPA
Enforces **policy-as-code** gates.

Examples:
- fail the build if critical CVEs are present
- fail the build if disallowed licenses are detected
- require mandatory security artifacts before release

**Why it matters:** turns security/compliance from "advice" into **enforceable release policy**.

---

## 🌐 Stage 3: DAST Scan

### OWASP ZAP (Baseline Scan)
Runs a baseline dynamic scan against the running application.

Checks may include:
- missing security headers
- basic injection indicators
- common web security weaknesses
- low-hanging misconfigurations

**Why it matters:** validates the running app, not just the source code or container.

---

## 📚 Why SBOM + License Checks Matter

Generating an SBOM on every build is useful because it creates a **machine-readable inventory** of what is actually shipped.

This enables:

- faster incident response during supply-chain events
- dependency transparency
- easier vulnerability triage
- license compliance review
- stronger audit readiness

License checks matter because not all open-source licenses are equal.

Examples:
- **MIT / Apache-2.0** → generally permissive
- **GPL family** → may introduce obligations that are risky for closed-source or commercial distribution

This pipeline helps catch those issues **before release**, not after legal or compliance review.

---

## 🔒 Why this project matters

This project is designed around three real-world DevSecOps principles:

### 1. Shift Security Left
Developers get feedback early, directly in CI/CD.

### 2. Enforce Policy Automatically
Critical risk should block releases automatically — not rely on manual review every time.

### 3. Preserve Auditability
Every decision can produce artifacts that are:

- searchable
- reviewable
- repeatable
- suitable for governance and compliance workflows

---

## 🧰 Tooling Used

- **Gitleaks** → secret scanning
- **Semgrep** → SAST
- **Docker** → build artifact creation
- **Syft** → SBOM generation
- **Trivy** → vulnerability + license scanning
- **Conftest / OPA** → policy-as-code enforcement
- **OWASP ZAP** → baseline DAST

---

## 🏗️ Example Workflow

```text
Code Push
   ↓
Gitleaks (secrets)
   ↓
Semgrep (SAST)
   ↓
Docker Build
   ↓
Syft (SBOM generation)
   ↓
Trivy (CVE + license scan)
   ↓
Conftest / OPA (policy gate)
   ↓
Run App
   ↓
OWASP ZAP Baseline (DAST)
   ↓
Pass → Continue Release
Fail → Block Build / Require Review




































