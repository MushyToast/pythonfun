import React from 'react';
import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

const loggedIn = false;

function App() {
  const [likes, setLikes] = useState(0);
  const [liked, setLike] = useState(0);
  function toggleLike() {
    if (liked === 1) {
      setLike(0);
      setLikes(likes - 1)
    } else {
      setLike(1);
      setLikes(likes + 1)
    } 
  }
  return (
    <div className="App">
      <button onClick={toggleLike}>
        Like
      </button>
      <p>{likes}</p>
    </div>
  );
}




export default App;
