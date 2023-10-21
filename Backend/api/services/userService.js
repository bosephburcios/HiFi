// handles the logic of user functions

// hashing passwords through bcrypt
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const userDao = require('../models/userDao');
const {
  pwValidationCheck,
  emailValidationCheck,
} = require('../utils/validation-check.js');
////////

const signUp = async (email, password) => {
  //pwValidationCheck(password);
  emailValidationCheck(email);

    if (await isExistedUser(email)) {
      const error = new Error('EMAIL_EXISTS');
      error.statusCode = 400;
      throw error;
    }
  const saltRounds = 10;
  const hashedPassword = await bcrypt.hash(password, saltRounds);

  const createUser = await userDao.createUser(
    email,
    hashedPassword,
  );

  return createUser;
};
const login = async (email, password) => {
  emailValidationCheck(email);

  const user = await userDao.getUserByEmail(email);
  // console.log( user );
  // console.log(email);
  // console.log(password);

  const passwordCheck = await bcrypt.compare(password, user.password);

  if (!user || !passwordCheck) {
    const error = new Error('INVALID_EMAIL_OR_PASSWORD');
    error.statusCode = 401;
    throw error;
  }

  return jwt.sign({ id: user.id }, process.env.JWT_SECRET);
};

const isExistedUser = async (email) => {
  return userDao.isExistedUser(email);
};
const isExistedUserID = async (user_id) => {
  return userDao.isExistedUserID(user_id);
};

const getUserById = async (id) => {
  return userDao.getUserById(id);
};


module.exports = {
  signUp,
  login,
  isExistedUser,
  getUserById,
};
