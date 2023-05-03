
import './App.css';
import { useState } from 'react';

document.cookie = "liked=1;"
document.cookie = "like=Like;"

function getCookie(name : string) {
  const value = `; ${document.cookie}`;
  const parts : any = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

function App() {
  const [likes, setLikes] = useState(getCookie());
  const [btnText, setBtnText] = useState("Like");
  const [liked, setLike] = useState(0);
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
      <button onClick={toggleLike}>
        {btnText}
      </button>
      <p>{likes}</p>
    </div>
  );
}




export default App;
