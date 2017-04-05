// Set the dimensions of the canvas / graph
var margin = {top: 30, right: 20, bottom: 80, left: 50},
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// Parse the date / time
var parseDate = d3.time.format("%m/%Y").parse;	

// Set the ranges
var x = d3.time.scale().range([0, width]);
var y = d3.scale.linear().range([height, 0]);

// Define the axes
var xAxis = d3.svg.axis().scale(x)
    .orient("bottom").ticks(14);

var yAxis = d3.svg.axis().scale(y)
    .orient("left").ticks(10);

// Define the line
var valueline = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.hours); });
    
// Adds the svg canvas
var svg = d3.select("body")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .attr("class","line")
    .append("g")
        .attr("transform", 
              "translate(" + margin.left + "," + margin.top + ")");

d3.csv("/static/events.csv", function(error, data) {
    data.forEach(function(d) {
        d.date = parseDate(d.date);
        d.hours = +d.hours;
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.hours; })]);

    // Add the valueline path.
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));
    // Add the X Axis
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)   
            .selectAll("text")      
                 .style("text-anchor", "end")
                 .attr("dx", "-.8em")
                 .attr("dy", ".15em")
                 .attr("transform", "rotate(-65)");
                // Add the Y Axis
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);

});