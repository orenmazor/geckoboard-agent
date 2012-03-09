types = {"number_and_secondary_stat":
			{ "item" : [ { "text" : "","value" : 0},{ "text" : "","value" : 238}] },
		"line_chart":{
			    "item": [],
			    "settings": {
			     "axisx": [],
			     "axisy": [],
			     "colour": "ff9900"
			    }
			},
            "highchart":{
                "chart": {
                    "renderTo": 'container',
                    "plotBackgroundColor": 'rgba(35,37,38,0)',
                    "backgroundColor": 'rgba(35,37,38,100)',
                    "borderColor": 'rgba(35,37,38,100)',
                    "lineColor": 'rgba(35,37,38,100)',
                    "plotBorderColor": 'rgba(35,37,38,100)',
                    "plotBorderWidth": 0,
                    "plotShadow": 0,
                    "height": 170
                },
                "colors": ['#058DC7','#50B432','#EF561A'],
                "credits": {    
                    "enabled": 0
                },
                "title": {
                    "text": ""
                },
                "legend": {
                    "borderColor": 'rgba(35,37,38,100)',
                    "itemWidth": 55,
                    "margin": 5,
                    "width": 200
                },
                "plotOptions": {
                    "pie": {
                        "animation": 1,
                        "allowPointSelect": 1,
                        "cursor": 'pointer',
                        "dataLabels": {
                            "enabled": 1
                        },
                    "showInLegend": 1,
                    "size": '100%'
                    }
                },
                "series": [{
                    "type": 'pie',
                    "name": '',
                    "data": []
                }]
            }
		}