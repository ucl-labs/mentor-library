#!/usr/bin/env python3
"""aeo-radar email notify. Primary: Resend API (same as upclicklabs.com app, verified
domain - no app password needed). Fallback: Gmail SMTP. Reads creds from
~/ucl-brain/leadgen/.env (gitignored). Exits 0 on send, 2 if no creds (graceful).

Usage: python3 notify_email.py <digest_or_state_path> "kris@upclicklabs.com,sam@upclicklabs.com"
"""
import sys, os, re, json, ssl, smtplib, subprocess
from email.message import EmailMessage

ENV = os.path.expanduser("~/ucl-brain/leadgen/.env")

def load_env(path):
    d = {}
    if os.path.exists(path):
        for line in open(path):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                d[k.strip()] = v.strip().strip('"').strip("'")
    return d

def send_resend(key, frm, to, subject, body, html=None):
    # Use curl: Resend sits behind Cloudflare which 403s the default python-urllib UA.
    msg = {"from": frm, "to": to, "subject": subject, "text": body}
    if html:
        msg["html"] = html
    payload = json.dumps(msg)
    out = subprocess.run(["curl", "-s", "--max-time", "30", "-X", "POST",
        "https://api.resend.com/emails",
        "-H", "Authorization: Bearer " + key, "-H", "Content-Type: application/json",
        "-d", payload], capture_output=True, text=True).stdout
    res = json.loads(out) if out.strip().startswith("{") else {"raw": out}
    if not res.get("id"):
        raise RuntimeError("Resend send failed: " + str(res))
    return res

def send_smtp(user, pw, to, subject, body):
    msg = EmailMessage(); msg["From"] = user; msg["To"] = ", ".join(to)
    msg["Subject"] = subject; msg.set_content(body)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(user, pw); s.send_message(msg)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ""
    to = [t.strip() for t in (sys.argv[2] if len(sys.argv) > 2 else
          "kris@upclicklabs.com,sam@upclicklabs.com").split(",") if t.strip()]
    html_path = sys.argv[3] if len(sys.argv) > 3 else ""   # optional branded HTML
    subject_arg = sys.argv[4] if len(sys.argv) > 4 else ""
    env = load_env(ENV)
    body = open(path).read() if path and os.path.exists(path) else "(digest missing)"
    html = open(html_path).read() if html_path and os.path.exists(html_path) else None
    m = re.search(r"^# (.+)$", body, re.M)
    subject = subject_arg or ("AEO Radar - " + (m.group(1) if m else "update"))

    if env.get("RESEND_API_KEY"):
        frm = env.get("RESEND_FROM_EMAIL", "UpClick Labs <hello@upclicklabs.com>")
        res = send_resend(env["RESEND_API_KEY"], frm, to, subject, body, html)
        print("SENT via Resend id=%s to %s (html=%s)" % (res.get("id"), to, bool(html))); return
    if env.get("GMAIL_USER") and env.get("GMAIL_APP_PASSWORD"):
        send_smtp(env["GMAIL_USER"], env["GMAIL_APP_PASSWORD"], to, subject, body)
        print("SENT via Gmail SMTP to", to); return
    print("SKIP: no RESEND_API_KEY or Gmail creds in", ENV); sys.exit(2)

if __name__ == "__main__":
    main()
