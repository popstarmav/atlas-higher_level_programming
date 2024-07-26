#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId]++;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
