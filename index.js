const express = require('express');
const { Pool } = require('pg');
const port = 5000;

const app = express();

const pool = new Pool({
  user: 'postgres',
  host: '5.tcp.eu.ngrok.io',
  database: 'workload',
  password: 'root',
  port: 12717,
});

app.use(function(req, res, next) {
  // res.render("Access-Control-Allow-Origin", "http://localhost:3000/");
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

// запрос к БД
app.get('/data', async (req, res) => {
  try {
    const client = await pool.connect();
    const result = await client.query('SELECT * FROM educators');
    const rows = result.rows;
    client.release();
    res.json(rows);
  } catch (err) {
    console.error(err);
    res.send("Error " + err);
  }
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
