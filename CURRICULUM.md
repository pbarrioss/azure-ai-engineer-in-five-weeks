# Azure AI Engineering in 5 Weeks - Curriculum 🚀

Welcome to the Azure AI Engineering in 5 Weeks curriculum. This guide will help you navigate through the weekly lessons and practical sessions designed to enhance your skills in Azure AI services.

# Table of Contents 📅
- [Week 1: Introduction to Azure AI Services](#week-1-introduction-to-azure-ai-services-📘)
- [Week 2: Advanced AI System Design](#week-2-advanced-ai-system-design-🛠️)
- [Week 3: Operationalizing AI Systems](#week-3-operationalizing-ai-systems-⚙️)
- [Week 4: Optimizing and Fine-Tuning AI Models](#week-4-optimizing-and-fine-tuning-ai-models-🔧)
- [Week 5: Building AI Agents with Azure AI](#week-5-building-ai-agents-with-azure-ai-🤖)

# Week by Week 📅

## Week 1: Introduction to Azure AI Services 📘
### Topics
- **Overview of Azure AI Services**:
  - Azure AI Foundry: Leran how to use the most comprehensive AI platform.
  - Azure OpenAI Service: Leverage large language models for NLP tasks.
  - Azure AI Search: Implement AI-powered search within applications.
  - Azure AI Document Intelligence: Process and extract information from documents.
  - Azure AI Vision Services: Image and video analysis tools.
  - Azure AI Speech Services: Speech recognition and synthesis functionalities.
- **Introduction to Retrieval-Augmented Generation (RAG) Patterns**:
  - Combining retrieval-based methods with generative AI for enhanced performance.
  - Implementing basic RAG architectures using Azure services.

### Practical Session
- **Building Your First Chatbot**:
  - Configure necessary Azure services.
  - Develop a chatbot using Azure AI Search and Azure OpenAI through the Azure AI foundry portal's UI.

### Homework
  - Reproduce the in-class chatbot deployment.
  - Upload sample data (Contoso HR documents) and index it using Azure AI Search.
  - Implement hybrid search combining vector-based and keyword-based retrieval.
  - Enable question-answering capabilities using Azure OpenAI as the reasoning engine.
    - Complete the assignments in the `notebook_homework.ipynb` file located in the `weeks/week-1` folder.


> **Note**: For setup and detailed instructions, refer to the [Week 1 README](./weeks/week-1/README.md).

## Week 2: Advanced AI System Design 🛠️
### Topics
- **Introduction to Orchestration Frameworks**:
  - **Semantic Kernel**: Explore Microsoft's open-source framework that facilitates the integration of large language models (LLMs) with conventional programming languages, enabling the creation and orchestration of complex AI solutions.
- **Enhancing Chatbot Functionality with Multimodality**:
  - **Multimodal AI Integration**: Learn how to extend your chatbot's capabilities by incorporating multiple data types, such as text, images, and documents, to provide richer and more context-aware interactions.
  - **Azure AI Services**: Utilize services like Azure AI Vision and Azure AI Content Understanding to process and analyze diverse data modalities.

### Practical Session
- **Upgrading Your Chatbot with Semantic Kernel**:
  - **Integration**: Rebuild the chatbot developed in Week 1 by incorporating Semantic Kernel as the orchestrator, allowing for seamless interaction between various AI services and data modalities.
  - **Multimodal Capabilities**: Enhance the chatbot to process and respond to inputs beyond text, such as images and documents, utilizing Azure AI Services.

### Homework
  - **Implement Multimodal Features**: Extend your chatbot to handle at least two data modality (e.g., image and document) using Semantic Kernel and Azure AI Services. Complete the assignments in the `notebook_homework.ipynb` file located in the `weeks/week-2` folder.
  - **Advanced (Optional)**: Deploy the chatbot using the Semantic Kernel framework and streamlit containerized with Azure App Services or Azure Container Apps.

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

## Week 4: Optimizing AI Systems 🔧
### Topics
- **Designing Scalable AI Systems**:
  - Architectural patterns for scalability in AI solutions.
  - Leveraging Azure's infrastructure to support large-scale AI deployments.
- **Leveraging Small Language Models**:
  - Introduction to small language models and their applications.
  - Understanding the Phi-4 architecture and its benefits.
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
- **Understanding Agent Architectures**:
  - **Single-Agent Systems**: Explore the structure and functionality of standalone AI agents, including their decision-making processes and applications.
  - **Multi-Agent Systems**: Delve into systems where multiple AI agents interact, collaborate, or compete to achieve individual or collective goals.

- **Designing Multi-Agent System Architectures on Azure**:
  - **System Design**: Learn to architect multi-agent applications using Azure services, ensuring scalability, security, and efficiency.
  - **Communication Protocols**: Understand the methods and protocols that facilitate effective communication between agents.
  - **Coordination Strategies**: Study strategies for coordinating tasks among agents to optimize performance and resource utilization.

- **Quickstart: Building Agents in Azure**:
  - **Azure AI Agent Service**: Introduction to Azure's fully managed service for building, orchestrating, and scaling AI agents.
  - **Development Tools**: Overview of tools like Azure AI Foundry and Azure AI Studio for agent development.
  - **Deployment Best Practices**: Guidelines for deploying AI agents in production environments, focusing on reliability and performance.
### Practical Session
- **Prototyping a Multi-Agent System**:
  - **Integration with RAG Patterns**: Implement a multi-agent system that utilizes Retrieval-Augmented Generation (RAG) to enhance information retrieval and response generation.
  - **Agent Collaboration**: Set up agents with distinct roles that collaborate to complete complex tasks, demonstrating effective inter-agent communication.
  - **Azure Services Utilization**: Leverage Azure AI Agent Service and other relevant Azure services to build and deploy your multi-agent system.
### Homework
- **Mandatory**:
  - **Prototype Development**: Develop a multi-agent system using Azure AI Foundry, showcasing integration with RAG patterns.
  - **Documentation**: Provide comprehensive documentation detailing the system architecture, agent roles, communication protocols, and deployment process.
  - **Demonstration**: Prepare a demo that illustrates the functionality and effectiveness of your multi-agent system.

- **Optional**:
  - **Advanced Features Exploration**: Investigate and implement advanced features such as complex agent collaboration strategies, incorporating additional data modalities (e.g., visual or auditory data), or enhancing agent learning capabilities.

> **Note**: For setup and detailed instructions, refer to the [Week 5 README](./weeks/week-5/README.md).


