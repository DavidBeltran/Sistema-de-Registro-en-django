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
		var json = JSON.parse(resp);
		var sms = json.sms; 
		switch(sms){
			case 1:
				$("#alert-sms").html("<div class='alert alert-info fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-times'></i> <strong>Error!</strong> Usuario o Email ya existen, por favor verifique.</div>");
			break;
			case 2:
				$("#alert-sms").html("<div class='alert alert-success fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-check'></i> <strong>Exito!</strong> Usuario actualizado correctamente.</div>");
			break;
			case 3:
				$("#alert-sms").html("<div class='alert alert-success fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-check'></i> <strong>Exito!</strong> Usuario almacenado correctamente.</div>");
			break;
			default:
				$("#alert-sms").html("<div class='alert alert-danger fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-times'></i> <strong>Error!</strong> Se ha producido un error, por favor comuniquese con el administrador.</div>");
			break;
		}
		$.closeAlert();
	})
	.fail(function(error){
		console.log(error);
	});
}

$.changeRoles = function(){
	var opcion = $("#select-group").val();
	$.get("/roles", {}, function(resp){
		if(resp != "-1" || resp != -1){
			$("#change-select").append(resp);
		}
		if(opcion != ""){
			$("#change-select").val(opcion);
		}
	})
	.fail(function(error){
		console.log(error);
	});
}

$.closeAlert =  function(){
	setTimeout(function(){
	    $('.alert').fadeTo("slow", 0, function(){
	        $('.alert').alert('close');
	        $(".alert").remove();
	    });     
    }, 3000);
}
