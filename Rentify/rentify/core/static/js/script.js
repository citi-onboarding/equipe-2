/*              NAVBAR              */
/*global $*/
$(document).ready(function() {
    function alertfunc(){
        alert("ola")
    }
    $(".btn-orange").click(function (){
        $("#modal").removeClass("not");
    });
    
    $("#navToggle").click(function (){
        if($("#myTopnav").hasClass("navbar responsive")) {
            $("#myTopnav").removeClass("navbar responsive").addClass("navbar");
        } else {
            $("#myTopnav").addClass(" responsive")
        }
    })
});