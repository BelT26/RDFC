//The below code is based on the map section in the Bootstrap resume walkthrough project

// Creates a new google map and sets the zoom and central location
function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: {
            lat: 51.23,
            lng: -0.215
        }
    });

// labels to be used to mark locations on the map
    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// co-ordinates of the club's grounds
    var locations = [
        { lat: 51.22475989430041, lng: -0.21370240175851882 },
    ];

// maps markers to co-ordinates in the locations array    
    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}

