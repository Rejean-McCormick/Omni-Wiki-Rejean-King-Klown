import os

# The mapping of BROKEN links -> CORRECT links
# Based on your file structure in 01_BIG_Rejean.txt and 02_BIG_fr.txt
REPLACEMENTS = {
    "Konnaxion/README.md": "Konnaxion/Konnaxion-Hub.md",
    "Orgo/README.md": "Orgo/Orgo-System-Hub.md",
    "SenTient/README.md": "SenTient/SenTient-Engine-Hub.md",
    "Ariane/README.md": "Ariane/Ariane-Hub.md",
    "SwarmCraft/README.md": "SwarmCraft/SwarmCraft-Hub.md",
    "Ame-Artificielle/README.md": "Ame-Artificielle/Ame-Vision-Hub.md",
    "abstract-wiki-architect/README.md": "abstract-wiki-architect/Wiki-Architect-Hub.md",
    "tools/README.md": "tools/Dev-Workflow-Hub.md"
}

def fix_files():
    # Get current working directory
    root_dir = os.getcwd()
    count = 0

    print(f"Scanning directory: {root_dir}")
    print("-" * 40)

    # Walk through all directories
    for subdir, dirs, files in os.walk(root_dir):
        # Skip .git or hidden folders
        if ".git" in subdir:
            continue

        for file in files:
            # Only process Markdown files
            if file.endswith(".md") or file.endswith(".mdx"):
                filepath = os.path.join(subdir, file)
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    original_content = content
                    
                    # Apply all replacements
                    for bad_link, good_link in REPLACEMENTS.items():
                        if bad_link in content:
                            content = content.replace(bad_link, good_link)
                    
                    # If file changed, write it back
                    if content != original_content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"✅ Fixed: {file}")
                        count += 1
                        
                except Exception as e:
                    print(f"❌ Error reading {file}: {e}")

    print("-" * 40)
    print(f"Job Done. {count} files updated.")

if __name__ == "__main__":
    fix_files()