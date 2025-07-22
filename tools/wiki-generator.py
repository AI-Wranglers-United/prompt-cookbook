import os

# Path to the prompts directory
PROMPT_DIR = "prompts"
WIKI_DIR = "wiki_generated"

def get_prompt_categories():
    return [cat for cat in os.listdir(PROMPT_DIR) if os.path.isdir(os.path.join(PROMPT_DIR, cat))]

def parse_prompt_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    title = lines[0].strip("# \n")
    body = "".join(lines[2:])  # skip title and prompt line
    return title, body

def make_wiki_page(category, filename, title, body):
    os.makedirs(WIKI_DIR, exist_ok=True)
    page_name = f"{category}_{filename.replace('.md', '')}.md"
    with open(os.path.join(WIKI_DIR, page_name), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(body)

def main():
    print("🔮 Generating Wiki Pages from Prompt Scrolls...")
    for category in get_prompt_categories():
        folder = os.path.join(PROMPT_DIR, category)
        for file in os.listdir(folder):
            if file.endswith(".md"):
                filepath = os.path.join(folder, file)
                title, body = parse_prompt_file(filepath)
                make_wiki_page(category, file, title, body)
    print(f"✅ Wiki pages saved to ./{WIKI_DIR}/")

if __name__ == "__main__":
    main()
