
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark mb-4">
        <div className="container-fluid">
          <Link className="navbar-brand fw-bold" to="/">Octofit Tracker</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <Link className="nav-link" to="/activities">Activities</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/leaderboard">Leaderboard</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/teams">Teams</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/users">Users</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/workouts">Workouts</Link>
              </li>
            </ul>
            <span className="navbar-text text-light">
              <a className="btn btn-outline-info btn-sm ms-2" href="https://github.com/justinharvey10-afk/skills-build-applications-w-copilot-agent-mode" target="_blank" rel="noopener noreferrer">GitHub Repo</a>
            </span>
          </div>
        </div>
      </nav>
      <div className="container">
        <Routes>
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/" element={
            <div className="card mt-5">
              <div className="card-body">
                <h2 className="card-title">Welcome to Octofit Tracker!</h2>
                <p className="card-text">Track your fitness, join teams, and compete on the leaderboard.</p>
                <a href="/activities" className="btn btn-primary m-2">View Activities</a>
                <a href="/leaderboard" className="btn btn-success m-2">Leaderboard</a>
                <a href="/teams" className="btn btn-info m-2">Teams</a>
                <a href="/users" className="btn btn-secondary m-2">Users</a>
                <a href="/workouts" className="btn btn-warning m-2">Workouts</a>
              </div>
            </div>
          } />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
