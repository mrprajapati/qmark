$(document).ready(function () {

    // var infinite = new.Waypoint.Infinite({
    //     element: $('#news-cont')[0],
    //     onBeforePageLoad: function () {
    //         $('.loading').show();
    //         alert('This is working');
    //     },
    //     onAfterPageLoad: function ($items) {
    //         $('.loading').hide();
    //     }
    // })

    $('#filter-btn').click(function () {
        $('.filter-pop').toggle();
    });


    $('.dropdown-toggle').dropdown('toggle');
})