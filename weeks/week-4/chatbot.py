import os
import logging
import asyncio
import time
from typing import List, Optional

import streamlit as st
from pymongo import MongoClient
from pymongo.collection import Collection
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import urllib.parse

from src.aoai.aoai_helper import AzureOpenAIManager

# ----------------------------- #
#         Configuration         #
# ----------------------------- #

# Load environment variables
from dotenv import load_dotenv
load_dotenv(".env")

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Streamlit Page Configuration
st.set_page_config(
    page_title="AI Engineering in Five Weeks Chatbot 🚀",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Page Title and Subtitle
st.title("🤖 AI Engineering in Five Weeks Chatbot")

# ----------------------------- #
#     Initialize Session State  #
# ----------------------------- #

def initialize_session_state():
    """Initialize necessary session state variables."""
    # Initialize 'enable_cache' first to ensure it's available for the sidebar
    if "enable_cache" not in st.session_state:
        st.session_state["enable_cache"] = True  # Default value
        logger.info("Initialized 'enable_cache' to True.")
    
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        logger.info("Initialized 'chat_history'.")

    # Initialize MongoDB (CosmosDB) Manager
    if "cosmosdb_manager" not in st.session_state:
        try:
            st.session_state["cosmosdb_manager"] = initialize_cosmosdb_manager()
            logger.info("Connected to CosmosDB.")
        except Exception as e:
            logger.error(f"Failed to connect to CosmosDB: {e}")
            st.error("Failed to connect to the database. Please check your configuration.")
            st.stop()  # Stop execution if critical initialization fails
    
    # Initialize Azure OpenAI Manager
    if "azure_openai_client_4o" not in st.session_state:
        try:
            st.session_state["azure_openai_client_4o"] = AzureOpenAIManager(
                api_key=os.getenv('AZURE_OPENAI_KEY'),
                api_version=os.getenv('AZURE_OPENAI_API_VERSION', "2023-05-15"),
                azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
                embedding_model_name=os.getenv('AZURE_OPENAI_EMBEDDING_DEPLOYMENT'),
                completion_model_name=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_ID'),
            )
            logger.info("Azure OpenAI Manager initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Azure OpenAI Manager: {e}")
            st.error("Failed to initialize AI components. Please check your configuration.")
            st.stop()  # Stop execution if critical initialization fails
    
    # Initialize Azure AI Search Client
    if "search_client" not in st.session_state:
        try:
            st.session_state["search_client"] = SearchClient(
                endpoint=os.getenv("AZURE_AI_SEARCH_SERVICE_ENDPOINT"),
                index_name=os.getenv("AZURE_SEARCH_INDEX_NAME", "lab-ai-index"),
                credential=AzureKeyCredential(os.getenv("AZURE_AI_SEARCH_ADMIN_KEY")),
            )
            logger.info("Azure Search Client initialized.")
        except Exception as e:
            logger.error(f"Failed to initialize Azure Search Client: {e}")
            st.error("Failed to initialize search components. Please check your configuration.")
            st.stop()  # Stop execution if critical initialization fails
    
    # Initialize other session variables
    session_vars = [
        "conversation_history",
        "ai_response",
        "messages",
        "uploaded_files",
        "disable_chatbot",
        "case_ids",
        "pa_processing_results",
        "current_case_id",
        "initialized_default",
    ]
    
    initial_values = {
        "conversation_history": [],
        "ai_response": "",
        "messages": [
            {
                "role": "assistant",
                "content": "Hey, this is your AI assistant. Please look at the AI request submit and let's work together to make your content shine!",
            }
        ],
        "uploaded_files": [],
        "disable_chatbot": True,
        "case_ids": [],
        "pa_processing_results": {},
        "current_case_id": None,
        "initialized_default": False,
    }
    
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = initial_values.get(var, None)
            logger.info(f"Initialized '{var}' to default value.")

def initialize_cosmosdb_manager() -> Collection:
    """Initialize MongoDB connection and return the collection."""
    COSMOS_MONGO_USER = os.environ.get('COSMOS_MONGO_USER')
    COSMOS_MONGO_PWD = os.environ.get('COSMOS_MONGO_PWD')
    COSMOS_MONGO_SERVER = os.environ.get('COSMOS_MONGO_SERVER')
    DB_NAME = 'ExampleDB'
    COLLECTION_NAME = "ExampleCollection"

    if not all([COSMOS_MONGO_USER, COSMOS_MONGO_PWD, COSMOS_MONGO_SERVER]):
        logger.error("MongoDB environment variables are not fully set.")
        raise ValueError("Missing MongoDB configuration in environment variables.")

    mongo_conn = (
        "mongodb+srv://"
        + urllib.parse.quote(COSMOS_MONGO_USER)
        + ":"
        + urllib.parse.quote(COSMOS_MONGO_PWD)
        + "@"
        + COSMOS_MONGO_SERVER
        + "?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
    )

    mongo_client = MongoClient(mongo_conn)
    db = mongo_client[DB_NAME]
    collection = db[COLLECTION_NAME]

    if COLLECTION_NAME not in db.list_collection_names():
        db.create_collection(COLLECTION_NAME)
        logger.info(f"Created collection '{COLLECTION_NAME}'.")
    else:
        logger.info(f"Using existing collection: '{COLLECTION_NAME}'.")

    return collection

# ----------------------------- #
#         Helper Functions      #
# ----------------------------- #

def generate_embeddings(text: str) -> List[float]:
    """Generates an embedding vector for the given text using Azure OpenAI."""
    try:
        embedding_response = st.session_state["azure_openai_client_4o"].generate_embedding(text)
        logger.debug(f"Generated embeddings: {embedding_response.data[0].embedding}")
        return embedding_response.data[0].embedding
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        return []

def retrieve_documents_from_azure_ai_search(query: str) -> List[str]:
    """Retrieve relevant documents from Azure AI Search."""
    try:
        search_client = st.session_state["search_client"]
        semantic_config = os.getenv("AZURE_SEARCH_SEMANTIC_CONFIG_NAME", None)
        if semantic_config:
            search_results = search_client.search(
                search_text=query,
                top=5,
                query_type="semantic",
                query_caption="extractive",
                query_answer="extractive",
                semantic_configuration_name=semantic_config,
            )
            logger.info("Performed semantic search.")
        else:
            search_results = search_client.search(
                search_text=query,
                top=5,
            )
            logger.info("Performed keyword search.")
        documents = [doc.get("chunk", "") for doc in search_results]
        logger.info(f"Retrieved {len(documents)} documents from search.")
        return documents
    except Exception as e:
        logger.error(f"Error retrieving documents: {e}")
        st.error("Failed to retrieve documents. Please try again later.")
        return []

async def generate_llm_response(query: str, context: List[str]) -> str:
    """Generate a response using the LLM with retrieved context."""
    prompt = f"""
Context:
{context}

User Query:
{query}

Instructions:
- If sufficient context exists, provide an answer.
- If insufficient information, respond with "I'm sorry, I don't have enough information."
"""
    try:
        response = await st.session_state["azure_openai_client_4o"].generate_chat_response(
            query=prompt,
            conversation_history=[],
            system_message_content="You are an AI assistant specializing in clinical prior authorization processes.",
            max_tokens=2000,
            temperature=0.5,
            stream=False,  # Disable streaming for simplicity
        )
        # Handle response format
        if isinstance(response, dict):
            # Adjust based on actual response structure
            content = response.get("choices", [{}])[0].get("message", {}).get("content", "")
            logger.debug(f"LLM Response: {content.strip()}")
            return content.strip()
        elif isinstance(response, str):
            logger.debug(f"LLM Response: {response.strip()}")
            return response.strip()
        else:
            logger.error("Unexpected response format from LLM.")
            return "I'm sorry, I encountered an unexpected response format."
    except Exception as e:
        logger.error(f"Error generating LLM response: {e}")
        return "I'm sorry, but I encountered an error processing your request."

def store_response(query: str, response: str, context: List[str], collection: Collection):
    """Store the response in MongoDB for caching."""
    try:
        entry = {
            "query": query,
            "response": response,
            "context": context,
            "queryVector": generate_embeddings(query),
            "created_at": time.time(),
        }
        collection.insert_one(entry)
        logger.info("Stored response in cache.")
    except Exception as e:
        logger.error(f"Error storing response: {e}")

def search_cached_response(query: str, collection: Collection, similarity_threshold: float) -> Optional[str]:
    """Search MongoDB for cached responses with high similarity."""
    try:
        embedding = generate_embeddings(query)
        pipeline = [
            {
                "$vectorSearch": {
                    "index": "VectorSearchIndex",
                    "path": "queryVector",
                    "queryVector": embedding,
                    "numCandidates": 5,
                    "limit": 5,
                }
            },
            {
                "$project": {
                    "similarityScore": {"$meta": "searchScore"},
                    "response": 1,
                }
            },
        ]
        results = list(collection.aggregate(pipeline))
        if not results:
            logger.info("No cached responses found.")
            return None
        best_result = max(results, key=lambda x: x.get("similarityScore", 0))
        if best_result.get("similarityScore", 0) >= similarity_threshold:
            logger.info("Found a cached response with sufficient similarity.")
            return best_result.get("response", "")
        logger.info("No cached response met the similarity threshold.")
        return None
    except Exception as e:
        logger.error(f"Error during cache search: {e}")
        return None

def run_async(coro):
    """Run an async coroutine and return the result."""
    try:
        return asyncio.run(coro)
    except Exception as e:
        logger.error(f"Asyncio run failed: {e}")
        return "I'm sorry, I encountered an error processing your request."

async def chatbot_main(query: str) -> str:
    """Main function orchestrating retrieval and LLM response generation."""
    start_time = time.time()
    collection = st.session_state["cosmosdb_manager"]
    
    if st.session_state.get("enable_cache", True):
        similarity_threshold = st.session_state.get("similarity_threshold", 0.96)
        cached_response = search_cached_response(query, collection, similarity_threshold)
        if cached_response:
            duration = time.time() - start_time
            logger.info(f"Cached response retrieved in {duration:.2f}s.")
            return f"🗄️ **(Cached Response in {duration:.2f}s)**\n\n{cached_response}"
    
    retrieved_docs = retrieve_documents_from_azure_ai_search(query)
    if not retrieved_docs:
        logger.warning("No documents retrieved from Azure AI Search.")
        return "I'm sorry, I couldn't retrieve any relevant documents to answer your query."
    
    llm_response = await generate_llm_response(query, retrieved_docs)
    if llm_response:
        store_response(query, llm_response, retrieved_docs, collection)
        duration = time.time() - start_time
        logger.info(f"LLM response generated in {duration:.2f}s.")
        return f"⏳ **(LLM Response in {duration:.2f}s)**\n\n{llm_response}"
    else:
        return "I'm sorry, I couldn't generate a response at this time."

# ----------------------------- #
#          UI Components        #
# ----------------------------- #

def configure_sidebar():
    """Configures the sidebar with settings and file uploader."""
    with st.sidebar:
        st.title("Chat Settings & Tools")
        with st.expander("🔧 Caching Settings", expanded=True):
            # Safely access 'enable_cache' with a default value to prevent KeyError
            enable_cache = st.checkbox(
                "Enable Response Caching",
                value=st.session_state.get("enable_cache", True)
            )
            st.session_state["enable_cache"] = enable_cache
            st.markdown("_This enables caching via MongoDB to retrieve previous responses quickly._")
            
            st.divider()
            
            # Slider to set similarity threshold
            similarity_threshold = st.slider(
                "Set Similarity Threshold",
                min_value=0.0,
                max_value=1.0,
                value=st.session_state.get("similarity_threshold", 0.96),
                step=0.01
            )
            st.session_state["similarity_threshold"] = similarity_threshold
            
        st.divider()
        # Button to clear chat history
        if st.button("Clear Chat History"):
            st.session_state["chat_history"] = []
            st.success("Chat history cleared.")

def display_chat_interface():
    """Displays the chat interface and handles user interactions."""
    st.markdown("_Ask anything and let the AI respond with real-time retrieval & caching._")
    
    user_query = st.chat_input("Type your message here...")
    
    if user_query:
        st.session_state["chat_history"].append({"role": "user", "content": user_query})
        
        with st.chat_message("user"):
            st.markdown(user_query)
        
        with st.chat_message("assistant"):
            ai_response = run_async(chatbot_main(user_query))
            st.session_state["chat_history"].append({"role": "assistant", "content": ai_response})
            st.markdown(ai_response)

def display_chat_history():
    """Displays the entire chat history."""
    for message in st.session_state["chat_history"]:
        role, content = message["role"], message["content"]
        avatar = "🧑‍💻" if role == "user" else "🤖"
        with st.chat_message(role, avatar=avatar):
            st.markdown(content)

# ----------------------------- #
#            Main App           #
# ----------------------------- #

def main():
    """Main function to run the Streamlit app."""
    initialize_session_state()
    configure_sidebar()
    st.markdown("---")
    display_chat_interface()
    display_chat_history()

if __name__ == "__main__":
    main()