# AI News Agent 🇩🇪🤖

An autonomous AI agent that collects German news articles, summarizes them, translates the content into Polish, creates German vocabulary learning materials, generates bilingual audio, and sends a daily email briefing.

The project combines LLMs, automation, text processing, speech synthesis and email delivery into an end-to-end AI workflow.

---

## Features

- Automatically collects German news from RSS feeds
- Selects the most relevant article using an AI ranking agent
- Generates a German B2-level summary
- Translates the summary into Polish
- Extracts useful German vocabulary for language learning
- Generates bilingual audio:
  - German summary
  - Polish translation
  - Vocabulary examples
- Sends a daily email briefing with:
  - original article link
  - German summary
  - Polish translation
  - vocabulary list
  - audio attachment
- Runs automatically using Windows Task Scheduler

---

# Architecture

```text
RSS Feed
    |
    v
News Collection Service
    |
    v
News Ranking Agent
    |
    v
Ollama LLM
(qwen2.5:7b)
    |
    +----------------+
    |                |
    v                v

Summary Agent   Vocabulary Agent
    |
    v
Translation Agent
    |
    v
TTS Service
(Edge Neural Voices)
    |
    v
MP3 Audio Briefing
    |
    v
Gmail
```


---

# Tech Stack

## AI / LLM

- Python
- Ollama
- Qwen 2.5 7B
- Prompt engineering
- Agent-based workflow

## Automation

- Windows Task Scheduler
- Scheduled execution
- Automated email delivery

## Text Processing

- RSS parsing
- JSON structured outputs
- Vocabulary extraction
- Translation pipeline

## Audio

- Microsoft Edge TTS
- German and Polish neural voices

## Email

- Gmail SMTP
- HTML email formatting
- MP3 attachments

---

# Project Structure

```text
ai-news-agent/

├── app/
│
│   ├── agents/
│   │   ├── news_ranker.py
│   │   ├── summary_agent.py
│   │   ├── translation_agent.py
│   │   ├── vocabulary_agent.py
│   │   └── vocabulary_reviewer.py
│   │
│   ├── services/
│   │   ├── rss_reader.py
│   │   ├── ollama_client.py
│   │   ├── tts_service.py
│   │   ├── email_service.py
│   │   ├── briefing_writer.py
│   │   └── logger.py
│   │
│   └── main.py
│
├── data/
│   └── audio/
│
├── logs/
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
```


---

# Example Workflow

Every morning:


07:00

Collect German news
|
v
Choose best article
|
v
Generate AI summary
|
v
Translate to Polish
|
v
Create vocabulary lesson
|
v
Generate audio
|
v
Send email briefing


---

# Local Setup

## Clone repository

```bash
git clone <repository-url>
```

## Create environment

```bash
uv venv
```

## Install dependencies

```bash
uv sync
```

## Configure environment variables

Create `.env` file:

```env
GMAIL_USER=your_email@gmail.com
GMAIL_PASSWORD=your_app_password
```

## Run agent

```bash
python app/main.py
```


## Example Output

The daily email briefing contains:

Original German article link
German summary
Polish translation
German vocabulary list
Audio lesson

Audio format:

German sentence
        |
        v
Polish translation
        |
        v
German example sentence
        |
        v
Polish example translation

## Automation

The agent runs automatically using Windows Task Scheduler.

Example:

Every day at 07:00

Windows Task Scheduler
        |
        v
python app/main.py
        |
        v
AI News Agent workflow
        |
        v
Gmail briefing

## Logging

Execution logs are stored in:

logs/
└── agent.log

Example:

AI News Agent started
Articles fetched: 20
Selected article: ...
German summary generated
Audio generated
Email sent

## Future Improvements

Cloud deployment
GitHub Actions scheduling
Web interface
More advanced agent orchestration
External LLM APIs
Multi-language support

## Author

Łukasz Pomiankiewicz

AI / ML Engineer Portfolio Project