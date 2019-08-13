// This example adds a search box to a map, using the Google Place Autocomplete
// feature. People can enter geographical searches. The search box will return a
// pick list containing a mix of places and predicted search terms.

// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
//


var btn = document.getElementById('btn')
var polygonArray = [];
var directionService = {};
var directionDisplay = {};
$("#distance_form").submit(false)

function initAutocomplete() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 13,
    mapTypeId: 'roadmap'
  });

  directionDisplay = new google.maps.DirectionsRenderer();
  directionService = new google.maps.DirectionsService();
  directionDisplay.setMap(map);

  // Create the search box and link it to the UI element.
  var input = document.getElementById('pac-input');
  var searchBox = new google.maps.places.SearchBox(input);
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(input);

  // Bias the SearchBox results towards current map's viewport.
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
  });

  var markers = [];
  // Listen for the event fired when the user selects a prediction and retrieve
  // more details for that place.
  searchBox.addListener('places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }

    // Clear out the old markers.
    markers.forEach(function(marker) {
      marker.setMap(null);
    });
    markers = [];

    // For each place, get the icon, name and location.
    var bounds = new google.maps.LatLngBounds();
    places.forEach(function(place) {
      if (!place.geometry) {
        console.log("Returned place contains no geometry");
        return;
      }
      var icon = {
        url: place.icon,
        size: new google.maps.Size(71, 71),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(17, 34),
        scaledSize: new google.maps.Size(25, 25)
      };

      // Create a marker for each place.
      markers.push(new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      }));

      if (place.geometry.viewport) {
        // Only geocodes have viewport.
        bounds.union(place.geometry.viewport);
      } else {
        bounds.extend(place.geometry.location);
      }
    });
    map.fitBounds(bounds);
  });

  var drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.POLYGON,
    drawingControl: true,
    drawingControlOptions: {
        editable:true,
      position: google.maps.ControlPosition.BOTTOM_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE
      ]
    },

  });

      drawingManager.setMap(map)

    google.maps.event.addListener(drawingManager, 'polygoncomplete', function(polygon) {

      let length = polygon.getPath().getLength();
      for (var i = 0; i < length; i++) {
        if (i< length-1 )
        document.getElementById('id_coordinates').value += polygon.getPath().getAt(i).toUrlValue(6) + "end";
        else
          document.getElementById('id_coordinates').value += polygon.getPath().getAt(i).toUrlValue(6);
      }
      polygonArray.push(polygon);
    });

      google.maps.event.addDomListener(window, 'load', function () {
            from_places = new google.maps.places.Autocomplete(document.getElementById('from_places'));
            to_places = new google.maps.places.Autocomplete(document.getElementById('to_places'));


        });
}

    var from_places;
    var to_places;
    var fromText;
    var toText;
  // add input listeners


        function getCoordinates(address){
          return new Promise(function(resolve, reject){
            var geocoder = new google.maps.Geocoder();
            geocoder.geocode({'address': address}, function (results, status) {

              if (status == "OK") {
                resolve([results[0].geometry.location.lat(), results[0].geometry.location.lng()]);
              } else {
                reject(new Error("Error occured"))
              }
            });
          })
        }


        btn.onclick = async () => {
          fromText = document.getElementById("from_places");
          toText = document.getElementById("to_places");
          const fromPoint = await getCoordinates(fromText.value);
          const toPoint = await getCoordinates(toText.value);
          var x = new google.maps.LatLng(fromPoint[0], fromPoint[1]);
          var y = new google.maps.LatLng(toPoint[0], toPoint[1]);

          var service = new google.maps.DistanceMatrixService();
          service.getDistanceMatrix(
            {
              origins: [x, fromText.value],
              destinations: [toText.value, y],
              travelMode: 'DRIVING'
            }, callback);

          function callback(response, status) {
            if (status == 'OK') {
              map.center = x;

              var request = {
                origin: x,
                destination: y,
                travelMode: 'DRIVING'

              };

              directionService.route(request, (res, status) => {
                if (status == "OK"){
                  directionDisplay.setDirections(res);
                }
              });

              var origins = response.originAddresses;
              var destinations = response.destinationAddresses;

              for (var i = 0; i < origins.length; i++) {
                var results = response.rows[i].elements;
                for (var j = 0; j < results.length; j++) {
                  var element = results[j];

                  // 400 rwf per Kilometer
                  var price = Math.round((element.distance.value)/1000 * 400).toLocaleString();
                  var distance = element.distance.text;
                  var duration = element.duration.text;
                  var from = origins[i];
                  var to = destinations[j];

                  document.getElementById("distance").value = distance;
                  document.getElementById("duration").value = duration;
                  document.getElementById("price").value = price + " Rwf";
                }
              }
            }
          }
        };



new google.maps.event.addDomListener(window, "load", initialize);


function showCoordinates(event){
  let coord = event.textContent.split('end');
  var point ={};
  var coordinates=[];

  for  (var i = 0; i < coord.length; i++){
    point.lat =parseFloat(coord[i].split(',')[0]);
    point.lng=parseFloat(coord[i].split(',')[1]);
    coordinates.push({lat: point.lat, lng: point.lng});
  }

  // console.log(coordinates);

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: coordinates[0].lat, lng: coordinates[0].lng},
    zoom: 10,
    mapTypeId: 'roadmap'
  });


  var poly = new google.maps.Polygon({
          paths: coordinates,
          strokeColor: '#FF0000',
          strokeOpacity: 5,
          strokeWeight: 2,
          fillColor: '#ff8e85',
          fillOpacity: 0.5
        });
  poly.setMap(map);
}
