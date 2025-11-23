import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [form, setForm] = useState({ login: '', password: '' });
  const [msg, setMsg] = useState<{text: string, type: 'error'|'success'|null}>({text:'', type:null});

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post('/api/register', form);
      setMsg({ text: 'USER CREATED SUCCESSFULLY', type: 'success' });
    } catch (err: any) {
      const d = err.response?.data?.detail;
      setMsg({ text: typeof d === 'string' ? d : 'VALIDATION ERROR', type: 'error' });
    }
  };

  return (
    <div className="neo-card">
      <h1>Auth Core</h1>
      <form onSubmit={submit}>
        <input 
          placeholder="LOGIN (3-32 chars)" 
          value={form.login}
          onChange={e => setForm({...form, login: e.target.value})}
        />
        <input 
          type="password" 
          placeholder="PASSWORD (Strong!)" 
          value={form.password}
          onChange={e => setForm({...form, password: e.target.value})}
        />
        <button type="submit">Register Now</button>
      </form>
      
      {msg.type && (
        <div className={`status-box ${msg.type}`}>
          {msg.text}
        </div>
      )}
    </div>
  );
}

export default App;
