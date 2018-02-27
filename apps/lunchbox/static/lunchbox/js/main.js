var input = document.getElementById('loc');
var autocomplete = new google.maps.places.Autocomplete(input);
var infowindowContent = document.getElementById('infowindow-content');


autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }
    var address = '';
          if (place.address_components) {
            address = [
              (place.address_components[0] && place.address_components[0].short_name || ''),
              (place.address_components[1] && place.address_components[1].short_name || ''),
              (place.address_components[2] && place.address_components[2].short_name || '')
            ].join(' ');
          }

        //   infowindowContent.children['place-icon'].src = place.icon;
        //   infowindowContent.children['place-name'].textContent = place.name;
        //   infowindowContent.children['place-address'].textContent = address;
        console.log(place)
        document.getElementById('city').value=place.address_components[2].long_name;
        document.getElementById('lng').value=place.geometry.viewport.b.b;
        document.getElementById('lat').value=place.geometry.viewport.f.b;
})
