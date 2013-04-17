
var title = $('<div class="control-group">');
title.append($('<label class="control-label" for="inputTitle">').text('Title'));
title.append($('<div class="controls">').append(
	$('<input type="text" id="game-title" placeholder="Game Title" style="height: 100%;">')));

var password = $('<div class="control-group">');
password.append($('<label class="control-label" for="inputPassword">').text('Password'));
password.append($('<div class="controls">').append(
	$('<input type="password" id="game-password" placeholder="Password (if protected)" style="height: 100%;">')));

var num_players = $('<div class="control-group">');
num_players.append($('<label class="control-label" for="inputPlayers">').text('Max Players'));
num_players.append($('<div class="controls">').append(
	$('<input type="number" id="game-players" placeholder="Maximum Number of Players" value="5" min="1" max="50" style="height: 100%;">')));

function create_game() {
	console.log('creating game');
	$('#old-dialog').remove();
	var dialog = $('<div id="old-dialog" class="modal fide hide" tabindex="-1" role="dialog" aria-labelledby="WATWAT" aria-hidden="true">');

	var header = $('<div class="modal-header">');
	header.append($('<button type="button" class="close" data-dismiss="modal" aria-hidden="true">').text('×'))
	header.append($('<h3>').text('Create A Game...'));

	var body = $('<div class="modal-body">');
	var form = $('<form id="create-game-form" class="form-horizontal" style="margin-bottom: 0px;">');


	body.append(title);
	body.append(password);
	body.append(num_players);

	var footer = $('<div class="modal-footer">');
	footer.append($('<button type="button" class="btn" data-dismiss="modal" aria-hidden="true">').text('Close'));
	footer.append($('<button type="submit" id="create-game-submit" class="btn btn-primary">').text('Create Game!'));

	form.append(body);
	form.append(footer);

	dialog.append(header);
	dialog.append(form);

	$('#dialogs').append(dialog);

	dialog.modal();

	form.submit(function() {

		build_game(
			$('#game-title').val(), 
			$('#game-password').val(), 
			$('#game-players').val());
		dialog.modal('hide');

		return false;
	});
}

function build_game(title, password, num_players) {
	$.ajax({
		url: 'https://jacobvgardner.com/game/build_game/',	
		crossDomain: true,
		success: function(data) {
			get_game(data.game_number, password);	
		},
		dataType: 'JSONP',
		data: {
			'title': title,
			'password': password,
			'num_players': num_players
		},
		error: function(jqXHR, textStatus, error) {
			console.log(textStatus);
			console.log(error);
		},
	});
	console.log(title, password, num_players);	
}