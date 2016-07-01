$(document).ready(function(){
	$.cargarTabla(1);
	$.changeRoles();
});

$.cargarTabla = function(page){
	var data = {"index":page}
	$.get("/menu/tabla-usuario", data, function(resp){
		$("#id_tabla").html(resp);
	})
	.fail(function(error){
		console.log(error);
	});
}
$
.changeRoles = function(){
	var opcion = $("#select-group").val();
	$.get("/roles", {}, function(resp){
		if(resp != "-1" || resp != -1){
			$("#select-rol").append(resp);
		}
	})
	.fail(function(error){
		console.log(error);
	});
}