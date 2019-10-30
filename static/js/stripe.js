/*global $*/ //Removes warning message for using $ in Jquery
$(document).ready(function(){
    $('#submit_payment_btn').click( function(){
        if ($("#id_credit_card_number").val().trim() == "" || $("#id_cvv").val().trim() == "") { //If a credit card field is empty then show an error
                $("#alert").show();
                $(window).scrollTop(0);
        } 
        if ($("#id_credit_card_number").val().trim() != "" || $("#id_cvv").val().trim() != "") { //If the credit card field is not empty then remove error
                $("#alert").hide();
        } 
        
}); 
});

$(function() {
    $("#payment-form").submit(function() {
        if ($("input:radio[name='what-button']").not(":checked")) { //Show the alert if a date button is not clicked 
                $("#alert-two").show();
                $(window).scrollTop(0);
                return false;
        }
        if ($("input:radio[name='what-button']").is(":checked")) { //Hide the alert if a date button is clicked 
                $("#alert-two").hide();
                var form = this;
                var card = {
                    number: $("#id_credit_card_number").val(),
                    expMonth: $("#id_expiry_month").val(),
                    expYear: $("#id_expiry_year").val(),
                    cvc: $("#id_cvv").val()
                };
        }
        
    
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {

            // Prevent the credit card details from being submitted
            // to our server
            $("#id_credit_card_number").removeAttr('name');
            $("#id_cvv").removeAttr('name');
            $("#id_expiry_month").removeAttr('name');
            $("#id_expiry_year").removeAttr('name');

            form.submit();
        }
    });
    return false;
    });
});