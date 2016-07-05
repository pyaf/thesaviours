// function initialize() {		
// 		var mapProp = {
// 			center:new google.maps.LatLng(25.2682211, 82.9900223),
// 			zoom:13,
// 		};

// 		var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
		
		
// 		var trafficLayer = new google.maps.TrafficLayer();
  
//   		trafficLayer.setMap(map);
// 		}
// 		google.maps.event.addDomListener(window, 'load', initialize);//event listener to load the map



// function initMap() {
	
// 	var mapProperties = {
// 		zoom: 13,
//     	center: {lat: 25.2682211, lng:82.9900223},
//         disableDefaultUI: true

	
// 	}
	
// 	var div = document.getElementById('googleMap');
//     var map = new google.maps.Map(div, mapProperties);
// 	var trafficLayer = new google.maps.TrafficLayer();
  
//   	trafficLayer.setMap(map);
	
// 	// var marker = new MarkerWithLabel({
//  //    position: map.getCenter(),
//  //    icon: {
//  //      path: google.maps.SymbolPath.CIRCLE,
//  //      scale: 0, //tamaño 0
//  //    },
//  //    map: map,
//  //    draggable: true,
//  //    labelAnchor: new google.maps.Point(10, 10),
//  //    labelClass: "label", // the CSS class for the label
//   // });

// 	}

// google.maps.event.addDomListener(window, 'load', initMap);


//External resources:
//http://maps.google.com/maps/api/js?sensor=false
//https://google-maps-utility-library-v3.googlecode.com/svn-history/r391/trunk/markerwithlabel/src/markerwithlabel.js

// function init() {
  
//   var mapOptions = {
//       zoom: 8,
//       center: new google.maps.LatLng(40.417181, -3.700823),
//       mapTypeId: google.maps.MapTypeId.ROADMAP,
//       disableDefaultUI: true
//   };
  
//   var myMap = new google.maps.Map(document.getElementById('myMap'), mapOptions);
  
//   var marker = new MarkerWithLabel({
//     position: myMap.getCenter(),
//     icon: {
//       path: google.maps.SymbolPath.CIRCLE,
//       scale: 0, //tamaño 0
//     },
//     map: myMap,
//     draggable: true,
//     labelAnchor: new google.maps.Point(10, 10),
//     labelClass: "label", // the CSS class for the label
//   });
// }
// google.maps.event.addDomListener(window, 'load', init);



function initMap() {
  var myLatLng =  {lat: 25.2682211, lng:82.9900223};
  // Create a map object and specify the DOM element for display.
  var map = new google.maps.Map(document.getElementById('googleMap'), {
    center: myLatLng,
    scrollwheel: false,
    zoom: 13
  });

var trafficLayer = new google.maps.TrafficLayer();
	trafficLayer.setMap(map);
  // Create a marker and set its position.
  var im = 'http://www.robotwoods.com/dev/misc/bluecircle.png'

  var marker = new google.maps.Marker({

    map: map,
    position: myLatLng,
    title: 'amb id',
    icon: im,
  });
}

google.maps.event.addDomListener(window, 'load', initMap);
