import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/quizzes/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        setQuizzes(response.data);
      } catch (error) {
        console.error('Failed to fetch quizzes', error);
      }
    };
    fetchQuizzes();
  }, []);

  return (
    <div>
      <h1>Dashboard</h1>
      <ul>
        {quizzes.map((quiz) => (
          <li key={quiz.id}>
            <button onClick={() => navigate(`/quiz/${quiz.id}`)}>
              {quiz.title}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;