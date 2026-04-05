import { Link } from 'react-router-dom';

function Dashboard({ user, onLogout }) {
  const role = user?.role || 'user';
  const displayName = user?.full_name || user?.username || 'User';

  const navItems = {
    admin: [
      { path: '/patients/new', label: 'Register Patient' },
      { path: '/appointments/book', label: 'Book Appointment' },
      { path: '/reports', label: 'Reports' },
    ],
    doctor: [
      { path: '/appointments/book', label: 'Book Appointment' },
      { path: '/reports', label: 'Reports' },
    ],
    receptionist: [
      { path: '/patients/new', label: 'Register Patient' },
      { path: '/appointments/book', label: 'Book Appointment' },
    ],
  };

  return (
    <div className="page-shell">
      <div className="dashboard-header">
        <div>
          <h1>{role.charAt(0).toUpperCase() + role.slice(1)} Dashboard</h1>
          <p>Welcome back, {displayName}.</p>
        </div>
        <button className="logout-button" onClick={onLogout}>Logout</button>
      </div>

      <div className="dashboard-panel">
        <div className="dashboard-card">
          <h2>Quick actions</h2>
          <div className="button-grid">
            {navItems[role]?.map((item) => (
              <Link key={item.path} className="nav-link" to={item.path}>
                {item.label}
              </Link>
            ))}
          </div>
        </div>

        <div className="dashboard-card">
          <h2>Overview</h2>
          <p>Role: <strong>{role}</strong></p>
          <p>Email: <strong>{user?.email || 'Not provided'}</strong></p>
          <p>Use the app navigation to register patients, book appointments, and review analytics.</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
