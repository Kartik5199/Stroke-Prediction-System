🧠 Stroke Prediction Web App
This is a Flask-based web application that predicts the risk of stroke based on user input. The model uses machine learning with StandardScaler for feature scaling. The frontend is built using HTML & Tailwind CSS, and the backend is powered by Flask & Scikit-learn.

🚀 Features
✅ Simple & User-friendly Interface
✅ Predicts Stroke Risk Based on Medical & Lifestyle Data
✅ StandardScaler Applied for Correct Predictions
✅ Deployed using Flask

📂 Project Structure
csharp
Copy
Edit
stroke-prediction/
│── static/                  # Static files (CSS, JS, images)
│── templates/               # HTML templates
│   └── index.html           # Main UI for input
│── Stroke_model.pkl         # Pre-trained ML model
│── scaler.pkl               # StandardScaler for feature scaling
│── app.py                   # Flask Backend
│── requirements.txt         # Dependencies
│── README.md                # Project Documentation
🛠 Tech Stack
🔹 Backend: Flask, Python
🔹 Frontend: HTML, Tailwind CSS
🔹 Machine Learning: Scikit-learn, NumPy, Pandas
🔹 Deployment: Flask Server

🚀 How to Run Locally
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/stroke-prediction.git
cd stroke-prediction
2️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the Flask App
bash
Copy
Edit
python app.py
The app will be available at http://127.0.0.1:5000/.

🎯 Usage
1️⃣ Open the web app in your browser.
2️⃣ Fill in the required details like age, gender, hypertension, heart disease, etc.
3️⃣ Click the "Predict" button.
4️⃣ The app will display the stroke risk as High Risk or Low Risk.

🏆 Model Details
Uses a trained machine learning model stored in Stroke_model.pkl.

Features are scaled using StandardScaler.pkl to match training data.

Prediction is based on random forest.

❓ Troubleshooting
👉 Ensure scaler.pkl is properly applied before prediction.

❌ ModuleNotFoundError
👉 Run pip install -r requirements.txt to install missing dependencies.

🤝 Contributing
Feel free to fork this repository, improve the model/UI, and submit a pull request. Suggestions are always welcome! 🎉

📜 License
This project is open-source under the MIT License.

Let me know if you want modifications! 🚀