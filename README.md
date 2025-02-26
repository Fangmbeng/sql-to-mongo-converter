# sql-to-mongo-converter
### Repository Name:  
**sql-to-mongo-converter**  

### Description:  
This project provides a Python class **`SQLToMongo`** that converts basic **SQL SELECT queries** into equivalent **MongoDB query formats**. It supports parsing SQL components like:  

- **SELECT fields** → Converted to MongoDB **projection**  
- **FROM table** → Converted to MongoDB **collection name**  
- **WHERE conditions** → Converted to MongoDB **filter** with operators like:  
  - `=` → MongoDB exact match `{ field: value }`  
  - `IN` → MongoDB `$in` operator `{ field: { $in: [...] } }`  
  - `LIKE` → MongoDB regex pattern `{ field: { $regex: ... } }`  
- **LIMIT clause** → Converted to MongoDB **limit**  

### Features:  
- **SQL to MongoDB query conversion** with simple syntax parsing  
- **Supports basic conditions** including `=`, `IN`, and `LIKE`  
- **Handles LIMIT for query results restriction**  
- **Lightweight and easy to extend**  

### Dependencies:  
- Python 3+  
- No external dependencies required  

### Usage:  
```python
from sql_to_mongo import SQLToMongo

sql_query = "SELECT name, age FROM users WHERE active = 'true' AND age IN (20, 30) AND name LIKE 'John%' LIMIT 10"
converter = SQLToMongo(sql_query)
mongo_query = converter.convert()

print(mongo_query)
```

### Example Output:  
```json
{
    "projection": { "name": 1, "age": 1 },
    "collection": "users",
    "filter": {
        "active": "true",
        "age": { "$in": ["20", "30"] },
        "name": { "$regex": "^John.*$" }
    },
    "limit": 10
}
```

---

💡 **Future Enhancements:**  
- Support for `ORDER BY`, `GROUP BY`, and `JOIN` statements  
- More complex condition handling (`>=`, `<=`, `!=`, etc.)  
- MongoDB aggregation framework support  

Welcomig to contributions and model improvements 🚀
