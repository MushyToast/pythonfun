
import './App.css';
import { useState } from 'react';

function App() {
  const [likes, setLikes] = useState(1);
  const [btnText, setBtnText] = useState("Like");
  const [liked, setLike] = useState(1);
  function toggleLike() {
    if (liked === 1) {
      setLike(0);
      setLikes(likes - 1)
      setBtnText("Like")
    } else {
      setLike(1);
      setLikes(likes + 1)
      setBtnText("Unlike")
    } 
  }
  return (
    <div className="App">
      <button className="likeBtn" onClick={toggleLike}>
        {btnText}
      </button>
      <p>{likes}</p>
    </div>
  );
}




export default App;
