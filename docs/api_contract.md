# API Contract - User Profile

  **Endpoint:** `/api/v1/profile`
  **Method:** `GET`
  **Response Body (JSON):**
```json
  {
    "id": 1,
    "username": "mahasiswa_sd",
    "email": "mhs@univ.ac.id",
    "avatar_url": "https://image.com/avatar.png"
  }
```
---

  ## Endpoint Login

  **Endpoint:** `/api/v1/login`
  **Method:** `POST`

  **Request Body (JSON):**
```json
  {
    "email": "mhs@univ.ac.id",
    "password": "password123"
  }
```

  **Response Body (JSON) - Sukses:**
```json
  {
    "status": "success",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": 1,
      "username": "mahasiswa_sd"
    }
  }
```

  **Response Body (JSON) - Gagal:**
```json
  {
    "status": "error",
    "message": "Email atau password salah"
  }
```
