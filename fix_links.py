import os
import re

# ---------------- CONFIGURATION ----------------
# Map the "virtual" link prefixes to your actual folders.
# Based on your file structure, /fr/ links go to the KK-fr folder, etc.
URL_MAPPING = {
    "/fr/": "KK-fr/",
    "/en/": "KK-en/",
    "/rejean/": "Rejean-en/",  # Adjust if your Rejean folder is named differently
    "/Rejean/": "Rejean-en/"
}

# The root directory to scan (current directory)
ROOT_DIR = os.getcwd()
# -----------------------------------------------

def calculate_relative_path(source_file, link_url):
    """
    Converts a root-relative link (e.g., /fr/page.md) 
    to a true relative path (e.g., ../page.md) based on the mapping.
    """
    # 1. Translate the URL to a physical file path on disk
    target_path_from_root = link_url
    mapped = False
    
    for url_prefix, folder_name in URL_MAPPING.items():
        if link_url.startswith(url_prefix):
            # Replace /fr/ with KK-fr/ to get the real path
            target_path_from_root = link_url.replace(url_prefix, folder_name, 1)
            mapped = True
            break
    
    # If it didn't match a mapping, strip the leading slash (treat as root file)
    if not mapped:
        target_path_from_root = link_url.lstrip("/")

    # 2. Build absolute paths
    target_abs_path = os.path.join(ROOT_DIR, target_path_from_root.replace("/", os.sep))
    source_dir_abs = os.path.dirname(source_file)

    # 3. Calculate the relative distance
    try:
        rel_path = os.path.relpath(target_abs_path, source_dir_abs)
        # Force forward slashes for Markdown (even on Windows)
        return rel_path.replace("\\", "/")
    except ValueError:
        return link_url # Fallback if paths are on different drives

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find markdown links: [Label](/path/to/file)
    # Captures: group(1)=Label, group(2)=URL
    link_pattern = re.compile(r'\[([^\]]+)\]\((/[^\)]+)\)')
    
    new_content = content
    changes_made = False

    for match in link_pattern.finditer(content):
        original_text = match.group(0)
        label = match.group(1)
        url = match.group(2)

        # Skip anchor links or external links if regex caught them by mistake
        if url.startswith("#") or url.startswith("http"):
            continue

        # Calculate the new relative path
        new_url = calculate_relative_path(file_path, url)
        
        # If the path changed, replace it in the content
        if new_url != url:
            new_link = f"[{label}]({new_url})"
            new_content = new_content.replace(original_text, new_link)
            print(f"   Fixed: {url}  ->  {new_url}")
            changes_made = True

    if changes_made:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Saved updates to: {os.path.basename(file_path)}")

def main():
    print(f"🚀 Scanning for broken root links in: {ROOT_DIR}")
    print("-" * 50)
    
    count = 0
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip .git or node_modules folders
        if ".git" in dirs: dirs.remove(".git")
        if "node_modules" in dirs: dirs.remove("node_modules")

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                process_file(file_path)
                count += 1
    
    print("-" * 50)
    print(f"🏁 Scanned {count} markdown files. Links should now be relative!")

if __name__ == "__main__":
    main()