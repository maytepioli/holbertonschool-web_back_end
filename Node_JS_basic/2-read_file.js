const fs = require('fs');

/**
 * Reads a database file and logs the number of students and their details.
 * @param {string} path - Path to the database file.
 */
function countStudents(path) {
  try {
    // Read the file synchronously
    const data = fs.readFileSync(path, 'utf8');

    // Split the file content into lines and filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      throw new Error('Cannot load the database');
    }

    // Extract the headers and rows
    const headers = lines[0].split(',');
    const rows = lines.slice(1);

    console.log(`Number of students: ${rows.length}`);

    // Group students by field
    const fields = {};
    for (const row of rows) {
      const values = row.split(',');
      if (values.length === headers.length) {
        const field = values[values.length - 1];
        const firstName = values[0];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstName);
      }
    }

    // Log the details for each field
    for (const [field, students] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    }
 } catch (error) {
  throw new Error('Cannot load the database');
 }
}

module.exports = countStudents;
