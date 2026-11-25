# 🧪 Virtual Environments in Python

A **virtual environment** is an isolated Python environment for a particular project. It keeps that project's installed packages separate from packages used by other projects.

## 1. What is a Virtual Environment?

A virtual environment gives each Python project its own isolated set of installed packages.

## 2. Why Do We Need It?

Different projects may need different versions of the same package. Separate environments help avoid dependency and version conflicts.

For example:
- Project A may need an older version of a package.
- Project B may need a newer version.

## 3. Creating a Virtual Environment

Open a terminal in your project folder and run:

```bash
python -m venv venv
```

This creates a folder named `venv` containing the isolated environment.

## 4. Activating on Windows (Command Prompt)

Run:

```bat
venv\Scripts\activate
```

When it is active, the environment name usually appears at the beginning of the terminal prompt:

```text
(venv) C:\path\to\your\project>
```

## 5. Deactivating

Run:

```bash
deactivate
```

This returns the terminal to the normal Python environment.

## 6. Installing Packages

Activate the environment first, then install packages using `pip`.

For example:

```bash
pip install numpy
```

The package is installed in the active virtual environment, not in every Python project on your computer.

## 7. Deleting an Environment

1. Run `deactivate` if the environment is active.
2. Delete the project's `venv` folder.
3. To recreate it, run:

```bash
python -m venv venv
```

Deleting the `venv` folder removes that environment and its installed packages. It does not delete your project files or uninstall the main Python installation.

## 8. Using .gitignore

A virtual environment contains generated files and can be large. It should generally not be uploaded to GitHub.

Add these entries to the repository's `.gitignore` file:

```gitignore
# Python virtual environments
venv/
.venv/
**/venv/
**/.venv/

# Python cache files
__pycache__/
*.py[cod]
```

Keep your source code and project files in GitHub. Other developers can create their own virtual environment on their computers.

> **Remember:** A virtual environment is separate from the actual Python installation. Python itself must be installed on your computer. In VS Code, select the project's virtual environment as the Python interpreter so the editor and terminal use the correct environment.
