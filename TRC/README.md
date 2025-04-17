# Technomantic Record Classifier v1.0
*An intelligent, schema-aware document classifier powered by GPT + Technomantic Scoring.*

---

## 📄 Purpose

This system receives a document or unstructured text and:
- Generates a brief summary (1–2 sentence abstract)
- Suggests classification terms from an external schema (CSV or JSON)
- Falls back on interpretive categories if no schema is provided
- Optionally includes confidence and rationale
- Runs all logic live (no pretraining); powered by base GPT + instruction tuning only
