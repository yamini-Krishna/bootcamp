Project Documentation Website

---

## Prerequisites

- Install Python (version 3.7 or higher recommended)
- Install MkDocs (a Python package)
- Basic command line usage

---

## Step 1: Install MkDocs

Open your terminal (Command Prompt, PowerShell, or shell) and run:

```bash
pip install mkdocs
````

---

## Step 2: Prepare the Documentation Site

Your Markdown (`.md`) files like `implementation.md`, `operationalization.md`, etc. are located in the `docs/` folder.

MkDocs uses a configuration file `mkdocs.yml` in the project root (next to `docs/`) to build the site.

---

## Step 3: Preview Locally

To preview your documentation website locally, run:

```bash
mkdocs serve
```

* This command starts a local web server.
* Open your web browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000)
* You will see a live preview of your documentation.
* Any changes you make to `.md` files will automatically refresh in the browser.

Press `Ctrl+C` to stop the server.

---

## Step 4: Build the Static Website

Once you are happy with the preview, build the static website files:

```bash
mkdocs build
```

* This creates a `site/` folder containing all the HTML, CSS, and JavaScript files needed to serve your docs as a website.





