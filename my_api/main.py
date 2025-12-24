from fastapi import FastAPI

# 1. Create the 'App' instance (The Restaurant)
app = FastAPI()

# 2. Define a "Route" or "Endpoint" (The Menu Item)
# This says: "If someone sends a GET request to the homepage (/), do this."
@app.get("/")
def read_root():
    # 3. Return data (The Meal)
    # FastAPI automatically converts this Python Dictionary into JSON!
    return {"message": "Hello, Student!", "role": "Teacher"}

# 4. Another endpoint
@app.get("/status")
def get_status():
    return {"status": "Online", "version": "1.0.0"}

@app.get("/menu")
def show_menu():
    return {
        "items": ["Coffee", "Tea", "Python-Latte"],
        "open": True
    }