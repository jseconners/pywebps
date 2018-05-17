# pywebps
Really basic Python web plotting service.

### Overview
pywebps is served using flask and builds plots using matplotlib and pandas. It's
a really simple microservice that takes a URL to a CSV file and some plot
configurations and returns a plot image.

Set up this app somewhere on your server, e.g.

`http://example.com/pywebps`

Then access the various plots with a POST request, like so:

`http://example.com/pywebps/scatter`

Post data:

    {
    	"data": "http://example.com/mydata.csv",
    	"config": {
    		"size": [8, 5],
    		"x": {
    			"col": "ws",
    			"label": "Wind Speed (knts)"
    		},
    		"y": {
    			"col": "temp",
    			"label": "Temp C"

    		}
    	}
    }

### Plots
Examples of plots below

#### Time series
![screenshot](https://raw.githubusercontent.com/jseconners/pywebps/master/docs/images/ts.png)
![screenshot](https://raw.githubusercontent.com/jseconners/pywebps/master/docs/images/ts_subplots.png)

The time series plot configuration takes three objects, a figure size (in inches),
an object with the x-axis config and another with the y-axis config.


**x**
| Param         | Description                       |
|:--------------|:----------------------------------|
| `date`      | Required date or datetime column in your CSV
| `time`    | Optional time column if date and time are in separate columns
| `label` | X-axis label

**y**
An array of objects for each line to plot agains the x-axis. Each additional
data line will be plotted in a subplot
| Param         | Description                       |
|:--------------|:----------------------------------|
| `col`      | Data column for this line in the CSV file
| `label` | Y-axis label for this data line


     {
    	"data": "http://example.com/mydata.csv",
    	"config": {
    		"size": [8, 5],
    		"x": {
    			"date": "date",
    			"time": "time",
    			"label": "Datetime"
    		},
    		"y": [
    			{
    			    "col": "temp",
    			    "label": "Temp C"

    		    },
    			{
    			    "col": "ws",
    			    "label": "Wind Speed (knts)"

    		    }
    		]
    	}
    }

#### Scatter
![screenshot](https://raw.githubusercontent.com/jseconners/pywebps/master/docs/images/scatter.png)




### Author

-  James Conners (jseconners@gmail.com)
