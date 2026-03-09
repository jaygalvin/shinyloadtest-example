## NBA dashboard app and shinyloadtest

Example from: <https://github.com/posit-dev/py-shiny-templates/tree/main/nba-dashboard>

Install from requirements.txt using uv: 

```bash
uv pip install -r requirements.txt
```

You might need to create a uv environment first: 

```bash
# Check what python versions you have access to
ls -1d /opt/python/*

# Create the uv project, this example declares the python version to use explicitly. Make sure this matches a version you have access to.
uv init --app --python 3.12.11
```

Activate the virtual environment

```bash
source .venv/bin/activate
```

After changing anything be sure to run `uv sync`.

Run the application:

```bash
uv run app.py
uv run shiny run --reload app-core.py
```


