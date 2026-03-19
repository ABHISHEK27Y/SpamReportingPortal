# 🛡️ Spam Reporting Portal

![Banner PlaceHolder](https://via.placeholder.com/1000x300?text=Spam+Reporting+Portal+-+Code+Ronin+Hackathon)

> **Built for the Code Ronin Hackathon 🏆**

The **Spam Reporting Portal** is an advanced, machine learning-powered web application designed to combat the rising threat of digital spam and fraudulent messages. This project serves as a centralized platform where users can report suspicious messages, get real-time AI-based spam predictions, manage their complaint history, and generate official PDF reports.

---

## 🎯 Project Objectives

1. **Win the Code Ronin Hackathon:** Deliver a robust, feature-rich, and visually appealing web application that solves a real-world problem (Spam/Fraud Detection).
2. **Advanced Spam Detection API:** Implement accurate ML models (currently utilizing TF-IDF Vectorization & Scikit-learn, with plans to integrate advanced BERT models for semantic understanding) to classify messages as *Spam* or *Legit*.
3. **Seamless User Experience (UX):** Provide a modern Glassmorphism UI that feels premium, intuitive, and engaging for end-users.
4. **Comprehensive Reporting:** Enable users to seamlessly generate structured, downloadable PDF reports for their spam complaints for official use or record-keeping.
5. **Data Management:** Implement a secure authentication system and personalized dashboard to track user complaint history securely.

---

## ✨ Key Features

- 🔐 **User Authentication:** Secure login and registration system using Flask-Login.
- 🧠 **AI-Powered Prediction:** Real-time spam detection powered by a trained ML Engine.
- 📊 **Confidence Scores:** View exact probability scores (Fraud vs Legit) for every analyzed message.
- 🗂️ **Personalized Dashboard:** A customized user dashboard to view all past predictions and complaints.
- 📄 **PDF Report Generation:** One-click automated PDF generation summarizing the spam report details.
- 🎨 **Modern Aesthetics:** Clean, premium frontend ready to be upgraded with Framer Motion and Glassmorphism effects.

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask (Python)
- **Database:** SQLite with Flask-SQLAlchemy
- **Authentication:** Flask-Login
- **PDF Generation:** FPDF

### Machine Learning Engine
- **Data Processing:** Pandas, NumPy
- **Model Training:** Scikit-learn (Various unified datasets: Enron, Nazario, Nigerian Fraud, SpamAssassin, etc.)
- **Serialization:** Joblib (`final_model.pkl`, `tfidf_vectorizer.pkl`)
- **Future Integration:** BERT (HuggingFace Transformers)

### Frontend
- **Templating:** HTML5, Jinja2
- **Styling:** CSS3 (Targeting modern Glassmorphism UI)

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed.

### Installation

1. **Clone the repository** and navigate to the project directory:
   ```bash
   cd Spam_reporting_portal
   ```

2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database and Run the App:**
   ```bash
   python app.py
   ```
   > The application will initialize the SQLite database automatically on the first run.

5. **Access the Portal:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## 🗺️ Roadmap & Future Enhancements

- [x] Integrate PDF Report Generation.
- [x] Unify diverse spam datasets for robust ML training.
- [ ] **BERT Model Integration:** Upgrade the ML engine to a fine-tuned BERT model for state-of-the-art NLP classification.
- [ ] **Glassmorphism UI Upgrade:** Refine the frontend with a premium Glassmorphism aesthetic and smooth Framer Motion animations.
- [ ] **Admin Dashboard:** Add an admin view to monitor overall system metrics and global spam trends.

---

*Developed with passion for the **Code Ronin Hackathon**.* 🚀
