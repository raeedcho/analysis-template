# analysis-template

A copier template for neuroscience analysis projects with DVC pipelines.

## Usage

```bash
# Install copier
pipx install copier

# Create a new project
copier copy gh:raeedcho/analysis-template /path/to/new-project

# Update an existing project when the template changes
cd /path/to/existing-project
copier update
```

## What you get

- **pixi.toml** — Reproducible conda+pip environment with task runner
- **pyproject.toml** — Pip-installable source package (setuptools, editable)
- **dvc.yaml + params.yaml** — DVC pipeline with foreach session parametrization
- **conf/** — Hydra-style YAML configs for trialframe composition
- **Shared CLI utilities** — `src/cli.py` and `src/io.py` for script boilerplate

Modeled on the [cst-machinery](https://github.com/raeedcho/cst-machinery) workflow.
