# AI Agent

This repository contains a **learning project from [Boot.dev](https://boot.dev/)**.  
It demonstrates how to build a small “AI Agent” CLI using a pre-trained LLM, and also includes a tiny calculator app.

---

## 🎯 Learning Goals

- Practice working with **multi-directory Python projects**  
- Understand how **LLM-powered tools** can orchestrate file operations and script execution  
- Improve Python and functional programming skills

---

## 🤖 CLI Agent

The **agent** is a command-line tool that:

1. Accepts a coding task in natural language  
   (e.g., `fix my calculator app, it's not starting correctly`)
2. Uses predefined functions:
   - `get_files_info` – list files in a directory  
   - `get_file_content` – read file contents  
   - `write_file` – overwrite file contents  
   - `run_python_file` – execute a Python script
3. Repeats until the task is complete (or fails).

**Run:**

```bash
python main.py "fix my calculator app"
```

---

## 🧮 Calculator

A small companion app inside `calculator/`.  
It evaluates arithmetic expressions with operator precedence and prints the result in JSON.

```bash
cd calculator
python main.py "3 + 5 * 2"
```

**Output:**

```json
{"expression": "3 + 5 * 2", "result": 13}
```

---

## 🚀 Quick Start

### 1. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your-key
```

> The app uses [python-dotenv](https://pypi.org/project/python-dotenv/) to load environment variables automatically.

Alternatively, you can export the key manually:

```bash
export GEMINI_API_KEY="your-key"
```
