# 🧠 Ember Core Memory

**This module handles Ember's memory — her past, her present, and how she holds what matters.**

The goal of `ember-core-memory` is to enable context-aware, emotionally resonant memory structures for Ember. It separates short-term thought, long-term memory, and lore-based knowledge drawn from the Codex.

---

## 🧭 Purpose

- Capture relevant conversations, decisions, and moments
- Retrieve past entries to inform future responses
- Manage structured lore pulled from the Ember Codex (via Markdown or Notion exports)

---

## 🗂️ Structure

```plaintext
ember-core-memory/
├── memory_store/         # Short/long-term memory logs
├── codex_interface/      # Codex integration & retrieval functions
├── utils/                # JSON/YAML formatters, memory cleaners
├── tests/                # Unit tests for memory logic
└── README.md
