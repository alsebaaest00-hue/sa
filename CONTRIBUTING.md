# Contributing

Thanks for your interest in contributing! Small, focused PRs are easiest to review.

Before you open a PR:
- Open an issue for non-trivial changes to discuss scope and design.
- Run tests and linters locally: `poetry install --no-interaction` then `poetry run pytest -q` and `poetry run ruff check .`.
- Run formatting and pre-commit hooks: `poetry run pre-commit install` then `poetry run pre-commit run --all-files`.

PR checklist:
- Use the provided PR template and fill out the checklist.
- Keep changes small and include tests where applicable.
- Update documentation (README) if you change public behavior.

Thank you — maintainers will review and respond to PRs asap.
