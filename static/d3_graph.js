console.log('it is start');

        // Function to update the D3 graph
        function updateGraph(data) {
            // Set dimensions and margins for the chart
            const margin = { top: 70, right: 30, bottom: 40, left: 80 };
            const width = 1200 - margin.left - margin.right;
            const height = 500 - margin.top - margin.bottom;

            // Set up the x and y scales
            const x = d3.scaleTime().range([0, width]);
            const y = d3.scaleLinear().range([height, 0]);

            // Create the SVG element and append it to the chart container
            const svg = d3.select("#chart-container")
                .html("")  // Clear previous SVG content
                .append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform", `translate(${margin.left},${margin.top})`);

            // Parse date values as JavaScript Date objects
            data.forEach(function (d) {
                d.date = new Date(d.date);
            });

            // Log the dataset to the console
            console.log(data);

            // Define the x and y domains
            x.domain(d3.extent(data, d => d.date));
            y.domain([0, d3.max(data, d => d.value)]);

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
                );

            // Add the y-axis
            svg.append("g")
                .call(d3.axisLeft(y))

            // Create the line generator
            const line = d3.line()
                .x(d => x(d.date))
                .y(d => y(d.value));

            // Add the line path to the SVG element
            svg.append("path")
                .datum(data)
                .attr("fill", "none")
                .attr("stroke", "red")
                .attr("stroke-width", 1)
                .attr("d", line);
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

        var selectedPropertyId = this.value;

        // Update the URL to include the selected property_id
        var url = '/get_meter_types/' + encodeURIComponent(selectedPropertyId) + '/';

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

        var selectedPropertyId = document.getElementById('propertyDropdown').value;
        var selectedMeterType = this.value;

        console.log(selectedPropertyId, selectedMeterType);

        // Update the URL to include the selected property_id and meter_type
        var url = '/get_property_data/' + encodeURIComponent(selectedPropertyId) + '/' + encodeURIComponent(selectedMeterType) + '/';

        // Fetch and display property data based on the selected property and meter type
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add any other headers if necessary
            },
            body: JSON.stringify({ property_id: selectedPropertyId, meter_type: selectedMeterType })
        })
        .then(response => response.json())
        .then(data => {
            // Update the D3 graph with the selected property data
            updateGraph(data);
        })
        .catch(error => console.error('Error:', error));
    });

    // Trigger the change event after setting up the listener
    document.getElementById('propertyDropdown').dispatchEvent(new Event('change'));