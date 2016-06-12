;(function($) {

"use strict";

var $body = $('body');

$(document).ready(function() {

  var subtleOptions = {
    id: "subtle",
    options:{
      name: "Subtle Grayscale"
    },
    styles: [
    {
        "featureType": "all",
        "elementType": "labels.text.fill",
        "stylers": [
            {
                "saturation": 36
            },
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 40
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.text.stroke",
        "stylers": [
            {
                "visibility": "on"
            },
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "all",
        "elementType": "labels.icon",
        "stylers": [
            {
                "visibility": "off"
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 17
            },
            {
                "weight": 1.2
            }
        ]
    },
    {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 20
            }
        ]
    },
    {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 21
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 17
            }
        ]
    },
    {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 29
            },
            {
                "weight": 0.2
            }
        ]
    },
    {
        "featureType": "road.arterial",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 18
            }
        ]
    },
    {
        "featureType": "road.local",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 16
            }
        ]
    },
    {
        "featureType": "transit",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#4b4b53"
            },
            {
                "lightness": 19
            }
        ]
    },
    {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
            {
                "color": "#fecb00"
            },
            {
                "lightness": 17
            }
        ]
    }
    ]
  };

  lightbox.option({
    'positionFromTop': 150
  })

  // OUR LOCATION MAP SETTINGS
  $('#map-contact').gmap3({
  	marker:{
      address: "London",
      options:{
        icon: "img/marker.png"
      }
    },
    map:{
      options: {
      	zoom:10,
		    mapTypeId: "subtle",
		    mapTypeControlOptions: {
		      mapTypeIds: ["subtle"]
		    },
		    scrollwheel: false,
		    streetViewControl: false,
		    disableDefaultUI: true,
      }
    },
    styledmaptype: subtleOptions
  });

	$("#testimonials-slider").owlCarousel({
		items: 6,
		navigation: true,
        autoPlay: true,
	    navigationText: [
	      '<div class="prev"><i class="fa fa-caret-left"></i></div>',
	      '<div class="next"><i class="fa fa-caret-right"></i></div>'
	    ]
	});

  $(".slider").owlCarousel({
      singleItem: true,
      autoPlay: 7500,
      navigation: true,
      navigationText: [
        '<div class="prev"><i class="fa fa-caret-left"></i></div>',
        '<div class="next"><i class="fa fa-caret-right"></i></div>'
      ]
  });

  $(window).scroll(function(){

    if($(window).width() >= 991) {
        if ($(window).scrollTop() > 50){
          $('#header').addClass("active");
        }
        else if ($(window).scrollTop() < 50){
          $('#header').removeClass("active");
        }
    };
  });

  // NAVBAR TOGGLE
  $('.toggle').each(function() {
    $(this).click(function() {
      $(this).parent().parent().find('.navigation nav').slideToggle('200');
    });
  });

  var top_offset = $('#header').height() - 20;  // get height of fixed navbar

  $('.navbar-nav').onePageNav({
    currentClass: 'current',
    changeHash: false,
    scrollSpeed: 750,
    scrollThreshold: 0.5,
    scrollOffset: top_offset,
    filter: '',
    easing: 'swing',
    begin: function() {
        //I get fired when the animation is starting
    },
    end: function() {
        //I get fired when the animation is ending
    },
    scrollChange: function($currentListItem) {
        //I get fired when you enter a section and I pass the list item of the section
    }
  });

  $(window).resize(function() {
    if($(window).width() >= 991) {
      $('.navigation nav').removeAttr( 'style' );
    }
  });

	$(window).scroll(function() {	
		animateProgressBars();
	});

	function animateProgressBars() {

		$('.progress-bar .progress-bar-outer:in-viewport').each(function() {
			
			var $t = $(this);
			
			if (!$t.hasClass("already-animated")) {
				$t.addClass("already-animated");
				$t.animate({
					width: $t.attr("data-width") + "%"
				}, 2500, 'easeOutQuint');
			}
		});
	}

	animateProgressBars();

});

$(window).load(function(){

    $('.filters').each(function() {
    var $container = $('.projects-wrapper').isotope({
      itemSelector: '.projects-wrapper .portfolio-single',
      layoutMode: 'masonry'
    });
     var filterFns = {
      };

    $('.filters li a').on( 'click', function() {
      var filterValue = $( this ).attr('data-filter');
      // use filterFn if matches value
      filterValue = filterFns[ filterValue ] || filterValue;
      $container.isotope({ filter: filterValue });

      $('.filters li a').each(function(){
        $(this).removeClass("active");
      });
      $(this).addClass("active");

      return false;
    });
  });
});


// Touch
// ---------------------------------------------------------
var dragging = false;

$body.on('touchmove', function() {
	dragging = true;
});

$body.on('touchstart', function() {
	dragging = false;
});



}(jQuery));
