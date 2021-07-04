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
      if( confirm("Are you sure you want to delete this book? This is not reversible once done. Click OK to confirm deletion or Cancel to go back")){
      return true;
      } else{
      return false;
      }
      });

      //Text character Counter initializer for book desc and comments
      $( '#desc, #comments').characterCounter(); 
  });

//copyright span year date
$("#copyright-date").text(new Date().getFullYear());