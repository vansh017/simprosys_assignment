import os
import sys
print("Before chdir:", sys.path)

# os.chdir(os.getcwd())

print("After chdir:", sys.path)

import uvicorn
from fastapi import FastAPI

from api.endpoints import user_router, categories_router, product_router

app = FastAPI()

app.include_router(user_router)
app.include_router(categories_router)
app.include_router(product_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, reload=False)