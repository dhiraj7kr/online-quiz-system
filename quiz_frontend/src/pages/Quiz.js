import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

const Quiz = () => {
    const { id } = useParams();
    const [questions, setQuestions] = useState([]);
    const [currentQuestion, setCurrentQuestion] = useState(0);
    const [selectedOption, setSelectedOption] = useState(null);
    const [timeLeft, setTimeLeft] = useState(60); // Default time duration for each question
    const navigate = useNavigate();

    useEffect(() => {
        const fetchQuestions = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/questions/?quiz=${id}`, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
                    },
                });
                setQuestions(response.data);
                setTimeLeft(response.data[currentQuestion]?.duration || 60); // Set time duration for the first question
            } catch (error) {
                console.error('Failed to fetch questions', error);
            }
        };
        fetchQuestions();
    }, [id]);

    useEffect(() => {
        if (timeLeft === 0) {
            handleNext(); // Automatically move to the next question when time runs out
        }
        const timer = setInterval(() => {
            setTimeLeft((prevTime) => prevTime - 1);
        }, 1000);
        return () => clearInterval(timer);
    }, [timeLeft]);

    const handleNext = () => {
        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
            setTimeLeft(questions[currentQuestion + 1]?.duration || 60); // Set time duration for the next question
        }
    };

    const handlePrevious = () => {
        if (currentQuestion > 0) {
            setCurrentQuestion(currentQuestion - 1);
            setTimeLeft(questions[currentQuestion - 1]?.duration || 60); // Set time duration for the previous question
        }
    };

    const handleSubmit = async () => {
        try {
            await axios.post(`http://127.0.0.1:8000/api/attempts/`, {
                quiz: id,
                responses: questions.map((q, index) => ({
                    question: q.id,
                    selected_option: selectedOption,
                })),
            });
            navigate(`/score/${id}`);
        } catch (error) {
            console.error('Failed to submit quiz', error);
        }
    };

    return (
        <div>
            <h1>Quiz</h1>
            {questions.length > 0 && (
                <div>
                    <h2>{questions[currentQuestion].question_text}</h2>
                    <p>Time Left: {timeLeft} seconds</p>
                    <ul>
                        {questions[currentQuestion].options.map((option) => (
                            <li key={option.id}>
                                <label>
                                    <input
                                        type="radio"
                                        name="option"
                                        value={option.id}
                                        onChange={() => setSelectedOption(option.id)}
                                    />
                                    {option.option_text}
                                </label>
                            </li>
                        ))}
                    </ul>
                    <button onClick={handlePrevious}>Previous</button>
                    <button onClick={handleNext}>Next</button>
                    <button onClick={handleSubmit}>Submit</button>
                </div>
            )}
        </div>
    );
};

export default Quiz;