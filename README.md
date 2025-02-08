# Number Classification API

This is a FastAPI-based web service that classifies numbers based on their mathematical properties. It determines whether a given number is **prime**, **perfect**, or an **Armstrong number** and provides additional information such as the sum of its digits and a fun fact.

## Features
- ✅ Check if a number is **prime**  
- ✅ Check if a number is **perfect**  
- ✅ Check if a number is an **Armstrong number**  
- ✅ Calculate the sum of digits  
- ✅ Provide a **fun fact** about the number  
- ✅ CORS enabled for cross-origin requests  
- ✅ Interactive API documentation via Swagger UI  

## Technologies Used
- **Python** 🐍  
- **FastAPI** 🚀  
- **Uvicorn** (for running the ASGI server)  
- **CORS Middleware** (for handling cross-origin requests)  

---

## Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ebube101/number-classification-api.git
cd number-classification-api
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Running the API Locally

Run the FastAPI application using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
Your API will now be accessible at:

📌 **Local:** `http://127.0.0.1:8000`  
📌 **Swagger UI:** `http://127.0.0.1:8000/docs` (API documentation)  
📌 **ReDoc UI:** `http://127.0.0.1:8000/redoc` (Alternative API documentation)

---

## API Endpoints

### 🟢 `GET /api/classify-number`
Classifies a number and returns its properties.

#### **Request Parameters**
| Parameter | Type  | Required | Description |
|-----------|-------|----------|-------------|
| `number`  | `int` | ✅ Yes  | The number to classify |

#### **Example Request**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/api/classify-number?number=28' -H 'accept: application/json'
```

#### **Example Response**
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["perfect"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number."
}
```

---

## Deployment on AWS EC2

### 1️⃣ Transfer Files to EC2 (From Local Machine)
Use SCP to copy your project to the EC2 instance:
```bash
scp -i "your-key.pem" -r number-classification-api ubuntu@your-ec2-ip:/home/ubuntu/
```

### 2️⃣ SSH into EC2
```bash
ssh -i "your-key.pem" ubuntu@your-ec2-ip
```

### 3️⃣ Install Dependencies on EC2
```bash
cd number-classification-api
pip install -r requirements.txt
```

### 4️⃣ Run the API on EC2
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
To keep it running even after logout, use:
```bash
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
```

---

## Troubleshooting
- **Port Already in Use**  
  🔹 Kill the existing process:  
  ```bash
  sudo lsof -i :8000
  sudo kill -9 <PID>
  ```
- **CORS Issues?**  
  🔹 Ensure CORS middleware is included in `main.py`:  
  ```python
  from fastapi.middleware.cors import CORSMiddleware
  app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
  ```
- **502 Bad Gateway on AWS?**  
  🔹 Check if Uvicorn is running and accessible via `your-ec2-ip:8000`. If necessary, update your security group to allow inbound traffic on port 8000.
