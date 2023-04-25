import { Link } from "react-router-dom";
import './App.css';

function Navbar() {
    return (
        <div className="navbar">
            <Link className="navbarButton" to="/">Home</Link>
            <Link className="navbarButton" to="/about">About</Link>
            <Link className="navbarButton" to="/other">Other</Link>
        </div>
    )
}