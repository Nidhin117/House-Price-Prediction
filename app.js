function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://localhost:8000/location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
  $.get(url,function(data, status) {
      console.log("got response for get_location_names request");
      if(data) {
          var locations = data.locations;
          var uiLocations = document.getElementById("location");
          $('#location').empty();
          for(var i in locations) {
              var opt = new Option(locations[i]);
              $('#location').append(opt);
          }
      }
  });
}

window.onload = onPageLoad;

function onClickedEstimatePrice() {
	
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("squareFeet").value;
  var bhk = document.getElementById("bhk").value;
  var bathrooms =  document.getElementById("bath").value;
  var loc = document.getElementById("location").value;
  var balcony = document.getElementById("balcony").value;
  var estPrice = document.getElementById("estimatedPrice");
  var url = "http://localhost:8000/estimate_houseprice"; 
  console.log(sqft + " " + bhk + " " + bathrooms + " " + loc + " " +  balcony )
  payload = {
"location" : loc,
"sqft" : sqft,
"bath" : bathrooms,
"balcony" : balcony,
"bhk" : bhk
  }
  $.ajax({
    url: url,
    method: 'POST', 
    data: JSON.stringify(payload), // Your request data
    contentType: 'application/json', // Set the Content-Type header
    success: function(response) {
      console.log(response.estimated_price);
      estPrice.innerHTML = "<h2>" + response.estimated_price.toString() + " Lakh</h2>";
	  estPrice.value = response.estimated_price.toString()
    },
    error: function(error) {
        console.log(error)
    }
});
}