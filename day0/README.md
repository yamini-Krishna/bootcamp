# bootcamp


# 👋 yamini_hello

**yamini_hello** is a simple, user-friendly Python CLI tool that greets you using rich-text formatting and a beautiful command-line interface powered by `typer`.

This project is a part of my Python packaging bootcamp exercises covering:
- ✅ Application setup and packaging
- ✅ Using external modules (`rich`, `typer`)
- ✅ Building a command-line interface
- ✅ Publishing to TestPyPI

---

## 📦 Installation

You can install this package from **TestPyPI**:

```bash
pip install -i https://test.pypi.org/simple/ yamini-hello
````

> 📌 *Make sure to use the full name with hyphen (`yamini-hello`) when installing.*

---

## 🚀 Usage

Once installed, simply run the following command from your terminal:

```bash
yamini_hello [name]
```

If no name is provided, it will default to `"world"`.

### 🎉 Examples

```bash
yamini_hello
# Output: Hello, [bold magenta]world[/] 👋

yamini_hello Yamini
# Output: Hello, [bold magenta]Yamini[/] 👋
```

---

## 🛠️ Development Setup (For Contributors)

Clone the repo and follow these steps:

```bash
cd day0
uv venv
source .venv/bin/activate
pip install -e .
```

To run locally:

```bash
python -m yamini_hello.main Yamini
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

Ensure you're in the virtual environment and all dependencies are installed.

---

## 🧾 Project Structure

```
bootcamp/
└── day0/
    ├── yamini_hello/
    │   ├── __init__.py
    │   └── main.py         # CLI logic using typer + rich
    ├── tests/
    │   └── test_main.py    # Unit tests
    ├── README.md           # 📄 You're here!
    ├── pyproject.toml      # 📦 Build config & CLI entrypoint
    └── LICENSE             # MIT License
```

---

## 🌐 Published Package

**🔗 TestPyPI**:
👉 [https://test.pypi.org/project/yamini-hello](https://test.pypi.org/project/yamini-hello)

---

## 📚 Technologies Used

* 🐍 Python 3.8+
* 🎨 [`rich`](https://github.com/Textualize/rich) for colorful terminal output
* ⚡ [`typer`](https://github.com/tiangolo/typer) for building CLIs easily
* 🧪 [`pytest`](https://docs.pytest.org/) for unit testing
* 📦 `uv`, `setuptools`, `twine` for environment & packaging

---

## 👩‍💻 Author

**Yamini Krishna**
💌 [yaminimusku04@example.com](mailto:yaminimusku04@example.com)
🔗 GitHub: [@yamini-krishna](https://github.com/yamini-Krishna/bootcamp)

---

## 📄 License

Licensed under the MIT License. See `LICENSE` for more info.


