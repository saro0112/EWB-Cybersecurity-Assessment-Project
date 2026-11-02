"""Command-line entry point for the EWB Cybersecurity Assessment Toolkit."""
import argparse
import logging
from datetime import datetime
from pathlib import Path

from modules.account_security import analyze as analyze_a
from modules.phishing_analysis import analyze as analyze_b
from modules.login_analysis import analyze as analyze_c
from modules.ai_advice_review import analyze as analyze_d

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUTPUT = ROOT / "output"

def build_report(results):
    OUTPUT.mkdir(parents=True, exist_ok=True)
    lines = [
        "# EWB Cybersecurity Assessment – Security Foundations Toolkit",
        "",
        f"**Generated:** {datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S %Z')}",
        "",
        "> Educational demonstration using fictional data only. Not a live security scanner.",
        ""
    ]
    for key in ("a", "b", "c", "d"):
        if key not in results:
            continue
        result = results[key]
        lines += [f"## {result['title']}", ""]
        if key == "a":
            for risk in result["risks"]:
                lines += [f"### {risk['risk']}", f"- **Asset:** {risk['asset']}",
                          f"- **Confidentiality:** {risk['confidentiality']}",
                          f"- **Integrity:** {risk['integrity']}",
                          f"- **Availability:** {risk['availability']}",
                          f"- **Control:** {risk['control']}",
                          f"- **Limitation:** {risk['limitation']}", ""]
        elif key == "b":
            email = result["email"]
            lines += [f"- **Sender:** {email['sender']}", f"- **Reply-To:** {email['reply_to']}",
                      f"- **Subject:** {email['subject']}", "", "### Warning signs"]
            lines += [f"- {item}" for item in email["warning_signs"]]
            lines += ["", "### Safe verification"]
            lines += [f"- {item}" for item in email["verification_steps"]]
            lines += [""]
        elif key == "c":
            lines += ["### Event timeline"]
            for event in result["events"]:
                lines.append(f"- {event['timestamp']}: {event['event_type']} / {event['status']} / "
                             f"IP {event['ip_address']} / MFA {event['mfa_status']} / session {event['session']}")
            lines += ["", "### Counts"]
            lines += [f"- {name.replace('_', ' ').title()}: {value}" for name, value in result["counts"].items()]
            lines += ["", f"**Interpretation:** {result['interpretation']}", "", "### Recommended checks"]
            lines += [f"- {item}" for item in result["checks"]]
            lines += [""]
        else:
            for claim in result["claims"]:
                lines += [f"### Claim: {claim['claim']}", f"- **Problem:** {claim['problem']}",
                          f"- **Correction:** {claim['correction']}",
                          f"- **Recommendation:** {claim['recommendation']}", ""]
    lines += ["## Safety limitations", "",
              "- Uses only fictional sample data supplied with the project.",
              "- Does not scan networks, access accounts, send messages, or collect credentials.",
              "- Results are educational and should not be treated as a professional incident determination.", ""]
    report_path = OUTPUT / "EWB_Cybersecurity_Assessment_Report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path

def run_module(choice):
    functions = {"a": analyze_a, "b": analyze_b, "c": analyze_c, "d": analyze_d}
    filenames = {"a": "task_a_risks.json", "b": "task_b_email.json",
                 "c": "task_c_signin_logs.csv", "d": "task_d_ai_claims.json"}
    return functions[choice](DATA / filenames[choice])

def print_result(choice, result):
    print(f"\n{'=' * 60}\n{result['title']}\n{'=' * 60}")
    if choice == "a":
        for risk in result["risks"]:
            print(f"\nRisk: {risk['risk']}\nAsset: {risk['asset']}\nControl: {risk['control']}")
    elif choice == "b":
        email = result["email"]
        print(f"Sender: {email['sender']}\nReply-To: {email['reply_to']}\nSubject: {email['subject']}")
        for sign in email["warning_signs"]:
            print(f"- Warning: {sign}")
    elif choice == "c":
        for event in result["events"]:
            print(f"{event['timestamp']} | {event['event_type']} | {event['status']} | "
                  f"{event['ip_address']} | MFA: {event['mfa_status']}")
        print("\nCounts:", result["counts"])
        print(result["interpretation"])
    else:
        for claim in result["claims"]:
            print(f"\nClaim: {claim['claim']}\nProblem: {claim['problem']}\nCorrection: {claim['correction']}")

def interactive():
    while True:
        print("\n" + "=" * 43)
        print(" EWB CYBERSECURITY ASSESSMENT TOOLKIT")
        print("=" * 43)
        print("1. Account Security Analysis")
        print("2. Phishing Email Analysis")
        print("3. Login Activity Analysis")
        print("4. AI Security Advice Evaluation")
        print("5. Run All Modules")
        print("6. Generate Assessment Report")
        print("0. Exit")
        choice = input("\nSelect an option: ").strip()
        if choice == "0":
            print("Goodbye.")
            return 0
        if choice in {"1", "2", "3", "4"}:
            key = {"1": "a", "2": "b", "3": "c", "4": "d"}[choice]
            print_result(key, run_module(key))
        elif choice == "5":
            results = {key: run_module(key) for key in "abcd"}
            for key, result in results.items():
                print_result(key, result)
            print(f"\nReport: {build_report(results)}")
        elif choice == "6":
            results = {key: run_module(key) for key in "abcd"}
            print(f"Report generated: {build_report(results)}")
        else:
            print("Invalid option. Please enter 0 to 6.")

def main():
    parser = argparse.ArgumentParser(description="EWB Cybersecurity Assessment Toolkit")
    parser.add_argument("task", nargs="?", choices=["a", "b", "c", "d", "all", "report"],
                        help="Choose a module or run all modules; omit for interactive menu.")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    try:
        if not args.task:
            return interactive()
        if args.task == "report":
            results = {key: run_module(key) for key in "abcd"}
            print(f"Report generated: {build_report(results)}")
            return 0
        choices = list("abcd") if args.task == "all" else [args.task]
        results = {}
        for key in choices:
            results[key] = run_module(key)
            print_result(key, results[key])
        if args.task == "all":
            print(f"\nAssessment report generated: {build_report(results)}")
        return 0
    except (FileNotFoundError, ValueError, OSError) as exc:
        logging.error("%s", exc)
        logging.error("Check that you are running this command from the project root folder.")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
