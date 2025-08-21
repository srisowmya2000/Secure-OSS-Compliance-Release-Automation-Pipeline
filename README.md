# Secure-OSS-Compliance-Release-Automation-Pipeline
Summary: 
Every time you push code, the pipeline acts as a security guard + health inspector for your app. This repository contains a sample secure CI/CD pipeline that shows how to “bake in” security and compliance checks automatically whenever code changes are pushed.

Goals:
Continuous SAST/SCA/DAST with policy gates.
SBOM (SPDX + CycloneDX) generated on every build.
License risk detection (GPL vs. MIT/Apache) and developer guidance.
REST API + dashboard so teams can see risks per commit/release.

Case study & problem statement : 
Automate the auditable platform that shifts security and license compliance left, giving developers early, actionable feedback, and gates releases on critical risks.


Pipeline description: 
In this pipeline, three jobs are performed: the static scan, build scan, and DAST scan. 

Static Scan: 
1. Used Gitleaks,  which finds secrets in code like API keys or passwords accidentally committed.
2. Used Semgrep -- scans the code for insecure patterns.

Build Scan: 
1. Docker build -- turns app into container image and solves problems like " IT works on my computer fine"
2. Syft tools used to generate an SBOM, a recipe card which lists every library inside your app.
3. The Trivy tool is used, which scans the image for known vulnerabilities, license issues.
4. Conftest(OPA) is used to enforce rules like if we found any CVE's it stops the build process and fails the build if disallowed licenses are present.

DAST test:
1. OWASP ZAP (baseline scan) checks the running app for common web vulnerabilities (missing security headers, simple injection issues).






