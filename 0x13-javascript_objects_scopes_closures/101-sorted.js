#!/usr/bin/node

const dict = require('./101-data.js');

const newDict = {};

/* Iterate over the keys of the dict object */
for (const key in dict) {
  /* Retrive user id for the current occurence count */
  const userId = dict[key];

  /* Check if the occurence already exists as a key in the new dict */
  if (newDict.hasOwnProperty(userId.length)) {
    /* Append the current user Id to the existsing list of user id */
    newDict[userId.length] = newDict[userId.length].concat(userId);
  } else {
    /* Create new key with occurence count and init it with current user id */
    newDict[userId.length] = userId;
  }
}
console.log(newDict);
