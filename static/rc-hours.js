var makePie = function() {
        var dataset = [
          { label: 'Seniors', count: 10 },
          { label: 'Juniors', count: 40 },
          { label: 'Sophomores', count: 30 },
          { label: 'Freshmen', count: 20 }
        ];

        var width = 700;
        var height = 400;
        var radius = Math.min(width, height) / 2;

        var color = d3.scaleOrdinal(d3.schemeCategory20c);

        var svg = d3.select('#chart')
          .append('svg')
          .attr('width', width)
          .attr('height', height)
					.attr('style', 'border: 1px solid')
          .append('g')
          .attr('transform', 'translate(' + (width / 2) +
            ',' + (height / 2) + ')');

        var arc = d3.arc()
          .innerRadius(0)
          .outerRadius(radius);

        var pie = d3.pie()
          .value(function(d) { return d.count; })
          .sort(null);					

        var path = svg.selectAll('g')
          .data(pie(dataset))
          .enter()
          .append('path')
          .attr('d', arc)
          .attr('fill', function(d) {
            return color(d.data.label);
          });
					
			  var text = svg.selectAll('g')
				  .data(pie(dataset))
          .enter()
					.append('text')
					.attr("transform", function(d) {
          d.innerRadius = 0;
          d.outerRadius = radius;
          return "translate(" + arc.centroid(d) + ")";
          })
          .attr("text-anchor", "middle")
          .text(function(d) { return d.data.label; });
};
		
makePie();