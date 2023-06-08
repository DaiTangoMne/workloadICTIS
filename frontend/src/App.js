import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/data')
      .then(response => setData(response.data))
      .catch(error => console.log(error));
  }, []);

  return (
    <div>
      <h1 className='table_educator'>Таблица с преподавателями</h1>
      <table>
        <thead>
          <tr>
            <th>Номер</th>
            <th>Подразделение</th>
            <th>Должность</th>
            <th>ФИО преподавателя</th>
            <th>Почта</th>
            <th>Вид занятости преподавателя</th>
            <th>Ученая степень преподавателя</th>
            <th>Учебное звание преподавателя</th>
            <th>Количество ставок</th>
          </tr>
        </thead>
        <tbody>
          {data.map(row =>
            <tr key={row.ID}>
              <td>{row.ID}</td>
              <td>{row.unit}</td>
              <td>{row.unit}</td>
              <td>{row.post}</td>
              <td>{row.name}</td>
              <td>{row.email}</td>
              <td>{row.state}</td>
              <td>{row.degree}</td>
              <td>{row.rank}</td>
              <td>{row.rate}</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
}
export default App;
