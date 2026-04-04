import { useEffect, useState } from "react";
import API from "./api";

function Patients() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    API.get("patients/")
      .then((res) => setPatients(res.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h2>Patients</h2>
      {patients.map((p) => (
        <div key={p.id}>
          {p.first_name} {p.last_name}
        </div>
      ))}
    </div>
  );
}

export default Patients;
