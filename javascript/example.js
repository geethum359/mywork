$(document).ready (function()
{
    $('#b1').click(function(){
        $("div").hide();
    });
    $('#b2').click(function(){
        $("div").show();
    });
    $('#b3').click(function(){
        $("div").toggle();
    });
});