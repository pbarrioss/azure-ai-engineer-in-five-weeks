# Azure AI Engineering in 5 Weeks - Curriculum 🚀

Welcome to the Azure AI Engineering in 5 Weeks curriculum. This guide will help you navigate through the weekly lessons and practical sessions designed to enhance your skills in Azure AI services.

## Table of Contents 📅
- [Week 1: Introduction to Azure AI Services](#week-1-introduction-to-azure-ai-services-📘)
- [Week 2: Advanced AI System Design](#week-2-advanced-ai-system-design-🛠️)
- [Week 3: Operationalizing AI Systems](#week-3-operationalizing-ai-systems-⚙️)
- [Week 4: Optimizing and Fine-Tuning AI Models](#week-4-optimizing-and-fine-tuning-ai-models-🔧)
- [Week 5: Building AI Agents with Azure AI](#week-5-building-ai-agents-with-azure-ai-🤖)

## Week by Week 📅!
## Week 1: Introduction to Azure AI Services 📘
### Topics
- **Overview of Azure AI Services**:
  - Azure OpenAI Service: Leverage large language models for NLP tasks.
  - Azure AI Search: Implement AI-powered search within applications.
  - Azure AI Document Intelligence: Process and extract information from documents.
  - Azure AI Vision Services: Image and video analysis tools.
  - Azure AI Speech Services: Speech recognition and synthesis functionalities.
- **Cloud-Native AI Solution Architecture**:
  - Designing scalable and resilient AI solutions on Azure.
  - Integrating various Azure services in AI workflows.
- **Introduction to Retrieval-Augmented Generation (RAG) Patterns**:
  - Combining retrieval-based methods with generative AI for enhanced performance.
  - Implementing basic RAG architectures using Azure services.

### Practical Session
- **Building Your First Chatbot**:
  - Set up a virtual environment on your machine.
  - Configure necessary Azure services.
  - Develop a chatbot using Azure AI Search and Azure OpenAI through the Azure portal's UI.

### Homework
- **Mandatory**:
  - Reproduce the in-class chatbot deployment.
  - Upload sample data (e.g., HR documents) and index it using Azure AI Search.
  - Implement hybrid search combining vector-based and keyword-based retrieval.
  - Enable question-answering capabilities using Azure OpenAI as the reasoning engine.
- **Advanced (Optional)**:
  - Utilize the Azure AI Search SDK to programmatically push data.
  - Develop the chatbot in a code-first environment, deploying the final endpoint without relying on low-code tools.

> **Note**: For setup and detailed instructions, refer to the [Week 1 README](./weeks/week-1/README.md).

## Week 2: Advanced AI System Design 🛠️
### Topics
- **Deep Dive into RAG Patterns**:
  - Advanced techniques for implementing RAG architectures.
  - Enhancing retrieval accuracy and response generation.
- **Multimodal AI Integration**:
  - Combining text, image, and document data sources.
  - Implementing AI solutions that process and generate multiple data types.
- **LLM Routing and Caching**:
  - Strategies for efficient model selection and response caching.
  - Improving system performance and reducing latency.

### Practical Session
- **Developing a Compound AI System**:
  - Integrate multiple Azure AI services into a cohesive application.
  - Implement document intelligence for semantic data processing.
  - Set up Cosmos DB for data storage and consistency.
  - Apply LLM routing and caching mechanisms to optimize performance.

### Homework
- **Mandatory**:
  - Deploy your own compound AI system incorporating the discussed components.
  - Ensure seamless integration and functionality of all services.
- **Optional**:
  - Enhance your system by adding multimodal capabilities, such as image understanding, to enrich user interactions.

> **Note**: For setup and detailed instructions, refer to the [Week 2 README](./weeks/week-2/README.md).

## Week 3: Operationalizing AI Systems ⚙️
### Topics
- **Transition from MLOps to LLMOps**:
  - Understanding the lifecycle of large language models in production.
  - Implementing best practices for deployment and maintenance.
- **Monitoring and Management**:
  - Utilizing Azure Monitor, Log Analytics, and KQL for system observability.
  - Setting up end-to-end monitoring with OpenTelemetry and correlation IDs.
- **Continuous Evaluation and Benchmarking**:
  - Establishing frameworks for ongoing model assessment.
  - Using Azure AI Studio for evaluation and tracing.

### Practical Session
- **Implementing LLMOps Practices**:
  - Set up CI/CD pipelines with GitHub Actions for automated deployments.
  - Configure monitoring tools to track system performance.
  - Implement data drift detection and automated retraining workflows.

### Homework
- **Mandatory**:
  - Establish comprehensive monitoring and evaluation for your AI system.
  - Implement an enterprise-grade evaluation framework within your RAG pattern.
- **Optional**:
  - Integrate multimodal evaluation to monitor diverse data types effectively.

> **Note**: For setup and detailed instructions, refer to the [Week 3 README](./weeks/week-3/README.md).

## Week 4: Optimizing and Fine-Tuning AI Models 🔧
### Topics
- **Designing Scalable AI Systems**:
  - Architectural patterns for scalability in AI solutions.
  - Leveraging Azure's infrastructure to support large-scale AI deployments.
- **Fine-Tuning Large Language Models (LLMs)**:
  - Techniques for customizing LLMs for specific domain tasks.
  - Tools and resources available in Azure for model fine-tuning.
- **Enhancing RAG Pattern Performance**:
  - Methods to reduce latency and improve accuracy in RAG implementations.
  - Case studies demonstrating performance optimization.

### Practical Session
- **Fine-Tuning an Azure OpenAI Model**:
  - Hands-on experience in customizing an OpenAI model within Azure.
  - Evaluating performance improvements post fine-tuning.

### Homework
- **Mandatory**:
  - Fine-tune an Azure OpenAI model for a specific use case and measure the performance improvements. Submit a detailed analysis of the results.
- **Optional**:
  - Compare the fine-tuned model with a baseline to assess the impact of your optimizations. Explore further tuning parameters for enhanced performance.

> **Note**: For setup and detailed instructions, refer to the [Week 4 README](./weeks/week-4/README.md).

## Week 5: Building AI Agents with Azure AI 🤖
### Topics
- **Leveraging Small Language Models and Phi-3 Architecture**:
  - Introduction to small language models and their applications.
  - Understanding the Phi-3 architecture and its benefits.
- **Introduction to Multi-Agent Architectures**:
  - Concepts and design principles of multi-agent AI systems.
  - Use cases where multi-agent architectures provide advantages.
- **Developing Robust AI Agents Using Azure AI Studio**:
  - Tools and frameworks in Azure AI Studio for agent development.
  - Best practices for deploying AI agents in production environments.

### Practical Session
- **Prototyping a Multi-Agent System**:
  - Building a multi-agent system integrated into a RAG pattern.
  - Ensuring effective communication and coordination between agents.

### Homework
- **Mandatory**:
  - Prototype a multi-agent system using Azure AI Studio, demonstrating integration with RAG patterns. Provide documentation and a demo of the system.
- **Optional**:
  - Explore advanced features, such as agent collaboration strategies or incorporating additional modalities into the agents' capabilities.

> **Note**: For setup and detailed instructions, refer to the [Week 5 README](./weeks/week-5/README.md).