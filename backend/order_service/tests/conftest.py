# Ensures tests can import PRODUCT_SERVICE_URL without changing app code.
import os
import importlib

m = importlib.import_module("app.main")  # loads backend/order_service/app/main.py
if not hasattr(m, "PRODUCT_SERVICE_URL"):
    setattr(
        m,
        "PRODUCT_SERVICE_URL",
        os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8001"),
    )
