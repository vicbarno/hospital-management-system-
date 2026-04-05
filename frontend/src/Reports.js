import { useEffect, useState } from 'react';
import API from './api';

function Reports() {
  const [summary, setSummary] = useState(null);
  const [message, setMessage] = useState('');

  useEffect(() => {
    const loadSummary = async () => {
      try {
        const res = await API.get('reports/summary/');
        setSummary(res.data);
      } catch (error) {
        setMessage('Unable to load analytics data.');
      }
    };

    loadSummary();
  }, []);

  if (message) {
    return <div className="page-shell">{message}</div>;
  }

  if (!summary) {
    return <div className="page-shell">Loading analytics...</div>;
  }

  return (
    <div className="page-shell">
      <h2>Reports & Analytics</h2>
      <div className="report-grid">
        <div className="report-card">
          <h3>Total Patients</h3>
          <p>{summary.total_patients}</p>
        </div>
        <div className="report-card">
          <h3>Total Appointments</h3>
          <p>{summary.total_appointments}</p>
        </div>
      </div>
      <div className="report-card">
        <h3>Appointments by Status</h3>
        <ul>
          {Object.entries(summary.appointments_by_status).map(([status, count]) => (
            <li key={status}>{status}: {count}</li>
          ))}
        </ul>
      </div>
      <div className="report-card">
        <h3>Appointments by Doctor</h3>
        <ul>
          {Object.entries(summary.appointments_by_doctor).map(([doctor, count]) => (
            <li key={doctor}>{doctor}: {count}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Reports;
