// run server
streamlit run app/main.py

// lint with ruff
ruff lint
ruff format

// setup precommit hook
pre-commit install

// manually run lint
pre-commit run --all-files
