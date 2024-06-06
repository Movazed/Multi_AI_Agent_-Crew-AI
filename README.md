# Multi_AI_Agent_with_Complex_Use_Cases

This project is aimed at utilizing the `crewai` library to establish a sophisticated AI-driven content creation pipeline for blogs. The system comprises two primary agents: a Blog Researcher and a Blog Writer. The Blog Researcher is responsible for gathering comprehensive information from YouTube videos related to a specified topic, while the Blog Writer synthesizes this data into compelling blog content.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/Multi_AI_Agent_with_Complex_Use_Cases_Crew_AI.git
    cd Multi_AI_Agent_with_Complex_Use_Cases_Crew_AI
    ```

2. **Create and Activate a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the Required Packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Environment Variables:**
    - Create a `.env` file in the project root directory and add the following:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    OPENAI_MODEL_NAME=gpt-4-0125-preview
    ```

## Usage

To run the project, execute the main script:

```bash
python main.py
