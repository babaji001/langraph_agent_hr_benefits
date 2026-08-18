
# config.py

import os

from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings

import chromadb


###############################################################
# LLM Configuration
###############################################################

LLM_MODEL = os.getenv(
    "LLM_MODEL",
    "qwen2.5:3b"
)

TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0"
    )
)

NUM_CTX = int(
    os.getenv(
        "NUM_CTX",
        "8192"
    )
)

NUM_PREDICT = int(
    os.getenv(
        "NUM_PREDICT",
        "1024"
    )
)

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434"
)


###############################################################
# Shared LLM
###############################################################

llm = ChatOllama(

    model=LLM_MODEL,

    base_url=OLLAMA_URL,

    temperature=TEMPERATURE,

    num_ctx=NUM_CTX,

    num_predict=NUM_PREDICT,

    streaming=True

)


###############################################################
# Embedding Model
###############################################################

embedding_model = OllamaEmbeddings(

    model="nomic-embed-text",

    base_url=OLLAMA_URL

)


###############################################################
# ChromaDB
###############################################################

CHROMA_PATH = "chromadb"


chroma_client = chromadb.PersistentClient(

    path=CHROMA_PATH

)


policy_collection = chroma_client.get_or_create_collection(

    "hr_policies"

)


###############################################################
# SQLite
###############################################################

DATABASE = "database/database/employee.db"


###############################################################
# Session Configuration
###############################################################

MAX_HISTORY = 10

SESSION_TIMEOUT = 1800


###############################################################
# ML Models
###############################################################

LEAVE_MODEL = "ml/models/leave_prediction.pkl"

CLAIMS_MODEL = "ml/models/claim_fraud.pkl"

RETIREMENT_MODEL = "ml/models/retirement_prediction_model.pkl"

BENEFITS_MODEL = "ml/models/benefits_recommendation.pkl"


###############################################################
# Confidence Thresholds
###############################################################

ML_THRESHOLD = 0.80

RAG_SCORE = 0.70


###############################################################
# Enterprise Defaults
###############################################################

DEFAULT_LANGUAGE = "English"

DEFAULT_COUNTRY = "US"

DEFAULT_TIMEZONE = "America/Chicago"


###############################################################
# Logging
###############################################################

LOG_LEVEL = "INFO"

ENABLE_TRACING = True

ENABLE_MEMORY = True

ENABLE_GUARDRAILS = True

ENABLE_FEEDBACK = True
