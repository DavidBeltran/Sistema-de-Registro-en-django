$("document").ready(function(){
	$.url();
});

$.url = function(){
	var url = window.location.pathname;
	var arrayUrl = url.split("/");
	var urlReal = arrayUrl[arrayUrl.length-1];
	$.searchActive(urlReal);	
}

$.searchActive = function(urlReal){
	switch(urlReal){
		case 'user': case 'menu':
			$("#user").addClass("active");
		break;	
		case 'nuevo-usuario': case "buscar-usuario":
			$("#conf").addClass("active");
		break;
		default:
			$("#user").addClass("active");
		break;
	}
}