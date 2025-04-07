# 📄 README.md: Claim Prediction App

## 📌 Project Overview
This is a **Claim Prediction App** that uses **Machine Learning** to predict whether an **insurance claim will be approved** based on user inputs.  
The project consists of:
- 🖥️ **Backend** → **Flask API** for prediction.
- 🌐 **Frontend** → **React App** for user interaction.
- 🧠 **ML Model** → **Random Forest Classifier** trained on insurance claim data.

---

## 📂 Project Structure
```
claim-prediction-app/
│── backend/
│   ├── app.py                # Flask API
│   ├── train_model.py         # ML Model Training
│   ├── claim_model.pkl        # Saved ML Model
│   ├── insurance_claims.csv   # Dataset
│── frontend/
│   ├── (React project files)  # React frontend
│── requirements.txt           # Python dependencies
│── README.md                  # Instructions
```

---

## 🚀 How to Install and Run the Project
### 1️⃣ Setup Backend (Flask API)
1. **Extract the Zip File**  
   - Unzip the project folder `claim-prediction-app.zip`.
2. **Navigate to the Backend Folder**
   ```bash
   cd claim-prediction-app/backend
   ```
3. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```
4. **Activate Virtual Environment**
   - **Windows:**  
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**  
     ```bash
     source venv/bin/activate
     ```
5. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
6. **Train the Machine Learning Model (If Needed)**
   ```bash
   python train_model.py
   ```
   ✅ This saves the model as `claim_model.pkl`.

7. **Run the Flask API**
   ```bash
   python app.py
   ```
   ✅ The API will be available at **`http://127.0.0.1:5000/`**.

---

### 2️⃣ Setup Frontend (React App)
1. **Navigate to the Frontend Folder**
   ```bash
   cd ../frontend
   ```
2. **Install Dependencies**
   ```bash
   npm install
   ```
3. **Start the Frontend**
   ```bash
   npm start
   ```
   ✅ The app will open at **`http://localhost:3000/`**.

---

## 🎯 How to Use the App
1. **Open the Frontend** in a browser → `http://localhost:3000/`
2. **Fill in Claim Details** (Age, Policy Type, Vehicle Damage, etc.).
3. **Submit the Form** to make a prediction.
4. **See the Result** → "Claim Approved ✅" or "Claim Denied ❌".

---

## 🔧 API Usage (For Testing)
### 📌 Test API with Postman or cURL
Send a **POST request** to:
```
http://127.0.0.1:5000/predict
```
With **JSON Data**:
```json
{
    "age": 35,
    "policy_type": "comprehensive",
    "previous_claims": 2,
    "vehicle_damage": "Yes"
}
```
**Expected Response:**
```json
{
    "claim_approved": 1
}
```
- `1` → Claim Approved ✅  
- `0` → Claim Denied ❌  

---

## 📦 Deployment Guide
### Option 1: Deploy Backend on Render
1. Push the **backend folder** to GitHub.
2. Create an account on **Render.com**.
3. Select **New Web Service** → Connect GitHub repo.
4. Choose **Python Environment**.
5. Set the **Start Command**:  
   ```bash
   gunicorn app:app
   ```
6. Deploy and get a **Live API URL**!

### Option 2: Deploy Frontend on Vercel
1. Push the **frontend folder** to GitHub.
2. Create an account on **Vercel.com**.
3. Select **New Project** → Connect GitHub repo.
4. Set the **Build Command**:  
   ```bash
   npm run build
   ```
5. Deploy and get a **Live Website URL**!

---

## 🛠️ Troubleshooting
### Issue 1: Flask API Not Running?
✔️ Make sure to **activate the virtual environment** before running `app.py`.  
✔️ Check if **port 5000 is already in use** and change it:
   ```python
   app.run(debug=True, port=5001)
   ```

### Issue 2: CORS Error in Frontend?
✔️ Ensure `Flask-CORS` is installed:
   ```bash
   pip install flask-cors
   ```
✔️ Add this line in `app.py`:
   ```python
   from flask_cors import CORS
   CORS(app)
   ```

### Issue 3: React Frontend Not Working?
✔️ Run `npm install` again to fix missing dependencies.  
✔️ If the API URL changes (e.g., when deploying), update it in **React’s `ClaimForm.js`**.

---

## 📌 Technologies Used
| **Component** | **Technology** |
|--------------|---------------|
| 🏗 **Backend** | Flask (Python) |
| 🌐 **Frontend** | React.js |
| 🧠 **ML Model** | Random Forest Classifier |
| 💾 **Data Handling** | Pandas, NumPy |
| 📊 **Model Deployment** | Flask API, Render, Vercel |

---

## 📢 About the Author
Created by **Adwait Bhavthankar** 🚀  
📩 Contact: [Your Email]  
📌 GitHub: [Your GitHub Profile]  

---

## 📌 Conclusion
🎯 **This Claim Prediction App is now fully functional!**  
✅ **Supports Flask API & React Frontend**  
✅ **Easily deployable on Render & Vercel**  
✅ **Ready to handle real-world insurance predictions!**  

🚀 Happy Coding! Let me know if you have any questions! 😊
