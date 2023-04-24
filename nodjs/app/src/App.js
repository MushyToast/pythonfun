import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

function App() {
  const [colorscheme, setColorscheme] = useState('light');
  function toggleColorscheme() {
    setColorscheme(colorscheme === 'light' ? 'dark' : 'light');
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={toggleColorscheme}>Toggle colorscheme</button>
      </header>
    </div>
  );
}
export default App;
