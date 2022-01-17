function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: {
            lat: 51.23,
            lng: -0.215
        }
    });

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    var locations = [
        { lat: 51.22475989430041, lng: -0.21370240175851882 },
    ];

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length]
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}

