import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';
import Login from './Login';
import Dashboard from './Dashboard';
import PatientForm from './PatientForm';
import AppointmentBooking from './AppointmentBooking';
import Reports from './Reports';
import API from './api';

function App() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      setLoading(false);
      return;
    }

    const loadUser = async () => {
      try {
        const res = await API.get('users/me/');
        setUser(res.data);
      } catch (_error) {
        localStorage.removeItem('token');
        setUser(null);
      } finally {
        setLoading(false);
      }
    };

    loadUser();
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  if (loading) {
    return <div className="page-shell">Loading application...</div>;
  }

  return (
    <Router>
      <Routes>
        <Route
          path="/login"
          element={<Login onLogin={setUser} />}
        />
        <Route
          path="/"
          element={user ? <Dashboard user={user} onLogout={handleLogout} /> : <Navigate to="/login" replace />}
        />
        <Route
          path="/patients/new"
          element={user ? <PatientForm /> : <Navigate to="/login" replace />}
        />
        <Route
          path="/appointments/book"
          element={user ? <AppointmentBooking /> : <Navigate to="/login" replace />}
        />
        <Route
          path="/reports"
          element={user ? <Reports /> : <Navigate to="/login" replace />}
        />
        <Route path="*" element={<Navigate to={user ? '/' : '/login'} replace />} />
      </Routes>
    </Router>
  );
}

export default App;
