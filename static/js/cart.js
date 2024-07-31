<!-- فرض کنید این بخش از کد HTML در صفحه محصول شما قرار دارد -->


<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

$(document).ready(function() {
    $('.add-to-cart').click(function() {
        var productId = $(this).data('product-id');
        $.ajax({
            url: '/add-to-cart/',
            method: 'POST',
            data: {
                'product_id': productId,
                'quantity': 1,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(response) {
                alert(response.message);
                // می‌توانید به جای alert از یک روش دیگر برای اطلاع رسانی به کاربر استفاده کنید
            },
            error: function(xhr, status, error) {
                alert('Something went wrong. Please try again.');
            }
        });
    });

$('.remove-from-cart').click(function() {
    var productId = $(this).data('product-id');
    $.ajax({
        url: '/remove-from-cart/',
        method: 'POST',
        data: {
            'product_id': productId,
            'csrfmiddlewaretoken': '{{ csrf_token }}'
        },
        success: function(response) {
            alert(response.message);
            // می‌توانید به جای alert از یک روش دیگر برای اطلاع رسانی به کاربر استفاده کنید
        },
        error: function(xhr, status, error) {
            alert('Something went wrong. Please try again.');
        }
    });
    });
});

