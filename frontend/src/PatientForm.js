import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API from './api';

function PatientForm() {
  const [form, setForm] = useState({ first_name: '', last_name: '', age: '', gender: '', phone: '', medical_history: '' });
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (event) => {
    setForm({ ...form, [event.target.name]: event.target.value });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await API.post('patients/', {
        ...form,
        age: Number(form.age),
      });
      setMessage('Patient registered successfully.');
      setForm({ first_name: '', last_name: '', age: '', gender: '', phone: '', medical_history: '' });
      navigate('/');
    } catch (error) {
      setMessage('Unable to register patient. Please check your values and try again.');
    }
  };

  return (
    <div className="page-shell">
      <h2>Register New Patient</h2>
      <form className="form-grid" onSubmit={handleSubmit}>
        <input name="first_name" value={form.first_name} onChange={handleChange} placeholder="First Name" required />
        <input name="last_name" value={form.last_name} onChange={handleChange} placeholder="Last Name" required />
        <input name="age" value={form.age} onChange={handleChange} placeholder="Age" type="number" min="0" required />
        <input name="gender" value={form.gender} onChange={handleChange} placeholder="Gender" required />
        <input name="phone" value={form.phone} onChange={handleChange} placeholder="Phone" required />
        <textarea name="medical_history" value={form.medical_history} onChange={handleChange} placeholder="Medical history" rows="4" />
        <button type="submit">Register Patient</button>
      </form>
      {message && <div className="message">{message}</div>}
    </div>
  );
}

export default PatientForm;
