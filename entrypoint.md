Good question — this is exactly the point that confuses many people when packaging Python projects.

The short answer: users usually don’t run `main.py` directly. Instead, the package exposes a **command-line entry point** that runs a function inside your package.

---

# How Users Run Your Package After Installing

### What Happens After Installation

`pip install my-project`

they can run it like this:

`my-project`

This works because the package defines a **console script entry point**.

### this is equivalant to 


`from my_project.cli import main `

`main()`

---

# Example Entry Function

`src/my_project/cli.py`

def main():

    print("App is running!")

---

# Connect It in `pyproject.toml`


[project.scripts]

my-project = "my_project.cli:main"


---




---
