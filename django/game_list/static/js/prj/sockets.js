
var websocket_timer = 0;
var connection = 0;
var response = 0;

var expect_ver = 'v0.02';

function command(data) {
	connection.send(JSON.stringify(data));
}

var SAFE_FUNCTIONS = {
	version: function(ver) {
		if(ver != expect_ver) {
			add_notification(
				'version-mismatch', 
				'Client Out of Date', 
				'Please update your client!  Expecting ' + expect_ver + 
					', but received ' + ver + 
					'.  You can download the latest client <a href="' +
					download_page + '">here</a>.',
				'alert-error')
		}
	}
}

function attempt_connection() {
	websocket_timer = setTimeout(attempt_connection, 1500);

	if( connected_to_client == true )
		return;

	connection = new WebSocket('ws://localhost:65456/');

	connection.onopen = function() {
		connected_to_client = true;	
		remove_notification('no-connection');

		command({
			func: 'check_version'
		});
	}

	connection.onerror = function(error) {
		console.log(error);
	}

	connection.onmessage = function(e) {
		var cmd_info = jQuery.parseJSON( e.data );

		console.log(cmd_info.func);
		SAFE_FUNCTIONS[cmd_info.func].apply(this, Array.prototype.slice.call(cmd_info.args, 0));
	}

	connection.onclose = function() {
		remove_notification('version-mismatch');
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
