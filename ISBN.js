// Sample string containing ISBN numbers
const string = "The book ISBN 123-4-567-89012-3 is a great read";

// Regular expression pattern for extracting ISBN numbers
const pattern = /ISBN \d{3}-\d-\d{3}-\d{5}-\d/;

// Extract ISBN numbers using regex
const match = string.match(pattern);

// Print the match
if (match) {
    console.log("ISBN:", match[0]);
}
