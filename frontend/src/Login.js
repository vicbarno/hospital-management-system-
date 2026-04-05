import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from './api';

function Login({ onLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const login = async () => {
    try {
      const res = await API.post('token/', { username, password });
      localStorage.setItem('token', res.data.access);
      const profile = await API.get('users/me/');
      onLogin(profile.data);
      navigate('/');
    } catch (err) {
      setError('Invalid username or password.');
    }
  };

  return (
    <div className="page-shell">
      <h2>Login</h2>
      <div className="form-grid">
        <input
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="button" onClick={login}>
          Sign In
        </button>
      </div>
      {error && <div className="message error">{error}</div>}
    </div>
  );
}

export default Login;
