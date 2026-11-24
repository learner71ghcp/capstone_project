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

## Current functionality
- List products
- View a product by ID
- Search products by name
- View low-stock products

## Case-study extension
The development team wants AI-assisted changes to follow consistent repository conventions, project-specific expectations, quality practices, and safe-change boundaries. Use this repository to inspect the existing application and establish a consistent approach before asking the coding assistant to implement a new feature.

Do not assume that every future project will use this technology stack. The practices you establish should be adaptable to other languages and frameworks.
