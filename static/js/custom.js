$(document).ready(function (){
    $(".increment-btn").click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest(".product_data").find(".qty-input").val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if(value < 10){
            value++;
            $(this).closest(".product_data").find(".qty-input").val(value);
        }
    });

   $(".decrement-btn").click(function (e) {
            e.preventDefault();
    
            var dec_value = $(this).closest(".product_data").find(".qty-input").val();
            var value = parseInt(dec_value, 10);
            value = isNaN(value) ? 0 : value;
            if(value > 1){
                value--;
                $(this).closest(".product_data").find(".qty-input").val(value);
            }
        });

        $(".addToCartBtn").click(function (e) {
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var product_qty = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: RootUrl + "/add-to-cart",
                data: {
                    "product_id": product_id,
                    "product_qty": product_qty,
                    csrfmiddlewaretoken: token
                },
    
                success: function (response) {
                    console.log(response)
                    alertify.success(response.status)
                }
            });
        });

        $(".addToWishlist").click(function (e) {
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: RootUrl + "/add-to-wishlist",
                data: {
                    "product_id": product_id,
                    csrfmiddlewaretoken: token
                },
    
                success: function (response) {
                    console.log(response)
                    alertify.success(response.status)
                }
            });
        });


        $(".changeQuantity").click(function (e) {
            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var product_qty = $(this).closest('.product_data').find('.qty-input').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: RootUrl + "/update-cart",
                data: {
                    "product_id": product_id,
                    "product_qty": product_qty,
                    csrfmiddlewaretoken: token
                },
    
                success: function (response) {
                    // console.log(response)
                    // alertify.success(response.status)
                }
            });
        });

        $(document).on("click", ".delete-wishlist-item", function(e) {

            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: RootUrl + "/delete-wishlist-item",
                data: {
                    "product_id": product_id,
                    csrfmiddlewaretoken: token
                },
    
                success: function (response) {
                    // console.log(response)
                    alertify.success(response.status)
                    $(".wishlistdata").load(location.href + " .wishlistdata");
                }
            });
        });

        
        $(document).on("click", ".delete-cart-item", function(e) {

            e.preventDefault();
            var product_id = $(this).closest('.product_data').find('.prod_id').val();
            var token = $('input[name=csrfmiddlewaretoken]').val();
            $.ajax({
                type: "POST",
                url: RootUrl + "/delete-cart-item",
                data: {
                    "product_id": product_id,
                    csrfmiddlewaretoken: token
                },
    
                success: function (response) {
                    // console.log(response)
                    alertify.success(response.status)
                    $(".carddata").load(location.href + " .carddata");
                }
            });
        });
        
});
