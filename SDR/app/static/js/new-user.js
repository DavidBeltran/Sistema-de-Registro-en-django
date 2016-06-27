$("document").ready(function(){
	$.changeRoles();
});

$("#form-new-user").on("submit", function(e){
	e.preventDefault();
	$.saveNewUser();
});

$.saveNewUser = function(){
	var data = $("#form-new-user").serialize();
	$.post("/saveUser", data, function(resp){
		console.log(resp);
	})
	.fail(function(error){
		console.log(error);
	});
}

$.changeRoles = function(){
	$.get("/roles", {}, function(resp){
		if(resp != "-1" || resp != -1){
			$("#change-select").append(resp);
		}
	})
	.fail(function(error){
		console.log(error);
	});
}