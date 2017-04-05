var makePie = function() {
	/*var dataset = [
		{ label: 'Seniors', count: 10 },
		{ label: 'Juniors', count: 40 },
		{ label: 'Sophomores', count: 30 },
		{ label: 'Freshmen', count: 20 }
	];*/
	var dataYr = dataset[0];
	var width = 700;
	var height = 400;
	var radius = Math.min(360, 360) / 2;
	var legendRectSize = 18;
  var legendSpacing = 4;

	var color = d3.scale.ordinal()
		.range(["#dd7777", "#c92e2e", "#aa2f2f", "#7c0000"]);
		
	var svg = d3.select('#chart')
		.append('svg')
		.attr('width', width)
		.attr('height', height)
		.append('g')
		.attr('transform', 'translate(' + (width / 2) +
			',' + (height / 2) + ')');

	var arc = d3.arc()
		.innerRadius(0)
		.outerRadius(radius);

	var pie = d3.pie()
		.value(function(d) { return d.count; })
		.sort(null);					

	var path = svg.selectAll("path")
		.data(pie(dataYr))
		.enter()
		.append('path')
		.attr('d', arc)
		.attr('fill', function(d) {
			return color(d.data.label);
		})
		.each(function(d) { this._current = d; });
		
	d3.selectAll(".rc")
      .on("change", change);
			
	function change() {
    var value = this.value;
		dataYr = dataset[value];
    path = path.data(pie(dataYr)); 
    path.transition().duration(750).attrTween("d", arcTween);
  }
	
	function arcTween(a) {
		var i = d3.interpolate(this._current, a);
		this._current = i(0);
		return function(t) {
			return arc(i(t));
		};
	}
	
	var legend = svg.selectAll('.legend')                     
		.data(color.domain())                                   
		.enter()                                                
		.append('g')                                            
		.attr('class', 'legend')                                
		.attr('transform', function(d, i) {                     
			var height = legendRectSize + legendSpacing;          
			var offset =  height * color.domain().length / 2;     
			var horz = legendRectSize + 205;                       
			var vert = i * height - offset;                       
			return 'translate(' + horz + ',' + vert + ')';        
		});                                                     

	legend.append('rect')                                     
		.attr('width', legendRectSize)                          
		.attr('height', legendRectSize)                         
		.style('fill', color)                                   
		.style('stroke', color);                                

	legend.append('text') 
		.attr('x', legendRectSize + legendSpacing)              
		.attr('y', legendRectSize - legendSpacing) 
		.text(function(d) { return d; })

};
		
makePie();