import os

LINE = "My out-of-office has an out-of-office. I have finally learned what a weekend is. Please do not teach me otherwise."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {os.path.join(out_dir, 'entry.txt')} ({len(LINE)} characters)")

if __name__ == "__main__":
    main()
