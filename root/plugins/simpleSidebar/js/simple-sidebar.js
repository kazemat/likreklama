$(function () {
    $("#menu-toggle").click(function (e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
//        $(".navbar-wrapper").toggleClass("toggled");
    });
//    var sidebar = $('#sidebar-wrapper');
//    var header = $('#main-menu');
    function setSidebarHeight  () {
        var width = $(document).width();
        if (width <= 768) {
            $('#sidebar-wrapper').css({'top': $('#main-menu').height()})
                .addClass('toggled');
        }
        else {
            $('#sidebar-wrapper').css({'top': 0})
                .removeClass('toggled');
        }
        console.log(width);
        return $(document).width()
    }
    $(window).ready(
            setSidebarHeight()
    ).resize(function () {
           var w = setSidebarHeight();
//           if (w >= 768){
//               $('#main-menu').css({'top': $('#header-image').height()});
//           }
//           else {
//               $('#main-menu').css({'top': 0});
//           }
        }
    );
});