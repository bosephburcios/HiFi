// Manipulation of the database for user functions
const { dataSource } = require('./dataSource');
const deleteUser = async (user_id) => {
  const queryRunner = dataSource.createQueryRunner();

  await queryRunner.connect();
  await queryRunner.startTransaction();
  try {
    await queryRunner.query(
      `
        DELETE FROM friend 
        WHERE 
          user_id = ? 
          OR 
          friend_user_id = ?
      `,
      [user_id, user_id]
    );
    await queryRunner.query(
      `
        DELETE FROM todo 
        WHERE 
          id = ? 
      `,
      [user_id]
    );
    await queryRunner.query(
      `
        DELETE FROM users 
        WHERE 
          id = ? 
      `,
      [user_id]
    );
    await queryRunner.commitTransaction();
    
  } catch (error) {
    console.log(error)
    await queryRunner.rollbackTransaction();

    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  } finally {
    if (queryRunner) {
      await queryRunner.release();
    }
  }
};

const createUser = async (
  email,
  password,
) => {
  try {
    return await dataSource.query(
      `
        INSERT INTO users (
            email,
            password
        ) VALUES (
          ?, ?
        )
      `,
      [email, password]
    );
  } catch (error) {
    console.log(error);
    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  }
};
const getUserByEmail = async (email) => {
  try {
    const [user] = await dataSource.query(
      `
      SELECT
        id, 
        email,
        password
      FROM users
      WHERE email = ? 
        `,
      [email]
    );
    return user;
  } catch (error) {
    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  }
};
const isExistedUser = async (email) => {
  try {
    const [result] = await dataSource.query(
      `
        SELECT EXISTS (
          SELECT
          id
          FROM users 
          WHERE email = ?
      ) idExists
      `,
      [email]
    );
    return !!parseInt(result.idExists);
  } catch (error) {
    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  }
};

const isExistedUserID = async (user_id) => {
  try {
    const [result] = await dataSource.query(
      `
        SELECT EXISTS (
          SELECT
          id
          FROM users 
          WHERE id = ?
      ) idExists
      `,
      [user_id]
    );
    return !!parseInt(result.idExists);
  } catch (error) {
    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  }
};

const getUserById = async (id) => {
  try {
    const [user] = await dataSource.query(
      `
      SELECT 
      id, 
        id, 
        email,
        password
        FROM users
        WHERE id = ? 
        `,
      [id]
    );
    return user;
  } catch (error) {
    error = new Error('DATABASE_CONNECTION_ERROR');
    error.statusCode = 400;
    throw error;
  }
};

module.exports = {
  createUser,
  getUserByEmail,
  getUserById,
  isExistedUser,
  isExistedUserID,
  deleteUser,
};
