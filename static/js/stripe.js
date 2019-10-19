$(document).ready(function(){
    $('#submit_payment_btn').click( function(){
        if ($("input:radio[name='what-button']").not(":checked")) {
                $("#alert").show();
        } 
        if ($("input:radio[name='what-button']").is(":checked")) {
                $("#alert").hide();
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
        if (status != 200) {
            $("#alert-two").show();
        }
        else if (status === 200 || $("input:radio[name='what-button']").not(":checked")) {
            $("#alert").show();
            return false;
        }    
        else if (status === 200) {
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