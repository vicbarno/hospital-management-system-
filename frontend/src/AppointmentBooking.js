import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from './api';

function AppointmentBooking() {
  const [doctors, setDoctors] = useState([]);
  const [patients, setPatients] = useState([]);
  const [appointment, setAppointment] = useState({ patient: '', doctor: '', date: '', time: '' });
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const loadData = async () => {
      try {
        const [doctorRes, patientRes] = await Promise.all([
          API.get('users/doctors/'),
          API.get('patients/'),
        ]);
        setDoctors(doctorRes.data);
        setPatients(patientRes.data);
      } catch (error) {
        setMessage('Unable to load doctors or patients.');
      }
    };
    loadData();
  }, []);

  const handleChange = (event) => {
    setAppointment({ ...appointment, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await API.post('appointments/', { ...appointment, status: 'scheduled' });
      setMessage('Appointment booked successfully.');
      navigate('/');
    } catch (error) {
      setMessage('Unable to book appointment. Check your selections and try again.');
    }
  };

  return (
    <div className="page-shell">
      <h2>Book Appointment</h2>
      <form className="form-grid" onSubmit={handleSubmit}>
        <select name="patient" value={appointment.patient} onChange={handleChange} required>
          <option value="">Select patient</option>
          {patients.map((patient) => (
            <option key={patient.id} value={patient.id}>
              {patient.first_name} {patient.last_name}
            </option>
          ))}
        </select>

        <select name="doctor" value={appointment.doctor} onChange={handleChange} required>
          <option value="">Select doctor</option>
          {doctors.map((doctor) => (
            <option key={doctor.id} value={doctor.id}>
              {doctor.full_name || doctor.username}
            </option>
          ))}
        </select>

        <input type="date" name="date" value={appointment.date} onChange={handleChange} required />
        <input type="time" name="time" value={appointment.time} onChange={handleChange} required />
        <button type="submit">Book Appointment</button>
      </form>
      {message && <div className="message">{message}</div>}
    </div>
  );
}

export default AppointmentBooking;
