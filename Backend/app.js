require('dotenv').config();

const express = require('express');
const cors = require('cors');
const routes = require('./api/routes');

const { dataSource } = require('./api/models/dataSource');
const { globalErrorHandler } = require('./api/middlewares/error.js');

const app = express();
const PORT = process.env.PORT;

// middleware:
app.use(cors()); // (cors policy 완화제)
app.use(express.json()); // json 형식으로 데이터를 주고 받을 수 있게 허용 해주는 미들웨어
app.use(routes);

//initialize database
const start = async () => {
  try {
    dataSource
      .initialize()
      .then(() => {
        console.log('Data Source has been initialized!');
      })
      .catch((err) => {
        console.log('Error occurred during Data Source initialization', err);
        dataSource.destroy();
      });
    // listen to express server on port 3000
    app.listen(PORT, () => console.log(`Server is listening on ${PORT}`));
  } catch (err) {
    console.error(err);
  }
};

start();

////////////////////////////////////////////////////////////////////////////////

// get request to the database server
app.get('/', (req, res) => {
  res.send('Hello, Express!');
});

// // get all information from users table
// app.get('/users', async (req, res) => {
//   const users = await dataSource.query(
//     `
//         SELECT * FROM users
//     `
//   );
//   res.send(users);
// });

// // post name profileImage and password into users database
// app.post('/users', async (req, res) => {
//   const { name, profileImage, password } = req.body;
//   try {
//     await dataSource.query(
//       `
//         INSERT INTO users 
//         (
//             name, 
//             profile_image, 
//             password
//         ) values ( ?, ?, ? )
//         `,
//       [name, profileImage, password]
//     );
//     res.send('reate success');
//   } catch (error) {
//     console.log(error);
//     throw error;
//   }
// });

// app.delete('/users/:id', async (req, res) => {
//   const { id } = req.params;
//   try {
//     await dataSource.query(
//       `
//         DELETE FROM users WHERE id = ?
//       `,
//       [id]
//     );
//     res.send('delete success');
//   } catch (error) {
//     console.log(error);
//     throw error;
//   }
// });
