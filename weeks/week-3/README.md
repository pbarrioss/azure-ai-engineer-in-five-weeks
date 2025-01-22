# Week 3: Evaluating and Monitoring GenAI Systems 🛠️

## Table of Contents 📑
- [Overview](#overview-📋)
- [Learning Objectives](#learning-objectives-🎯)
- [Prerequisites](#prerequisites-📚)
- [Materials](#materials-📂)
- [In-Class Activities](#in-class-activities-🛠️)
- [Assignments](#assignments-📝)
- [Setup Instructions](#setup-instructions-⚙️)

---

## Overview 📋

In **Week 3**, we shift our focus to the **evaluation and monitoring** of the GenAI systems you have been building. By this point, you should already have:

- A **vector database** (Azure AI Search) set up with vectorization embedded.
- Integrated **GPT-4** (or GPT-4o).
- A working from scratch **Retrieval-Augmented Generation (RAG)** pattern from the prior weeks.

### Why Focus on Evaluation and Monitoring?

As your system grows in complexity—especially when incorporating multiple services and advanced LLMs—the need for **robust evaluation** and **traceability** increases. This week, you will learn to:

1. **Evaluate** your AI solutions using low-code tools like **AI Foundry**.
2. Implement **traceability** measures to capture every interaction in your RAG pipeline.
3. **Streamline your code** for better performance and maintainability.
4. Integrate feedback loops and telemetry data to ensure system **efficiency** and reliability.

---

## Learning Objectives 🎯

By the end of **Week 3**, you will be able to:

1. **Conduct Low-Code Evaluations**: Use **AI Foundry** and **promptflow** to assess LLM-generated outputs, measure quality, and iterate faster.
2. **Implement Traceability**: Leverage simple code decorators and AI Foundry’s backend for capturing interactions and analyzing RAG workflow performance.
3. **Enhance System Efficiency**: Diagnose and optimize API calls, reduce latency, and handle inbound/outbound requests more effectively.

---

## Prerequisites 📚

Before diving into Week 3:

- You should have **completed Week 2**, where you set up a working RAG pipeline, integrated Azure AI Search (with vectorization), and used GPT-4 for question answering.
- Have access to **Azure AI Foundry** (or plan to get it set up) for the low-code evaluation exercises.
- Familiarity with **promptflow** is recommended (we will use it as our orchestration tool for evaluations).

---

## Materials 📂

### Required Readings & Notebooks
1. **Microsoft Learn Documentation**:  
   - [Evaluate your Generative AI app](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/evaluate-generative-ai-app)  
     Outlines how to use existing datasets and CSV formats for easy evaluations.
2.  [Article by Pablo](https://pabloaicorner.hashnode.dev/building-an-effective-enterprise-llmslm-evaluation-framework-key-strategies-and-tools#heading-evaluating-the-retrieval-systemqa)  
  Explores how a validation framework improved the reliability of a Q&A system

---

## In-Class Activities 🛠️

During Day 3, we will focus on hands-on exercises that illustrate **evaluation and monitoring** in practice:

### 1. Learn by Industry Examples
- **Learn from the Customer**: We’ll review real-world lessons from MSFT on how proving Q&A system quality led to broader AI adoption and understand the value of telemetry and performance tracking when scaling solutions.

### 2.Evaluations
- **AI Foundry & promptflow**:  
  - We’ll use `promptflow` as the orchestration layer specifically for running large-scale evaluations.  
  - Review the pre-made `.csv` dataset containing fields (`question`, `truth`, `answer`, `context`).  
  - Learn how to feed data into AI Foundry to quickly gauge the accuracy and robustness of your RAG responses.

### 3. Traceability
- **Decorator-Driven Logging**: Implement a simple Python decorator to log interactions and maintain a record of all RAG calls.  
- **Advanced Logging in AI Foundry**: Explore how Foundry captures and correlates logs for deeper analysis of LLM behavior.

### 4. Baseline Data Review
- We provide a **baseline dataset** (synthetic data from HR documents, now in `.csv` format) for consistent evaluations.  
- You’ll see how to **simulate queries** and compare LLM-generated answers with “ground truth” in real-time.

---

## Assignments 📝

Please visit README.md in /homework -> (./weeks/week-3/homework/README.md) for more details.

> **Due Date**: Submit before the start of **Week 4**.

---

## Setup Instructions ⚙️

---

### By the End of Week 3

You will have:

- **Evaluation & Traceability**: In-depth understanding of how to measure and document the performance of your generative components.  
- **System Efficiency**: Insights gained from telemetry, logging, and debugging to further optimize your AI solution.  

Continue iterating on your solution, and be prepared to **scale your evaluations** and **monitoring** strategies as we move into the next phases of our AI journey!
