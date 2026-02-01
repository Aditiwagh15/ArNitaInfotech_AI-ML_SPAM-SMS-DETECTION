# 🛡️ Spam SMS Detector

A modern web application that uses machine learning to classify SMS and email messages as spam or legitimate (ham). Built with Flask, scikit-learn, and a premium dark mode UI.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🤖 **Machine Learning Classification** - Trained on 5,000+ SMS messages
- 🎨 **Premium UI/UX** - Dark mode with glassmorphism effects
- ⚡ **Real-time Predictions** - Instant spam detection with confidence scores
- 📊 **Visual Feedback** - Animated progress bars and color-coded results
- 🔒 **Input Validation** - Secure handling with character limits
- 📱 **Responsive Design** - Works on desktop and mobile devices
- ⌨️ **Keyboard Shortcuts** - `Ctrl+Enter` for quick predictions

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Aditi
   ```

2. **Install dependencies**

   ```bash
   pip install flask scikit-learn joblib nltk
   ```

3. **Download NLTK data** (if needed)

   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
Aditi/
├── Model/                      # Machine learning models
│   ├── spam_classifier.joblib  # Primary model (preferred)
│   ├── spam_classifier.pkl     # Fallback model
│   └── spam_classifier.h5      # Keras format
├── static/                     # Static assets
│   ├── favicon.svg
│   └── logo.svg
├── templates/                  # HTML templates
│   └── index.html             # Main interface
├── app.py                     # Flask application
├── spam.csv                   # Training dataset
└── Spam SMS Detector.ipynb    # Model training notebook
```

## 🎯 Usage

### Web Interface

1. Enter or paste a message in the text area
2. Click **Predict** or press `Ctrl+Enter`
3. View the classification result with confidence score

### API Endpoint

**POST** `/api/predict`

**Request:**

```json
{
  "message": "Congratulations! You've won a free prize!"
}
```

**Response:**

```json
{
  "ok": true,
  "label": "SPAM",
  "prediction": 1,
  "spam_probability": 0.95,
  "latency_ms": 12.34
}
```

## 🧠 Machine Learning Pipeline

### Dataset

- **Size:** 5,169 messages (after cleaning)
- **Distribution:** 87.37% ham, 12.63% spam
- **Source:** `spam.csv`

### Preprocessing Steps

1. Text normalization (lowercase)
2. Tokenization (NLTK)
3. Remove non-alphanumeric characters
4. Stop words removal
5. Porter stemming
6. Feature extraction

### Model

- **Type:** scikit-learn pipeline
- **Format:** Joblib serialization
- **Output:** Binary classification (0=ham, 1=spam)
- **Probability:** Confidence scores via `predict_proba()`

## 🎨 UI Design

### Color Scheme

- **Primary Gradient:** Indigo (#6366f1) → Purple (#a855f7) → Pink (#ec4899)
- **Background:** Dark slate (#020617) with radial gradient overlays
- **HAM:** Emerald green (#10b981)
- **SPAM:** Rose red (#f43f5e)

### Technologies

- **CSS Framework:** Bootstrap 5.3.3 + Tailwind CSS
- **Animations:** anime.js
- **Typography:** Google Fonts (Outfit)
- **Effects:** Glassmorphism, backdrop blur

## 📊 Model Performance

The model was trained using the Jupyter notebook (`Spam SMS Detector.ipynb`) which includes:

- Data exploration and visualization
- Feature engineering
- Model training and evaluation
- Word cloud generation
- Performance metrics

## 🔧 Configuration

### Model Loading

The application attempts to load models in this order:

1. `Model/spam_classifier.joblib` (preferred)
2. `Model/spam_classifier.pkl` (fallback)

### Limits

- **Max message length:** 5,000 characters
- **Max request size:** 1 MB

## 🚀 Deployment

### Development

```bash
python app.py
```

### Production

```bash
python -m flask --app app run
```

For production deployment, consider using:

- **Gunicorn** or **uWSGI** as WSGI server
- **Nginx** as reverse proxy
- Environment variables for configuration

## 📝 API Examples

### Python

```python
import requests

response = requests.post('http://127.0.0.1:5000/api/predict',
    json={'message': 'Win a free iPhone now!'})
result = response.json()
print(f"Label: {result['label']}, Confidence: {result['spam_probability']}")
```

### JavaScript

```javascript
const response = await fetch("/api/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: "Your message here" }),
});
const data = await response.json();
```

### cURL

```bash
curl -X POST http://127.0.0.1:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"message": "Free prize waiting for you!"}'
```

## 🛠️ Development

### Training a New Model

1. Open `Spam SMS Detector.ipynb` in Jupyter
2. Update the dataset if needed
3. Run all cells to train and save the model
4. Models will be saved in the `Model/` directory

### Customizing the UI

Edit `templates/index.html` to modify:

- Color scheme (CSS variables in `:root`)
- Layout and components
- Animations and transitions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Dataset: SMS Spam Collection
- Libraries: Flask, scikit-learn, NLTK, Bootstrap, Tailwind CSS
- Animations: anime.js

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using Flask and Machine Learning**
