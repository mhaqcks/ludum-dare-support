function get_game(game_number, password) {

	function pre_cunnect(xhr, settings) {
		set_csrf(xhr, settings);
	}

	$.ajax({
		url: game_url,
		beforeSend: pre_cunnect,
		data: {
			'game_number': game_number,
			'password': password,
		},
		type: 'POST',
		success: function(data, textStatus, jqXHR) {
			if(data.error != null) {
				alert(data.error);
			} else {
				$('#connect-dialog').modal();
				console.log(data.connect_info);
			}

		},
	});
}