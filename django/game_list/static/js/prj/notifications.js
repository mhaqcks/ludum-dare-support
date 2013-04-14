function remove_notification(id) {
	$('#' + id).animate({
		left: '100%'
	}, 600, 'swing', function() {
		$('#' + id).remove();	
	});
}

function add_notification(id, title, message, style) {

	if( $('#' + id).length != 0 )
		return;

	new_alert = $('<div class="alert new-alert">').addClass(style);
	new_alert.attr('id', id);

	close_btn = $('<button type="button" class="close" data-dismiss="alert">').html('&times;');
	new_alert.append(close_btn);

	title_txt = $('<strong>').html(title + ' ');
	new_alert.append(title_txt);

	msg_txt = $('<span>').html(message);
	new_alert.append(msg_txt);

	$('#alert-header').after(new_alert);

	new_alert.animate({
		left: '0'
 	}, 800);
}
