console.log('I am loaded');
function get_data_scientist(){

	const defaultURL = "/data_scientist";
	d3.json(defaultURL).then(function(data) {
 	var data = [data];
  	console.log('data',data);
  	var layout = { margin: { t: 30, b: 100 } };
  	Plotly.plot("bar", data, layout);
});

}
