//Side nave-bar for mobile initialisation
$(document).ready(function(){
  //Side nave-bar for mobile initialisation
    $('.sidenav').sidenav();
//Terms and conditions terms and cons
    $('#termsCon').hide();
    
    $('#termsConTrigger').click(function(){
      $('#termsCon').toggle();
    });
  });

//copyright span year date
$("#copyright-date").text(new Date().getFullYear());
