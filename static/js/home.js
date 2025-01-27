
// Preloader
$(window).on('load', function () {
  if ($('#preloader').length) {
    $('#preloader').delay(100).fadeOut('slow', function () {
      $(this).remove();
    });
  }
});

/*     // Smooth scroll for the navigation menu and links with .scrollto classes
 $(document).on('click', '.nav-menu a, .mobile-nav a, .scrollto', function(e) {
      if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        e.preventDefault();
        var target = $(this.hash);
        if (target.length) {
  
          var scrollto = target.offset().top;
          var scrolled = 20;
  
          if ($('#header').length) {
            scrollto -= $('#header').outerHeight()
  
            if (!$('#header').hasClass('header-scrolled')) {
              scrollto += scrolled;
            }
          }
  
          if ($(this).attr("href") == '#header') {
            scrollto = 0;
          }
  
          $('html, body').animate({
            scrollTop: scrollto
          }, 1500, 'easeInOutExpo');
  
          if ($(this).parents('.nav-menu, .mobile-nav').length) {
            $('.nav-menu .active, .mobile-nav .active').removeClass('active');
            $(this).closest('li').addClass('active');
          }
  
          if ($('body').hasClass('mobile-nav-active')) {
            $('body').removeClass('mobile-nav-active');
            $('.mobile-nav-toggle i').toggleClass('fa fa-bars fa fa-window-close');
            $('.mobile-nav-overly').fadeOut();
          }
          return false;
        }
      }
    });
 */


// change active class 
/* $(document).on('click', '.nav-menu a, .mobile-nav a', function() {
  
  $('.nav-menu .active, .mobile-nav .active').removeClass('active');
    $(this).parent().addClass('active');
}); */

$('.nav-menu li, .mobile-nav li').each(function () {
  if (window.location.href.indexOf($(this).find('a:first').attr('href')) > -1) {
    $(this).addClass('active').siblings().removeClass('active');
  }
});


// change navbar transplarent 
$(window).on('load', function () {
  if (this.location.pathname != '/') {
    $('#header').addClass("header-inner-pages");
  }
});


// Mobile Navigation
if ($('.nav-menu').length) {
  var $mobile_nav = $('.nav-menu').clone().prop({
    class: 'mobile-nav d-lg-none'
  });
  $('body').append($mobile_nav);
  $('body').prepend('<button type="button" class="mobile-nav-toggle d-lg-none"><i class="fa fa-bars"></i></button>');
  $('body').append('<div class="mobile-nav-overly"></div>');

  $(document).on('click', '.mobile-nav-toggle', function (e) {
    $('body').toggleClass('mobile-nav-active');
    $('.mobile-nav-toggle i').toggleClass('fa fa-bars fa fa-window-close');
    $('.mobile-nav-overly').toggle();
  });

  $(document).on('click', '.mobile-nav .drop-down > a', function (e) {
    e.preventDefault();
    $(this).next().slideToggle(300);
    $(this).parent().toggleClass('active');
  });

  $(document).click(function (e) {
    var container = $(".mobile-nav, .mobile-nav-toggle");
    if (!container.is(e.target) && container.has(e.target).length === 0) {
      if ($('body').hasClass('mobile-nav-active')) {
        $('body').removeClass('mobile-nav-active');
        $('.mobile-nav-toggle i').toggleClass('fa fa-bars fa fa-window-close');
        $('.mobile-nav-overly').fadeOut();
      }
    }
  });
} else if ($(".mobile-nav, .mobile-nav-toggle").length) {
  $(".mobile-nav, .mobile-nav-toggle").hide();
}

// Navigation active state on scroll
/*   var nav_sections = $('section');
  var main_nav = $('.nav-menu, #mobile-nav');
 
  $(window).on('scroll', function() {
    var cur_pos = $(this).scrollTop() + 90;
 
    nav_sections.each(function() {
      var top = $(this).offset().top,
        bottom = top + $(this).outerHeight();
 
      if (cur_pos >= top && cur_pos <= bottom) {
        if (cur_pos <= bottom) {
          main_nav.find('li').removeClass('active');
        }
        main_nav.find('a[href="#' + $(this).attr('id') + '"]').parent('li').addClass('active');
      }
      if (cur_pos < 300) {
        $(".nav-menu ul:first li:first").addClass('active');
      }
    });
  }); */

// Toggle .header-scrolled class to #header when page is scrolled
$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
  } else {
    $('#header').removeClass('header-scrolled');
  }
});

if ($(window).scrollTop() > 100) {
  $('#header').addClass('header-scrolled');
}

// Back to top button
$(window).scroll(function () {
  if ($(this).scrollTop() > 100) {
    $('.back-to-top').fadeIn('slow');
  } else {
    $('.back-to-top').fadeOut('slow');
  }
});

$('.back-to-top').click(function () {
  $('html, body').animate({
    scrollTop: 0
  }, 1500, 'easeInOutExpo');
  return false;
});

// Initi AOS
function aos_init() {
  AOS.init({
    duration: 1000,
    once: true
  });
}
aos_init();



// //Modal Init
// $('#signIn').on('click', function () {
//   $('#signIn').modal('toggle');
// });

