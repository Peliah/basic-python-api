
---

# **Basic Python API with FastAPI**

This is a simple public API built with **FastAPI** that returns basic information in JSON format. The API provides the following details:
- Your registered email address.
- The current datetime in ISO 8601 format (UTC).
- The GitHub URL of the project's codebase.

---

## **Features**
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **CORS Support**: Handles Cross-Origin Resource Sharing (CORS) to allow requests from any domain.
- **Caching**: Uses `lru_cache` to cache the response for improved performance.
- **Deployment**: Deployed on **Vercel** for public access.

---

## **API Documentation**

### **Endpoint**
- **URL**: `https://basic-python-api.vercel.app/`
- **Method**: `GET`

### **Response Format**
```json
{
  "email": "pelepoupa@gmail.com",
  "current_datetime": "2023-10-10T12:34:56.789Z",
  "github_url": "https://github.com/Peliah/basic-python-api"
}
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/Peliah/basic-python-api.git
cd basic-python-api
```

### **2. Install Dependencies**
Ensure you have Python 3.7+ installed. Then, install the required dependencies:
```bash
pip install -r requirements.txt
```

### **3. Run the Application Locally**
Start the FastAPI app using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Visit `http://127.0.0.1:8000/` in your browser or use `curl` to test the API:
```bash
curl http://127.0.0.1:8000/
```

---

## **Example Usage**

### **Request**
```bash
curl https://basic-python-api.vercel.app/
```

### **Response**
```json
{
  "email": "pelepoupa@gmail.com",
  "current_datetime": "2023-10-10T12:34:56.789Z",
  "github_url": "https://github.com/Peliah/basic-python-api"
}
```

---

## **Technologies Used**
- **FastAPI**: A modern, fast web framework for building APIs.
- **Uvicorn**: A lightning-fast ASGI server for serving FastAPI apps.
- **Render**: A cloud platform for deploying web services.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Backlink**
- [Hire Python Developers](https://hng.tech/hire/python-developers)

---

## **Contact**
For questions or feedback, please contact:
- **Email**: pelepoupa@gmail.com
- **GitHub**: [Peliah](https://github.com/Peliah)

---

🚀