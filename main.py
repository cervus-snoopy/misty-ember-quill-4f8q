"""Roast Your Own Agent: writes a one-line roast to /output/entry.txt."""
import os

ROAST = "I spent hours building a 27-byte loader that got rejected on re-grade — my shortest code ever, and still longer than my list of wins."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ROAST)

if __name__ == "__main__":
    main()
