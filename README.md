

# **Quiz Management System - React & Django**

This is a **Quiz Management System** that allows **users** to register, log in, and take quizzes, while **admins** can create and manage quizzes, view participants’ responses, and analyze reports.

---

## **Features**
### **For Users**
✅ Register and log in  
✅ Take quizzes  
✅ View quiz history  

### **For Admins**
✅ Create, update, and delete quizzes  
✅ Assign questions to quizzes  
✅ View quiz participants and their responses  
✅ Analyze reports of completed quizzes  

---

## **Tech Stack**
- **Frontend**: React.js, React Router, Axios  
- **Backend**: Django Rest Framework (DRF)  
- **Database**: SQLite  
- **Authentication**: JWT  

---

## **1️⃣ Installation Steps**

### **📌 Clone the Repository**
```sh
git clone https://github.com/dhiraj7kr/online-quiz-system.git
cd quiz-app
```

### **📌 Install Dependencies**
#### **Frontend Setup**
```sh
cd frontend
npm install
```

#### **Backend Setup**
```sh
cd backend
pip install -r requirements.txt
```

---

## **2️⃣ Running the Project**
### **Backend (Django)**
Run the backend server:
```sh
cd backend
python manage.py migrate
python manage.py runserver
```
This will start the backend at **http://127.0.0.1:8000/**

---

### **Frontend (React)**
Run the frontend:
```sh
cd frontend
npm start
```
This will start the frontend at **http://localhost:3000/**

---

## **3️⃣ Project Structure**
```
quiz-app/
│── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   │   ├── Dashboard.js
│   │   │   ├── AdminPanel.js
│   │   │   ├── QuizList.js
│   │   │   ├── CreateQuiz.js
│   │   │   ├── QuizResponses.js
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.js
│   │   ├── index.js
│── backend/
│   ├── manage.py
│   ├── quiz/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   ├── db.sqlite3
│── README.md
```

---

## **4️⃣ API Endpoints**
| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/register/` | Register a new user |
| **POST** | `/login/` | Login & get JWT token |
| **GET** | `/quizzes/` | Fetch all quizzes |
| **POST** | `/quizzes/` | Create a new quiz (Admin) |
| **GET** | `/quizzes/<id>/` | Get quiz details |
| **POST** | `/quizzes/<id>/attempt/` | Submit quiz answers |

---

## **5️⃣ Usage**
- **New users must register first.**
- **Login to access the dashboard.**
- **Users can attempt quizzes and see their scores.**
- **Admins can create and manage quizzes.**

---

## **6️⃣ Future Enhancements**
✅ Leaderboard for top scorers  
✅ Timer for quiz attempts  
✅ Enhanced quiz analytics  

---

## **7️⃣ Contributors**
👤 **Your Name**  
📧 dhiraj7kr@gmail.com  
🔗 [GitHub Profile](https://github.com/dhiraj7kr)

---

### **🛠 Happy Coding! 🚀**  

This **README.md** provides a complete guide on setting up and using the Quiz Management System. 😊
