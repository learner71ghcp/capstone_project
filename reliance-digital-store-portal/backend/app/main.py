from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from app.models import Product
from app.services.product_service import (
    get_product,
    list_low_stock_products,
    list_products,
)

app = FastAPI(title="Reliance Digital Store Operations API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/products", response_model=list[Product])
def get_products(search: str | None = None):
    return list_products(search)


@app.get("/api/products/low-stock", response_model=list[Product])
def get_low_stock_products(threshold: int = Query(default=5, ge=0)):
    return list_low_stock_products(threshold)


@app.get("/api/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product = get_product(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
