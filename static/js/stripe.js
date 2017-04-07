$(function() {
    alert("Stripe JS happening");
    $("#payment-form").submit(function() {
        alert("Hijacking Submit");
      var form = this;
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };


    Stripe.createToken(card, function(status, response) {
        if (status === 200) {
        alert("Stripe Replied");
        console.log(status, response);
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          form.submit();
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
    });
    return false;
  });
});

