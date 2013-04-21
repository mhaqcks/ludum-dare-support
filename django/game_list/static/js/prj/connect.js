function get_game(game_number, password) {

	console.log('Connecting to Game...');
	$('#connect-dialog').remove();
	var dialog = $('<div id="connect-dialog" class="modal fide hide" tabindex="-1" role="dialog" aria-labelledby="WATWAT" aria-hidden="true">');
	var header = $('<div class="modal-header">');
	header.append($('<button type="button" class="close" data-dismiss="modal" aria-hidden="true">').text('×'))
	header.append($('<h3>').text('Create A Game...'));

	var body = $('<div class="modal-body">').text('Connect Info Here...');
	var footer = $('<div class="modal-footer">');
	footer.append($('<button type="button" class="btn" data-dismiss="modal" aria-hidden="true">').text('Close'));

	dialog.append(header);
	dialog.append(body);
	dialog.append(footer);

	$('#dialogs').append(dialog);

	dialog.modal();

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
				dialog.modal();
				console.log(data.connect_info);
			}

		},
	});
}