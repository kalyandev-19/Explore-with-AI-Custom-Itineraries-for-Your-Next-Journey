# Explore with AI: Custom Itineraries for Your Next Journey

![Team ID](https://img.shields.io/badge/Team%20ID-LTVIP2026TMIDS91327-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32.0-red)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-API-orange)

Welcome to **Explore with AI**, your premier AI-powered travel assistant designed to create personalized, detailed, and exciting travel itineraries tailored just for you. Whether you're a nature lover, a foodie, or a history buff, our application leverages the power of Google's Gemini AI to curate the perfect journey for your next adventure.

---

## 🚀 Project Overview

**Explore with AI** simplifies travel planning by generating custom day-by-day itineraries based on your destination, trip duration, and specific interests. No more endless scrolling through travel blogs or generic guides—get a unique plan that fits your style in seconds!

### ✨ Key Features

-   **Personalized Itineraries**: Enter your dream destination and get a tailor-made plan.
-   **flexible Duration**: Specify the number of days and nights for your trip.
-   **Interest-Based Planning**: select from various interests like *Food & Dining*, *History & Culture*, *Nature & Hiking*, and more to customize your experience.
-   **AI-Powered Recommendations**: Utilizes Google's advanced **Gemini 2.5 Flash** model to suggest attractions, restaurants, and hidden gems.
-   **Beautiful UI**: A clean, modern, and responsive interface built with Streamlit for a seamless user experience.

---

## 🛠️ Installation & Setup

Follow these steps to set up the project locally on your machine.

### Prerequisites

-   Python 3.8 or higher installed.
-   A Google Cloud Platform account with an API key for Gemini (Generative AI).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/explore-with-ai.git
cd explore-with-ai
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using `pip`.

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

You need a Google Gemini API Key to run this application.

1.  Get your API key from [Google AI Studio](https://aistudio.google.com/).
2.  Create a `.streamlit/secrets.toml` file in the project root directory (if it doesn't exist).
3.  Add your API key to the file:

```toml
# .streamlit/secrets.toml
GOOGLE_API_KEY = "your_actual_api_key_here"
```

*Alternatively, you can set it as an environment variable:*
```bash
export GOOGLE_API_KEY="your_actual_api_key_here"
```

---

## 🏃‍♂️ Usage

1.  Run the Streamlit application:

```bash
streamlit run travel.py
```

2.  The application will open in your default web browser (usually at `http://localhost:8501`).

3.  **Plan Your Trip**:
    -   Enter your **Destination** (e.g., "Paris, France").
    -   Set the **Duration** (Days and Nights).
    -   Select your **Interests** (optional).
    -   Click **"🚀 Plan My Adventure"**.

4.  Wait for the AI to generate your custom itinerary and enjoy your trip planning!

---

## 🤝 Contributing

We welcome contributions to make **Explore with AI** even better!

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Happy Traveling! 🌍✈️*
