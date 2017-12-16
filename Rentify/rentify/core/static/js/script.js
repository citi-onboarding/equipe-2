/*              NAVBAR              */
$(document).ready(function() {
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "navbar") {
        x.className += " responsive";
    } else {
        x.className = "navbar";
    }
}
    $(".btn-orange").click(function (){
        $("#modal").removeClass("not");
    });
});