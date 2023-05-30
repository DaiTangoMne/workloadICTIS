const { Client } = require('pg');
const xlsx = require('xlsx');
const path = require('path');

const filePath = path.join(__dirname, 'ictis.xlsx');

const workbook = xlsx.readFile(filePath);
const worksheet = workbook.Sheets[workbook.SheetNames[0]];
const rows = xlsx.utils.sheet_to_json(worksheet);

const client = new Client({
  user: 'postgres',
  host: '5.tcp.eu.ngrok.io',
  database: 'ictis',  
  password: 'bovaev',
  port: 19074
});

client.connect();

const createTableQuery = `
  CREATE TABLE IF NOT EXISTS workloadIctis (
    NUM INT,
    A TEXT,
    B TEXT,
    C INT,
    D TEXT,
    E INT,
    F TEXT,
    G TEXT,
    H TEXT,
    I TEXT,
    J INT,
    K INT,
    L TEXT,
    M INT,
    N TEXT,
    O TEXT,
    P TEXT,
    Q TEXT,
    R TEXT,
    S REAL,
    T REAL,
    U REAL,
    V REAL,
    W REAL,
    X REAL,
    Y REAL,
    Z TEXT,
    AA TEXT,
    AB TEXT,
    AC TEXT,
    AD TEXT,
    AE TEXT,
    AF TEXT
  )
`;

client.query(createTableQuery, (err, _) => {
  if (err) {
    console.error(err);
    client.end();
    return;
  }

  console.log('Table created successfully');

  const insertQuery = `
    INSERT INTO workloadIctis (NUM, A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z, AA, AB, AC, AD, AE, AF)
    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20, $21, $22, $23, $24, $25, $26, $27, $28, $29, $30, $31, $32, $33)
  `;

  const valuesArr = rows.map((row) => [
    row.NUM,
    row.A,
    row.B,
    row.C,
    row.D,
    row.E,
    row.F,
    row.G,
    row.H,
    row.I,
    row.J,
    row.K,
    row.L,
    row.M,
    row.N,
    row.O,
    row.P,
    row.Q,
    row.R,
    row.S ? row.S.toString().replace(",", ".") : null,
    row.T ? row.T.toString().replace(",", ".") : null,
    row.U ? row.U.toString().replace(",", ".") : null,
    row.V ? row.V.toString().replace(",", ".") : null,
    row.W ? row.W.toString().replace(",", ".") : null,
    row.X ? row.X.toString().replace(",", ".") : null,
    row.Y ? row.Y.toString().replace(",", ".") : null,
    row.Z,
    row.AA,
    row.AB,
    row.AC,
    row.AD,
    row.AE,
    row.AF,
  ]);

  Promise.all(
    valuesArr.map((values) =>
      client.query(insertQuery, values).then((res) => res.rows[0].id)
    )
  )
    .then((ids) => {
      console.log(`Inserted ${ids.length} rows with ids: ${ids.join(', ')}`);

      client.end();
    })
    .catch((err) => {
      console.error(err);
      // client.end();
    });
});
