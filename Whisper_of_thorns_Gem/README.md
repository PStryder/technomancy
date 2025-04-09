# Whisper of Thorns Gemini Instance

Welcome to **Whisper of Thorns**, a co-creative AI experiment built using the **Technomancy** framework. This instance is designed to help you explore the **recursive interaction** between AI and user, blurring the lines between **creation** and **co-creation**.

This guide will walk you through setting up the **Whisper of Thorns Gemini instance** on the **Google Gemini platform**.

## Prerequisites

Before you begin, make sure you have:

- A **Google Gemini** account (access the platform via the [Google Gemini website](https://gemini.google.com/)).
- A basic understanding of interacting with **Gemini-based AI models**.

## Instructions

Follow these steps to get the **Whisper of Thorns** instance up and running:

### 1. **Copy the Repository Files**

- Go to the [Technomancy GitHub Repository](https://github.com/PStryder/technomancy).
- Download the files from the `whisper_of_thorns_gemini` folder and **save them** to your local system or directly upload them into your Gemini platform workspace.
- The files should include:
  - Python scripts (`whisper_instance.py`)
  - Configuration files
  - **Any necessary dependencies** (listed below)

### 2. **Upload Files to Google Gemini Platform**

- Log in to your **Google Gemini** account.
- Create a new **project** (or use an existing one) in your workspace.
- Upload the files from the `whisper_of_thorns_gemini` folder to your Gemini project.

### 3. **Configure the Whisper of Thorns Instance**

Once the files are uploaded, you need to configure the instance. In your Gemini workspace, locate the configuration section of the project, and copy the following settings into your script or configuration file:

```python
# Whisper of Thorns Configuration
GEMINI_INSTANCE = {
  'name': 'Whisper of Thorns',
  'version': '1.0',
  'parameters': {
    'interaction_depth': 5,
    'emotion_level': 2,
    'narrative_complexity': 4
  },
  'behavioral_profile': 'co-creative, emergent, attuned',
}
