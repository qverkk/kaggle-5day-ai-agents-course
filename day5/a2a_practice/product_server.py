import uvicorn
from product_agent import product_catalog_a2a_app

if __name__ == "__main__":
    uvicorn.run(product_catalog_a2a_app, host="127.0.0.1", port=8001)
