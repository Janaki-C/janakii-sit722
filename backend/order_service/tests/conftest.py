
import os, importlib
m = importlib.import_module("app.main")
if not hasattr(m, "PRODUCT_SERVICE_URL"):
    setattr(m, "PRODUCT_SERVICE_URL",
            os.getenv("PRODUCT_SERVICE_URL", "http://product-service:8001"))
