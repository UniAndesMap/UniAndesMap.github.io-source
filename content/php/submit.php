<?php
if(isset($_POST['url']) && $_POST['url'] == ''){
  // The form was submitted
  $ouremail = 'contacto@mapanica.net';

  // Important: if we add any form fields to the HTML,
  // and want them included in the email, we will need to add them here also
  $body = "Un reporte sobre $_POST[ruta]
  De: $_POST[name]
  E-Mail: $_POST[email]
  Telefono: $_POST[phone]
  Mensaje: $_POST[message]";
    // From:
    // Use the submitters email if they supplied one
    // (and it isn't trying to hack our form).
    // Otherwise send from our email address.
    if( $_POST['email'] && !preg_match( "/[\r\n]/", $_POST['email']) ) {
      $headers = "From: $_POST[email]";
    }
    else {
      $headers = "From: $ouremail";
    }
    // finally, send the message
    mail($ouremail, 'Reporte de rutas.mapanica.net', $body, $headers );
    header('Location: ../../index.html?message=¡Muchas gracias por su reporte!');
  }
  else {
    header('Location: ../../index.html?message="Mensaje no enviado"');
  }
?>
