function get_game(game_number, password) {

	$.ajax({
		url: game_url,
		beforeSend: set_csrf,
		data: {
			'game_number': selected_game,
			'password': $('#pass').val(),
		},
		type: 'POST',
		success: function(data, textStatus, jqXHR) {
			if(data.error != null) {
				alert(data.error);
			} else {
				console.log(data.connect_info);
			}

		},
	});
}

function add_row(element, index, array)
{
	var row = $('<tr>');

	var game_number = $('<td>').text(element.game_number);
	var game_name = $('<td>').text(element.game_name);
	var players = $('<td>').text(element.players);
	var status = $('<td>').text(element.status);
	var locked = $('<td>');

	var icon_string = 'icon-unlock';

	var button = $('<button>').addClass('btn btn-info span12');

	if( element.locked == true )
	{
		icon_string = 'icon-lock';
		row.addClass('warning');
		button.click(function() {
			selected_game = element.game_number;
			$('#pass').val('');
			$('#password-dialog').modal();
		});
	} else {
		button.click(function() {
			selected_game = element.game_number;
			get_game(selected_game, null);
		});
	}

	var players_info = element.players.split('/');
	if( players_info[0] == players_info[1] ) {
		row.removeClass('warning');
		row.addClass('error');
	}

	var icon = $('<i>').addClass(icon_string).text(' Connect! ');
	button.append(icon);
	button.append($('<i>').addClass(icon_string));
	locked.append(button);

	row.append(game_number, game_name, players, status, locked);

	$('#gametable > tbody:last').append(row);

}

function populate_table(data, textStatus, jqXHR) {
	$('#gametable > tbody').empty();
	data.gamedata.forEach(add_row);
}

function load_list() {

	var game_number = $('#game-number').val();
	if( game_number == '' )
		game_number = null;

	var game_name = $('#game-name').val();
	if( game_name == '' )
		game_name = null;


	var filters = {
		'game_number': game_number,
		'game_name': game_name,
		'players': player_filter,
		'status': null,
		'locked': lock_filter,
	};

	$.ajax({
		url: server_list,
		type: 'POST',
		beforeSend: start_load,
		complete: end_load,
		data: filters,
		success: populate_table,
		error: function(jqXHR, textStatus, error) {
			console.log(textStatus);
			console.log(error);
		},
	});
}
