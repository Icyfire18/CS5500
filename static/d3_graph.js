// Function to update the D3 graph
function updateGraph(data) {
    console.log("Data received:", data);

    // Check if data is valid
    if (!data || !data.usage || !data.temperature) {
        console.error("Invalid data format");
        return;
    }

    // Set dimensions and margins for the chart
    const margin = { top: 70, right: 30, bottom: 60, left: 80 };  // Increased bottom margin for x-axis title
    const width = 1200 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    // Set up the x and y scales
    const x = d3.scaleTime().range([0, width]);
    const y = d3.scaleLinear().range([height, 0]);

    // Create the SVG element and append it to the chart container
    const svg = d3.select("#chart-container")
        .html("")  // Clear previous SVG content
        .append("svg")
        .attr("viewBox", `0 0 ${width + margin.left + margin.right} ${height + margin.top + margin.bottom}`)
        .attr("preserveAspectRatio", "xMidYMid meet")
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

    // create tooltip div
    const tooltip = d3.select("body")
        .append("div")
        .attr("class", "tooltip");

    // Parse date values as JavaScript Date objects
data.usage.forEach(function (d) {
    d.date = new Date(d.date);
    d.value = +d.value; // convert to numeric value
});

data.temperature.forEach(function (d) {
    d.date = new Date(d.date);
    d.temperature = +d.value; // convert to numeric value
});

// Combine usage and temperature data
console.log("Data Usage : ", data.usage);
console.log("Data Temp: ", data.temperature);
const combinedData = data.usage.concat(data.temperature);

// Fill missing temperature values with the average of previous and next month's values
const filledTemperatureData = fillMissingTemperature(combinedData);

    // Define the x and y domains
    x.domain(d3.extent(filledTemperatureData, d => d.date));
    y.domain([0, d3.max(filledTemperatureData, d => d.value)]);

    // Add the x-axis with only first and last month-year
    svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x)
            .ticks(d3.timeMonth.every(1))
            .tickFormat((date, i) => {
                // Display only first and last month-year
                if (i === 0 || i === (d3.timeMonth.range(x.domain()[0], x.domain()[1]).length - 1)) {
                    return d3.timeFormat("%b %Y")(date);
                } else {
                    return "";
                }
            })
        )
        .append("text")
        .attr("x", width / 2)
        .attr("y", margin.bottom - 10)
        .attr("fill", "#000")
        .style("font-weight", "bold")
        .text("DATE");

    // Add the y-axis
    svg.append("g")
        .call(d3.axisLeft(y));

    // Create the line generators
    const lineUsage = d3.line()
        .x(d => x(d.date))
        .y(d => y(d.value));

    const lineTemperature = d3.line()
        .x(d => x(d.date))
        .y(d => y(d.temperature)); // Use temperature value for y-axis

    // Add the line paths to the SVG element
    svg.append("path")
        .datum(data.usage)
        .attr("fill", "none")
        .attr("stroke", "green") // Set color for usage line
        .attr("stroke-width", 1)
        .attr("d", lineUsage);

    svg.append("path")
        .datum(data.temperature)
        .attr("fill", "none")
        .attr("stroke", "red") // Set color for temperature line
        .attr("stroke-width", 1)
        .attr("d", lineTemperature);

    // create a listening rectangle
    const listeningRect = svg.append("rect")
        .attr("width", width)
        .attr("height", height)
        .style("fill", "none")
        .style("pointer-events", "all")
        .on("mousemove", mousemove)
        .on("mouseleave", mouseleave);

        function mousemove(event) {
            const [xCoord] = d3.pointer(event);
            const x0 = x.invert(xCoord);
        
            // Use bisector to find the index of date in the original usage data
            const bisectDate = d3.bisector(d => d.date).left;
            const i = bisectDate(data.usage, x0, 1);
        
            // Determine the closer data point in the original usage data
            const dUsage = i < data.usage.length ? data.usage[i] : data.usage[i - 1];
        
            // Find the closest temperature in temperature data
            const closestTemperature = findClosestTemperature(data.temperature, dUsage.date);
        
            // Display the vertical line
            svg.selectAll(".vertical-line").remove();
            svg.append("line")
                .attr("class", "vertical-line")
                .attr("x1", x(dUsage.date))
                .attr("x2", x(dUsage.date))
                .attr("y1", 0)
                .attr("y2", height)
                .attr("stroke", "white")
                .attr("stroke-width", 1)
                .attr("stroke-dasharray", "4");
        
            // Display the data below the graph
            tooltip
                .style("display", "block")
                .style("left", `${x(dUsage.date) + margin.left}px`)
                .style("top", `${height + margin.top + 10}px`)
                .html(`<strong>Date:</strong> ${dUsage.date.toLocaleDateString()}<br><strong>Usage:</strong> ${!isNaN(dUsage.value) ? dUsage.value.toFixed(2) : 'N/A'}<br><strong>Temperature:</strong> ${closestTemperature !== null && !isNaN(closestTemperature.value) ? closestTemperature.value.toFixed(2) : 'N/A'}`);
        }
        
        // Function to find the closest temperature data point for a given date
        function findClosestTemperature(temperatureData, targetDate) {
            let closestTemperature = null;
            let minDateDifference = Infinity;
        
            temperatureData.forEach(entry => {
                const dateDifference = Math.abs(entry.date - targetDate);
        
                if (dateDifference < minDateDifference) {
                    minDateDifference = dateDifference;
                    closestTemperature = entry;
                }
            });
        
            return closestTemperature;
        }   


// listening rectangle mouse leave function
    function mouseleave() {
        // Remove the vertical line and hide the tooltip
        svg.selectAll(".vertical-line").remove();
        tooltip.style("display", "none");
    }

    // Function to fill missing temperature values with the average of previous and next month's values
function fillMissingTemperature(data) {
    const filledData = [...data];

    for (let i = 1; i < filledData.length - 1; i++) {
        if (isNaN(filledData[i].value)) {
            const prevValue = filledData[i - 1].value;
            const nextValue = filledData[i + 1].value;

            if (!isNaN(prevValue) && !isNaN(nextValue)) {
                filledData[i].value = (prevValue + nextValue) / 2;
            } else if (!isNaN(prevValue)) {
                filledData[i].value = prevValue;
            } else if (!isNaN(nextValue)) {
                filledData[i].value = nextValue;
            }
        }
    }

    return filledData;
}

    // Function to calculate average temperature based on the given date
    function calculateAverageTemperature(d, data) {
        const month = d.date.getMonth();
        const year = d.date.getFullYear();

        const relevantData = data.filter(entry => entry.date.getMonth() === month && entry.date.getFullYear() === year);
        const validTemperatures = relevantData.map(entry => entry.temperature).filter(temp => !isNaN(temp));

        if (validTemperatures.length > 0) {
            return d3.mean(validTemperatures).toFixed(2);
        } else {
            return 'N/A';
        }
    }
}

// Function to update the meter types dropdown
function updateMeterTypes(meterTypes) {
    var meterDropdown = document.getElementById('meterDropdown');
    meterDropdown.innerHTML = '';  // Clear previous options

    meterTypes.forEach(function (meterType) {
        var option = document.createElement('option');
        option.value = meterType;
        option.text = meterType;
        meterDropdown.add(option);
    });
}

// Set up the change event listener for the property dropdown
document.getElementById('propertyDropdown').addEventListener('change', function (event) {
    event.preventDefault();  // Prevent default form submission behavior

    var selectedPropertyName = this.value;

    // Update the URL to include the selected property_id
    var url = '/get_meter_types/' + encodeURIComponent(selectedPropertyName) + '/';

    // Fetch meter types based on the selected property_id
    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Add any other headers if necessary
        },
    })
        .then(response => response.json())
        .then(data => {
            // Update the meter types dropdown
            updateMeterTypes(data.meter_types);

            // Select the first meter type by default
            var defaultMeterType = data.meter_types[0];
            document.getElementById('meterDropdown').value = defaultMeterType;

            // Trigger the change event for the meter dropdown
            document.getElementById('meterDropdown').dispatchEvent(new Event('change'));
        })
        .catch(error => console.error('Error:', error));
});

// Set up the change event listener for the meter dropdown
document.getElementById('meterDropdown').addEventListener('change', function (event) {
    event.preventDefault();  // Prevent default form submission behavior

    var selectedPropertyName = document.getElementById('propertyDropdown').value;
    var selectedMeterType = this.value;

    // Update the URL to include the selected property_id and meter_type
    var url = '/get_property_data/' + encodeURIComponent(selectedPropertyName) + '/' + encodeURIComponent(selectedMeterType) + '/';

    // Fetch and display property data based on the selected property and meter type
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Add any other headers if necessary
            'X-CSRFToken': getCookie('csrftoken'),  // Include CSRF token in the headers
        },
        body: JSON.stringify({ property_id: selectedPropertyName, meter_type: selectedMeterType })
    })
        .then(response => response.json())
        .then(data => {
            // Update the D3 graph with the selected property data
            updateGraph(data.data);
        })
        .catch(error => console.error('Error:', error));
});

// Trigger the change event after setting up the listener
document.getElementById('propertyDropdown').dispatchEvent(new Event('change'));

// Function to get the CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}