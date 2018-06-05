$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);

    function basketUpdating(product_id, nmb, is_delete){
        var data = {};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true
        }

        var url = form.attr("action");

        console.log(data);

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.products_total_nmb);
                if (data.products_total_nmb || data.products_total_nmb == 0){
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li>'+v.name+', ' + v.nmb + ' шт. ' + 'по ' + v.price_per_item + '$   ' +
                            '<a class="delete-item" href="" data-product_id="'+v.id+'">x</a>'+
                        '</li>');
                    });
                }

            },
            error:function () {
                console.log("error")
            }
        })
    }

    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("name");
        var product_price = submit_btn.data("price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketUpdating(product_id, nmb, is_delete=false)


    });

    function shovingBasket(){
        $('.basket-items').removeClass('hidden');
    };

    $('.basket-container').on('click', function(e) {
        e.preventDefault();
        shovingBasket();
    });

    $('.basket-container').mouseover(function() {
        shovingBasket();
    });

    // $('.basket-container').mouseout(function() {
    //     shovingBasket();
    // });

    $(document).on('click', '.delete_checkout', function() {

		var current_tr = $(this).closest('tr');
		var current_index = parseInt(current_tr.find('.item-index').val());
		var current_id = parseInt(current_tr.find('.item-id').val());
		current_tr.empty();
		  var data = {};
		  var csrf_token = getCookie('csrftoken');
		  data["csrfmiddlewaretoken"] = csrf_token;
		  data["is_delete"] = true;
		  var order = {
			 id: current_id,
			 count: 0
		  };
		  $.extend(true, data, order);
		  $.ajax({
			 url: 'remove',
			 type: 'POST',
			 data: data,
			 cache: true,
			 success: function(data)
			 {
				console.log("OK");
				if (data.products_total_nmb || data.products_total_nmb == 0)
				{
                    $('#basket_total_nmb').text("("+data.products_total_nmb+")");
				}
			 },
			 error: function()
			 {
				console.log("ERROR")
			 }
		  })

		calculatingBasketAmount();
    });

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            console.log($(this).text());
            total_order_amount += parseFloat($(this).text());
        });
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };

    $(document).on('change', ".product-in-basket-nmb", function () {
        var current_nmb = $(this).val();
        console.log(current_nmb);
        var current_tr = $(this).closest('tr');
		var current_id = parseInt(current_tr.find('.item-id').val());
		console.log(current_id);
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_nmb*current_price).toFixed(2);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);

		var data = {};
		  var csrf_token = getCookie('csrftoken');
		  data["csrfmiddlewaretoken"] = csrf_token;
		  data["is_delete"] = true;
		  var order = {
			 id: current_id,
			 count: current_nmb
		  };
		  $.extend(true, data, order);
		  $.ajax({
			 url: 'continue',
			 type: 'POST',
			 data: data,
			 cache: true,
			 success: function(data)
			 {
				console.log("OK");
			 },
			 error: function()
			 {
				console.log("ERROR")
			 }
		  })

        calculatingBasketAmount();
    });

    calculatingBasketAmount();
});


$('#carousel').carousel({
    interval: 4100,
    keyboard: false,
    ride: 'carousel',
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
