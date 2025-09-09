# Food Ordering Backend

A FastAPI backend for a Zomato-like food ordering system with custom DSA implementations.
 ## Folder structure
 ```bash
 food-ordering-backend/
├── main.py
├── requirements.txt
├── README.md
├── auth/
│   ├── __init__.py
│   ├── router.py
│   └── utils.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── user.py
│   ├── restaurant.py
│   ├── product.py
│   └── order.py
├── schemas/
│   ├── __init__.py
│   ├── user.py
│   ├── restaurant.py
│   ├── product.py
│   └── order.py
├── dsa/
│   ├── __init__.py
│   ├── hash_map.py
│   ├── stack.py
│   ├── queue.py
│   ├── min_heap.py
│   └── max_heap.py
├── routes/
│   ├── __init__.py
│   ├── users.py
│   ├── restaurants.py
│   ├── products.py
│   ├── orders.py
│   └── search.py
├── utils/
│   ├── __init__.py
│   ├── database.py
│   ├── password.py
│   └── jwt_handler.py
└── tests/
    ├── __init__.py
    ├── test_dsa.py
    ├── test_auth.py
    └── test_routes.py
 ```