$("#form-login").on("submit", function(e){
	e.preventDefault();
	$.sendFormLogin();
});

$.sendFormLogin =  function(){
	var data = $("#form-login").serialize();
	$.post("/validar-login", data, function(respData){
		var resp = JSON.parse(respData);
		if(resp.sms == 1 || resp.sms == "1"){
			$("#sms-alert").html("<div class='alert alert-success fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-check'></i> <strong>Bienvenid@</strong> "+resp.username+".</div>");
		}else
		if(resp.sms == 4 || resp.sms == "4"){
			$("#sms-alert").html("<div class='alert alert-info fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-info'></i> <strong>Usuario:</strong> "+resp.username+" se encuentra desactivado.</div>");
		}else
		if(resp.sms == 3 || resp.sms == "3"){
			$("#sms-alert").html("<div class='alert alert-danger fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-times'></i> <strong>Error! Usuario:</strong> "+resp.username+" no se encuetra, por favor, verique su informaci&oacute;n.</div>");
		}else{
			$("#sms-alert").html("<div class='alert alert-danger fade in'><a href='#' class='close' data-dismiss='alert' aria-label='close' title='close'>×</a><i class='fa fa-times'></i> <strong>Error!</strong> Se ha producido un error, por favor comuniquese con el administrador.</div>");
		}
		$.closeAlert(resp.sms);
	})
	.fail(function(error){
		console.log(error);
	});
}

$.closeAlert =  function(valor){
	setTimeout(function(){
	    $('.alert').fadeTo("slow", 0, function(){
	        $('.alert').alert('close');
	        $(".alert").remove();
	        if(valor == 1 || valor == "1"){window.location.href = "/menu"}
	    });     
    }, 3000);
}