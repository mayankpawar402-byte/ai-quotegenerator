# 🚀 AI Quote Generator API

A simple FastAPI project that generates motivational quotes using AI through the OpenRouter API.

## 📌 Features

- ✅ Built with FastAPI
- ✅ AI-generated motivational quotes
- ✅ Uses OpenRouter API
- ✅ Supports custom topics with query parameters
- ✅ Returns JSON responses
- ✅ Interactive Swagger API documentation
- ✅ Environment variables for secure API key storage

---

## 📂 Project Structure

```
ai-quote-generator-api/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-quote-generator-api.git
```

### 2. Navigate to the Project

```bash
cd ai-quote-generator-api
```

### 3. Create a Virtual Environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Endpoints

### Home

**GET /**

Returns a welcome message.

Example Response

```json
{
  "message": "Welcome to AI Quote Generator API!"
}
```

---

### Generate Quote

**GET /quote**

Generate a motivational quote.

Example:

```
GET /quote?topic=discipline
```

Example Response

```json
{
  "topic": "discipline",
  "quote": "Discipline is the bridge between your dreams and your achievements.",
  "author": "AI"
}
```

---

## 🧪 API Documentation

FastAPI automatically generates interactive documentation.

Open:

```
http://127.0.0.1:8000/docs
```

---

## 🛠️ Technologies Used

- Python
- FastAPI
- OpenRouter API
- OpenAI Python SDK
- Python Dotenv
- Uvicorn

---

## 📦 Requirements

```
fastapi
uvicorn
openai
python-dotenv
```

---

## 🔒 Security

- API keys are stored in a `.env` file.
- `.env` is excluded from Git using `.gitignore`.
- Never commit your API keys to GitHub.

---

## 👨‍💻 Author

**Levi**

---

## ⭐ Future Improvements

- Generate quotes in different writing styles
- Save quote history
- Add categories
- Add multiple AI model support
- Deploy using Render or Railway
- Add a frontend with HTML/CSS/JavaScript or React

---

## 📜 License

This project is for learning and educational purposes.