
from __future__ import annotations

import os
import re
from html import escape
from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse

BASE_DIR = Path(__file__).resolve().parent
RESUME_PATH = BASE_DIR / "resume_shwet.docx"

PROFILE = {
    "name": "Shwet Prakash",
    "title": "Senior Machine Learning Engineer",
    "subtitle": "Masters in Computer Science with 6 years of professional experience in Machine Learning, Data Science and LLMs",
    "summary": (
        "I design and ship production-grade LLM and ML systems: multi-agent workflows, hybrid RAG, "
        "voice AI, NLP model optimization, and scalable MLOps pipelines."
    ),
    "email": "shwet.prakash97@gmail.com",
    "phone": "+91-9566218457",
    "github": "https://github.com/Architectshwet",
    "linkedin": "https://www.linkedin.com/in/shwet-prakash-902b54111/",
}

SKILLS = [
    {
        "category": "Programming & Frameworks",
        "items": "Python, TypeScript, SQL, PyTorch, Scikit-learn, Pydantic, Asyncio, Pandas, NumPy",
    },
    {
        "category": "LLM & Generative AI",
        "items": (
            "LangChain, LangGraph, Multi-Agent Systems, RAG (Hybrid/Graph), OpenAI (GPT-4o/5.1), "
            "LiveKit (Voice AI), Hugging Face, Vector Databases (Qdrant, Pinecone, Chroma, FAISS), "
            "Prompt Engineering, Function Calling/Tool Use"
        ),
    },
    {
        "category": "Machine Learning",
        "items": (
            "Regression, Classification, Tree-Based Models, Bagging, Boosting, Ensembles, "
            "Clustering, Dimensionality Reduction"
        ),
    },
    {
        "category": "Deep Learning & NLP",
        "items": (
            "Transformers (BERT, RoBERTa), PEFT/LoRA Fine-tuning, Knowledge Distillation, "
            "Attention Mechanisms, RNN (LSTM/GRU), Word Embeddings, SetFit"
        ),
    },
    {
        "category": "ML Deployment & MLOps",
        "items": (
            "Docker, MLflow, DVC, CML, GitHub Actions, Amazon SageMaker, FastAPI, Flask, "
            "Model Quantization"
        ),
    },
    {
        "category": "Cloud, CI Tools & Backend",
        "items": (
            "AWS (EC2, ECS/Fargate, Lambda, S3, SES, API Gateway), NestJS, BullMQ, Redis, "
            "PostgreSQL, Neo4j, PrismaORM, CI/CD Pipelines"
        ),
    },
]

EXPERIENCE = [
    {
        "company": "Hexaware",
        "location": "Bangalore, India",
        "employment_type": "Full-time",
        "duration": "Feb 2026 - Present",
        "designation": "Senior Machine Learning Engineer",
        "technologies": (
            "Python, FastAPI, LangGraph, LangChain, Multi-Agent Systems, OpenAI (GPT-5.1), "
            "RAG, Docker, Azure, Pydantic"
        ),
        "highlights": [
            "Building agents for ITOps Automation",
        ],
    },
    {
        "company": "Quant.ai",
        "location": "Bangalore, India",
        "employment_type": "Full-time",
        "duration": "June 2025 - Jan 2026",
        "designation": "Senior Machine Learning Engineer",
        "technologies": (
            "Python, FastAPI, LangGraph, LangChain, Multi-Agent Systems, OpenAI (GPT-5.1), LiveKit, "
            "Hugging Face Transformers, Hybrid RAG, Qdrant, PostgreSQL, Asyncio, MLflow, Docker, "
            "GitHub Actions, AWS (EC2, ECS, ECR), Pydantic"
        ),
        "highlights": [
            (
                "Architected a multi-agent conversational AI for airline booking leveraging LangGraph Swarm, "
                "FastAPI streaming, and PostgreSQL persistence, implementing 4 specialized agents with async "
                "connection pooling and session state management to orchestrate stateful flight search, "
                "multi-city bookings, fare selection, change flight, check-in, and AlFursan loyalty workflows, "
                "deployed via Docker Compose with 75-80% latency reduction through parallel asyncio execution."
            ),
            (
                "Architected multi-agent voice AI system on LiveKit Cloud with 2 specialized agents "
                "(Category Discovery Agent and Product Suggestion Agent), 15 GPT-5.1 function tools, "
                "session-based state management, real-time voice pipeline (VAD->STT->LLM->TTS) with "
                "interruption handling, and middleware API integration for dynamic furniture catalog querying "
                "(decision tree navigation, 50+ categories, series-based filtering, nested product customization)."
            ),
            (
                "Developed intelligent product search using hybrid RAG with Qdrant vector DB, OpenAI embeddings "
                "(text-embedding-3-small), LLM-based query decomposition (GPT-4o-mini), metadata filtering "
                "(price/category/dimensions) and async FastAPI deployment with Docker"
            ),
            (
                "Engineered a production-grade MLOps pipeline to automate the deployment of Hugging Face Transformer "
                "models (BERT, RoBERTa) on AWS. Leveraged MLflow for experiment tracking and model versioning, "
                "containerized a FastAPI-based API with Docker, and built a full CI/CD workflow with GitHub Actions "
                "to enable zero-downtime deployments to a scalable AWS ECS and ECR environment."
            ),
        ],
    },
    {
        "company": "Ohai.ai",
        "location": "Kolkata, India",
        "employment_type": "Full-time",
        "duration": "Jan 2024 - May 2025",
        "designation": "Senior Machine Learning Engineer",
        "technologies": (
            "Python, FastAPI, Typescript, Nestjs, Langchain, Openai, GPT-4o, LLM, Agents, RAG, Vector Database, "
            "Pinecone, Multimodal AI, AWS (SES, S3, cloudfront, EC2), PrismaORM, Redis, BullMQ Pro, Docker, "
            "PostgreSQL, Knowledge graph"
        ),
        "highlights": [
            (
                "Designed and implemented a production-grade LLM agent stack using LangChain, tailored for a "
                "household assistant product with a modular toolchain of 25+ custom tools (calendar, reminders, "
                "messaging, email, household management, meal planning etc.), each built with conditional logic, "
                "and a dynamic system prompt enriched with contextual chat history to drive accurate tool selection "
                "and intelligent agent behavior."
            ),
            (
                "Implemented Redis-based low-latency caching to retain conversational context, optimizing AI "
                "assistant response times and minimizing database load in a real-time production environment."
            ),
            (
                "Architected scalable background processing pipelines using BullMQ Pro for async email scanning and "
                "multimodal document parsing (email/PDF/image -> LLM-based extraction); enabled job-level concurrency, "
                "fault-tolerant retries, smart rate limiting and downstream task orchestration"
            ),
            (
                "Built a robust LLM-based document understanding engine using Openai GPT-4o; with dynamic system "
                "prompt, multimodal inputs (image, email, text), schema-constrained JSON output, and downstream "
                "post-processing to extract structured actions (titles, events, todos, reminders)"
            ),
            (
                "Implemented a Neo4j-based knowledge graph system to model and query calendar events using "
                "LLM-generated Cypher queries, enabling semantic search over event metadata"
            ),
            (
                "Fine-tuned and benchmarked open-source LLMs using LoRA and Hugging Face for the task of classifying "
                "tools and their structured arguments"
            ),
            (
                "Integrated cloud-native infrastructure into a NestJS application, leveraging AWS services "
                "(S3, SES, CloudFront, Secrets Manager) to support secure file handling and email workflows, "
                "and utilized Prisma ORM across services for efficient database operations."
            ),
        ],
    },
    {
        "company": "Skuad",
        "location": "Bangalore, India",
        "employment_type": "Full-time",
        "duration": "Sept 2020 - Dec 2023",
        "designation": "Applied Data Scientist",
        "technologies": (
            "Python, Deep Learning, Machine Learning, NLP, MLOps, Generative AI, AWS (S3, ECR, Lambda, Fargate, "
            "EC2), Pytorch, Huggingface, Tensorflow, GPT-3, LLM, BERT, Langchain, CML, DVC, Mlflow, scikit learn, "
            "SQL, Boto3, Docker, Github actions, pandas, numpy, FAISS, chroma"
        ),
        "highlights": [
            (
                "Employed GPT-4 models to annotate job functions based on their job title, finetuned "
                "BERT/Roberta/Distibert models on this annotated data and applied post-training quantization "
                "techniques, resulting in a 2x enhancement in model inference latency on CPU instances while "
                "keeping 99.8% of the accuracy"
            ),
            (
                "Developed a SetFit Model (Few-Shot Learning approach) on a limited dataset for a "
                "email-classification problem, then compressed it with Knowledge Distillation which improved "
                "latency by 4x while maintaining an accuracy of 93%"
            ),
            (
                "Finetuned LLM models like GPT-3 to extract timelines and convert them into appropriate date and "
                "time format along with the rule based regex system from the Schedule based emails with an overall "
                "accuracy of 97%"
            ),
            (
                "Leveraged Base LLM models, like ChatGPT, for automated email response generation using dynamic "
                "few-shot examples driven by email categorization"
            ),
            (
                "Designed and implemented a scalable NLP API using FastAPI and Docker, deploying it on AWS Fargate "
                "with the aid of AWS ECS and ECR"
            ),
            (
                "Designed MLOPs pipeline using CML, DVC, AWS EC2 instances, and GitHub Actions to implement robust "
                "retraining schedules and strategies, ensuring continuous model accuracy and relevance"
            ),
        ],
    },
    {
        "company": "Kaleidofin Pvt Limited",
        "location": "Chennai, India",
        "employment_type": "Internship",
        "duration": "May 2019 - July 2020",
        "designation": "Data Science Research Intern",
        "technologies": (
            "Python, Machine Learning, Tensorflow, Postgres, MongoDB, Dash, flask, HDF5, pandas, numpy, folium"
        ),
        "highlights": [
            (
                "Developed a Mutual Fund Recommendation model to compute the XIRR of Mutual Funds based on the "
                "rolling window for different horizons on the NAV and forecasted future NAV with time series "
                "models with LSTMs"
            ),
            (
                "Developed ETL Pipeline of updating both the Mutual Funds NAV and XIRR returns data periodically and "
                "incorporated them in a Dash Web application which reduces computation time on 20 million data points "
                "by 90%"
            ),
            (
                "Incorporated HDF5 & Postgres which significantly reduced the space and improved querying speed by "
                "30% for Fund Database."
            ),
            (
                "Developed end to end Data Engineering and Machine Learning Modelling pipeline for Credit Risk "
                "prediction using MongoDB, Model Ensembling and Boosting Methods"
            ),
            "Implemented an intelligent Insurance Automation system with 100% accuracy and saved thousands of work hours annually",
            "Implemented Anomaly Detection, Payment Analytics and Payment Prediction Models as per the business usecase",
        ],
    },
]

PROJECTS = [
    {
        "title": "Banking Multi-Agent Assistant with LangChain Multi-Agent Supervisor Tool Pattern",
        "technologies": (
            "Python, LangChain, LangGraph, FastAPI, PostgreSQL, Docker, Server-Sent Events (SSE), "
            "Pydantic, Asyncio, Tool Calling"
        ),
        "highlights": [
            "Engineered a supervisor-first digital banking assistant in Python (LangChain/LangGraph), where a single BankingSupervisor handles authentication and routes each user turn to the correct workflow.",
            "Built tool-wrapped specialist agents (account_agent_tool, payments_agent_tool) to separate orchestration from domain logic for account services (profile, balances, transactions, cards) and payment flows (payees, transfers, bill pay).",
            "Designed a robust memory strategy using parent-thread checkpointing for the supervisor and isolated scoped specialist threads (:account, :payments) with suppressed specialist-level checkpoint mixing to avoid context bleed.",
            "Implemented persistent conversation state with PostgreSQL-backed checkpointing and shared session context via LangGraph Store (e.g., customer_id) for reliable multi-turn continuity.",
            "Shipped a developer-ready runtime with SSE streaming responses, web testing UI, Dockerized local setup, and seeded demo banking data for fast validation and onboarding."
        ],
        "links": [
            {
                "label": "GitHub Repository",
                "url": "https://github.com/Architectshwet/Banking-Multi-Agent-Assistant-with-LangChain-Multi-Agent-Supervisor-Tool-Pattern",
            }
        ],
    },
    {
        "title": "Reflection Agent using LangGraph StateGraph",
        "technologies": (
            "Python, LangGraph StateGraph, LangChain ToolNode, FastAPI, Tavily Search API, PostgreSQL, "
            "Asyncio, Docker, Server-Sent Events (SSE)"
        ),
        "highlights": [
            "Engineered a production-style reflection agent backend using LangGraph StateGraph, implementing an iterative reasoning loop (researcher -> tools -> critique -> revise/END) to improve response quality through self-critique.",
            "Integrated Tavily-powered web search via LangChain ToolNode to fetch real-time evidence during reasoning, enabling more accurate and context-grounded answers.",
            "Built a FastAPI streaming pipeline with Server-Sent Events to deliver live tool events and final responses, and added a built-in browser test UI at /web for rapid end-to-end validation.",
            "Implemented durable conversational memory using a remote PostgreSQL checkpointer, with persistent conversation_history and session_store tables to support multi-turn, memory-aware follow-up interactions.",
            "Designed for scale and deployment readiness with async PostgreSQL connection pooling, clean graph/tool/persistence layer separation, Dockerized setup, and health monitoring endpoint."
        ],
        "links": [
            {
                "label": "GitHub Repository",
                "url": "https://github.com/Architectshwet/reflection-agent-using-langgraph",
            }
        ],
    },
    {
        "title": "Production-Grade MLOps with Automated CI/CD",
        "technologies": (
            "Python, FastAPI, Docker, MLflow, GitHub Actions, AWS ECS Fargate, AWS EC2, AWS S3, "
            "AWS ECR, Prometheus, Grafana"
        ),
        "highlights": [
            "Built a production-grade end-to-end MLOps CI/CD pipeline automating ML model deployment from GitHub Pull Requests to production using GitHub Actions workflows.",
            "Implemented MLflow-based experiment tracking and model registry with stage-based governance (Staging/Production) for reproducible experimentation and controlled model lifecycle management.",
            "Developed containerized FastAPI inference services using Docker and deployed scalable serverless model-serving workloads on AWS ECS Fargate.",
            "Architected cloud infrastructure leveraging AWS EC2 for MLflow control plane, S3 for artifact storage, and ECR for secure Docker image registry management.",
            "Integrated Prometheus and Grafana monitoring stack for real-time observability, system health tracking, and production performance monitoring of deployed ML services."
        ],
        "links": [
            {
                "label": "Medium Article",
                "url": "https://medium.com/@shwet.prakash97/the-ultimate-guide-to-production-grade-mlops-a-fully-automated-ci-cd-pipeline-with-mlflow-github-54956235bd71",
            }
        ],
    },
    {
        "title": "Multimodal PDF RAG Chatbot",
        "technologies": (
            "Python, FastAPI, GPT-5.1, RAG, Qdrant, OpenAI Embeddings, PostgreSQL (Neon), "
            "Server-Sent Events (SSE), Docker, LangChain"
        ),
        "highlights": [
            "Built an end-to-end multimodal RAG pipeline that converts PDF pages into images, generates high-fidelity page descriptions, creates embeddings, and indexes them for semantic search.",
            "Designed page-level multimodal representation for every document page, using GPT-5.1 to describe each page and combining generated content with structured metadata to preserve source traceability and retrieval precision.",
            "Implemented history-aware query reformulation followed by top-k vector retrieval in Qdrant to consistently surface the most relevant pages for each user turn.",
            "Developed image-grounded answer generation that uses retrieved page images and rewritten user query to produce concise, evidence-based responses.",
            "Delivered a production-ready chat system with FastAPI streaming responses, persistent conversation memory in remote Neon PostgreSQL, and robust indexing/debug observability for quality control."
        ],
        "links": [
            {
                "label": "GitHub Repository",
                "url": "https://github.com/Architectshwet?tab=repositories",
            }
        ],
    },
    {
        "title": "Banking Multi-Agent Assistant with LangGraph StateGraph",
        "technologies": (
            "Python, LangGraph StateGraph, LangChain, FastAPI, PostgreSQL, Docker, Server-Sent Events (SSE), "
            "Pydantic, Asyncio, Tool Calling"
        ),
        "highlights": [
            "Architected an LLM-powered router-led LangGraph StateGraph that makes explicit stepwise decisions (CALL_AUTH, CALL_ACCOUNT, CALL_PAYMENTS, FINAL_RESPONSE) for transparent, controllable multi-agent orchestration.",
            "Built three specialist agent nodes (Authentication, Account, Payments) with domain-specific tools to handle secure auth-first flows, account insights (profile/balances/transactions/cards), and payment operations (payees, transfers, bill pay).",
            "Implemented advanced memory design with isolated specialist checkpointing (<thread_id>:auth|account|payments) plus shared parent session context via LangGraph Store for seamless cross-agent continuity in multi-turn conversations.",
            "Developed a streaming FastAPI backend with SSE and node-level event visibility, improving real-time UX and making graph execution/debugging significantly easier.",
            "Productionized the system using PostgreSQL-backed persistence, Dockerized environment, and seeded banking demo data to enable reproducible setup and realistic end-to-end testing."
        ],
        "links": [
            {
                "label": "GitHub Repository",
                "url": "https://github.com/Architectshwet/langgraph_stategraph_multiagent_banking",
            }
        ],
    },
    {
        "title": "Corrective RAG Chatbot with LangGraph",
        "technologies": (
            "Python, LangGraph, LangChain, ChromaDB, Tavily Search API, FastAPI, OpenAI Embeddings, "
            "Prompt Engineering, Docker"
        ),
        "highlights": [
            "Developed a Corrective RAG chatbot using LangGraph with graph-based orchestration for retrieval, document grading, web search fallback, and response generation.",
            "Implemented self-correcting retrieval logic by grading retrieved documents for relevance and triggering Tavily web search when internal knowledge retrieval failed.",
            "Built context-aware query reformulation to convert follow-up questions into standalone queries using conversation history for improved conversational retrieval.",
            "Integrated ChromaDB-based semantic search pipeline with embeddings retrieval, reducing hallucinations and improving factual grounding of LLM responses."
        ],
        "links": [
            {
                "label": "Medium Article",
                "url": "https://medium.com/@shwet.prakash97/build-a-corrective-rag-chatbot-with-langgraph-ee4cd4cf7144",
            }
        ],
    },
]

EDUCATION = {
    "degree": "B. Tech and M. Tech (Dual Degree) in Computer Science",
    "institution": "Indian Institute of Information Technology, Chennai",
    "duration": "2015 - 2020",
    "cgpa": "7.8",
    "coursework": (
        "Data Science, Machine Learning, Big Data, DBMS, Programming Languages, Object Oriented Programming"
    ),
}

app = FastAPI(title="Shwet Prakash | Senior ML Engineer", version="1.0.0")


def render_skill_cards() -> str:
    cards: list[str] = []
    for idx, skill in enumerate(SKILLS, start=1):
        items = re.split(r',\s*(?![^()]*\))', skill["items"])
        pills = "".join(f'<span class="pill">{escape(item.strip())}</span>' for item in items if item.strip())
        cards.append(
            f"""
            <article class="skill-card reveal" style="animation-delay: {(idx % 6) * 0.1}s">
                <div class="skill-icon">
                    <svg viewBox="0 0 24 24" width="20" height="20" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                </div>
                <h3>{escape(skill["category"])}</h3>
                <div class="pill-container">{pills}</div>
            </article>
            """
        )
    return "".join(cards)


def render_experience() -> str:
    blocks: list[str] = []
    for idx, role in enumerate(EXPERIENCE, start=1):
        points = "".join(f"<li>{escape(item)}</li>" for item in role["highlights"])
        tech_list = re.split(r',\s*(?![^()]*\))', role["technologies"])
        tech_pills = "".join(f'<span class="tech-pill">{escape(t.strip())}</span>' for t in tech_list if t.strip())
        blocks.append(
            f"""
            <div class="timeline-item reveal" style="animation-delay: {(idx % 6) * 0.1}s">
                <div class="timeline-dot"></div>
                <div class="timeline-date">{escape(role["duration"])}</div>
                <div class="timeline-content">
                    <h3>{escape(role["designation"])}</h3>
                    <h4>{escape(role["company"])} <span class="dot-divider">•</span> {escape(role["location"])} <span class="dot-divider">•</span> {escape(role["employment_type"])}</h4>
                    <div class="tech-stack-container">
                        {tech_pills}
                    </div>
                    <ul class="highlights">{points}</ul>
                </div>
            </div>
            """
        )
    return "".join(blocks)


def render_projects() -> str:
    cards: list[str] = []
    for idx, project in enumerate(PROJECTS, start=1):
        links = "".join(
            f'<a href="{escape(link["url"])}" target="_blank" rel="noopener noreferrer" class="btn-link">{escape(link["label"])} <svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg></a>'
            for link in project.get("links", [])
        )
        
        desc_html = f'<p style="margin-bottom: 0;">{escape(project["description"])}</p>' if project.get("description") else ""

        tech_stack_html = ""
        if project.get("technologies"):
            tech_list = re.split(r',\s*(?![^()]*\))', project["technologies"])
            tech_pills = "".join(
                f'<span class="tech-pill">{escape(t.strip())}</span>' for t in tech_list if t.strip()
            )
            tech_stack_html = f'<div class="project-tech-stack">{tech_pills}</div>'
        
        highlights_html = ""
        if project.get("highlights"):
            points = "".join(f"<li>{escape(item)}</li>" for item in project["highlights"])
            highlights_html = f'<ul class="highlights" style="margin-top: 1rem;">{points}</ul>'

        cards.append(
            f"""
            <article class="project-card reveal" style="animation-delay: {(idx % 6) * 0.1}s">
                <div class="project-top">
                    <div class="folder-icon">
                        <svg viewBox="0 0 24 24" width="28" height="28" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
                    </div>
                    <div class="project-links">{links}</div>
                </div>
                <h3>{escape(project["title"])}</h3>
                {desc_html}
                {tech_stack_html}
                {highlights_html}
            </article>
            """
        )
    return "".join(cards)


def page_html() -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="Portfolio of Shwet Prakash - Senior Machine Learning Engineer specializing in LLM systems, RAG, and MLOps." />
    <title>{escape(PROFILE["name"])} | Senior ML Engineer</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet" />
    <style>
        :root {{
            --bg-main: #0B1120;
            --bg-surface: #151E32;
            --bg-card: #1E293B;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
            --accent: #3B82F6;
            --accent-glow: rgba(59, 130, 246, 0.5);
            --secondary: #8B5CF6;
            --border: rgba(255, 255, 255, 0.08);
            --max-w: 1100px;
        }}
        
        * {{ box-sizing: border-box; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            margin: 0;
            background-color: var(--bg-main);
            color: var(--text-muted);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            overflow-x: hidden;
            background-image: radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.04), transparent 25%),
                              radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.04), transparent 25%);
        }}

        h1, h2, h3, h4, h5 {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--text-main);
            margin: 0;
        }}

        .container {{
            max-width: var(--max-w);
            margin: 0 auto;
            padding: 0 1.5rem;
        }}

        /* Navbar */
        nav {{
            position: fixed;
            top: 0; left: 0; right: 0;
            background: rgba(11, 17, 32, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border);
            z-index: 1000;
        }}
        .nav-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 70px;
            max-width: var(--max-w);
            margin: 0 auto;
            padding: 0 1.5rem;
        }}
        .logo {{ font-weight: 800; font-size: 1.25rem; color: var(--text-main); text-decoration: none; letter-spacing: -0.5px; }}
        .nav-links {{ display: flex; gap: 2rem; }}
        .nav-links a {{
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: color 0.2s ease;
        }}
        .nav-links a:hover, .nav-links a.active-nav {{ color: var(--accent); }}
        .nav-links a.active-nav {{ font-weight: 600; }}

        /* SPA Layout Sections */
        .page-section {{
            display: none;
            padding-top: 100px;
            padding-bottom: 4rem;
            min-height: calc(100vh - 70px);
        }}
        .page-section.active-section {{
            display: block;
        }}

        /* Hero Section */
        .hero {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            min-height: calc(100vh - 120px);
        }}
        .hero h2 {{
            color: var(--accent);
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            font-size: 1.1rem;
            letter-spacing: 1px;
            margin-bottom: 1rem;
        }}
        .hero h1 {{
            font-size: clamp(3rem, 6vw, 5rem);
            line-height: 1.1;
            letter-spacing: -1.5px;
            margin-bottom: 1rem;
            background: linear-gradient(to right, #F8FAFC, #94A3B8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero .subtitle {{
            font-size: clamp(1.5rem, 3vw, 2.5rem);
            color: var(--text-muted);
            margin-bottom: 1.5rem;
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 600;
        }}
        .hero p {{
            font-size: 1.1rem;
            max-width: 600px;
            margin-bottom: 2.5rem;
        }}
        .cta-group {{ display: flex; gap: 1rem; flex-wrap: wrap; }}
        .btn {{
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: 500;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s ease;
            font-size: 0.95rem;
        }}
        .btn-primary {{
            background: var(--accent);
            color: #fff;
            box-shadow: 0 0 20px var(--accent-glow);
        }}
        .btn-primary:hover {{ background: #2563EB; transform: translateY(-2px); box-shadow: 0 4px 25px var(--accent-glow); }}
        .btn-outline {{
            background: transparent;
            color: var(--text-main);
            border: 1px solid var(--border);
        }}
        .btn-outline:hover {{ background: var(--bg-surface); transform: translateY(-2px); }}

        /* Reusable Section Headers */
        .section-title {{
            font-size: 2rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 3rem;
            white-space: nowrap;
        }}
        .section-title::after {{
            content: "";
            height: 1px;
            width: 100%;
            background: var(--border);
            display: block;
        }}

        /* Skills */
        .skills-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }}
        .skill-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            transition: transform 0.3s ease, border-color 0.3s ease;
        }}
        .skill-card:hover {{ transform: translateY(-5px); border-color: var(--accent); }}
        .skill-icon {{
            color: var(--accent);
            margin-bottom: 1rem;
        }}
        .skill-card h3 {{ font-size: 1.1rem; margin-bottom: 1rem; }}
        .pill-container {{ display: flex; flex-wrap: wrap; gap: 0.5rem; }}
        .pill {{
            background: rgba(59, 130, 246, 0.1);
            color: #60A5FA;
            font-size: 0.8rem;
            padding: 0.25rem 0.75rem;
            border-radius: 999px;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }}

        /* Shared Highlights List */
        .highlights {{
            list-style-type: none;
            padding: 0; margin: 0;
            display: flex; flex-direction: column; gap: 0.5rem;
        }}
        .highlights li {{ position: relative; padding-left: 1.25rem; font-size: 0.95rem; color: #94A3B8; }}
        .highlights li::before {{
            content: "▹"; position: absolute; left: 0; top: 0;
            color: var(--accent); font-family: sans-serif; font-size: 1.1rem; line-height: 1.4;
        }}

        /* Experience Timeline */
        .timeline {{
            position: relative;
            max-width: 900px;
            margin: 0 auto;
        }}
        .timeline::before {{
            content: '';
            position: absolute;
            left: 0; top: 0; bottom: 0;
            width: 2px;
            background: var(--border);
        }}
        .timeline-item {{
            position: relative;
            padding-left: 3rem;
            padding-bottom: 3rem;
        }}
        .timeline-item:last-child {{ padding-bottom: 0; }}
        .timeline-dot {{
            position: absolute;
            left: -5px; top: 5px;
            width: 12px; height: 12px;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 0 4px var(--bg-main);
        }}
        .timeline-date {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 0.9rem;
            color: var(--accent);
            margin-bottom: 0.5rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        }}
        .timeline-content h3 {{ font-size: 1.4rem; margin-bottom: 0.25rem; }}
        .timeline-content h4 {{
            font-size: 1rem; color: var(--text-muted);
            font-weight: 400; margin-bottom: 1rem;
        }}
        .dot-divider {{ color: #475569; margin: 0 0.5rem; }}
        .tech-stack-container {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin-bottom: 1rem; }}
        .tech-pill {{
            background: var(--bg-card);
            color: #CBD5E1;
            font-size: 0.75rem;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            border: 1px solid var(--border);
        }}

        /* Projects List Design */
        .projects-list {{
            display: flex;
            flex-direction: column;
            gap: 2rem;
            max-width: 950px;
            margin: 0 auto;
        }}
        .project-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            display: flex; flex-direction: column;
            transition: all 0.3s ease;
        }}
        .project-card:hover {{ transform: translateY(-5px); background: var(--bg-card); }}
        .project-top {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }}
        .folder-icon {{ color: var(--accent); }}
        .project-card h3 {{ font-size: 1.4rem; margin-bottom: 0.75rem; }}
        .project-card p {{ font-size: 0.95rem; line-height: 1.6; color: #94A3B8; }}
        .project-tech-stack {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.75rem 0 1rem; }}
        .btn-link {{
            color: var(--text-main); text-decoration: none;
            display: inline-flex; align-items: center; gap: 0.3rem;
            font-size: 0.85rem; font-weight: 500;
            transition: color 0.2s;
        }}
        .btn-link:hover {{ color: var(--accent); }}

        /* Education & Contact */
        .edu-grid {{
            display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;
        }}
        .edu-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 2rem;
            text-align: left;
        }}
        .edu-card h3 {{ font-size: 1.3rem; margin-bottom: 0.5rem; }}
        .edu-card p {{ margin-bottom: 0.5rem; }}
        .edu-card a {{ color: var(--accent); text-decoration: none; transition: color 0.2s; }}
        .edu-card a:hover {{ color: #60A5FA; }}

        /* Footer */
        footer {{
            text-align: center; padding: 2rem;
            border-top: 1px solid var(--border);
            font-size: 0.85rem; color: #475569;
            margin-top: 4rem;
        }}

        /* Animations connected to Active Section Load */
        .reveal {{ opacity: 0; }}
        .active-section .reveal {{
            animation: revealAnim 0.6s ease-out forwards;
        }}
        
        @keyframes revealAnim {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        /* Mobile Adjustments */
        @media (max-width: 768px) {{
            .nav-content {{ flex-direction: column; height: auto; padding: 1rem; }}
            .nav-links {{ display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap; justify-content: center; }}
            .page-section {{ padding-top: 140px; }}
            .hero h1 {{ font-size: 2.5rem; }}
            .hero .subtitle {{ font-size: 1.5rem; }}
            .edu-grid {{ grid-template-columns: 1fr; }}
            .timeline {{ padding-left: 1rem; }}
            .timeline-item {{ padding-left: 2rem; }}
            .project-card {{ padding: 1.5rem; }}
        }}
    </style>
</head>
<body>
    <nav>
        <div class="nav-content">
            <a href="#about" class="logo">Home</a>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#experience">Experience</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </div>
        </div>
    </nav>

    <div class="container">
        <!-- About Section -->
        <div class="page-section active-section" id="about">
            <header class="hero">
                <h2 class="reveal">Hi, my name is</h2>
                <h1 class="reveal" style="animation-delay: 0.1s">{escape(PROFILE["name"])}.</h1>
                <div class="subtitle reveal" style="animation-delay: 0.2s">{escape(PROFILE["title"])}</div>
                <p class="reveal" style="animation-delay: 0.3s">{escape(PROFILE["summary"])}<br><br>{escape(PROFILE["subtitle"])}.</p>
                
                <div class="cta-group reveal" style="animation-delay: 0.4s">
                    <a class="btn btn-primary" href="/resume">
                        <svg viewBox="0 0 24 24" width="18" height="18" stroke="currentColor" stroke-width="2" fill="none"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
                        Download Resume
                    </a>
                    <a class="btn btn-outline" href="{escape(PROFILE["linkedin"])}" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                    <a class="btn btn-outline" href="{escape(PROFILE["github"])}" target="_blank" rel="noopener noreferrer">GitHub</a>
                </div>
            </header>
        </div>

        <!-- Skills Section -->
        <div class="page-section" id="skills">
            <section>
                <h2 class="section-title reveal">Technical Arsenal</h2>
                <div class="skills-grid">
                    {render_skill_cards()}
                </div>
            </section>
        </div>

        <!-- Experience Section -->
        <div class="page-section" id="experience">
            <section>
                <h2 class="section-title reveal">Where I've Worked</h2>
                <div class="timeline">
                    {render_experience()}
                </div>
            </section>
        </div>

        <!-- Projects Section -->
        <div class="page-section" id="projects">
            <section>
                <h2 class="section-title reveal">Featured Projects</h2>
                <div class="projects-list">
                    {render_projects()}
                </div>
            </section>
        </div>

        <!-- Contact & Education Section -->
        <div class="page-section" id="contact">
            <section>
                <h2 class="section-title reveal">Education & Contact</h2>
                <div class="edu-grid">
                    <article class="edu-card reveal">
                        <h3>{escape(EDUCATION["degree"])}</h3>
                        <p style="color: var(--text-main); font-weight: 500;">{escape(EDUCATION["institution"])}</p>
                        <p><strong>Timeline:</strong> {escape(EDUCATION["duration"])}</p>
                        <p><strong>CGPA:</strong> <span style="color: var(--accent); font-weight: 600;">{escape(EDUCATION["cgpa"])}</span></p>
                        <p style="margin-top: 1rem; font-size: 0.9rem;"><strong>Coursework:</strong> {escape(EDUCATION["coursework"])}</p>
                    </article>
                    <article class="edu-card reveal" style="animation-delay: 0.1s">
                        <h3>Get In Touch</h3>
                        <p style="margin-bottom: 1.5rem;">I'm currently looking for new opportunities. Whether you have a question or just want to say hi, I'll try my best to get back to you!</p>
                        <p><strong>Email:</strong> <a href="mailto:{escape(PROFILE["email"])}">{escape(PROFILE["email"])}</a></p>
                        <p><strong>Phone:</strong> <a href="tel:{escape(PROFILE["phone"])}">{escape(PROFILE["phone"])}</a></p>
                        <p><strong>GitHub:</strong> <a href="{escape(PROFILE["github"])}" target="_blank" rel="noopener noreferrer">@Architectshwet</a></p>
                    </article>
                </div>
            </section>
        </div>
    </div>

    <footer>
        <p>Built with FastAPI & Python • Designed for performance and style.</p>
    </footer>

    <!-- Single Page App Routing Script -->
    <script>
        function showSection(sectionId) {{
            // 1. Hide all main sections
            document.querySelectorAll('.page-section').forEach(sec => {{
                sec.classList.remove('active-section');
            }});

            // 2. Remove active styling from nav links
            document.querySelectorAll('.nav-links a').forEach(link => {{
                link.classList.remove('active-nav');
            }});

            // 3. Show targeted section
            const targetSec = document.getElementById(sectionId);
            if (targetSec) {{
                targetSec.classList.add('active-section');
            }}

            // 4. Highlight the active nav link
            const navLink = document.querySelector(`.nav-links a[href="#${{sectionId}}"]`);
            if (navLink) {{
                navLink.classList.add('active-nav');
            }}

            // 5. Instantly jump exactly to the top
            window.scrollTo(0, 0);

            // 6. Update URL Hash silently 
            if (history.pushState) {{
                history.pushState(null, null, '#' + sectionId);
            }} else {{
                window.location.hash = '#' + sectionId;
            }}
        }}

        // Setup Event Listeners and Initial Load
        window.addEventListener('DOMContentLoaded', () => {{
            let hash = window.location.hash.substring(1);
            if (!hash || !['about', 'skills', 'experience', 'projects', 'contact'].includes(hash)) {{
                hash = 'about';
            }}
            showSection(hash);

            // Bind click events to nav and logo 
            document.querySelectorAll('.nav-links a, .logo').forEach(link => {{
                link.addEventListener('click', (e) => {{
                    const href = link.getAttribute('href');
                    if (href && href.startsWith('#')) {{
                        e.preventDefault();
                        showSection(href.substring(1));
                    }}
                }});
            }});
        }});

        // Handle browser back/forward buttons seamlessly
        window.addEventListener('hashchange', () => {{
            let hash = window.location.hash.substring(1);
            if (hash && ['about', 'skills', 'experience', 'projects', 'contact'].includes(hash)) {{
                showSection(hash);
            }}
        }});
    </script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def home() -> HTMLResponse:
    return HTMLResponse(content=page_html())


@app.get("/web", response_class=HTMLResponse)
def web() -> HTMLResponse:
    return HTMLResponse(content=page_html())


@app.get("/index", include_in_schema=False)
def index_redirect() -> RedirectResponse:
    return RedirectResponse(url="/web", status_code=307)


@app.get("/resume")
def download_resume():
    if RESUME_PATH.exists():
        return FileResponse(path=RESUME_PATH, filename=RESUME_PATH.name)
    return HTMLResponse(
        content="<h3>Resume file not found.</h3>",
        status_code=404,
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8008"))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
