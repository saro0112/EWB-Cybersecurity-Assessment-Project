# Project Documentation
## EWB Cybersecurity Assessment – Security Foundations Toolkit

### Abstract
This project is a local Python command-line toolkit that demonstrates four cybersecurity foundations using fictional data. It covers student account risks, phishing indicators, login-event analysis, and critical review of AI-generated security advice.

### Introduction
Students increasingly use online accounts and digital services. Understanding basic security controls helps protect information and recognise suspicious activity. This project turns sample assessment scenarios into simple, repeatable Python analyses.

### Problem Statement
Beginners may find it difficult to connect cybersecurity concepts with practical examples. The toolkit provides a safe, offline way to examine fictional scenarios without interacting with real accounts or networks.

### Objectives
1. Identify common account-security risks and CIA impacts.
2. Recognise warning signs in a fictional phishing email.
3. Summarise synthetic login events while separating facts from interpretations.
4. Correct unsafe or unsupported AI-generated security claims.
5. Generate a readable Markdown assessment report.

### System Requirements
- Windows 10 or Windows 11
- Python 3.9+
- PowerShell / Windows Terminal
- No external packages, API keys, or database

### System Architecture
`Sample JSON/CSV data → Python analysis modules → Terminal results → Markdown report`

### Module Descriptions
**Task A – Account Security:** Reads JSON records describing weak/reused passwords, unexpected MFA approvals, delayed updates, and shared access to an unlocked device. Each record includes the affected asset, confidentiality/integrity/availability impacts, a control, and a limitation.

**Task B – Phishing Analysis:** Reads a fictional scholarship email scenario. It lists urgency, sender/reply-to mismatch, credential and OTP requests, identity-document requests, and discouragement of independent verification as warning signs.

**Task C – Login Activity:** Reads synthetic CSV events and sorts them chronologically. It counts failed and successful password events, MFA denials/approvals, and session creation. A different IP address is not treated as proof of an attacker.

**Task D – AI Advice Review:** Reads fictional AI-generated claims and provides the problem, correction, and safer recommendation for each.

### Implementation Details
The program uses Python's standard library: `argparse` for command-line choices, `pathlib` for file paths, `json` and `csv` for sample data, `datetime` for report timestamps, and `logging` for clear errors. The modules are kept separate to make the code easier to maintain and test.

### Execution
From the project root folder:

```powershell
py main.py
py main.py all
py main.py a
py main.py b
py main.py c
py main.py d
py main.py report
py -m unittest discover -s tests -v
```

### Testing
Four unit-test files check that the sample datasets load, the expected sample records are present, and key analysis counts are produced. Run the test command above from the project root.

### Results
The toolkit displays each selected module's findings in the terminal. Running `py main.py all` also creates `output/EWB_Cybersecurity_Assessment_Report.md`.

### Limitations
- All input data is fictional and fixed sample data.
- The toolkit does not monitor real accounts or networks.
- It does not determine an attacker's identity.
- Results require human interpretation and are not professional forensic conclusions.

### Future Enhancements
- Add more fictional scenarios.
- Add optional charts for synthetic event counts.
- Add configurable sample datasets.
- Improve report styling and export formats.

### Conclusion
The project provides a safe, beginner-friendly demonstration of core security foundations through Python. It reinforces account protection, phishing awareness, evidence-based log interpretation, and critical evaluation of AI-generated advice.

### References
1. CISA, Secure Our World: https://www.cisa.gov/secure-our-world
2. NIST, Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (AI 600-1): https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
