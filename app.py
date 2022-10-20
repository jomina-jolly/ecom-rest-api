from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name" : "mystore_1",
        "items" : [
            {
                "name": "Chair",
                "price": 15.99
            },
            {
              "name": "Table",
              "price": 20.99
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}