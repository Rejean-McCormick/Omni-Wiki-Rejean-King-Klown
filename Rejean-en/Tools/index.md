

##  AI-Assisted Development Workflow Toolkit

**Component:** Project Analysis, Code Extraction, and LLM Integration
**Role:** Automates the creation of highly precise, context-rich prompts for Large Language Models (LLMs) and manages the subsequent code re-integration.

---

## 1.  Overview and Methodology

This toolkit is a specialized workflow designed to create a tight feedback loop between a code repository and an external AI service (like ChatGPT) for systematic code analysis and modification. It orchestrates several Python scripts and configuration data to achieve granular control over which parts of the codebase are analyzed and updated.

### Core Workflow Principle (Scan $\rightarrow$ Prompt $\rightarrow$ Insert)

1.  **Scanning:** Systematically discovers all relevant files in a project directory.
2.  **Prompt Generation:** Extracts and concatenates specific, isolated **code blocks** (rather than entire files) to create a highly focused prompt for the LLM.
3.  **Re-Integration:** Applies the LLM's output directly back into the repository with high precision using line-aware insertion scripts.

---

## 2.  Core Utility Scripts

This group of Python scripts performs the essential tasks of path discovery, data extraction, and content modification.

| File Name | Function | Details |
| :--- | :--- | :--- |
| **`scanAppProjectForPaths.py`** | **Path Discovery** | Scans the project using `os.walk` to identify all relevant file paths, generating the initial dataset used by the system. |
| **`smart_dump.py`** | **Content Extraction** | Iterates over files defined in the configuration and concatenates their content, often with specific delimiters and headers, for easy input into the LLM. |
| **`concatFilesAndSubs.py`** | **Block Substitution** | Combines file contents and performs necessary text substitutions or block replacements based on defined configuration lists. |
| **`pythonInsert.py`** | **Precise Code Insertion** | Reads content (typically LLM output) and injects it at a precisely defined line or block marker within target Python files. |
| **`openInNotepad.py`** | **Inspection Utility** | A simple utility to quickly open files identified by the workflow in a local text editor (e.g., Notepad) for inspection. |

---

## 3.  Data Configuration and Mapping

The system's intelligence relies heavily on the structured data provided in these files (exports from `path_blocks_combinedv2.xlsx`), which serve as the configuration layer.

| File Name | Role in Workflow | Key Data Defined |
| :--- | :--- | :--- |
| **`path_blocks_combinedv2.xlsx - Paths.csv`** | **File Index** | The master list of all source files to be considered for analysis. |
| **`path_blocks_combinedv2.xlsx - Blocks.csv`** | **Code Isolation** | Defines specific, granular code segments or "blocks" within the files, allowing the prompt to be highly focused (e.g., only a single function definition). |
| **`path_blocks_combinedv2.xlsx - Concat_Fetch.csv`** | **Prompt Blueprint** | Specifies the exact sequence of files and blocks that `smart_dump.py` must combine to construct the prompt sent *to* the LLM. |
| **`path_blocks_combinedv2.xlsx - Concat_Give.csv`** | **Injection Blueprint** | Specifies the target paths and block markers where the modified code or LLM output must be inserted *into* the repository. |

---

## 4.  Automation and Maintenance

The workflow is managed by local scripts that handle version control and execution.

* **`GitSink.bat`:** A Windows Batch script used to automate common tasks such as triggering the Python scripts in sequence, handling file synchronization, and managing Git operations (e.g., commit/push). This script defines the robust, automated loop for the AI-assisted process.

---

##  Installation and Usage

*(Instructions for setting up the Python environment, dependencies, and initial execution would go here, sourced from the local `README.md`.)*

