// Sample string containing hex color codes
const string = "The color #FFFFFF is white, and #00FF00 is green";

// Regular expression pattern for extracting hex color codes
const pattern = /#([a-fA-F0-9]{6})/g;

// Extract hex color codes using regex
const colors = string.match(pattern);

// Print the colors
if (colors) {
    colors.forEach(color => {
        console.log("Hex Color Code:", color);
    });
}
