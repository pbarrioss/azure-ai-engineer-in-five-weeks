# Week 1: Introduction to Azure AI Services 📘

## Table of Contents 📑
- [Overview](#overview-📋)
- [Learning Objectives](#learning-objectives-🎯)
- [Prerequisites](#prerequisites-📚)
- [Materials](#materials-📂)
- [In-Class Activities](#in-class-activities-🛠️)
- [Assignments](#assignments-📝)
- [Setup Instructions](#setup-instructions-⚙️)

## Overview 📋
In Week 1, we focus on introducing Azure AI Services, laying the foundation for building intelligent, scalable AI solutions. Key topics include exploring Azure AI Foundry, Azure OpenAI Service, Azure AI Search, Document Intelligence, Vision Services, and Speech Services. This week provides an in-depth understanding of how Azure AI integrates various tools to enable cloud-native AI architectures.

We will emphasize hands-on learning by implementing Retrieval-Augmented Generation (RAG) patterns in a low-code environment, using Azure AI Foundry as the development and deployment platform. You'll also explore the latest Azure OpenAI models, integrate data retrieval capabilities through Azure AI Search, and understand the complete end-to-end orchestration of AI workflows.

## Learning Objectives 🎯
- **Deepen Your Azure AI Foundations**: Gain hands-onexperience using essential Azure AI services.  
- **Design Cloud-Native Solutions**: Harness Azure AI Foundry and other foundational tools to create scalable, low-code AI applications.  
- **Implement RAG Architectures**: Combine retrieval and generation to deliver intelligent, context-sensitive responses.  
- **Leverage Azure AI Search**: Utilize vector-based and keyword-based retrieval techniques for accurate and relevant search capabilities.  
- **Explore Unified AI Development**: See how Azure Foundry unifies the entire AI workflow, enabling faster prototyping and deployment.  

## Prerequisites 📚
To make the most of this session, you should have:

- **AI Basics**: A foundational understanding of AI and machine learning concepts, such as natural language processing (NLP) and document retrieval.
- **Cloud Fundamentals**: Familiarity with cloud computing concepts and basic experience with Azure services, including creating and managing resources.
- **Access Requirements**:
  - Ensure you have access to the Azure AI Foundry platform.
  - Set up an Azure subscription with permissions to deploy and use services like Azure AI Search and Azure OpenAI.
> For more details, see the [Setup Instructions](#setup-instructions-⚙️).

## Materials 📂
- **Slides**: [Link to presentation slides]
- **Readings**: 
    - **Get Started with Azure AI Services**: A comprehensive learning path introducing Azure AI services and their applications. [Learn more](https://learn.microsoft.com/en-us/training/paths/get-started-azure-ai/)
    - **Retrieval-Augmented Generation in Azure AI Search**: An in-depth article on implementing RAG patterns using Azure AI Search. [Learn more](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
    - **Retrieval-Augmented Generation in Azure AI Foundry Portal**: An article introducing RAG for use in generative AI applications within Azure AI Foundry. [Learn more](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/retrieval-augmented-generation)
- **Additional Resources**: 
    - **Azure AI Foundry**: Learn how to use the most comprehensive AI platform. [Learn more](https://learn.microsoft.com/en-us/azure/ai-studio/)
    - **Azure OpenAI Service**: Leverage large language models for NLP tasks. [Learn more](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
    - **Azure AI Search**: Implement AI-powered search within applications. [Learn more](https://learn.microsoft.com/en-us/azure/search/search-what-is-azure-search)
    - **Azure AI Document Intelligence**: Process and extract information from documents. [Learn more](https://azure.microsoft.com/en-us/products/ai-services/ai-document-intelligence)
    - **Azure AI Vision Services**: Image and video analysis tools. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
    - **Azure AI Speech Services**: Speech recognition and synthesis functionalities. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)

## In-Class Activities 🛠️
This session guides you through building a low-code chatbot using Azure AI Foundry and Azure OpenAI. Below is an overview:

### Configuring Azure AI Services
- Set up foundational services, including Azure AI Search, Azure OpenAI, and Azure AI Document Intelligence.
- Enable data ingestion and indexing capabilities in Azure AI Search for your project.

### Data: Contoso Employee Handbook
- The folder `assets/contoso_data` contains PDFs with employee benefits, handbook policies, and other related materials.
- These documents will be used to showcase Retrieval-Augmented Generation (RAG), enabling the chatbot to provide data-driven answers.

### Developing the Chatbot
- Use Contoso HR documents as sample data to simulate real-world scenarios.
- Integrate vectorized and contextual indexing with Azure AI Search to retrieve precise and relevant responses.
- Deploy and test the chatbot, leveraging the OpenAI reasoning engine to answer user queries based on the embedded Contoso data.

## Assignments 📝
- **Homework**:
  - Reproduce the in-class chatbot deployment.
  - Upload sample data from the `assets/contoso_data` folder and index it using Azure AI Search.
  - Implement hybrid search, combining vector-based and keyword-based retrieval.
  - Enable question-answering capabilities using Azure OpenAI as the reasoning engine.
- **Due Date**: Before the start of Week 2.

## Setup Instructions ⚙️

To participate effectively in the upcoming session, please ensure that you have the following prerequisites in place and follow the setup instructions for each Azure AI service we'll be using.

### Prerequisites 📚

- **Azure Subscription**: Ensure you have an active Azure subscription. If you don't have one, you can create a free account [here](https://azure.microsoft.com/free/).

- **Azure Portal Access**: Familiarize yourself with the [Azure Portal](https://portal.azure.com/), as it will be used for resource management.

- **Development Environment**: Set up a development environment with the following tools:
  - **Visual Studio Code**: Download and install from [here](https://code.visualstudio.com/).
  - **Azure CLI**: Install the Azure Command-Line Interface from [here](https://learn.microsoft.com/cli/azure/install-azure-cli).

### Azure AI Services Setup

To effectively participate in our upcoming session, please ensure you have the following prerequisites and complete the setup for each Azure AI service as outlined below.

### Prerequisites 📚

- **Azure Subscription**: Ensure you have an active Azure subscription. If you don't have one, you can create a free account [here](https://azure.microsoft.com/free/).

- **Azure Portal Access**: Familiarize yourself with the [Azure Portal](https://portal.azure.com/), as it will be used for resource management.

### Azure AI Services Setup

We'll be working with several Azure AI services. Please follow the setup instructions for each service below:

#### 1. Azure AI Foundry

Azure AI Foundry is a comprehensive platform for building AI solutions.

- **Setup Instructions**:
  1. **Create an AI Hub**: Follow the quickstart guide to create a new AI Hub and Project. [Learn more](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/create-projects?tabs=ai-studio)
  2. **Configure Resources**: Set up necessary resources like AI Services, storage accounts, and Azure AI Search as per your project requirements.

#### 2. Azure OpenAI Service

Azure OpenAI Service allows you to leverage large language models for NLP tasks.

- **Setup Instructions**:
  1. **Create a Resource**: Follow the instructions to create an Azure OpenAI Service resource. [Learn more](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource)
  2. **Deploy a Model**: After creating the resource, deploy a model suitable for your application needs.

#### 3. Azure AI Search

Azure AI Search enables AI-powered search within applications.

- **Setup Instructions**:
  1. **Create a Search Service**: Set up a new Azure AI Search service through the Azure portal. [Learn more](https://learn.microsoft.com/en-us/azure/search/search-create-service-portal)
  2. **Configure Indexes**: Define and configure indexes based on your data requirements. [Learn more](https://learn.microsoft.com/en-us/azure/search/search-get-started-portal)




