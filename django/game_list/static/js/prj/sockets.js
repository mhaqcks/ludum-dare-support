
var websocket_timer = 0;
var connection = 0;
function attempt_connection() {
	websocket_timer = setTimeout(attempt_connection, 1500);

	if( connected_to_client == true )
		return;

	connection = new WebSocket('ws://localhost:65456/');

	connection.onopen = function() {
		connected_to_client = true;	
		remove_notification('no-connection');
		connection.send(JSON.stringify({
			command: 'this is a command'
		}));
	}

	connection.onerror = function(error) {
		console.log(error);
	}

	connection.onmessage = function(e) {
		console.log('Server: ' + e.data);
	}

	connection.onclose = function() {
		add_notification(
			'no-connection', 
			'Connection could not be established!', 
			'Please make sure you are running the <a href="' 
				+ download_page + '">game client</a>.', 
			'alert-error');
		if( connected_to_client == true ) {
			console.log('Connection Lost');
		}
		connected_to_client = false;
	}
}
