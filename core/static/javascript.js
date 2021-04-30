jQuery(function($){

	$('#qrcode').keyup(function(key){
		var value = $(this).val();
		if (key.which==13) {
			return false;
		}
		$.ajax({
			url: '/generate/',
			type: 'POST',
			data: {'key':value},
			dataType: 'json',
			success: function(result) {
				if (result.success == true) {
					$('#qrcode_result').html(result.qrcode);
					$('#png').html(result.png)
				} else {
					$('#qrcode_result').html("<em>Empty</em>");
				}
			},
			error:function(error) {
				return false;
			}
		});
	});
});

