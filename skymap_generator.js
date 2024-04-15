// skymap_generator.js

// Function to parse the text file and extract RA and Dec data
function parseTextFile(contents) {
    const lines = contents.split('\n');
    const raData = [];
    const decData = [];
    lines.forEach(line => {
        const [ra, dec] = line.split(',').map(parseFloat);
        raData.push(ra);
        decData.push(dec);
    });
    return { ra: raData, dec: decData };
}

// Function to generate a skymap based on the uploaded data
function generateSkymap(data) {
    // Create a scatter plot using Plotly
    const layout = {
        title: 'Sky Map',
        xaxis: { title: 'RA (deg)' },
        yaxis: { title: 'Dec (deg)' }
    };

    const trace = {
        x: data.ra,
        y: data.dec,
        mode: 'markers',
        type: 'scattergl',
        marker: { size: 6, color: 'blue' }
    };

    Plotly.newPlot('skymap', [trace], layout);
}

// Function to handle file upload
function handleFileUpload(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    // Define what happens when the file is loaded
    reader.onload = function (e) {
        const contents = e.target.result;
        // Parse the uploaded text file
        const data = parseTextFile(contents);
        // Generate the skymap using the parsed data
        generateSkymap(data);
    };

    // Read the file as text
    reader.readAsText(file);
}

// Add event listener to the file input element
const fileInput = document.getElementById('fileInput');
fileInput.addEventListener('change', handleFileUpload);
