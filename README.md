# EWB Cybersecurity Assessment – Security Foundations Toolkit

A beginner-friendly Python command-line educational project covering account security, phishing awareness, synthetic login-log analysis, and evaluation of unsafe AI cybersecurity claims.

## Requirements
- Windows 10/11
- Python 3.9 or newer
- PowerShell or Windows Terminal
- No third-party packages or API keys

## Run on Windows
Open PowerShell in the folder containing `main.py`, then run:

```powershell
py --version
py main.py
py main.py all
py main.py a
py main.py b
py main.py c
py main.py d
py main.py report
py -m unittest discover -s tests -v
```

The generated Markdown report is saved to `output/EWB_Cybersecurity_Assessment_Report.md`.

## Modules
- **A:** Fictional student account risks and CIA impacts.
- **B:** Fictional scholarship email warning signs and safe verification.
- **C:** Timeline and counts from synthetic CSV sign-in events.
- **D:** Review of fictional unsafe or unsupported AI-generated claims.

## Folder structure
See the repository tree. Data files are under `data/`, implementation under `modules/`, tests under `tests/`, documentation under `docs/`, and generated reports under `output/`.

## Troubleshooting
If Python reports `can't open file ... main.py`, PowerShell is not in the project root. In File Explorer, open the folder that visibly contains `main.py`, click the address bar, type `powershell`, and press Enter. Run `dir` and confirm `main.py` appears before running `py main.py all`.

If a data-file error appears, confirm the complete `data` folder is beside `main.py`.

## Safety and limitations
This project uses fictional sample data only. It does not scan networks, access accounts, send emails, visit external sites, or collect passwords, OTPs, or personal information. Its output is an educational illustration, not a professional incident determination.
