
const mysql = require('mysql2/promise'); // Import the mysql2 library

async function getDataFromDb(table, type) {
    // Create a connection pool (you don't need to manually open/close connections)
    const pool = mysql.createPool({
        host: 'localhost',
        user: 'root',
        password: 'your_password',
        database: 'your_database',
    });

    try {
        // Acquire a connection from the pool
        const connection = await pool.getConnection();

        try {
            // Define your SQL query
            if (type !== 'none') { // Corrected the condition
                type = type.substring(0, 3).toUpperCase();
                const sqlQuery = `SELECT Count(*) FROM ${table} WHERE type = ${type}`; // Use a placeholder for the type
                const [rows] = await connection.query(sqlQuery, [type]); // Pass type as a parameter
                console.log(rows);
            }

            // Release the connection back to the pool (this automatically closes the connection)
            connection.release();
        } catch (error) {
            console.error('Error executing SQL query:', error);
        }
    } catch (error) {
        console.error('Error acquiring a database connection:', error);
    }
}

// JavaScript function to handle the button click
const getDataButton = document.getElementById('getDataButton');
getDataButton.addEventListener('click', function () {
    // Retrieve the value of the "data-type" attribute
    const type = getDataButton.getAttribute('data-type');

    // Check if the type value exists (not null or undefined)
    if (type) {
        const table = 'your_table_name'; // Replace with the actual table name

        // Call the function with the specified table and type
        getDataFromDb(table, type)
            .then(() => {
                console.log('getDataFromDb function executed successfully');
                // You can add code here to handle the result if needed
            })
            .catch((error) => {
                console.error('Error executing getDataFromDb:', error);
            });
    }
});