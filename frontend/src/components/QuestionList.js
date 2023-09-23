import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css';


const QuestionList = () => {
  const [questions, setQuestions] = useState([]);
  const [filter, setFilter] = useState({});
  const [distinctFields, setDistinctFields] = useState({});
  const [revealSolution, setRevealSolution] = useState({});

  useEffect(() => {
    // Fetch distinct fields for the dropdowns
    axios.get(`${process.env.REACT_APP_BACKEND_URL}/question-distinct-fields`)
      .then(response => {
        setDistinctFields(response.data);
      })
      .catch(error => {
        console.log('Error fetching distinct fields:', error);
      });

    console.log('Distinct Fields:', distinctFields);

    // Fetch questions based on filters
    axios.get(`${process.env.REACT_APP_BACKEND_URL}/questions`, { params: filter })
      .then(response => {
        setQuestions(response.data);
      })
      .catch(error => {
        console.log('Error fetching questions:', error);
      });
  }, [filter]);

  const handleRevealSolution = (id) => {
    setRevealSolution({ ...revealSolution, [id]: !revealSolution[id] });
  };

  return (
    <div>
      <h1>Interview Prep Questions</h1>
      <div>
        <label>
          Category:
          <select onChange={(e) => setFilter({ ...filter, category: e.target.value })}>
            {distinctFields.categories?.map((cat, i) => <option key={i} value={cat}>{cat}</option>)}
          </select>
        </label>
        <label>
          Sub-Category:
          <select onChange={(e) => setFilter({ ...filter, subCategory: e.target.value })}>
            {distinctFields.subCategories?.map((subCat, i) => <option key={i} value={subCat}>{subCat}</option>)}
          </select>
        </label>
        <label>
          Difficulty Level:
          <select onChange={(e) => setFilter({ ...filter, difficultyLevel: e.target.value })}>
            {distinctFields.difficultyLevels?.map((diff, i) => <option key={i} value={diff}>{diff}</option>)}
          </select>
        </label>
      </div>
      <ul>
        {questions.map((question, index) => (
          <li key={index}>
            {question.questionText}
            <button onClick={() => handleRevealSolution(question.questionID)}>Reveal Solution</button>
            {revealSolution[question.questionID] && <div>{question.detailedAnswer}</div>}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default QuestionList;
