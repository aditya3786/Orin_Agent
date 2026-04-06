# ORIN AI Agent System

An intelligent AI agent system built with LangChain and Groq for private and government offices to instantly resolve queries, reduce staff workload, and streamline coordination processes.

## 🌟 Features

- **Groq-powered AI Chat**: Uses Groq LLM via `langchain-groq` for query generation
- **RAG (Retrieval-Augmented Generation)**: Uses Pinecone vector database and document search tools
- **Secure Authentication**: JWT-based authentication with API key support
- **Document Management**: Upload, index, and search official documents and policies
- **User & Admin Controls**: Admin panel for user management and system statistics
- **Department-aware Answers**: Supports document metadata by department and type
- **Safe Answering**: Agent is instructed to answer only from uploaded documents

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Groq API Key
- Pinecone Account

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aditya3786/Orin_Agent.git
   cd "Orin_Agent"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

### Docker Setup

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

## 📚 API Documentation

### Authentication Endpoints

- **POST** `/auth/login` - User login
- **POST** `/auth/register` - User registration
- **GET** `/auth/profile` - Get user profile

### Chat & AI Endpoints

- **POST** `/api/v1/chat` - Chat with AI agent (JWT auth)
- **POST** `/api/v1/chat/api-key` - Chat with API key
- **POST** `/api/v1/documents/upload` - Upload documents
- **GET** `/api/v1/documents/search` - Search documents

### Example Usage

#### Authentication
```bash
# Register a user
curl -X POST "http://localhost:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "password123",
    "full_name": "John Doe",
    "department": "IT"
  }'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=password123"
```

#### Chat with AI Agent
```bash
# Using JWT token
curl -X POST "http://localhost:8000/api/v1/chat" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is the leave policy for HR employees?"
  }'

# Using API key
curl -X POST "http://localhost:8000/api/v1/chat/api-key?api_key=YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me the sick leave rules."
  }'
```

#### Document Upload
```bash
curl -X POST "http://localhost:8000/api/v1/documents/upload" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "files=@leave_policy.txt" \
  -F "department=HR" \
  -F "document_type=policy"
```

## 🏗️ System Architecture

```
Client UI / Admin UI
        │
        ▼
    FastAPI Backend
        │
        ▼
    LangChain + Groq LLM
        │
        ▼
    Pinecone Vector Store
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Groq API key for the model | Yes |
| `GROQ_MODEL` | Groq model name | Yes |
| `GOOGLE_API_KEY` | Google API key for embeddings | Optional |
| `OPENAI_API_KEY` | OpenAI API key | Optional (compatibility) |
| `OPENAI_MODEL` | OpenAI model name | Optional |
| `PINECONE_API_KEY` | Pinecone API key | Yes |
| `PINECONE_ENVIRONMENT` | Pinecone environment | Yes |
| `PINECONE_INDEX_NAME` | Pinecone index name | `orin-documents` |
| `SECRET_KEY` | JWT secret key | Yes |
| `DATABASE_URL` | Database connection string | `sqlite:///./orin.db` |
| `PORTAL_BASE_URL` | Internal portal URL | Optional |
| `PORTAL_API_KEY` | Internal portal API key | Optional |

## 🎯 Use Cases

### Government Offices
- Instant answers for policy, leave, and procedure queries
- Document-backed responses for internal and citizen services
- Centralized knowledge access for departments

### Private Organizations
- Employee self-service for HR and IT policies
- Automated support using uploaded documents
- Better coordination across departments

### Educational Institutions
- Student policy and administrative query support
- Document search for academic guidelines
- Faculty and staff assistance with internal processes

## 🧪 Testing

Run the tests:
```bash
pytest tests/
```

## 🚀 Deployment

1. Use production-ready secrets and HTTPS
2. Configure a persistent database such as PostgreSQL
3. Set up Pinecone index and backup strategy
4. Add app monitoring and logging

## 🤝 Contributing

1. Fork the repository
2. Create a new branch
3. Add your changes and tests
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For questions or issues, open an issue in this repository.

- [ ] Database integration (PostgreSQL)
- [ ] Advanced user management
- [ ] Multi-language support
- [ ] Voice interface integration
- [ ] Advanced analytics and reporting
- [ ] Workflow automation features
- [ ] Mobile application support