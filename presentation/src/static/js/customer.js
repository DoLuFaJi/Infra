$(document).ready(function(){
	var dataTable = $("#dataTable").DataTable()
	var customerChannel = pusher.subscribe('customer');
	customerChannel.bind('add', function(data) {
	var date = new Date();
	dataTable.row.add([
	    data.store_id,
	    data.nb_transactions,
	    data.type_payment,
	    `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
	  ]).draw( false );
	});
});
