/*global $*/ //Removes warning message for using $ in Jquery
$(document).ready(function(){
    $('#submit_payment_btn').click( function(e){
        if ($("#id_credit_card_number").val().trim() == "" || $("#id_cvv").val().trim() == "") { //If a credit card firld is empty then show an error
                $("#alert").show();
                $(window).scrollTop(0);
        }
        if ($("input:radio[name='what-button']").is(":checked")) { //Hide the alert if a date button is clicked 
                $("#alert").hide();
                $(window).scrollTop(0);
        }
}); 
});

$(function() {
    $("#payment-form").submit(function() {
        var form = this;
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };
    
    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
            $("#credit-card-errors").hide();
            $("#id_stripe_id").val(response.id);

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