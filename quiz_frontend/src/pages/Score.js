import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const Score = () => {
    const { id } = useParams();
    const [score, setScore] = useState(null);

    useEffect(() => {
        const fetchScore = async () => {
            try {
                const response = await axios.get(`http://127.0.0.1:8000/api/quizzes/${id}/response/`, {
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem('access_token')}`,
                    },
                });
                setScore(response.data);
            } catch (error) {
                console.error('Failed to fetch score', error);
            }
        };
        fetchScore();
    }, [id]);

    return (
        <div>
            <h1>Your Score</h1>
            {score && (
                <div>
                    <p>Total Marks: {score.total_marks}</p>
                    <p>Your Score: {score.user_score}</p>
                </div>
            )}
        </div>
    );
};

export default Score;   