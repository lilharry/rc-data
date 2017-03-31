var pie = new d3pie("pieChart", {
	"header": {
		"title": {
			"text": "Red Cross",
			"fontSize": 22,
			"font": "helvetica"
		},
		"subtitle": {
			"color": "#999999",
			"fontSize": 10,
			"font": "verdana"
		},
		"titleSubtitlePadding": 12
	},
	"footer": {
		"color": "#999999",
		"fontSize": 11,
		"font": "open sans",
		"location": "bottom-center"
	},
	"size": {
		"canvasHeight": 400,
		"canvasWidth": 700,
		"pieInnerRadius": "44%",
		"pieOuterRadius": "79%"
	},
	"data": {
		"content": [
			{
				"label": "Seniors",
				"value": 6000,
				"color": "#7c0000"
			},
			{
				"label": "Juniors",
				"value": 5000,
				"color": "#aa2f2f"
			},
			{
				"label": "Sophomores",
				"value": 4000,
				"color": "#c92e2e"
			},
			{
				"label": "Freshmen",
				"value": 3000,
				"color": "#dd7777"
			}
		]
	},
	"labels": {
		"outer": {
			"pieDistance": 19
		},
		"inner": {
			"format": "value"
		},
		"mainLabel": {
			"font": "verdana"
		},
		"percentage": {
			"color": "#e1e1e1",
			"font": "verdana",
			"decimalPlaces": 0
		},
		"value": {
			"color": "#e1e1e1",
			"font": "verdana"
		},
		"lines": {
			"enabled": true,
			"style": "straight"
		},
		"truncation": {
			"enabled": true
		}
	},
	"effects": {
		"pullOutSegmentOnClick": {
			"effect": "none",
			"speed": 400,
			"size": 8
		}
	},
	"callbacks": {}
});