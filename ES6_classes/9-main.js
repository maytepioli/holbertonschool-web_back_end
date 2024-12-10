// eslint-disable-next-line import/extensions
import listOfStudents from './9-hoisting.js';

// eslint-disable-next-line jest/require-hook
console.log(listOfStudents);

const listPrinted = listOfStudents.map(
  (student) => student.fullStudentDescription,
);
// eslint-disable-next-line jest/require-hook
console.log(listPrinted);
