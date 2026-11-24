# Reliance Digital – Store Operations Portal

A small starter repository for the Reliance Digital case study. It provides a product catalogue and inventory view that can be extended by a development team using an AI coding assistant.

## Technology stack
- Backend: Python 3.11+, FastAPI
- Frontend: React 18, Vite, JavaScript
- Tests: pytest

## Repository layout
```text
reliance-digital-store-portal/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   └── services/
│   │       └── product_service.py
│   ├── tests/
│   │   └── test_products.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   └── main.jsx
│   ├── index.html
│   └── package.json
└── README.md
```

## Run the backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API: http://127.0.0.1:8000  
API docs: http://127.0.0.1:8000/docs

## Run the frontend
In a second terminal:
```bash
cd frontend
npm install
npm run dev
```
Open the URL printed by Vite (normally http://localhost:5173).

## Run backend tests
```bash
cd backend
pytest
```

## GitHub MCP in VS Code

The workspace includes a GitHub MCP server configuration in `.vscode/mcp.json`.
Open this repository in VS Code, start GitHub Copilot Chat in Agent mode, and
approve the GitHub sign-in prompt to use repository and pull-request tools.

After pushing a feature branch, ask Copilot to open a pull request. To review a
pull request, ask Copilot to inspect its changes and provide findings. MCP makes
these tools available to Copilot; it does not independently create or review
pull requests in the background. For event-triggered automation, configure a
GitHub Actions workflow or GitHub's Copilot code review settings.

## Current functionality
- List products
- View a product by ID
- Search products by name
- View low-stock products

## Case-study extension
The development team wants AI-assisted changes to follow consistent repository conventions, project-specific expectations, quality practices, and safe-change boundaries. Use this repository to inspect the existing application and establish a consistent approach before asking the coding assistant to implement a new feature.

Do not assume that every future project will use this technology stack. The practices you establish should be adaptable to other languages and frameworks.
