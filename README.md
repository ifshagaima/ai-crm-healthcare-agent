# AI CRM System (Healthcare Representative Assistant)

## Project Overview

This project is an AI-powered CRM system designed to assist healthcare representatives in managing interactions with healthcare professionals (HCPs). The system allows users to log interactions, edit notes, view interaction history, schedule follow-ups, and summarize notes using an AI agent.

The backend is built using **FastAPI**, and the AI agent architecture is designed using **LangGraph** tools.

---

## Features

* Log interaction with healthcare professionals
* Edit interaction notes
* View interaction history
* Schedule follow-up meetings
* Summarize interaction notes

---

## Tech Stack

Frontend: React (optional UI)
Backend: FastAPI
AI Agent Framework: LangGraph
Language: Python

---

## Project Structure

```
AI_CRM_PROJECT
│
├── main.py          # FastAPI backend APIs
├── agent.py         # LangGraph tools and agent simulation
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## Installation

Clone the repository:

```
git clone <your-repository-link>
cd AI_CRM_PROJECT
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Backend Server

Start the FastAPI server:

```
uvicorn main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

## Running the AI Agent

Run the LangGraph agent:

```
python agent.py
```

This will simulate the AI agent calling one of the CRM tools.

---

## LangGraph Tools Implemented

The system includes the following AI tools:

1. Log Interaction
2. Edit Interaction
3. View Interaction History
4. Schedule Follow-up
5. Summarize Notes

These tools allow the AI agent to manage CRM tasks dynamically.

---

## System Architecture

User
↓
Frontend UI
↓
FastAPI Backend
↓
LangGraph Agent
↓
Tool Execution
↓
CRM Data

---

## Demo

The system demonstrates how an AI agent can automate CRM workflows for healthcare representatives by selecting the appropriate tools to perform tasks.

---

## Author

Developed as part of an AI CRM assignment.
