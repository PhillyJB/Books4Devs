//Side nave-bar for mobile initialisation
$(document).ready(function(){
  //Side nave-bar for mobile initialisation
    $('.sidenav').sidenav();

//Terms and conditions hide then toggle
    $('#termsCon').hide();
    $('#termsConTrigger').click(function(){
      $('#termsCon').toggle(300);
    });

    //J query defence programming for are you sure 
    $('.deletion-alert').click(function(){
      if( confirm("are you sure you want to delete this book? Click OK to Confirm deletion or Cancel to go back")){
      return true;
      } else{
      return false;
      }
      });
  });

//copyright span year date
$("#copyright-date").text(new Date().getFullYear());