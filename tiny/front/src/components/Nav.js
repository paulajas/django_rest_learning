import React from 'react';
import { Outlet, Link } from "react-router-dom";
import "./styles.css"

export default function Navbar(props) {
  return (
<>
<nav className="nav">
    <ul>
    <li>
        <Link className="site-title" to="/">Home</Link>
    </li>
    <li>
        <Link to="/receipe/">Receipe</Link>
</li>
    <li>
        <Link to="/cookbook/">Cookbook</Link>
</li>
    <li>
        <Link to="/cookbookreceipe/">Cookbook-Receipe</Link>
</li>
</ul>
</nav>
    <Outlet />
</>
      );
}

