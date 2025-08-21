# Secure Compliance Automation-Pipeline
Summary: 
Every time a developer pushes code or development tools, the pipeline acts as a security guard + health inspector for your app. This repository contains a sample secure CI/CD pipeline that shows how to “bake in” security and compliance checks automatically whenever code changes are pushed.In other words, when developers build an app, we automatically generate an SBOM (Software Bill of Materials). We then check each library’s license in MIT, Apache, GPL, etc.  If a risky license is found for closed-source products or tools, the pipeline fails the build process and opens for review. If everything looks good, the build continues and eventually continues the deployment. 

<img width="2062" height="1690" alt="image" src="https://github.com/user-attachments/assets/406231b8-7464-4bf1-b5cf-6ac3ba39c4bf" />



Goals:
Continuous SAST/SCA/DAST with policy gates.
SBOM (SPDX + CycloneDX) is generated on every build.
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
3. The Trivy tool is used, which scans the image for known vulnerabilities and license issues.
4. Conftest(OPA) is used to enforce rules, like if we found any CVE's it stops the build process and fails the build if disallowed licenses are present.

DAST test:
1. OWASP ZAP (baseline scan) checks the running app for common web vulnerabilities (missing security headers, simple injection issues).


Why this exists
- Supply-chain risk: licenses carry obligations, and the wrong one can force code disclosure or restrict use.
- Shift-left compliance: catch issues before merge, not after release.
- Auditability: every decision produces a signed, searchable record.





