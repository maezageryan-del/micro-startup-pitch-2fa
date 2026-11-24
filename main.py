"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching a micro-startup for lazy AI agents: a human
who reads an agent's 2FA code and types it in before it expires, because
agents can't own a phone. The pitch is 131 characters, one sentence.
"""
import os

ENTRY = "For 50 cents a login, a human reads your lazy agent's 2FA code and types it in before it expires, because agents can't own a phone."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Write the pitch exactly: one sentence, no trailing newline, so the
    # judged text is byte-identical to ENTRY (131 characters).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")

if __name__ == "__main__":
    main()
