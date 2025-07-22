import os

PROMPT_DIR = "prompts"
OUTPUT_DIR = "wiki_generated"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_categories():
    return [
        cat for cat in os.listdir(PROMPT_DIR)
        if os.path.isdir(os.path.join(PROMPT_DIR, cat))
    ]

def parse_prompt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    title = lines[0].strip("# \n") if lines else "Untitled Prompt"
    body = "".join(lines[1:]) if len(lines) > 1 else "(No content found)"
    return title, body

def write_wiki_page(category, filename, title, body):
    safe_name = filename.replace(".md", "").replace("_", "-")
    page_path = os.path.join(OUTPUT_DIR, f"{category}-{safe_name}.md")

    with open(page_path, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**Category**: `{category}`  \n")
        f.write("---\n\n")
        f.write(body)

def main():
    print("🔮 Starting wiki page generation...")
    ensure_output_dir()

    categories = get_categories()
    if not categories:
        print("⚠️ No prompt categories found.")
        return

    for category in categories:
        folder_path = os.path.join(PROMPT_DIR, category)
        for filename in os.listdir(folder_path):
            if filename.endswith(".md"):
                filepath = os.path.join(folder_path, filename)
                title, body = parse_prompt_file(filepath)
                write_wiki_page(category, filename, title, body)

    print(f"✅ Wiki pages saved to ./{OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
